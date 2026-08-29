_A=None
class Node:
	def __init__(A,tag,value,start_mark,end_mark):A.tag=tag;A.value=value;A.start_mark=start_mark;A.end_mark=end_mark
	def __repr__(A):B=A.value;B=repr(B);return'%s(tag=%r, value=%s)'%(A.__class__.__name__,A.tag,B)
class ScalarNode(Node):
	id='scalar'
	def __init__(A,tag,value,start_mark=_A,end_mark=_A,style=_A):A.tag=tag;A.value=value;A.start_mark=start_mark;A.end_mark=end_mark;A.style=style
class CollectionNode(Node):
	def __init__(A,tag,value,start_mark=_A,end_mark=_A,flow_style=_A):A.tag=tag;A.value=value;A.start_mark=start_mark;A.end_mark=end_mark;A.flow_style=flow_style
class SequenceNode(CollectionNode):id='sequence'
class MappingNode(CollectionNode):id='mapping'