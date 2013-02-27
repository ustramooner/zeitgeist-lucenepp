# -.- coding: utf-8 -.-

# Zeitgeist
#
# Copyright © 2009 Mikkel Kamstrup Erlandsen <mikkel.kamstrup@gmail.com>
# Copyright © 2010 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#
# TODO
#
# - Delete events hook
# - ? Filter on StorageState
# - Throttle IO and CPU where possible

import os, sys
import time
import pickle
import dbus
import dbus.service
from xdg import BaseDirectory
from xdg.DesktopEntry import DesktopEntry, xdg_data_dirs
import logging
import subprocess
from xml.dom import minidom
import lucene
import os
from Queue import Queue, Empty
import threading
from urllib import quote as url_escape, unquote as url_unescape
import gobject, gio

from zeitgeist.datamodel import Symbol, StorageState, ResultType, TimeRange, NULL_EVENT, NEGATION_OPERATOR
from _zeitgeist.engine.datamodel import Event, Subject
from _zeitgeist.engine.extension import Extension
from _zeitgeist.engine import constants
from zeitgeist.datamodel import Interpretation, Manifestation

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("zeitgeist.fts")

INDEX_FILE = os.path.join(constants.DATA_PATH, "fts.clucene.index")
FTS_DBUS_OBJECT_PATH = "/org/gnome/zeitgeist/index/activity"
FTS_DBUS_INTERFACE = "org.gnome.zeitgeist.Index"

FILTER_PREFIX_EVENT_INTERPRETATION = "ZGEI"
FILTER_PREFIX_EVENT_MANIFESTATION = "ZGEM"
FILTER_PREFIX_ACTOR = "ZGA"
FILTER_PREFIX_SUBJECT_URI = "ZGSU"
FILTER_PREFIX_SUBJECT_INTERPRETATION = "ZGSI"
FILTER_PREFIX_SUBJECT_MANIFESTATION = "ZGSM"
FILTER_PREFIX_SUBJECT_ORIGIN = "ZGSO"
FILTER_PREFIX_SUBJECT_MIMETYPE = "ZGST"
FILTER_PREFIX_SUBJECT_STORAGE = "ZGSS"
FILTER_PREFIX_XDG_CATEGORY = "AC"

LUCENE_FIELD_CATEGORY = "category"
LUCENE_FIELD_CONTENTS = "contents"
LUCENE_FIELD_APP = "app"
LUCENE_FIELD_TITLE = "title"
LUCENE_FIELD_NAME = "name"
LUCENE_FIELD_SITE = "site"
LUCENE_FIELD_FLAGS = "flags"

VALUE_EVENT_ID = "id"
VALUE_TIMESTAMP = "ms"

# When sorting by of the COALESCING_RESULT_TYPES result types,
# we need to fetch some extra events from the Lucene index because
# the final result set will be coalesced on some property of the event
COALESCING_RESULT_TYPES = [ \
	ResultType.MostRecentSubjects,
	ResultType.LeastRecentSubjects,
	ResultType.MostPopularSubjects,
	ResultType.LeastPopularSubjects,
	ResultType.MostRecentActor,
	ResultType.LeastRecentActor,
	ResultType.MostPopularActor,
	ResultType.LeastPopularActor,
]

class Deletion:
	"""
	A marker class that marks an event id for deletion
	"""
	def __init__ (self, event_id):
		self.event_id = event_id

