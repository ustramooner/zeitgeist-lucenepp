#
# Auto-generated from all .trig files (zg.trig nie.trig nco.trig nfo.trig ncal.trig nao.trig nmo.trig nmm.trig). Do not edit
#
Symbol('CONTACT', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nco#Contact', display_name='Contact', doc='A Contact. A piece of data that can provide means to identify or communicate with an entity.', auto_resolve=False)
Symbol('CONTACT_GROUP', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nco#ContactGroup', display_name='ContactGroup', doc='A group of Contacts. Could be used to express a group in an addressbook or on a contact list of an IM application. One contact can belong to many groups.', auto_resolve=False)
Symbol('CONTACT_LIST', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nco#ContactList', display_name='ContactList', doc='A contact list, this class represents an addressbook or a contact list of an IM application. Contacts inside a contact list can belong to contact groups.', auto_resolve=False)
Symbol('CONTACT_LIST_DATA_OBJECT', parent=set(['Manifestation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nco#ContactListDataObject', display_name='ContactListDataObject', doc='An entity occuring on a contact list (usually interpreted as an nco:Contact)', auto_resolve=False)
Symbol('ORGANIZATION_CONTACT', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nco#Contact']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nco#OrganizationContact', display_name='OrganizationContact', doc='A Contact that denotes on Organization.', auto_resolve=False)
Symbol('PERSON_CONTACT', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nco#Contact']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nco#PersonContact', display_name='PersonContact', doc='A Contact that denotes a Person. A person can have multiple Affiliations.', auto_resolve=False)
Symbol('APPLICATION', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Software']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Application', display_name='Application', doc='An application', auto_resolve=False)
Symbol('ARCHIVE', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#DataContainer']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Archive', display_name='Archive', doc='A compressed file. May contain other files or folder inside.', auto_resolve=False)
Symbol('ARCHIVE_ITEM', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#EmbeddedFileDataObject']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#ArchiveItem', display_name='ArchiveItem', doc='A file entity inside an archive.', auto_resolve=False)
Symbol('ATTACHMENT', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#EmbeddedFileDataObject']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Attachment', display_name='Attachment', doc='A file attached to another data object. Many data formats allow for attachments: emails, vcards, ical events, id3 and exif...', auto_resolve=False)
Symbol('AUDIO', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Media']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Audio', display_name='Audio', doc='A file containing audio content', auto_resolve=False)
Symbol('BOOKMARK', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Bookmark', display_name='Bookmark', doc='A bookmark of a webbrowser. Use nie:title for the name/label, nie:contentCreated to represent the date when the user added the bookmark, and nie:contentLastModified for modifications. nfo:bookmarks to store the link.', auto_resolve=False)
Symbol('BOOKMARK_FOLDER', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#BookmarkFolder', display_name='Bookmark Folder', doc='A folder with bookmarks of a webbrowser. Use nfo:containsBookmark to relate Bookmarks. Folders can contain subfolders, use containsBookmarkFolder to relate them.', auto_resolve=False)
Symbol('CURSOR', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#RasterImage']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Cursor', display_name='Cursor', doc='A Cursor.', auto_resolve=False)
Symbol('DATA_CONTAINER', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#DataContainer', display_name='DataContainer', doc='A superclass for all entities, whose primary purpose is to serve as containers for other data object. They usually don\'t have any \"meaning\" by themselves. Examples include folders, archives and optical disc images.', auto_resolve=False)
Symbol('DELETED_RESOURCE', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#FileDataObject']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#DeletedResource', display_name='DeletedResource', doc='A file entity that has been deleted from the original source. Usually such entities are stored within various kinds of \'Trash\' or \'Recycle Bin\' folders.', auto_resolve=False)
Symbol('DOCUMENT', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Document', display_name='Document', doc='A generic document. A common superclass for all documents on the desktop.', auto_resolve=False)
Symbol('EMBEDDED_FILE_DATA_OBJECT', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#FileDataObject']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#EmbeddedFileDataObject', display_name='EmbeddedFileDataObject', doc='A file embedded in another data object. There are many ways in which a file may be embedded in another one. Use this class directly only in cases if none of the subclasses gives a better description of your case.', auto_resolve=False)
Symbol('EXECUTABLE', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Executable', display_name='Executable', doc='An executable file.', auto_resolve=False)
Symbol('FILE_DATA_OBJECT', parent=set(['Manifestation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#FileDataObject', display_name='File', doc='A resource containing a finite sequence of bytes with arbitrary information, that is available to a computer program and is usually based on some kind of durable storage. A file is durable in the sense that it remains available for programs to use after the current program has finished.', auto_resolve=False)
Symbol('FILESYSTEM', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#DataContainer']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Filesystem', display_name='Filesystem', doc='A filesystem. Examples of filesystems include hard disk partitions, removable media, but also images thereof stored in files.', auto_resolve=False)
Symbol('FILESYSTEM_IMAGE', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Filesystem']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#FilesystemImage', display_name='FilesystemImage', doc='An image of a filesystem. Instances of this class may include CD images, DVD images or hard disk partition images created by various pieces of software (e.g. Norton Ghost)', auto_resolve=False)
Symbol('FOLDER', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#DataContainer']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Folder', display_name='Folder', doc='A folder/directory. Examples of folders include folders on a filesystem and message folders in a mailbox.', auto_resolve=False)
Symbol('FONT', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Font', display_name='Font', doc='A font.', auto_resolve=False)
Symbol('HARD_DISK_PARTITION', parent=set(['Manifestation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#HardDiskPartition', display_name='HardDiskPartition', doc='A partition on a hard disk', auto_resolve=False)
Symbol('HTML_DOCUMENT', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#PlainTextDocument']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#HtmlDocument', display_name='HtmlDocument', doc='A HTML document, may contain links to other files.', auto_resolve=False)
Symbol('ICON', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Image']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Icon', display_name='Icon', doc='An Icon (regardless of whether it\'s a raster or a vector icon. A resource representing an icon could have two types (Icon and Raster, or Icon and Vector) if required.', auto_resolve=False)
Symbol('IMAGE', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Visual']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Image', display_name='Image', doc='A file containing an image.', auto_resolve=False)
Symbol('MEDIA', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Media', display_name='Media', doc='A piece of media content. This class may be used to express complex media containers with many streams of various media content (both aural and visual).', auto_resolve=False)
Symbol('MEDIA_LIST', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#MediaList', display_name='MediaList', doc='A file containing a list of media files.e.g. a playlist', auto_resolve=False)
Symbol('MEDIA_STREAM', parent=set(['Manifestation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#MediaStream', display_name='MediaStream', doc='A stream of multimedia content, usually contained within a media container such as a movie (containing both audio and video) or a DVD (possibly containing many streams of audio and video). Most common interpretations for such a DataObject include Audio and Video.', auto_resolve=False)
Symbol('MIND_MAP', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Document']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#MindMap', display_name='MindMap', doc='A MindMap, created by a mind-mapping utility. Examples might include FreeMind or mind mapper.', auto_resolve=False)
Symbol('OPERATING_SYSTEM', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Software']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#OperatingSystem', display_name='OperatingSystem', doc='An OperatingSystem', auto_resolve=False)
Symbol('PAGINATED_TEXT_DOCUMENT', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#TextDocument']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#PaginatedTextDocument', display_name='PaginatedTextDocument', doc='A file containing a text document, that is unambiguously divided into pages. Examples might include PDF, DOC, PS, DVI etc.', auto_resolve=False)
Symbol('PLAIN_TEXT_DOCUMENT', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#TextDocument']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#PlainTextDocument', display_name='PlainTextDocument', doc='A file containing plain text (ASCII, Unicode or other encodings). Examples may include TXT, HTML, XML, program source code etc.', auto_resolve=False)
Symbol('PRESENTATION', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Document']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Presentation', display_name='Presentation', doc='A Presentation made by some presentation software (Corel Presentations, OpenOffice Impress, MS Powerpoint etc.)', auto_resolve=False)
Symbol('RASTER_IMAGE', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Image']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#RasterImage', display_name='RasterImage', doc='A raster image.', auto_resolve=False)
Symbol('REMOTE_DATA_OBJECT', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#FileDataObject']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#RemoteDataObject', display_name='RemoteDataObject', doc='A file data object stored at a remote location. Don\'t confuse this class with a RemotePortAddress. This one applies to a particular resource, RemotePortAddress applies to an address, that can have various interpretations.', auto_resolve=False)
Symbol('REMOTE_PORT_ADDRESS', parent=set(['Manifestation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#RemotePortAddress', display_name='RemotePortAddress', doc='An address specifying a remote host and port. Such an address can be interpreted in many ways (examples of such interpretations include mailboxes, websites, remote calendars or filesystems), depending on an interpretation, various kinds of data may be extracted from such an address.', auto_resolve=False)
Symbol('SOFTWARE', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Software', display_name='Software', doc='A piece of software. Examples may include applications and the operating system. This interpretation most commonly applies to SoftwareItems.', auto_resolve=False)
Symbol('SOFTWARE_ITEM', parent=set(['Manifestation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#SoftwareItem', display_name='SoftwareItem', doc='A DataObject representing a piece of software. Examples of interpretations of a SoftwareItem include an Application and an OperatingSystem.', auto_resolve=False)
Symbol('SOFTWARE_SERVICE', parent=set(['Manifestation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#SoftwareService', display_name='SoftwareService', doc='A service published by a piece of software, either by an operating system or an application. Examples of such services may include calendar, addresbook and mailbox managed by a PIM application. This category is introduced to distinguish between data available directly from the applications (Via some Interprocess Communication Mechanisms) and data available from files on a disk. In either case both DataObjects would receive a similar interpretation (e.g. a Mailbox) and wouldn\'t differ on the content level.', auto_resolve=False)
Symbol('SOURCE_CODE', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#PlainTextDocument']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#SourceCode', display_name='SourceCode', doc='Code in a compilable or interpreted programming language.', auto_resolve=False)
Symbol('SPREADSHEET', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Document']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Spreadsheet', display_name='Spreadsheet', doc='A spreadsheet, created by a spreadsheet application. Examples might include Gnumeric, OpenOffice Calc or MS Excel.', auto_resolve=False)
Symbol('TEXT_DOCUMENT', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Document']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#TextDocument', display_name='TextDocument', doc='A text document', auto_resolve=False)
Symbol('TRASH', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#DataContainer']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Trash', display_name='Trash', doc='Represents a container for deleted files, a feature common in modern operating systems.', auto_resolve=False)
Symbol('VECTOR_IMAGE', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Image']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#VectorImage', display_name='VectorImage', doc='', auto_resolve=False)
Symbol('VIDEO', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Visual']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Video', display_name='Video', doc='A video file.', auto_resolve=False)
Symbol('VISUAL', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Media']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Visual', display_name='Visual', doc='File containing visual content.', auto_resolve=False)
Symbol('WEBSITE', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Website', display_name='Website', doc='A website, usually a container for remote resources, that may be interpreted as HTMLDocuments, images or other types of content.', auto_resolve=False)
Symbol('EMAIL', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nmo#Message']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nmo#Email', display_name='Email', doc='An email.', auto_resolve=False)
Symbol('IMMESSAGE', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nmo#Message']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nmo#IMMessage', display_name='IMMessage', doc='A message sent with Instant Messaging software.', auto_resolve=False)
Symbol('MAILBOX', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nmo#Mailbox', display_name='Mailbox', doc='A mailbox - container for MailboxDataObjects.', auto_resolve=False)
Symbol('MAILBOX_DATA_OBJECT', parent=set(['Manifestation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nmo#MailboxDataObject', display_name='MailboxDataObject', doc='An entity encountered in a mailbox. Most common interpretations for such an entity include Message or Folder', auto_resolve=False)
Symbol('MESSAGE', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nmo#Message', display_name='Message', doc='A message. Could be an email, instant messanging message, SMS message etc.', auto_resolve=False)
Symbol('MIME_ENTITY', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/03/22/nmo#MimeEntity', display_name='MimeEntity', doc='A MIME entity, as defined in RFC2045, Section 2.4.', auto_resolve=False)
Symbol('ALARM', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/04/02/ncal#Alarm', display_name='Alarm', doc='Provide a grouping of component properties that define an alarm.', auto_resolve=False)
Symbol('ATTACHMENT', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Attachment']), uri='http://www.semanticdesktop.org/ontologies/2007/04/02/ncal#Attachment', display_name='Attachment', doc='An object attached to a calendar entity. This class has been introduced to serve as a structured value of the ncal:attach property. See the documentation of ncal:attach for details.', auto_resolve=False)
Symbol('CALENDAR', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/04/02/ncal#Calendar', display_name='Calendar', doc='A calendar. Inspirations for this class can be traced to the VCALENDAR component defined in RFC 2445 sec. 4.4, but it may just as well be used to represent any kind of Calendar.', auto_resolve=False)
Symbol('CALENDAR_DATA_OBJECT', parent=set(['Manifestation']), uri='http://www.semanticdesktop.org/ontologies/2007/04/02/ncal#CalendarDataObject', display_name='CalendarDataObject', doc='A DataObject found in a calendar. It is usually interpreted as one of the calendar entity types (e.g. Event, Journal, Todo etc.)', auto_resolve=False)
Symbol('EVENT', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/04/02/ncal#Event', display_name='Event', doc='Provide a grouping of component properties that describe an event.', auto_resolve=False)
Symbol('FREEBUSY', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/04/02/ncal#Freebusy', display_name='Freebusy', doc='Provide a grouping of component properties that describe either a request for free/busy time, describe a response to a request for free/busy time or describe a published set of busy time.', auto_resolve=False)
Symbol('JOURNAL', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/04/02/ncal#Journal', display_name='Journal', doc='Provide a grouping of component properties that describe a journal entry.', auto_resolve=False)
Symbol('TIMEZONE', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/04/02/ncal#Timezone', display_name='Timezone', doc='Provide a grouping of component properties that defines a time zone.', auto_resolve=False)
Symbol('TODO', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2007/04/02/ncal#Todo', display_name='Todo', doc='Provide a grouping of calendar properties that describe a to-do.', auto_resolve=False)
Symbol('MOVIE', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Video']), uri='http://www.semanticdesktop.org/ontologies/2009/02/19/nmm#Movie', display_name='movie', doc='A Movie', auto_resolve=False)
Symbol('MUSIC_ALBUM', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#MediaList']), uri='http://www.semanticdesktop.org/ontologies/2009/02/19/nmm#MusicAlbum', display_name='music album', doc='The music album as provided by the publisher. Not to be confused with media lists or collections.', auto_resolve=False)
Symbol('MUSIC_PIECE', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Media']), uri='http://www.semanticdesktop.org/ontologies/2009/02/19/nmm#MusicPiece', display_name='music', doc='Used to assign music-specific properties such a BPM to video and audio', auto_resolve=False)
Symbol('TVSERIES', parent=set(['Interpretation']), uri='http://www.semanticdesktop.org/ontologies/2009/02/19/nmm#TVSeries', display_name='tv series', doc='A TV Series has multiple seasons and episodes', auto_resolve=False)
Symbol('TVSHOW', parent=set(['http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Video']), uri='http://www.semanticdesktop.org/ontologies/2009/02/19/nmm#TVShow', display_name='tv show', doc='A TV Show', auto_resolve=False)
Symbol('ACCEPT_EVENT', parent=set(['http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventInterpretation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#AcceptEvent', display_name='ACCEPT_EVENT', doc='Event triggered when the user accepts a request of some sort. Examples could be answering a phone call, accepting a file transfer, or accepting a friendship request over an IM protocol. See also DenyEvent for when the user denies a similar request', auto_resolve=False)
Symbol('ACCESS_EVENT', parent=set(['http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventInterpretation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#AccessEvent', display_name='ACCESS_EVENT', doc='Event triggered by opening, accessing, or starting a resource. Most zg:AccessEvents will have an accompanying zg:LeaveEvent, but this need not always be the case', auto_resolve=False)
Symbol('CREATE_EVENT', parent=set(['http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventInterpretation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#CreateEvent', display_name='CREATE_EVENT', doc='Event type triggered when an item is created', auto_resolve=False)
Symbol('DELETE_EVENT', parent=set(['http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventInterpretation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#DeleteEvent', display_name='DELETE_EVENT', doc='Event triggered because a resource has been deleted or otherwise made permanently unavailable. Fx. when deleting a file. FIXME: How about when moving to trash?', auto_resolve=False)
Symbol('DENY_EVENT', parent=set(['http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventInterpretation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#DenyEvent', display_name='DENY_EVENT', doc='Event triggered when the user denies a request of some sort. Examples could be rejecting a phone call, rejecting a file transfer, or denying a friendship request over an IM protocol. See also AcceptEvent for the converse event type', auto_resolve=False)
Symbol('EVENT_INTERPRETATION', parent=set(['Interpretation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventInterpretation', display_name='EVENT_INTERPRETATION', doc='Base class for event interpretations. Please do no instantiate directly, but use one of the sub classes. The interpretation of an event describes \'what happened\' - fx. \'something was created\' or \'something was accessed\'', auto_resolve=False)
Symbol('EVENT_MANIFESTATION', parent=set(['Manifestation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventManifestation', display_name='EVENT_MANIFESTATION', doc='Base class for event manifestation types. Please do no instantiate directly, but use one of the sub classes. The manifestation of an event describes \'how it happened\'. Fx. \'the user did this\' or \'the system notified the user\'', auto_resolve=False)
Symbol('EXPIRE_EVENT', parent=set(['http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventInterpretation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#ExpireEvent', display_name='EXPIRE_EVENT', doc='Event triggered when something expires or times out. These types of events are normally not triggered by the user, but by the operating system or some external party. Examples are a recurring calendar item or task deadline that expires or a when the user fails to respond to an external request such as a phone call', auto_resolve=False)
Symbol('HEURISTIC_ACTIVITY', parent=set(['http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventManifestation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#HeuristicActivity', display_name='HEURISTIC_ACTIVITY', doc='An event that is caused indirectly from user activity or deducted via analysis of other events. Fx. if an algorithm divides a user workflow into disjoint \'projects\' based on temporal analysis it could insert heuristic events when the user changed project', auto_resolve=False)
Symbol('LEAVE_EVENT', parent=set(['http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventInterpretation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#LeaveEvent', display_name='LEAVE_EVENT', doc='Event triggered by closing, leaving, or stopping a resource. Most zg:LeaveEvents will be following a zg:Access event, but this need not always be the case', auto_resolve=False)
Symbol('MODIFY_EVENT', parent=set(['http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventInterpretation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#ModifyEvent', display_name='MODIFY_EVENT', doc='Event triggered by modifying an existing resources. Fx. when editing and saving a file on disk or correcting a typo in the name of a contact', auto_resolve=False)
Symbol('RECEIVE_EVENT', parent=set(['http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventInterpretation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#ReceiveEvent', display_name='RECEIVE_EVENT', doc='Event triggered when something is received from an external party. The event manifestation must be set according to the world view of the receiving party. Most often the item that is being received will be some sort of message - an email, instant message, or broadcasted media such as micro blogging', auto_resolve=False)
Symbol('SCHEDULED_ACTIVITY', parent=set(['http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventManifestation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#ScheduledActivity', display_name='SCHEDULED_ACTIVITY', doc='An event that was directly triggered by some user initiated sequence of actions. For example a music player automatically changing to the next song in a playlist', auto_resolve=False)
Symbol('SEND_EVENT', parent=set(['http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventInterpretation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#SendEvent', display_name='SEND_EVENT', doc='Event triggered when something is send to an external party. The event manifestation must be set according to the world view of the sending party. Most often the item that is being send will be some sort of message - an email, instant message, or broadcasted media such as micro blogging', auto_resolve=False)
Symbol('SYSTEM_NOTIFICATION', parent=set(['http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventManifestation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#SystemNotification', display_name='SYSTEM_NOTIFICATION', doc='An event send to the user by the operating system. Examples could include when the user inserts a USB stick or when the system warns that the hard disk is full', auto_resolve=False)
Symbol('USER_ACTIVITY', parent=set(['http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventManifestation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#UserActivity', display_name='USER_ACTIVITY', doc='An event that was actively performed by the user. For example saving or opening a file by clicking on it in the file manager', auto_resolve=False)
Symbol('WORLD_ACTIVITY', parent=set(['http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#EventManifestation']), uri='http://www.zeitgeist-project.com/ontologies/2010/01/27/zg#WorldActivity', display_name='WORLD_ACTIVITY', doc='An event that was performed by an entity, usually human or organization, other than the user. An example could be logging the activities of other people in a team', auto_resolve=False)

