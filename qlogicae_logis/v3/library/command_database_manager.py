from __future__ import annotations
_D='key_paths'
_C=False
_B=True
_A=None
from typing import Any
from.decorator_manager import DecoratorManager
__all__='CommandDatabaseManager'
_TaskManager=_A
_ImportManager=_A
_DisplayManager=_A
_DatabaseManager=_A
_DecoratorManager=DecoratorManager
_CommandStorageManager=_A
_ValueCacheDatabaseManager=_A
_PersistentCacheDatabasManager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _TaskManager;global _ImportManager;global _DisplayManager;global _CommandStorageManager;global _DatabaseManager;global _ValueCacheDatabaseManager;global _PersistentCacheDatabasManager;from.import command_storage_manager as A,database_manager as B,display_manager as C,import_manager as D,persistent_cache_database_manager as E,task_manager as F,value_cache_database_manager as G;_TaskManager=F.TaskManager;_DisplayManager=C.DisplayManager;_DatabaseManager=B.DatabaseManager;_ValueCacheDatabaseManager=G.ValueCacheDatabaseManager;_PersistentCacheDatabasManager=E.PersistentCacheDatabasManager;_ImportManager=D.ImportManager;_CommandStorageManager=A.CommandStorageManager;_handle_dynamic_imports=lambda:_A
class CommandDatabaseManager:
	__slots__='_command_storage_manager','_task_manager','_import_manager','_display_manager','_database_manager','_value_cache_database_manager','_persistent_cache_database_manager'
	def __init__(A):_handle_dynamic_imports();A._command_storage_manager=_ImportManager.read_singleton(_CommandStorageManager);A._display_manager=_ImportManager.read_singleton(_DisplayManager);A._task_manager=_ImportManager.read_singleton(_TaskManager);A._import_manager=_ImportManager.read_singleton(_ImportManager);A._database_manager=_ImportManager.read_singleton(_DatabaseManager);A._value_cache_database_manager=_ImportManager.read_singleton(_ValueCacheDatabaseManager);A._persistent_cache_database_manager=_ImportManager.read_singleton(_PersistentCacheDatabasManager);A._command_storage_manager.add_commands(((A._command_storage_manager.read_command_name('cache_view_disk'),A.run_command_database_view_disk),(A._command_storage_manager.read_command_name('cache_view_value'),A.run_command_database_view_value),(A._command_storage_manager.read_command_name('cache_clear_disk'),A.run_command_database_clear_disk),(A._command_storage_manager.read_command_name('cache_clear_value'),A.run_command_database_clear_value)))
	@_DecoratorManager.command_decorator
	def run_command_database_view_disk(self,**C):
		A=self
		if not C:return _C
		A._task_manager.run_task_full_debug_disk_cache_setup();D=C.get(_D,[]);E=A._persistent_cache_database_manager.read_all_values()
		if len(D)<1:A._display_manager.display_tree_object(value=E)
		else:
			for F in D:
				if not F:continue
				for B in E:
					if not B:continue
					if B['key']==F:A._display_manager.display_tree_object(value=B)
		return _B
	@_DecoratorManager.command_decorator
	def run_command_database_view_value(self,**B):
		A=self
		if not B:return _C
		C=B.get(_D,[])
		if len(C)<1:A._display_manager.display_tree_object(value=A._value_cache_database_manager.read_any_value(tuple()))
		else:
			for D in C:
				if not D:continue
				A._display_manager.display_tree_object(value=A._value_cache_database_manager.read_any_value(tuple(D.split('.'))))
		return _B
	@_DecoratorManager.command_decorator
	def run_command_database_clear_disk(self,**C):
		A=self;A._task_manager.run_task_full_debug_disk_cache_setup();B=A._database_manager.read_default_cache_disk_output_folder_path()or''
		if not B:return _C
		A._import_manager.clean_filesystem_paths(target_paths=(B,));return _B
	@_DecoratorManager.command_decorator
	def run_command_database_clear_value(self,**A):self._import_manager.clear_all_values_via_value_cache();return _B