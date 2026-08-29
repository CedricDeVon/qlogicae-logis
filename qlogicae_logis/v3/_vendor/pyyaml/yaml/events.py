A=None
class B:
	def __init__(A,start_mark=A,end_mark=A):A.start_mark=start_mark;A.end_mark=end_mark
	def __repr__(A):B=[B for B in['anchor','tag','implicit','value']if hasattr(A,B)];C=', '.join(['%s=%r'%(B,getattr(A,B))for B in B]);return'%s(%s)'%(A.__class__.__name__,C)
class C(B):
	def __init__(A,anchor,start_mark=A,end_mark=A):A.anchor=anchor;A.start_mark=start_mark;A.end_mark=end_mark
class D(C):
	def __init__(A,anchor,tag,implicit,start_mark=A,end_mark=A,flow_style=A):A.anchor=anchor;A.tag=tag;A.implicit=implicit;A.start_mark=start_mark;A.end_mark=end_mark;A.flow_style=flow_style
class E(B):0
class F(B):
	def __init__(A,start_mark=A,end_mark=A,encoding=A):A.start_mark=start_mark;A.end_mark=end_mark;A.encoding=encoding
class G(B):0
class H(B):
	def __init__(A,start_mark=A,end_mark=A,explicit=A,version=A,tags=A):A.start_mark=start_mark;A.end_mark=end_mark;A.explicit=explicit;A.version=version;A.tags=tags
class I(B):
	def __init__(A,start_mark=A,end_mark=A,explicit=A):A.start_mark=start_mark;A.end_mark=end_mark;A.explicit=explicit
class J(C):0
class K(C):
	def __init__(A,anchor,tag,implicit,value,start_mark=A,end_mark=A,style=A):A.anchor=anchor;A.tag=tag;A.implicit=implicit;A.value=value;A.start_mark=start_mark;A.end_mark=end_mark;A.style=style
class L(D):0
class M(E):0
class N(D):0
class O(E):0