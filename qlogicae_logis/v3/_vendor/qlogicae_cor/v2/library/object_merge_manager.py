from __future__ import annotations
H=list
G=dict
D=None
B=isinstance
__all__='ObjectMergeManager',
from typing import Any
A=D
def C():global C;global A;from copy import deepcopy as B;A=B;C=lambda:D
class E:
	def __init__(A):C()
	def deep_merge(K,left,right):
		E=left;C=right
		if E is D:return A(C)
		if C is D:return A(E)
		if B(E,G)and B(C,G):
			F=A(E)
			for(I,J)in C.items():
				if I in F:F[I]=K.deep_merge(F[I],J)
				else:F[I]=A(J)
			return F
		if B(E,H)and B(C,H):return A(E)+A(C)
		return A(C)
	def deep_merge_fragments(K,left,right):
		E=left;C=right
		if E is D:return A(C)
		if C is D:return A(E)
		if B(E,G)and B(C,G):
			F=A(E)
			for(I,J)in C.items():
				if I in F:F[I]=K.deep_merge_fragments(F[I],J)
				else:F[I]=A(J)
			return F
		if B(E,H)and B(C,H):return A(C)
		return A(C)