class SearchEngineExtension (Extension, dbus.service.Object):
	"""
	Full text indexing and searching extension for Zeitgeist
	"""
	PUBLIC_METHODS = []
	
	def __init__ (self, engine):
		Extension.__init__(self, engine)
		dbus.service.Object.__init__(self, dbus.SessionBus(),
		                             FTS_DBUS_OBJECT_PATH)
		self._indexer = Indexer(self.engine)
	
	def pre_insert_event(self, event, sender):
		# Fix when Zeitgeist 0.5.1 hits the street use post_insert_event() instead
		self._indexer.index_event (event)
		return event

	def post_delete_events (self, ids, sender):
		for _id in ids:
			self._indexer.delete_event (_id)
        		
	@dbus.service.method(FTS_DBUS_INTERFACE,
	                     in_signature="s(xx)a("+constants.SIG_EVENT+")uuu",
	                     out_signature="a("+constants.SIG_EVENT+")u")
	def Search(self, query_string, time_range, filter_templates, offset, count, result_type):
		"""
		DBus method to perform a full text search against the contents of the
		Zeitgeist log. Returns an array of events.
		"""
		time_range = TimeRange(time_range[0], time_range[1])
		filter_templates = map(Event, filter_templates)
		events, hit_count = self._indexer.search(query_string, time_range,
		                                         filter_templates,
		                                         offset, count, result_type)
		return self._make_events_sendable (events), hit_count
	
	def _make_events_sendable(self, events):
		for event in events:
			if event is not None:
				event._make_dbus_sendable()
		return [NULL_EVENT if event is None else event for event in events]

def mangle_uri (uri):
	"""
	Converts a URI into an index- and query friendly string. The problem
	is that Xapian doesn't handle CAPITAL letters or most non-alphanumeric
	symbols in a boolean term when it does prefix matching. The mangled
	URIs returned from this function are suitable for boolean prefix searches.
	
	IMPORTANT: This is a 1-way function! You can not convert back.
	"""
	result = ""
	for c in uri.lower():
		if c in (": /"):
			result += "_"
		else:
			result += c
	return result

def expand_type (type_prefix, uri):
	"""
	Return a string with a Xapian query matching all child types of 'uri'
	inside the Xapian prefix 'type_prefix'.
	"""
	is_negation = uri.startswith(NEGATION_OPERATOR)
	uri = uri[1:] if is_negation else uri
	children = Symbol.find_child_uris_extended(uri)
	children = [ "%s:%s" % (type_prefix, child) for child in children ]

	result = " OR ".join(children)
	return result if not is_negation else "NOT (%s)" % result

