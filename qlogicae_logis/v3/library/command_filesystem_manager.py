from __future__ import annotations
_C=True
_B=None
_A=False
from typing import Any
from..library.decorator_manager import DecoratorManager
__all__='CommandFilesystemManager'
_TaskManager=_B
_ImportManager=_B
_DisplayManager=_B
_DatabaseManager=_B
_DecoratorManager=DecoratorManager
_CommandStorageManager=_B
_ValueCacheDatabaseManager=_B
_PersistentCacheDatabasManager=_B
def _handle_dynamic_imports():global _handle_dynamic_imports;global _TaskManager;global _ImportManager;global _DisplayManager;global _CommandStorageManager;global _DatabaseManager;global _ValueCacheDatabaseManager;global _PersistentCacheDatabasManager;from..library import command_storage_manager as A,database_manager as B,display_manager as C,import_manager as D,persistent_cache_database_manager as E,task_manager as F,value_cache_database_manager as G;_TaskManager=F.TaskManager;_DisplayManager=C.DisplayManager;_DatabaseManager=B.DatabaseManager;_ValueCacheDatabaseManager=G.ValueCacheDatabaseManager;_PersistentCacheDatabasManager=E.PersistentCacheDatabasManager;_ImportManager=D.ImportManager;_CommandStorageManager=A.CommandStorageManager;_handle_dynamic_imports=lambda:_B
class CommandFilesystemManager:
	__slots__='_command_storage_manager','_task_manager','_import_manager','_display_manager','_database_manager','_value_cache_database_manager','_persistent_cache_database_manager'
	def __init__(A):_handle_dynamic_imports();A._command_storage_manager=_ImportManager.read_singleton(_CommandStorageManager);A._display_manager=_ImportManager.read_singleton(_DisplayManager);A._task_manager=_ImportManager.read_singleton(_TaskManager);A._import_manager=_ImportManager.read_singleton(_ImportManager);A._database_manager=_ImportManager.read_singleton(_DatabaseManager);A._value_cache_database_manager=_ImportManager.read_singleton(_ValueCacheDatabaseManager);A._persistent_cache_database_manager=_ImportManager.read_singleton(_PersistentCacheDatabasManager);A._command_storage_manager.add_commands(((A._command_storage_manager.read_command_name('filesystem_copy'),A.run_command_filesystem_copy),(A._command_storage_manager.read_command_name('filesystem_move'),A.run_command_filesystem_move),(A._command_storage_manager.read_command_name('filesystem_rename'),A.run_command_filesystem_rename),(A._command_storage_manager.read_command_name('filesystem_tree_setup'),A.run_command_filesystem_tree_setup),(A._command_storage_manager.read_command_name('filesystem_clean_path'),A.run_command_filesystem_clean_path),(A._command_storage_manager.read_command_name('filesystem_clean_selection'),A.run_command_filesystem_clean_selection),(A._command_storage_manager.read_command_name('filesystem_clean_list_included'),A.run_command_filesystem_clean_list_included),(A._command_storage_manager.read_command_name('filesystem_clean_list_excluded'),A.run_command_filesystem_clean_list_excluded)))
	@_DecoratorManager.command_decorator
	def run_command_filesystem_copy(self,**A):
		if not A:return _A
		self._task_manager.run_task_common_setup();B=self._import_manager.copy_filesystem_paths(**A);return B
	@_DecoratorManager.command_decorator
	def run_command_filesystem_move(self,**A):
		if not A:return _A
		self._task_manager.run_task_common_setup();B=self._import_manager.move_filesystem_path(**A);return B
	@_DecoratorManager.command_decorator
	def run_command_filesystem_rename(self,**A):
		if not A:return _A
		self._task_manager.run_task_common_setup();B=self._import_manager.rename_filesystem_entity(**A);return B
	@_DecoratorManager.command_decorator
	def run_command_filesystem_tree_setup(self,**A):
		if not A:return _A
		self._task_manager.run_task_common_setup();B=self._import_manager.setup_filesystem_tree_paths(**A);return B
	@_DecoratorManager.command_decorator
	def run_command_filesystem_clean_path(self,**C):
		A=self
		if not C:return _A
		A._task_manager.run_task_common_setup();A._task_manager.run_task_filesystem_clean_exclude_setup();D=C.get('target_paths',tuple())
		if len(D)<1:return _A
		E=A._value_cache_database_manager.read_filesystem_clean_excluded()or{}
		for B in D:
			if not B or B in E:continue
			A._import_manager.clean_filesystem_paths(target_paths=(B,))
		return _C
	@_DecoratorManager.command_decorator
	def run_command_filesystem_clean_selection(self,**D):
		G='targets';A=self
		if not D:return _A
		A._task_manager.run_task_common_setup();A._task_manager.run_task_filesystem_clean_include_setup();A._task_manager.run_task_filesystem_clean_exclude_setup();H=D.get(G,tuple());I=A._value_cache_database_manager.read_configuration_workspace_data_command_filesystem_clean_include_selection()or{};E=A._value_cache_database_manager.read_filesystem_clean_included()or{};J=A._value_cache_database_manager.read_filesystem_clean_excluded()or{}
		for B in H:
			if not B or B not in E:continue
			F=I.get(E.get(B,''),'')
			if not F:continue
			K=A._value_cache_database_manager.read_object_filesystem_pattern_values(F.get(G,{}))
			for C in K:
				if not C or C in J:continue
				A._import_manager.clean_filesystem_paths(target_paths=(C,))
		return _C
	@_DecoratorManager.command_decorator
	def run_command_filesystem_clean_list_included(self,**D):
		A=self;A._task_manager.run_task_common_setup();A._task_manager.run_task_filesystem_clean_include_setup();B={};C=A._value_cache_database_manager.read_filesystem_clean_included()or{}
		if C:B['included']=C
		if not B:return _A
		A._display_manager.display_tree_object(value=B);return _C
	@_DecoratorManager.command_decorator
	def run_command_filesystem_clean_list_excluded(self,**D):
		A=self;A._task_manager.run_task_common_setup();A._task_manager.run_task_filesystem_clean_exclude_setup();B={};C=A._value_cache_database_manager.read_filesystem_clean_excluded()or{}
		if C:B['excluded']=C
		if not B:return _A
		A._display_manager.display_tree_object(value=B);return _C