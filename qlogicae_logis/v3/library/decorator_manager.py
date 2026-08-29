from __future__ import annotations
_B=True
_A=None
from collections.abc import Callable
from functools import wraps
from typing import Any,ParamSpec,TypeVar
P=ParamSpec('P')
R=TypeVar('R')
__all__='DecoratorManager'
_ImportManager=_A
_DatabaseManager=_A
_TaskStorageManager=_A
_ValueCacheDatabaseManager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _ImportManager;global _DatabaseManager;global _TaskStorageManager;global _ValueCacheDatabaseManager;from..library import database_manager as A,import_manager as B,task_storage_manager as C,value_cache_database_manager as D;_TaskStorageManager=C.TaskStorageManager;_DatabaseManager=A.DatabaseManager;_ValueCacheDatabaseManager=D.ValueCacheDatabaseManager;_ImportManager=B.ImportManager;_handle_dynamic_imports=lambda:_A
class DecoratorManager:
	__slots__=()
	@staticmethod
	def single_use_method_decorator(callback):
		A=callback;_handle_dynamic_imports()
		@wraps(A)
		def B(self,*B,**C):
			D=_ImportManager.read_singleton(_TaskStorageManager)
			if D.is_executed(label=A):return _B
			E=A(self,*B,**C);return E
		return B
	@staticmethod
	def debug_method_decorator(callback):
		A=callback;_handle_dynamic_imports()
		@wraps(A)
		def B(self,*C,**D):
			F=_ImportManager.read_singleton(_ImportManager);G=_ImportManager.read_singleton(_DatabaseManager);B=_ImportManager.read_singleton(_ValueCacheDatabaseManager)
			if G.read_debug_is_enabled():B.write_debug_snapshot_execution_timestamp_start(label=A);E=A(self,*C,**D);B.write_debug_snapshot_execution_timestamp_complete(label=A);H=f"{A} - {B.read_debug_snapshot_execution(label=A)}";F.log_cache_debug_to_file(message=H)
			else:E=A(self,*C,**D)
			return E
		return B
	@staticmethod
	def log_method_decorator(callback):
		A=callback;_handle_dynamic_imports()
		@wraps(A)
		def B(self,*D,**E):
			B=_ImportManager.read_singleton(_ImportManager);B.log_cache_info_to_file(message=f"{A} - start");C=A(self,*D,**E)
			if not C:B.log_cache_info_to_file(message=f"{A} - skip");return C
			B.log_cache_info_to_file(message=f"{A} - complete");return C
		return B
	@staticmethod
	def single_task_decorator(callback):
		A=callback;_handle_dynamic_imports()
		@wraps(A)
		def B(self,*E,**F):
			G=_ImportManager.read_singleton(_TaskStorageManager);C=_ImportManager.read_singleton(_ImportManager);H=_ImportManager.read_singleton(_DatabaseManager);D=_ImportManager.read_singleton(_ValueCacheDatabaseManager)
			if G.is_executed(label=A):return _B
			C.log_cache_info_to_file(message=f"{A} - start");B=_B
			if H.read_debug_is_enabled():D.write_debug_snapshot_execution_timestamp_start(label=A);B=A(self,*E,**F);D.write_debug_snapshot_execution_timestamp_complete(label=A);I=f"{A} - {D.read_debug_snapshot_execution(label=A)}";C.log_cache_debug_to_file(message=I)
			else:B=A(self,*E,**F)
			if not B:C.log_cache_info_to_file(message=f"{A} - skip");return B
			C.log_cache_info_to_file(message=f"{A} - complete");return B
		return B
	@staticmethod
	def multi_task_decorator(callback):
		A=callback;_handle_dynamic_imports()
		@wraps(A)
		def B(self,*E,**F):
			C=_ImportManager.read_singleton(_ImportManager);G=_ImportManager.read_singleton(_DatabaseManager);D=_ImportManager.read_singleton(_ValueCacheDatabaseManager);C.log_cache_info_to_file(message=f"{A} - start");B=_B
			if G.read_debug_is_enabled():D.write_debug_snapshot_execution_timestamp_start(label=A);B=A(self,*E,**F);D.write_debug_snapshot_execution_timestamp_complete(label=A);H=f"{A} - {D.read_debug_snapshot_execution(label=A)}";C.log_cache_debug_to_file(message=H)
			else:B=A(self,*E,**F)
			if not B:C.log_cache_info_to_file(message=f"{A} - skip");return B
			C.log_cache_info_to_file(message=f"{A} - complete");return B
		return B
	@staticmethod
	def command_decorator(callback):
		A=callback;_handle_dynamic_imports()
		@wraps(A)
		def B(self,*E,**F):
			C=_ImportManager.read_singleton(_ImportManager);G=_ImportManager.read_singleton(_DatabaseManager);D=_ImportManager.read_singleton(_ValueCacheDatabaseManager);C.log_cache_info_to_file(message=f"{A} - start");B=_B
			if G.read_debug_is_enabled():D.write_debug_snapshot_execution_timestamp_start(label=A);B=A(self,*E,**F);D.write_debug_snapshot_execution_timestamp_complete(label=A);H=f"{A} - {D.read_debug_snapshot_execution(label=A)}";C.log_cache_debug_to_file(message=H)
			else:B=A(self,*E,**F)
			if not B:C.log_cache_info_to_file(message=f"{A} - skip");return B
			C.log_cache_info_to_file(message=f"{A} - complete");return B
		return B