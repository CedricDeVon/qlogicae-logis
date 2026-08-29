_A=None
class Event:
	def __init__(A,start_mark=_A,end_mark=_A):A.start_mark=start_mark;A.end_mark=end_mark
	def __repr__(A):B=[B for B in['anchor','tag','implicit','value']if hasattr(A,B)];C=', '.join(['%s=%r'%(B,getattr(A,B))for B in B]);return'%s(%s)'%(A.__class__.__name__,C)
class NodeEvent(Event):
	def __init__(A,anchor,start_mark=_A,end_mark=_A):A.anchor=anchor;A.start_mark=start_mark;A.end_mark=end_mark
class CollectionStartEvent(NodeEvent):
	def __init__(A,anchor,tag,implicit,start_mark=_A,end_mark=_A,flow_style=_A):A.anchor=anchor;A.tag=tag;A.implicit=implicit;A.start_mark=start_mark;A.end_mark=end_mark;A.flow_style=flow_style
class CollectionEndEvent(Event):0
class StreamStartEvent(Event):
	def __init__(A,start_mark=_A,end_mark=_A,encoding=_A):A.start_mark=start_mark;A.end_mark=end_mark;A.encoding=encoding
class StreamEndEvent(Event):0
class DocumentStartEvent(Event):
	def __init__(A,start_mark=_A,end_mark=_A,explicit=_A,version=_A,tags=_A):A.start_mark=start_mark;A.end_mark=end_mark;A.explicit=explicit;A.version=version;A.tags=tags
class DocumentEndEvent(Event):
	def __init__(A,start_mark=_A,end_mark=_A,explicit=_A):A.start_mark=start_mark;A.end_mark=end_mark;A.explicit=explicit
class AliasEvent(NodeEvent):0
class ScalarEvent(NodeEvent):
	def __init__(A,anchor,tag,implicit,value,start_mark=_A,end_mark=_A,style=_A):A.anchor=anchor;A.tag=tag;A.implicit=implicit;A.value=value;A.start_mark=start_mark;A.end_mark=end_mark;A.style=style
class SequenceStartEvent(CollectionStartEvent):0
class SequenceEndEvent(CollectionEndEvent):0
class MappingStartEvent(CollectionStartEvent):0
class MappingEndEvent(CollectionEndEvent):0