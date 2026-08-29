A=None
class B:
	def __init__(A,tag,value,start_mark,end_mark):A.tag=tag;A.value=value;A.start_mark=start_mark;A.end_mark=end_mark
	def __repr__(A):B=A.value;B=repr(B);return'%s(tag=%r, value=%s)'%(A.__class__.__name__,A.tag,B)
class D(B):
	id='scalar'
	def __init__(A,tag,value,start_mark=A,end_mark=A,style=A):A.tag=tag;A.value=value;A.start_mark=start_mark;A.end_mark=end_mark;A.style=style
class C(B):
	def __init__(A,tag,value,start_mark=A,end_mark=A,flow_style=A):A.tag=tag;A.value=value;A.start_mark=start_mark;A.end_mark=end_mark;A.flow_style=flow_style
class E(C):id='sequence'
class F(C):id='mapping'