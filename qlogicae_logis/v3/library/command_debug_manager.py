from __future__ import annotations
_A=None
from typing import Any
from..library.decorator_manager import DecoratorManager
__all__='CommandDebugManager'
_TaskManager=_A
_ImportManager=_A
_DisplayManager=_A
_DatabaseManager=_A
_CommandStorageManager=_A
_ValueCacheDatabaseManager=_A
_PersistentCacheDatabasManager=_A
_DecoratorManager=DecoratorManager
def _handle_dynamic_imports():global _handle_dynamic_imports;global _TaskManager;global _ImportManager;global _DisplayManager;global _DatabaseManager;global _CommandStorageManager;global _ValueCacheDatabaseManager;global _PersistentCacheDatabasManager;from..library import command_storage_manager as A,database_manager as B,display_manager as C,import_manager as D,persistent_cache_database_manager as E,task_manager as F,value_cache_database_manager as G;_TaskManager=F.TaskManager;_ImportManager=D.ImportManager;_DatabaseManager=B.DatabaseManager;_DisplayManager=C.DisplayManager;_ValueCacheDatabaseManager=G.ValueCacheDatabaseManager;_CommandStorageManager=A.CommandStorageManager;_PersistentCacheDatabasManager=E.PersistentCacheDatabasManager;_handle_dynamic_imports=lambda:_A
class CommandDebugManager:
	__slots__='_command_storage_manager','_task_manager','_import_manager','_database_manager','_decorator_manager','_value_cache_database_manager','_display_manager','_persistent_cache_database_manager'
	def __init__(A):_handle_dynamic_imports();A._command_storage_manager=_ImportManager.read_singleton(_CommandStorageManager);A._decorator_manager=_ImportManager.read_singleton(_DecoratorManager);A._database_manager=_ImportManager.read_singleton(_DatabaseManager);A._task_manager=_ImportManager.read_singleton(_TaskManager);A._import_manager=_ImportManager.read_singleton(_ImportManager);A._value_cache_database_manager=_ImportManager.read_singleton(_ValueCacheDatabaseManager);A._display_manager=_ImportManager.read_singleton(_DisplayManager);A._persistent_cache_database_manager=_ImportManager.read_singleton(_PersistentCacheDatabasManager);A._command_storage_manager.add_commands(((A._command_storage_manager.read_command_name('debug_view_value_cache'),A.run_command_debug_view_value_cache),(A._command_storage_manager.read_command_name('debug_view_disk_cache'),A.run_command_debug_view_disk_cache)))
	@_DecoratorManager.command_decorator
	def run_command_debug_view_value_cache(self,**D):
		A=self;A._task_manager.run_task_full_debug_value_cache_setup();B=D.get('key_paths',[])
		if len(B)<1:A._display_manager.display_tree_object(value=A._value_cache_database_manager.read_any_value(tuple()))
		else:
			for C in B:
				if not C:continue
				A._display_manager.display_tree_object(value=A._value_cache_database_manager.read_any_value(tuple(C.split('.'))))
		return True
	@_DecoratorManager.command_decorator
	def run_command_debug_view_disk_cache(self,**C):A=self;A._task_manager.run_task_full_debug_disk_cache_setup();B=A._persistent_cache_database_manager.read_all_values();A._display_manager.display_tree_object(value=B);return True