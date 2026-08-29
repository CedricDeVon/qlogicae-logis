from __future__ import annotations
from collections.abc import Hashable,Mapping,Sequence
__all__='GroupSelectionManager'
def A():global A;A=lambda:None
class B:
	def __init__(B):A()
	def flatten_group(E,target,data):
		C=[];D=set();B=[target]
		while B:
			A=B.pop()
			if A in D:continue
			D.add(A)
			if A not in data:C.append(A);continue
			B.extend(reversed(data[A]))
		return tuple(C)