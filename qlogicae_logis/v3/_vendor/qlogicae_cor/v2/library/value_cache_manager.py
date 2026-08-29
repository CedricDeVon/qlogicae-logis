from __future__ import annotations
_B=False
_A=None
__all__='ValueCacheManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from.target_cache_value import TargetCacheValue
_FilesystemManager=_A
_SingletonManager=_A
_TargetCacheValue=_A
_ValueCacheStorageManager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _FilesystemManager;global _SingletonManager;global _TargetCacheValue;global _ValueCacheStorageManager;from.filesystem_manager import FilesystemManager as A;from.singleton_manager import SingletonManager as B;from.target_cache_value import TargetCacheValue as C;from.value_cache_storage_manager import ValueCacheStorageManager as D;_FilesystemManager=A;_SingletonManager=B;_TargetCacheValue=C;_ValueCacheStorageManager=D;_handle_dynamic_imports=lambda:_A
class ValueCacheManager:
	__slots__='_filesystem_manager','_value_cache_storage_manager'
	def __init__(A):_handle_dynamic_imports();A._filesystem_manager=_SingletonManager.get_singleton(_FilesystemManager);A._value_cache_storage_manager=_SingletonManager.get_singleton(_ValueCacheStorageManager)
	def is_key_found(A,key_path):B=A._value_cache_storage_manager.is_key_found(key_path);return B
	def get_one_value(B,key_path,output_type=_A):
		A=output_type
		if A is _A:A=_TargetCacheValue.DEFINED
		C=B._value_cache_storage_manager.get_one_value(key_path);B.throw_if_value_is_explicitly_invalid(C,A);return C
	def set_one_value(B,key_path,value,output_type=_A):
		C=value;A=output_type
		if A is _A:A=_TargetCacheValue.DEFINED
		B.throw_if_value_is_explicitly_invalid(C,A);D=B._value_cache_storage_manager.set_one_value(key_path,C);return D
	def remove_one_value(A,key_path):B=key_path;A.throw_if_key_not_found(B);C=A._value_cache_storage_manager.remove_one_value(B);return C
	def clear_all_values(A):B=A._value_cache_storage_manager.clear_all_values();return B
	def display_all_items(A):B=A._value_cache_storage_manager.display_all_items();return B
	def throw_if_value_is_explicitly_invalid(A,value,output_type=_A):
		D=output_type;C=True;B=value
		if D is _A:D=_TargetCacheValue.DEFINED
		match D:
			case _TargetCacheValue.FILESYSTEM_PATH:A._filesystem_manager.throw_if_filesystem_path_invalid(B);return C
			case _TargetCacheValue.FILE_PATH:A._filesystem_manager.throw_if_file_path_invalid(B);return C
			case _TargetCacheValue.FOLDER_PATH:A._filesystem_manager.throw_if_folder_path_invalid(B);return C
			case _TargetCacheValue.DEFINED:A.throw_if_undefined(B);return C
			case _:return _B
	def throw_if_key_not_found(B,key_path):
		A=key_path
		if not B._value_cache_storage_manager.is_key_found(A):raise KeyError(f"key path '{A}' does not exist")
		return _B
	def throw_if_undefined(A,value):
		if value is _A:raise KeyError('value is not defined')
		return _B