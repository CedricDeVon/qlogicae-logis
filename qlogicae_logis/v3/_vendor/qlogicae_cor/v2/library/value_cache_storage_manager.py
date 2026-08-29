from __future__ import annotations
R='destination is neither a dictionary nor a list'
Q=print
P=ValueError
L=tuple
O=None
N=IndexError
M=KeyError
K=type
J=len
I=int
G=True
B=False
F=list
E=dict
D=TypeError
A=isinstance
__all__='ValueCacheStorageManager',
from typing import Any
C=O
def H():global H;global C;import json;C=json;H=lambda:O
class S:
	__slots__='_collection',
	def __init__(A):H();A._collection={}
	@property
	def collection(self):return self._collection
	def is_key_found(H,keys):
		if not keys:return B
		C=H._collection
		for D in keys:
			if A(C,E):
				if D not in C:return B
			elif A(C,(F,L)):
				if not A(D,I):return B
				if D<0 or D>=J(C):return B
			else:return B
			C=C[D]
		return G
	def get_one_value(D,keys):
		if not keys:return
		B=D._collection
		for C in keys:
			if A(B,E):
				if C not in B:return
			elif A(B,(F,L)):
				if not A(C,I):return
				if C<0 or C>=J(B):return
			else:return
			B=B[C]
		return B
	def set_one_value(Q,keys,value,create_missing=G):
		O=value;L=keys
		if not L:raise P("'keys' cannot be empty")
		B=Q._collection
		for C in L[:-1]:
			if A(B,E):
				if C not in B:
					if not create_missing:raise M(f"key path '{L}' not found")
					B[C]={}
				elif not A(B[C],(E,F)):raise D(f"key path '{L}' does not reference a dictionary or list")
				B=B[C]
			elif A(B,F):
				if not A(C,I):raise D(f"expected an index, got '{K(C).__name__}'")
				if C<0 or C>=J(B):raise N(f"index '{C}' is out of range")
				B=B[C]
			else:raise D(f"cannot traverse into '{K(B).__name__}'")
		H=L[-1]
		if A(B,E):B[H]=O
		elif A(B,F):
			if not A(H,I):raise D(f"expected an index, got {K(H).__name__}")
			if H<0 or H>=J(B):raise N(f"index '{H}' is out of range")
			B[H]=O
		else:raise D(R)
		return G
	def remove_one_value(Q,keys):
		L=keys
		if not L:raise P('keys cannot be empty')
		B=Q._collection
		for H in L[:-1]:
			if A(B,E):
				if H not in B:raise M(f"key path '{L}' not found")
			elif A(B,F):
				if not A(H,I):raise D(f"expected an index, got {K(H).__name__}")
				if H<0 or H>=J(B):raise N(f"index path '{L}' is out of range")
			else:raise D(f"cannot traverse into '{K(B).__name__}'")
			B=B[H]
		C=L[-1]
		if A(B,E):
			try:del B[C]
			except M:raise M(f"key '{C}' not found")from O
		elif A(B,F):
			if not A(C,I):raise D(f"expected an index, got {K(C).__name__}")
			if C<0 or C>=J(B):raise N(f"index '{C}' is out of range")
			del B[C]
		else:raise D(R)
		return G
	def clear_all_values(A):A._collection.clear();return G
	def display_one_item(A,key):Q(f"- {key}: {A._collection[key]}");return G
	def display_all_items(A):Q(C.dumps(A._collection,indent=2,sort_keys=B,ensure_ascii=B,default=str));return G