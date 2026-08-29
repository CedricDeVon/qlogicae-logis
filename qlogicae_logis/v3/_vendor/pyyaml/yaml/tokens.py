_A=None
class Token:
	def __init__(A,start_mark,end_mark):A.start_mark=start_mark;A.end_mark=end_mark
	def __repr__(A):B=[A for A in A.__dict__ if not A.endswith('_mark')];B.sort();C=', '.join(['%s=%r'%(B,getattr(A,B))for B in B]);return'%s(%s)'%(A.__class__.__name__,C)
class DirectiveToken(Token):
	id='<directive>'
	def __init__(A,name,value,start_mark,end_mark):A.name=name;A.value=value;A.start_mark=start_mark;A.end_mark=end_mark
class DocumentStartToken(Token):id='<document start>'
class DocumentEndToken(Token):id='<document end>'
class StreamStartToken(Token):
	id='<stream start>'
	def __init__(A,start_mark=_A,end_mark=_A,encoding=_A):A.start_mark=start_mark;A.end_mark=end_mark;A.encoding=encoding
class StreamEndToken(Token):id='<stream end>'
class BlockSequenceStartToken(Token):id='<block sequence start>'
class BlockMappingStartToken(Token):id='<block mapping start>'
class BlockEndToken(Token):id='<block end>'
class FlowSequenceStartToken(Token):id='['
class FlowMappingStartToken(Token):id='{'
class FlowSequenceEndToken(Token):id=']'
class FlowMappingEndToken(Token):id='}'
class KeyToken(Token):id='?'
class ValueToken(Token):id=':'
class BlockEntryToken(Token):id='-'
class FlowEntryToken(Token):id=','
class AliasToken(Token):
	id='<alias>'
	def __init__(A,value,start_mark,end_mark):A.value=value;A.start_mark=start_mark;A.end_mark=end_mark
class AnchorToken(Token):
	id='<anchor>'
	def __init__(A,value,start_mark,end_mark):A.value=value;A.start_mark=start_mark;A.end_mark=end_mark
class TagToken(Token):
	id='<tag>'
	def __init__(A,value,start_mark,end_mark):A.value=value;A.start_mark=start_mark;A.end_mark=end_mark
class ScalarToken(Token):
	id='<scalar>'
	def __init__(A,value,plain,start_mark,end_mark,style=_A):A.value=value;A.plain=plain;A.start_mark=start_mark;A.end_mark=end_mark;A.style=style