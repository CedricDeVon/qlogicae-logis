from __future__ import annotations
W='key'
V=print
U=RuntimeError
T=tuple
S=dict
R=str
O=ValueError
N=bool
M=Exception
L='created_at'
K=False
J='value'
I=int
G=float
E=TypeError
D=property
C=True
B=isinstance
A=None
__all__='DiskCacheStorageManager',
from typing import Any,cast
P=A
H=A
F=A
def Q():global Q;global P;global H;global F;import pickle as B,time;from dbm import gnu;P=gnu;H=B;F=time;Q=lambda:A
class X:
	__slots__='_database','_database_path','_create_missing','_lifespan_in_seconds','_file_mode','_key_encoding','_pickle_protocol','_auto_remove_expired','_auto_remove_invalid','_sync_on_write'
	def __init__(B):Q();B._database=A;B._database_path='cache.db';B._create_missing=C;B._lifespan_in_seconds=.0;B._file_mode=384;B._key_encoding='utf-8';B._pickle_protocol=H.HIGHEST_PROTOCOL;B._auto_remove_expired=C;B._auto_remove_invalid=C;B._sync_on_write=K
	def __exit__(A,exc_type,exc_value,traceback):A.close()
	def __del__(B):
		C=B._database
		if C is not A:
			try:C.close()
			except M:pass
			B._database=A
	@D
	def is_open(self):return self._database is not A
	@D
	def database_path(self):return self._database_path
	@database_path.setter
	def database_path(self,value):
		A=value
		if not B(A,R):raise E("'database_path' must be a string")
		self._ensure_closed();self._database_path=A
	@D
	def create_missing(self):return self._create_missing
	@create_missing.setter
	def create_missing(self,value):
		A=value
		if not B(A,N):raise E("'create_missing' must be a boolean")
		self._ensure_closed();self._create_missing=A
	@D
	def lifespan_in_seconds(self):return self._lifespan_in_seconds
	@lifespan_in_seconds.setter
	def lifespan_in_seconds(self,value):
		A=value
		if not B(A,(I,G)):raise E("'lifespan_in_seconds' must be a number")
		if A<0:raise O("'lifespan_in_seconds' must be >= 0")
		self._lifespan_in_seconds=G(A)
	@D
	def file_mode(self):return self._file_mode
	@file_mode.setter
	def file_mode(self,value):
		A=value
		if not B(A,I):raise E("'file_mode' must be an integer")
		if A<0 or A>511:raise O("'file_mode' must be between 0 and 0o777")
		self._ensure_closed();self._file_mode=A
	@D
	def key_encoding(self):return self._key_encoding
	@key_encoding.setter
	def key_encoding(self,value):
		A=value
		if not B(A,R):raise E("'key_encoding' must be a string")
		try:''.encode(A)
		except LookupError as C:raise O(f"unknown encoding: '{A}'")from C
		self._key_encoding=A
	@D
	def pickle_protocol(self):return self._pickle_protocol
	@pickle_protocol.setter
	def pickle_protocol(self,value):
		A=value
		if not B(A,I):raise E("'pickle_protocol' must be an integer")
		if not 0<=A<=H.HIGHEST_PROTOCOL:raise O("'pickle_protocol' is outside the supported range")
		self._pickle_protocol=A
	@D
	def auto_remove_expired(self):return self._auto_remove_expired
	@auto_remove_expired.setter
	def auto_remove_expired(self,value):
		A=value
		if not B(A,N):raise E("'auto_remove_expired' must be a boolean")
		self._auto_remove_expired=A
	@D
	def auto_remove_invalid(self):return self._auto_remove_invalid
	@auto_remove_invalid.setter
	def auto_remove_invalid(self,value):
		A=value
		if not B(A,N):raise E("'auto_remove_invalid' must be a boolean")
		self._auto_remove_invalid=A
	@D
	def sync_on_write(self):return self._sync_on_write
	@sync_on_write.setter
	def sync_on_write(self,value):
		A=value
		if not B(A,N):raise E("'sync_on_write' must be a boolean")
		self._sync_on_write=A
	def _ensure_closed(B):
		if B._database is not A:raise U('database must be closed before changing database configuration')
	def _require_database(C):
		B=C._database
		if B is A:raise U('database is not open')
		return B
	def open(B):
		if B._database is not A:return K
		B._database=P.open(B.database_path,'c'if B.create_missing else'r',B.file_mode);return C
	def close(B):
		D=B._database
		if D is A:return K
		try:D.close()
		finally:B._database=A
		return C
	def _sync_database(A,database):
		if A.sync_on_write:database.sync()
	def _encode_key(C,key_path):
		A=key_path
		if not B(A,R):raise E("'key_path' must be a string")
		return A.encode(C.key_encoding)
	def _decode_key(A,key_path):return key_path.decode(A.key_encoding)
	def _serialize(A,value):return cast(bytes,H.dumps(value,protocol=A.pickle_protocol))
	@staticmethod
	def _deserialize(value):return H.loads(value)
	def _is_expired(A,created_at,current_time):
		if A.lifespan_in_seconds<=0:return K
		return current_time-created_at>=A.lifespan_in_seconds
	def _read_item(A,database,encoded_key,current_time):
		D=encoded_key;C=database
		if D not in C:return
		try:E=A._deserialize(C[D])
		except M:
			if A.auto_remove_invalid:del C[D]
			return
		if not B(E,S):
			if A.auto_remove_invalid:del C[D]
			return
		if L not in E or J not in E:
			if A.auto_remove_invalid:del C[D]
			return
		F=E[L]
		if not B(F,(I,G)):
			if A.auto_remove_invalid:del C[D]
			return
		if A._is_expired(G(F),current_time):
			if A.auto_remove_expired:del C[D]
			return
		return E
	def is_keys_found(B,key_paths):
		E=B._require_database();G=F.time();C={}
		for D in key_paths:H=B._encode_key(D);C[D]=B._read_item(E,H,G)is not A
		return C
	def is_key_found(B,key_path):A=key_path;return B.is_keys_found((A,))[A]
	def is_key_expired(C,key_paths):
		H=C._require_database();O=F.time();D={}
		for E in key_paths:
			J=C._encode_key(E)
			if J not in H:D[E]=A;continue
			try:K=C._deserialize(H[J])
			except M:
				if C.auto_remove_invalid:del H[J]
				D[E]=A;continue
			if not B(K,S):
				if C.auto_remove_invalid:del H[J]
				D[E]=A;continue
			N=K.get(L)
			if not B(N,(I,G)):
				if C.auto_remove_invalid:del H[J]
				D[E]=A;continue
			D[E]=C._is_expired(G(N),O)
		return D
	def is_item_expired(B,key_path):A=key_path;return B.is_key_expired((A,))[A]
	def get_many_values(B,key_paths):
		G=B._require_database();H=F.time();C={}
		for D in key_paths:
			I=B._encode_key(D);E=B._read_item(G,I,H)
			if E is A:C[D]=A
			else:C[D]=E[J]
		return C
	def get_one_value(B,key_path):A=key_path;return B.get_many_values((A,))[A]
	def set_many_values(A,values):
		B=A._require_database();D=F.time()
		for(E,G)in values.items():H=A._encode_key(E);B[H]=A._serialize({L:D,J:G})
		A._sync_database(B);return C
	def set_one_value(A,key_path,value):return A.set_many_values({key_path:value})
	def remove_many_values(A,key_paths):
		B=A._require_database();D={}
		for E in key_paths:
			F=A._encode_key(E)
			if F not in B:D[E]=K;continue
			del B[F];D[E]=C
		A._sync_database(B);return D
	def remove_one_value(B,key_path):A=key_path;return B.remove_many_values((A,))[A]
	def clear_all_values(B):
		A=B._require_database()
		for D in T(A.keys()):del A[D]
		B._sync_database(A);return C
	def remove_expired_values(A):
		C=A._require_database();K=F.time();D=0
		for E in T(C.keys()):
			try:H=A._deserialize(C[E])
			except M:
				if A.auto_remove_invalid:del C[E];D+=1
				continue
			if not B(H,S):
				if A.auto_remove_invalid:del C[E];D+=1
				continue
			J=H.get(L)
			if not B(J,(I,G)):
				if A.auto_remove_invalid:del C[E];D+=1
				continue
			if A._is_expired(G(J),K):del C[E];D+=1
		A._sync_database(C);return D
	def reorganize(A):B=A._require_database();B.reorganize();return C
	def sync(A):B=A._require_database();B.sync();return C
	def display_many_items(A,key_paths):
		B=A.get_many_values(key_paths)
		for(D,E)in B.items():V({W:D,J:E})
		return C
	def display_one_item(A,key_path):return A.display_many_items((key_path,))
	def display_all_items(B):
		D=B._require_database();H=F.time()
		for E in T(D.keys()):
			I=B._decode_key(E);G=B._read_item(D,E,H)
			if G is A:continue
			V({W:I,J:G[J]})
		return C