class Indexer:
	"""
	Abstraction of the FT indexer and search engine
	"""
	
	
	def __init__ (self, engine):
		self._engine = engine
	
		log.debug("Opening full text index: %s" % INDEX_FILE)
		self._analyzer = lucene.StandardAnalyzer(lucene.Version.LUCENE_CURRENT)
		self._query_parser = lucene.QueryParser(lucene.Version.LUCENE_CURRENT, "defaultfield", self._analyzer)
		self._directory = lucene.FSDirectory.open(INDEX_FILE)
		self._maxFieldLength = 10000
		self._index = lucene.IndexWriter(self._directory, self._analyzer, self._maxFieldLength)
		#TODO 
		#self._query_parser.add_prefix("name", "N")
		#self._query_parser.add_prefix("title", "N")
		#self._query_parser.add_prefix("site", "S")
		#self._query_parser.add_prefix("app", "A")
		#self._query_parser.add_boolean_prefix("zgei", FILTER_PREFIX_EVENT_INTERPRETATION)
		#self._query_parser.add_boolean_prefix("zgem", FILTER_PREFIX_EVENT_MANIFESTATION)
		#self._query_parser.add_boolean_prefix("zga", FILTER_PREFIX_ACTOR)
		#self._query_parser.add_boolean_prefix("zgsi", FILTER_PREFIX_SUBJECT_INTERPRETATION)
		#self._query_parser.add_boolean_prefix("zgsm", FILTER_PREFIX_SUBJECT_MANIFESTATION)
		#self._query_parser.add_prefix("category", FILTER_PREFIX_XDG_CATEGORY)
		#self._query_parser.add_valuerangeprocessor(
		#      xapian.NumberValueRangeProcessor(VALUE_EVENT_ID, "id", True))
		#self._query_parser.add_valuerangeprocessor(
		#      xapian.NumberValueRangeProcessor(VALUE_TIMESTAMP, "ms", False))
		#self._query_parser.set_default_op(xapian.Query.OP_AND)
		self._enquire = lucene.IndexSearcher(self._directory)
		
		# Cache of parsed DesktopEntrys
		self._desktops = {}
		
		gobject.threads_init()
		self._may_run = True
		self._queue = Queue(0)
		self._worker = threading.Thread(target=self._worker_thread,
		                                name="IndexWorker")
		self._worker.daemon = True
		self._worker.start()
		
		self._check_index ()
		
	def _check_index (self):
		if self._index.numDocs() == 0:
			# If the index is empty we trigger a rebuild
			# We must delay reindexing until after the engine is done setting up
			log.info("Empty index detected. Doing full rebuild")
			gobject.idle_add (self._reindex)

	
	def _reindex (self):
		"""
		Index everything in the ZG log
		"""
		self._index.close ()
		self._index = lucene.IndexWriter(self._directory, self._analyzer, self._maxFieldLength)
		
		all_events = self._engine.find_events(TimeRange.always(),
		                                      [], StorageState.Any,
		                                      sys.maxint,
		                                      ResultType.MostRecentEvents)
		log.info("Preparing to index %s events" % len(all_events))
		for e in all_events : self._queue.put(e)
	
	def index_event (self, event):
		"""
		This method schedules and event for indexing. It returns immediate and
		defers the actual work to a bottom half thread. This means that it
		will not block the main loop of the Zeitgeist daemon while indexing
		(which may be a heavy operation)
		"""
		self._queue.put (event)
		return event
	
	def delete_event (self, event_id):
		"""
		Remove an event from the index given its event id
		"""
		self._queue.put (Deletion(event_id))
		return		
	
	def search (self, query_string, time_range=None, filters=None, offset=0, maxhits=10, result_type=100):
		"""
		Do a full text search over the indexed corpus. The `result_type`
		parameter may be a zeitgeist.datamodel.ResultType or 100. In case it is
		100 the textual relevancy of the search engine will be used to sort the
		results. Result type 100 is the fastest (and default) mode.
		
		The filters argument should be a list of event templates.
		"""
		print "search %s " % query_string
		exit(1)
		# Expand event template filters if necessary
		if filters:
			query_string = "(%s) AND (%s)" % (query_string, self._compile_event_filter_query (filters))
		
		# Expand time range value query
		if time_range and not time_range.is_always():
			query_string = "(%s) AND (%s)" % (query_string, self._compile_time_range_filter_query (time_range))
		
		# If the result type coalesces the events we need to fetch some extra
		# events from the index to have a chance of actually holding 'maxhits'
		# unique events
		if result_type in COALESCING_RESULT_TYPES:
			raw_maxhits = maxhits * 3
		else:
			raw_maxhits = maxhits
		
		# When not sorting by relevance, we fetch the results from Xapian sorted,
		# by timestamp. That minimizes the skew we get from otherwise doing a
		# relevancy ranked xapaian query and then resorting with Zeitgeist. The
		# "skew" is that low-relevancy results may still have the highest timestamp
		if result_type == 100:
		  self._enquire.set_sort_by_relevance()
		else:
		  self._enquire.set_sort_by_value(VALUE_TIMESTAMP, True)
		
		# Allow wildcards
		query_start = time.time()
		query = self._query_parser.parse_query (query_string,
		                                        self.QUERY_PARSER_FLAGS)
		self._enquire.set_query (query)
		hits = self._enquire.get_mset (offset, raw_maxhits)
		hit_count = hits.get_matches_estimated()
		log.debug("Search '%s' gave %s hits in %sms" %
		          (query_string, hits.get_matches_estimated(), (time.time() - query_start)*1000))
		
		if result_type == 100:
			event_ids = []
			for m in hits:
				event_id = int(xapian.sortable_unserialise(
				                          m.document.get_value(VALUE_EVENT_ID)))				
				event_ids.append (event_id)
			if event_ids:
				return self._engine.get_events(ids=event_ids), hit_count
			else:
				return [], 0
		else:
			templates = []
			for m in hits:
				event_id = int(xapian.sortable_unserialise(
				                          m.document.get_value(VALUE_EVENT_ID)))
				ev = Event()
				ev[0][Event.Id] = str(event_id)
				templates.append(ev)
		
			if templates:
				return self._engine._find_events(1, TimeRange.always(),
				                                 templates,
				                                 StorageState.Any,
				                                 maxhits,
				                                 result_type), hit_count
			else:
				return [], 0
	
	def _worker_thread (self):
		is_dirty = False
		while self._may_run:
			# FIXME: Throttle IO and CPU
			try:
				# If we are dirty wait a while before we flush,
				# or if we are clean wait indefinitely to avoid
				# needless wakeups
				if is_dirty:
					event = self._queue.get(True, 0.5)
				else:
					event = self._queue.get(True)
				
				if isinstance (event, Deletion):
					self._delete_event_real (event.event_id)
				else:
					self._index_event_real (event)
				
				is_dirty = True
			except Empty:
				if is_dirty:
					# Write changes to disk
					log.debug("Committing FTS index")
					self._index.commit()
					is_dirty = False
				else:
					log.debug("No changes to index. Sleeping")
	
	def _delete_event_real (self, event_id):
		"""
		Look up the doc id given an event id and remove the xapian.Document
		for that doc id.
		Note: This is slow, but there's not much we can do about it
		"""
		print "TODO delete"
		return
		try:
			_id = xapian.sortable_serialise(float(event_id))
			query = xapian.Query(xapian.Query.OP_VALUE_RANGE, 
			                     VALUE_EVENT_ID, _id, _id)
			
			self._enquire.set_query (query)
			hits = self._enquire.get_mset (0, 10)
			
			total = hits.get_matches_estimated()
			if total > 1:
				log.warning ("More than one event found with id '%s'" % event_id)
			elif total <= 0:
				log.debug ("No event for id '%s'" % event_id)
				return
		
			for m in hits:
				log.debug("Deleting event '%s' with docid '%s'" %
				          (event_id, m.docid))
				self._index.delete_document(m.docid)
		except Exception, e:
			log.error("Failed to delete event '%s': %s" % (event_id, e))
		
	def _split_uri (self, uri):
		"""
		Returns a triple of (scheme, host, and path) extracted from `uri`
		"""		
		i = uri.find(":")
		if i == -1 :
			scheme =  ""
			host = ""
			path = uri
		else:
			scheme = uri[:i]
			host = ""
			path = ""
	  	
		if uri[i+1] == "/" and uri[i+2] == "/":
			j = uri.find("/", i+3)
			if j == -1 :
				host = uri[i+3:]
			else:
				host = uri[i+3:j]
				path = uri[j:]
		else:
			host = uri[i+1:]
		
		# Strip out URI query part
		i = path.find("?")
		if i != -1:
			path = path[:i]
		
		return scheme, host, path
	
	def _get_desktop_entry (self, app_id):
		"""
		Return a xdg.DesktopEntry.DesktopEntry `app_id` or None in case
		no file is found for the given desktop id
		"""
		if app_id in self._desktops:
			return self._desktops[app_id]
		
		for datadir in xdg_data_dirs:
			path = os.path.join(datadir, "applications", app_id)
			if os.path.exists(path):
				try:
					desktop = DesktopEntry(path)
					self._desktops[app_id] = desktop
					return desktop
				except Exception, e:
					log.warning("Unable to load %s: %s" % (path, e))
					return None
		
		return None
	
	def _index_actor (self, doc, actor):
		"""
		Takes an actor as a path to a .desktop file or app:// uri
		and index the contents of the corresponding .desktop file
		into the document currently set for self._tokenizer.
		"""
		if not actor : return

		# Get the path of the .desktop file and convert it to
		# an app id (eg. 'gedit.desktop')
		scheme, host, path = self._split_uri(url_unescape (actor))
		if not path:
			path = host
		
		if not path :
			log.debug("Unable to determine application id for %s" % actor)
			return
		
		if path.startswith("/") :
			path = os.path.basename(path)
		
		desktop = self._get_desktop_entry(path)
		if desktop:
			if not desktop.getNoDisplay():
				f = lucene.Field(LUCENE_FIELD_APP, desktop.getName(), lucene.Field.STORE_YES, lucene.Field.INDEX_ANALYZED)
				f.setBoost(5)
				doc.add(f)
				f = lucene.Field(LUCENE_FIELD_APP, desktop.getGenericName(), lucene.Field.STORE_YES, lucene.Field.INDEX_ANALYZED)
				f.setBoost(5)
				doc.add(f)
				f = lucene.Field(LUCENE_FIELD_APP, desktop.getComment(), lucene.Field.STORE_YES, lucene.Field.INDEX_ANALYZED)
				f.setBoost(2)
				doc.add(f)
			
				for cat in desktop.getCategories():
					doc.add(lucene.Field(LUCENE_FIELD_CATEGORY, cat.lower(), lucene.Field.STORE_YES, lucene.Field.INDEX_ANALYZED))
		else:
			log.debug("Unable to look up app info for %s" % actor)
		
	
	def _index_uri (self, doc, uri):
		"""
		Index `uri` into the document currectly set on self._tokenizer
		"""
		#TODO:
		# File URIs and paths are indexed in one way, and all other,
		# usually web URIs, are indexed in another way because there may
		# be domain name etc. in there we want to rank differently
		scheme, host, path = self._split_uri (url_unescape (uri))
		if scheme == "file://" or not scheme:
			path, name = os.path.split(path)
			
			#store in name field
			f = lucene.Field(LUCENE_FIELD_NAME, name, lucene.Field.STORE_YES, lucene.Field.INDEX_ANALYZED)
			f.setBoost(5)
			doc.add(f)
			
			#store as content
			f = lucene.Field(LUCENE_FIELD_CONTENTS, name, lucene.Field.STORE_NO, lucene.Field.INDEX_ANALYZED)
			f.setBoost(5)
			doc.add(f)
			
			# Index parent names with descending weight
			weight = 5
			while path and name:
				weight = weight / 1.5
				path, name = os.path.split(path)
				f = lucene.Field(LUCENE_FIELD_CONTENTS, name, lucene.Field.STORE_NO, lucene.Field.INDEX_ANALYZED)
				f.setBoost(weight)
				doc.add(f)
				
			
		elif scheme == "mailto:":
			tokens = host.split("@")
			name = tokens[0]
			
			#store as content (TODO?? why is that)
			f = lucene.Field(LUCENE_FIELD_CONTENTS, name, lucene.Field.STORE_NO, lucene.Field.INDEX_ANALYZED)
			f.setBoost(6)
			doc.add(f)
			
			if len(tokens) > 1:
				#TODO: what's this doing???
				#self._tokenizer.index_text(" ".join[1:], 1)
				pass
				
		else:
			# We're cautious about indexing the path components of
			# non-file URIs as some websites practice *extremely* long
			# and useless URLs
			path, name = os.path.split(path)
			if len(name) > 30 : name = name[:30]
			if len(path) > 30 : path = path[30]
			if name:
				#store in name field
				f = lucene.Field(LUCENE_FIELD_NAME, name, lucene.Field.STORE_YES, lucene.Field.INDEX_ANALYZED)
				f.setBoost(5)
				doc.add(f)
				
				#store as content
				f = lucene.Field(LUCENE_FIELD_CONTENTS, name, lucene.Field.STORE_NO, lucene.Field.INDEX_ANALYZED)
				f.setBoost(5)
				doc.add(f)
	  		if path:
				#store in name field
				f = lucene.Field(LUCENE_FIELD_NAME, path, lucene.Field.STORE_YES, lucene.Field.INDEX_ANALYZED)
				f.setBoost(1)
				doc.add(f)
				
				#store as content
				f = lucene.Field(LUCENE_FIELD_CONTENTS, path, lucene.Field.STORE_NO, lucene.Field.INDEX_ANALYZED)
				f.setBoost(1)
				doc.add(f)
			if host:
				#store in name field
				f = lucene.Field(LUCENE_FIELD_NAME, host, lucene.Field.STORE_YES, lucene.Field.INDEX_ANALYZED)
				f.setBoost(2)
				doc.add(f)
				
				#store as content
				f = lucene.Field(LUCENE_FIELD_CONTENTS, host, lucene.Field.STORE_NO, lucene.Field.INDEX_ANALYZED)
				f.setBoost(2)
				doc.add(f)
				
				#store as site
				f = lucene.Field(LUCENE_FIELD_SITE, host, lucene.Field.STORE_NO, lucene.Field.INDEX_ANALYZED)
				f.setBoost(2)
				doc.add(f)
	
	def _index_text (self, doc, text):
		"""
		Index `text` as raw text data for the document currently
		set on self._tokenizer. The text is assumed to be a primary
		description of the subject, such as the basename of a file.
		
		Primary use is for subject.text
		"""
		f = lucene.Field(LUCENE_FIELD_CONTENTS, text, lucene.Field.STORE_NO, lucene.Field.INDEX_ANALYZED)
		f.setBoost(5)
		doc.add(f)
	
	def _index_contents (self, uri):
		# xmlindexer doesn't extract words for URIs only for file paths
		
		# FIXME: IONICE and NICE on xmlindexer
		
		path = uri.replace("file://", "")
		xmlindexer = subprocess.Popen(['xmlindexer', path],
		                              stdout=subprocess.PIPE)
		xml = xmlindexer.communicate()[0].strip()
		xmlindexer.wait()		
		
		dom = minidom.parseString(xml)
		text_nodes = dom.getElementsByTagName("text")
		lines = []
		if text_nodes:
			for line in text_nodes[0].childNodes:
				lines.append(line.data)
		
		if lines:
				f = lucene.Field(LUCENE_FIELD_CONTENTS, " ".join(lines), lucene.Field.STORE_NO, lucene.Field.INDEX_ANALYZED)
				doc.add(f)
		
	
	def _add_doc_filters (self, event, doc):
		"""Adds the filtering rules to the doc. Filtering rules will
		   not affect the relevancy ranking of the event/doc"""
		if event.interpretation:
			doc.add(lucene.Field(FILTER_PREFIX_EVENT_INTERPRETATION, event.interpretation, lucene.Field.STORE_NO, lucene.Field.INDEX_NOT_ANALYZED_NO_NORMS))
		if event.manifestation:
			doc.add(lucene.Field(FILTER_PREFIX_EVENT_MANIFESTATION, event.manifestation, lucene.Field.STORE_NO, lucene.Field.INDEX_NOT_ANALYZED_NO_NORMS))
		if event.actor:
			doc.add(lucene.Field(FILTER_PREFIX_ACTOR, mangle_uri(event.actor), lucene.Field.STORE_NO, lucene.Field.INDEX_NOT_ANALYZED_NO_NORMS))
		
		for su in event.subjects:
			if su.uri:
				doc.add(lucene.Field(FILTER_PREFIX_SUBJECT_URI, mangle_uri(su.uri), lucene.Field.STORE_NO, lucene.Field.INDEX_NOT_ANALYZED_NO_NORMS))
			if su.interpretation:
				doc.add(lucene.Field(FILTER_PREFIX_SUBJECT_INTERPRETATION, su.interpretation, lucene.Field.STORE_NO, lucene.Field.INDEX_NOT_ANALYZED_NO_NORMS))
			if su.manifestation:
				doc.add(lucene.Field(FILTER_PREFIX_SUBJECT_MANIFESTATION, su.manifestation, lucene.Field.STORE_NO, lucene.Field.INDEX_NOT_ANALYZED_NO_NORMS))
			if su.origin:
				doc.add(lucene.Field(FILTER_PREFIX_SUBJECT_ORIGIN, mangle_uri(su.origin), lucene.Field.STORE_NO, lucene.Field.INDEX_NOT_ANALYZED_NO_NORMS))
			if su.mimetype:
				doc.add(lucene.Field(FILTER_PREFIX_SUBJECT_MIMETYPE, su.mimetype, lucene.Field.STORE_NO, lucene.Field.INDEX_NOT_ANALYZED_NO_NORMS))
			if su.storage:
				doc.add(lucene.Field(FILTER_PREFIX_SUBJECT_STORAGE, su.storage, lucene.Field.STORE_NO, lucene.Field.INDEX_NOT_ANALYZED_NO_NORMS))
	
	def _index_event_real (self, event):
		if not isinstance (event, Event):
			log.error("Not an Event, found: %s" % type(event))
		if not event.id:
			log.debug("Not indexing event. Event has no id")
			return
		
		try:
			doc = lucene.Document()
			doc.add(lucene.NumericField(VALUE_EVENT_ID).setLongValue(int(event.id)))
			doc.add(lucene.NumericField(VALUE_TIMESTAMP).setLongValue(int(event.timestamp)))
			
			self._index_actor (doc, event.actor)

			for subject in event.subjects:
				if not subject.uri : continue
				
				# By spec URIs can have arbitrary length. In reality that's just silly.
				# The general online "rule" is to keep URLs less than 2k so we just
				# choose to enforce that
				if len(subject.uri) > 2000:
					log.info ("URI too long (%s). Discarding: %s..."% (len(subject.uri), subject.uri[:30]))
					continue
				log.debug("Indexing '%s'" % subject.uri)
				self._index_uri (doc, subject.uri)
				self._index_text (doc, subject.text)
				
				# If the subject URI is an actor, we index the .desktop also
				if subject.uri.startswith ("application://"):
					self._index_actor (doc, subject.uri)

				# File contents indexing disabled for now...
				#self._index_contents (subject.uri)
				
				# FIXME: Possibly index payloads when we have apriori knowledge
			
			self._add_doc_filters (event, doc)
			self._index.addDocument(doc)
		except Exception, e:
			log.error("Error indexing event: %s" % e)

	def _compile_event_filter_query (self, events):
		"""Takes a list of event templates and compiles a filter query
		   based on their, interpretations, manifestations, and actor,
		   for event and subjects.
		   
		   All fields within the same event will be ANDed and each template
		   will be ORed with the others. Like elsewhere in Zeitgeist the
		   type tree of the interpretations and manifestations will be expanded
		   to match all child symbols as well
		"""
		print "_compile_event_filter_query"
		exit(1)
		query = []
		for event in events:
			if not isinstance(event, Event):
				raise TypeError("Expected Event. Found %s" % type(event))
			
			tmpl = []
			if event.interpretation :
				tmpl.append(expand_type("zgei", event.interpretation))
			if event.manifestation :
				tmpl.append(expand_type("zgem", event.manifestation))
			if event.actor : tmpl.append("zga:%s" % mangle_uri(event.actor))
			for su in event.subjects:
				if su.uri :
					tmpl.append("zgsu:%s" % mangle_uri(su.uri))
				if su.interpretation :
					tmpl.append(expand_type("zgsi", su.interpretation))
				if su.manifestation :
					tmpl.append(expand_type("zgsm", su.manifestation))
				if su.origin :
					tmpl.append("zgso:%s" % mangle_uri(su.origin))
				if su.mimetype :
					tmpl.append("zgst:%s" % su.mimetype)
				if su.storage :
					tmpl.append("zgss:%s" % su.storage)
			
			tmpl = "(" + ") AND (".join(tmpl) + ")"
			query.append(tmpl)
		
		return " OR ".join(query)
	
	def _compile_time_range_filter_query (self, time_range):
		"""Takes a TimeRange and compiles a range query for it"""
		
		print "_compile_time_range_filter_query"
		exit(1)
		if not isinstance(time_range, TimeRange):
			raise TypeError("Expected TimeRange, but found %s" % type(time_range))
		
		return "%s..%sms" % (time_range.begin, time_range.end)

if __name__ == "__main__":
	indexer = Indexer(None)
	print indexer._compile_filter_query([Event.new_for_values(subject_interpretation="http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Document")])
