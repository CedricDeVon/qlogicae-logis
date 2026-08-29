from __future__ import annotations
H=KeyError
G=False
A=None
__all__='ValueCacheManager',
from typing import TYPE_CHECKING as I,Any
if I:from.target_cache_value import TargetCacheValue
D=A
C=A
B=A
E=A
def F():global F;global D;global C;global B;global E;from.filesystem_manager import FilesystemManager as G;from.singleton_manager import SingletonManager as H;from.target_cache_value import TargetCacheValue as I;from.value_cache_storage_manager import ValueCacheStorageManager as J;D=G;C=H;B=I;E=J;F=lambda:A
class J:
	__slots__='_filesystem_manager','_value_cache_storage_manager'
	def __init__(A):F();A._filesystem_manager=C.get_singleton(D);A._value_cache_storage_manager=C.get_singleton(E)
	def is_key_found(A,key_path):B=A._value_cache_storage_manager.is_key_found(key_path);return B
	def get_one_value(D,key_path,output_type=A):
		C=output_type
		if C is A:C=B.DEFINED
		E=D._value_cache_storage_manager.get_one_value(key_path);D.throw_if_value_is_explicitly_invalid(E,C);return E
	def set_one_value(D,key_path,value,output_type=A):
		E=value;C=output_type
		if C is A:C=B.DEFINED
		D.throw_if_value_is_explicitly_invalid(E,C);F=D._value_cache_storage_manager.set_one_value(key_path,E);return F
	def remove_one_value(A,key_path):B=key_path;A.throw_if_key_not_found(B);C=A._value_cache_storage_manager.remove_one_value(B);return C
	def clear_all_values(A):B=A._value_cache_storage_manager.clear_all_values();return B
	def display_all_items(A):B=A._value_cache_storage_manager.display_all_items();return B
	def throw_if_value_is_explicitly_invalid(C,value,output_type=A):
		F=output_type;E=True;D=value
		if F is A:F=B.DEFINED
		match F:
			case B.FILESYSTEM_PATH:C._filesystem_manager.throw_if_filesystem_path_invalid(D);return E
			case B.FILE_PATH:C._filesystem_manager.throw_if_file_path_invalid(D);return E
			case B.FOLDER_PATH:C._filesystem_manager.throw_if_folder_path_invalid(D);return E
			case B.DEFINED:C.throw_if_undefined(D);return E
			case _:return G
	def throw_if_key_not_found(B,key_path):
		A=key_path
		if not B._value_cache_storage_manager.is_key_found(A):raise H(f"key path '{A}' does not exist")
		return G
	def throw_if_undefined(B,value):
		if value is A:raise H('value is not defined')
		return G