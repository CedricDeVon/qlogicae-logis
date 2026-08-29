from __future__ import annotations
_A=None
from typing import Any
from..library.decorator_manager import DecoratorManager
__all__='CommandAboutManager'
_TaskManager=_A
_ImportManager=_A
_DisplayManager=_A
_DatabaseManager=_A
_DecoratorManager=DecoratorManager
_CommandStorageManager=_A
_ValueCacheDatabaseManager=_A
_PersistentCacheDatabasManager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _TaskManager;global _ImportManager;global _DisplayManager;global _CommandStorageManager;global _DatabaseManager;global _ValueCacheDatabaseManager;global _PersistentCacheDatabasManager;from..library import command_storage_manager as A,database_manager as B,display_manager as C,import_manager as D,persistent_cache_database_manager as E,task_manager as F,value_cache_database_manager as G;_TaskManager=F.TaskManager;_DisplayManager=C.DisplayManager;_DatabaseManager=B.DatabaseManager;_ValueCacheDatabaseManager=G.ValueCacheDatabaseManager;_PersistentCacheDatabasManager=E.PersistentCacheDatabasManager;_ImportManager=D.ImportManager;_CommandStorageManager=A.CommandStorageManager;_handle_dynamic_imports=lambda:_A
class CommandAboutManager:
	__slots__='_command_storage_manager','_task_manager','_import_manager','_display_manager','_database_manager','_value_cache_database_manager','_persistent_cache_database_manager'
	def __init__(A):_handle_dynamic_imports();A._command_storage_manager=_ImportManager.read_singleton(_CommandStorageManager);A._display_manager=_ImportManager.read_singleton(_DisplayManager);A._task_manager=_ImportManager.read_singleton(_TaskManager);A._import_manager=_ImportManager.read_singleton(_ImportManager);A._database_manager=_ImportManager.read_singleton(_DatabaseManager);A._value_cache_database_manager=_ImportManager.read_singleton(_ValueCacheDatabaseManager);A._persistent_cache_database_manager=_ImportManager.read_singleton(_PersistentCacheDatabasManager);A._command_storage_manager.add_commands(((A._command_storage_manager.read_command_name('about_version'),A.run_command_about_version),))
	@_DecoratorManager.command_decorator
	def run_command_about_version(self,**E):
		D=False;A=self;B=A._database_manager.read_company_project_name()
		if not B:return D
		C=A._import_manager.read_metadata_version(B)
		if not C:return D
		A._display_manager.display_highlight_value(value=C);return True