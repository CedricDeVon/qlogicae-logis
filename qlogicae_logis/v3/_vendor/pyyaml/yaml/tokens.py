B=None
class A:
	def __init__(A,start_mark,end_mark):A.start_mark=start_mark;A.end_mark=end_mark
	def __repr__(A):B=[A for A in A.__dict__ if not A.endswith('_mark')];B.sort();C=', '.join(['%s=%r'%(B,getattr(A,B))for B in B]);return'%s(%s)'%(A.__class__.__name__,C)
class C(A):
	id='<directive>'
	def __init__(A,name,value,start_mark,end_mark):A.name=name;A.value=value;A.start_mark=start_mark;A.end_mark=end_mark
class D(A):id='<document start>'
class E(A):id='<document end>'
class F(A):
	id='<stream start>'
	def __init__(A,start_mark=B,end_mark=B,encoding=B):A.start_mark=start_mark;A.end_mark=end_mark;A.encoding=encoding
class G(A):id='<stream end>'
class H(A):id='<block sequence start>'
class I(A):id='<block mapping start>'
class J(A):id='<block end>'
class K(A):id='['
class L(A):id='{'
class M(A):id=']'
class N(A):id='}'
class O(A):id='?'
class P(A):id=':'
class Q(A):id='-'
class R(A):id=','
class S(A):
	id='<alias>'
	def __init__(A,value,start_mark,end_mark):A.value=value;A.start_mark=start_mark;A.end_mark=end_mark
class T(A):
	id='<anchor>'
	def __init__(A,value,start_mark,end_mark):A.value=value;A.start_mark=start_mark;A.end_mark=end_mark
class U(A):
	id='<tag>'
	def __init__(A,value,start_mark,end_mark):A.value=value;A.start_mark=start_mark;A.end_mark=end_mark
class V(A):
	id='<scalar>'
	def __init__(A,value,plain,start_mark,end_mark,style=B):A.value=value;A.plain=plain;A.start_mark=start_mark;A.end_mark=end_mark;A.style=style