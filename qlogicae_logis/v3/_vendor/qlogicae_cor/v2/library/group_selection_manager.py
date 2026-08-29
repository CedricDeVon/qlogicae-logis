from __future__ import annotations
from collections.abc import Hashable,Mapping,Sequence
__all__='GroupSelectionManager'
def _handle_dynamic_imports():global _handle_dynamic_imports;_handle_dynamic_imports=lambda:None
class GroupSelectionManager:
	def __init__(A):_handle_dynamic_imports()
	def flatten_group(E,target,data):
		C=[];D=set();B=[target]
		while B:
			A=B.pop()
			if A in D:continue
			D.add(A)
			if A not in data:C.append(A);continue
			B.extend(reversed(data[A]))
		return tuple(C)