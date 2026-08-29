from __future__ import annotations
_C='destination is neither a dictionary nor a list'
_B=True
_A=False
__all__='ValueCacheStorageManager',
from typing import Any
_json=None
def _handle_dynamic_imports():global _handle_dynamic_imports;global _json;import json;_json=json;_handle_dynamic_imports=lambda:None
class ValueCacheStorageManager:
	__slots__='_collection',
	def __init__(A):_handle_dynamic_imports();A._collection={}
	@property
	def collection(self):return self._collection
	def is_key_found(C,keys):
		if not keys:return _A
		A=C._collection
		for B in keys:
			if isinstance(A,dict):
				if B not in A:return _A
			elif isinstance(A,(list,tuple)):
				if not isinstance(B,int):return _A
				if B<0 or B>=len(A):return _A
			else:return _A
			A=A[B]
		return _B
	def get_one_value(C,keys):
		if not keys:return
		A=C._collection
		for B in keys:
			if isinstance(A,dict):
				if B not in A:return
			elif isinstance(A,(list,tuple)):
				if not isinstance(B,int):return
				if B<0 or B>=len(A):return
			else:return
			A=A[B]
		return A
	def set_one_value(F,keys,value,create_missing=_B):
		E=value;D=keys
		if not D:raise ValueError("'keys' cannot be empty")
		A=F._collection
		for B in D[:-1]:
			if isinstance(A,dict):
				if B not in A:
					if not create_missing:raise KeyError(f"key path '{D}' not found")
					A[B]={}
				elif not isinstance(A[B],(dict,list)):raise TypeError(f"key path '{D}' does not reference a dictionary or list")
				A=A[B]
			elif isinstance(A,list):
				if not isinstance(B,int):raise TypeError(f"expected an index, got '{type(B).__name__}'")
				if B<0 or B>=len(A):raise IndexError(f"index '{B}' is out of range")
				A=A[B]
			else:raise TypeError(f"cannot traverse into '{type(A).__name__}'")
		C=D[-1]
		if isinstance(A,dict):A[C]=E
		elif isinstance(A,list):
			if not isinstance(C,int):raise TypeError(f"expected an index, got {type(C).__name__}")
			if C<0 or C>=len(A):raise IndexError(f"index '{C}' is out of range")
			A[C]=E
		else:raise TypeError(_C)
		return _B
	def remove_one_value(E,keys):
		D=keys
		if not D:raise ValueError('keys cannot be empty')
		A=E._collection
		for C in D[:-1]:
			if isinstance(A,dict):
				if C not in A:raise KeyError(f"key path '{D}' not found")
			elif isinstance(A,list):
				if not isinstance(C,int):raise TypeError(f"expected an index, got {type(C).__name__}")
				if C<0 or C>=len(A):raise IndexError(f"index path '{D}' is out of range")
			else:raise TypeError(f"cannot traverse into '{type(A).__name__}'")
			A=A[C]
		B=D[-1]
		if isinstance(A,dict):
			try:del A[B]
			except KeyError:raise KeyError(f"key '{B}' not found")from None
		elif isinstance(A,list):
			if not isinstance(B,int):raise TypeError(f"expected an index, got {type(B).__name__}")
			if B<0 or B>=len(A):raise IndexError(f"index '{B}' is out of range")
			del A[B]
		else:raise TypeError(_C)
		return _B
	def clear_all_values(A):A._collection.clear();return _B
	def display_one_item(A,key):print(f"- {key}: {A._collection[key]}");return _B
	def display_all_items(A):print(_json.dumps(A._collection,indent=2,sort_keys=_A,ensure_ascii=_A,default=str));return _B