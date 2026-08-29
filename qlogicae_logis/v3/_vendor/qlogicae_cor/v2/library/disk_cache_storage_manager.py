from __future__ import annotations
_E='created_at'
_D=False
_C='value'
_B=True
_A=None
__all__='DiskCacheStorageManager',
from typing import Any,cast
_dbm_gnu=_A
_pickle=_A
_time=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _dbm_gnu;global _pickle;global _time;import pickle as A,time;from dbm import gnu;_dbm_gnu=gnu;_pickle=A;_time=time;_handle_dynamic_imports=lambda:_A
class DiskCacheStorageManager:
	__slots__='_database','_database_path','_create_missing','_lifespan_in_seconds','_file_mode','_key_encoding','_pickle_protocol','_auto_remove_expired','_auto_remove_invalid','_sync_on_write'
	def __init__(A):_handle_dynamic_imports();A._database=_A;A._database_path='cache.db';A._create_missing=_B;A._lifespan_in_seconds=.0;A._file_mode=384;A._key_encoding='utf-8';A._pickle_protocol=_pickle.HIGHEST_PROTOCOL;A._auto_remove_expired=_B;A._auto_remove_invalid=_B;A._sync_on_write=_D
	def __exit__(A,exc_type,exc_value,traceback):A.close()
	def __del__(A):
		B=A._database
		if B is not _A:
			try:B.close()
			except Exception:pass
			A._database=_A
	@property
	def is_open(self):return self._database is not _A
	@property
	def database_path(self):return self._database_path
	@database_path.setter
	def database_path(self,value):
		A=value
		if not isinstance(A,str):raise TypeError("'database_path' must be a string")
		self._ensure_closed();self._database_path=A
	@property
	def create_missing(self):return self._create_missing
	@create_missing.setter
	def create_missing(self,value):
		A=value
		if not isinstance(A,bool):raise TypeError("'create_missing' must be a boolean")
		self._ensure_closed();self._create_missing=A
	@property
	def lifespan_in_seconds(self):return self._lifespan_in_seconds
	@lifespan_in_seconds.setter
	def lifespan_in_seconds(self,value):
		A=value
		if not isinstance(A,(int,float)):raise TypeError("'lifespan_in_seconds' must be a number")
		if A<0:raise ValueError("'lifespan_in_seconds' must be >= 0")
		self._lifespan_in_seconds=float(A)
	@property
	def file_mode(self):return self._file_mode
	@file_mode.setter
	def file_mode(self,value):
		A=value
		if not isinstance(A,int):raise TypeError("'file_mode' must be an integer")
		if A<0 or A>511:raise ValueError("'file_mode' must be between 0 and 0o777")
		self._ensure_closed();self._file_mode=A
	@property
	def key_encoding(self):return self._key_encoding
	@key_encoding.setter
	def key_encoding(self,value):
		A=value
		if not isinstance(A,str):raise TypeError("'key_encoding' must be a string")
		try:''.encode(A)
		except LookupError as B:raise ValueError(f"unknown encoding: '{A}'")from B
		self._key_encoding=A
	@property
	def pickle_protocol(self):return self._pickle_protocol
	@pickle_protocol.setter
	def pickle_protocol(self,value):
		A=value
		if not isinstance(A,int):raise TypeError("'pickle_protocol' must be an integer")
		if not 0<=A<=_pickle.HIGHEST_PROTOCOL:raise ValueError("'pickle_protocol' is outside the supported range")
		self._pickle_protocol=A
	@property
	def auto_remove_expired(self):return self._auto_remove_expired
	@auto_remove_expired.setter
	def auto_remove_expired(self,value):
		A=value
		if not isinstance(A,bool):raise TypeError("'auto_remove_expired' must be a boolean")
		self._auto_remove_expired=A
	@property
	def auto_remove_invalid(self):return self._auto_remove_invalid
	@auto_remove_invalid.setter
	def auto_remove_invalid(self,value):
		A=value
		if not isinstance(A,bool):raise TypeError("'auto_remove_invalid' must be a boolean")
		self._auto_remove_invalid=A
	@property
	def sync_on_write(self):return self._sync_on_write
	@sync_on_write.setter
	def sync_on_write(self,value):
		A=value
		if not isinstance(A,bool):raise TypeError("'sync_on_write' must be a boolean")
		self._sync_on_write=A
	def _ensure_closed(A):
		if A._database is not _A:raise RuntimeError('database must be closed before changing database configuration')
	def _require_database(B):
		A=B._database
		if A is _A:raise RuntimeError('database is not open')
		return A
	def open(A):
		if A._database is not _A:return _D
		A._database=_dbm_gnu.open(A.database_path,'c'if A.create_missing else'r',A.file_mode);return _B
	def close(A):
		B=A._database
		if B is _A:return _D
		try:B.close()
		finally:A._database=_A
		return _B
	def _sync_database(A,database):
		if A.sync_on_write:database.sync()
	def _encode_key(B,key_path):
		A=key_path
		if not isinstance(A,str):raise TypeError("'key_path' must be a string")
		return A.encode(B.key_encoding)
	def _decode_key(A,key_path):return key_path.decode(A.key_encoding)
	def _serialize(A,value):return cast(bytes,_pickle.dumps(value,protocol=A.pickle_protocol))
	@staticmethod
	def _deserialize(value):return _pickle.loads(value)
	def _is_expired(A,created_at,current_time):
		if A.lifespan_in_seconds<=0:return _D
		return current_time-created_at>=A.lifespan_in_seconds
	def _read_item(A,database,encoded_key,current_time):
		C=encoded_key;B=database
		if C not in B:return
		try:D=A._deserialize(B[C])
		except Exception:
			if A.auto_remove_invalid:del B[C]
			return
		if not isinstance(D,dict):
			if A.auto_remove_invalid:del B[C]
			return
		if _E not in D or _C not in D:
			if A.auto_remove_invalid:del B[C]
			return
		E=D[_E]
		if not isinstance(E,(int,float)):
			if A.auto_remove_invalid:del B[C]
			return
		if A._is_expired(float(E),current_time):
			if A.auto_remove_expired:del B[C]
			return
		return D
	def is_keys_found(A,key_paths):
		D=A._require_database();E=_time.time();B={}
		for C in key_paths:F=A._encode_key(C);B[C]=A._read_item(D,F,E)is not _A
		return B
	def is_key_found(B,key_path):A=key_path;return B.is_keys_found((A,))[A]
	def is_key_expired(A,key_paths):
		D=A._require_database();H=_time.time();B={}
		for C in key_paths:
			E=A._encode_key(C)
			if E not in D:B[C]=_A;continue
			try:F=A._deserialize(D[E])
			except Exception:
				if A.auto_remove_invalid:del D[E]
				B[C]=_A;continue
			if not isinstance(F,dict):
				if A.auto_remove_invalid:del D[E]
				B[C]=_A;continue
			G=F.get(_E)
			if not isinstance(G,(int,float)):
				if A.auto_remove_invalid:del D[E]
				B[C]=_A;continue
			B[C]=A._is_expired(float(G),H)
		return B
	def is_item_expired(B,key_path):A=key_path;return B.is_key_expired((A,))[A]
	def get_many_values(A,key_paths):
		E=A._require_database();F=_time.time();B={}
		for C in key_paths:
			G=A._encode_key(C);D=A._read_item(E,G,F)
			if D is _A:B[C]=_A
			else:B[C]=D[_C]
		return B
	def get_one_value(B,key_path):A=key_path;return B.get_many_values((A,))[A]
	def set_many_values(A,values):
		B=A._require_database();C=_time.time()
		for(D,E)in values.items():F=A._encode_key(D);B[F]=A._serialize({_E:C,_C:E})
		A._sync_database(B);return _B
	def set_one_value(A,key_path,value):return A.set_many_values({key_path:value})
	def remove_many_values(A,key_paths):
		B=A._require_database();C={}
		for D in key_paths:
			E=A._encode_key(D)
			if E not in B:C[D]=_D;continue
			del B[E];C[D]=_B
		A._sync_database(B);return C
	def remove_one_value(B,key_path):A=key_path;return B.remove_many_values((A,))[A]
	def clear_all_values(B):
		A=B._require_database()
		for C in tuple(A.keys()):del A[C]
		B._sync_database(A);return _B
	def remove_expired_values(A):
		B=A._require_database();G=_time.time();C=0
		for D in tuple(B.keys()):
			try:E=A._deserialize(B[D])
			except Exception:
				if A.auto_remove_invalid:del B[D];C+=1
				continue
			if not isinstance(E,dict):
				if A.auto_remove_invalid:del B[D];C+=1
				continue
			F=E.get(_E)
			if not isinstance(F,(int,float)):
				if A.auto_remove_invalid:del B[D];C+=1
				continue
			if A._is_expired(float(F),G):del B[D];C+=1
		A._sync_database(B);return C
	def reorganize(A):B=A._require_database();B.reorganize();return _B
	def sync(A):B=A._require_database();B.sync();return _B
	def display_many_items(A,key_paths):
		B=A.get_many_values(key_paths)
		for(C,D)in B.items():print({'key':C,_C:D})
		return _B
	def display_one_item(A,key_path):return A.display_many_items((key_path,))
	def display_all_items(A):
		B=A._require_database();E=_time.time()
		for C in tuple(B.keys()):
			F=A._decode_key(C);D=A._read_item(B,C,E)
			if D is _A:continue
			print({'key':F,_C:D[_C]})
		return _B