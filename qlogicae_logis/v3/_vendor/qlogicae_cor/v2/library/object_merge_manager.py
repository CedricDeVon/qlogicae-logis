from __future__ import annotations
_A=None
__all__='ObjectMergeManager',
from typing import Any
_deepcopy=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _deepcopy;from copy import deepcopy as A;_deepcopy=A;_handle_dynamic_imports=lambda:_A
class ObjectMergeManager:
	def __init__(A):_handle_dynamic_imports()
	def deep_merge(F,left,right):
		B=left;A=right
		if B is _A:return _deepcopy(A)
		if A is _A:return _deepcopy(B)
		if isinstance(B,dict)and isinstance(A,dict):
			C=_deepcopy(B)
			for(D,E)in A.items():
				if D in C:C[D]=F.deep_merge(C[D],E)
				else:C[D]=_deepcopy(E)
			return C
		if isinstance(B,list)and isinstance(A,list):return _deepcopy(B)+_deepcopy(A)
		return _deepcopy(A)
	def deep_merge_fragments(F,left,right):
		B=left;A=right
		if B is _A:return _deepcopy(A)
		if A is _A:return _deepcopy(B)
		if isinstance(B,dict)and isinstance(A,dict):
			C=_deepcopy(B)
			for(D,E)in A.items():
				if D in C:C[D]=F.deep_merge_fragments(C[D],E)
				else:C[D]=_deepcopy(E)
			return C
		if isinstance(B,list)and isinstance(A,list):return _deepcopy(A)
		return _deepcopy(A)