from __future__ import annotations
_B=False
_A=None
from typing import Any
from..library.decorator_manager import DecoratorManager
__all__='CommandWorkflowManager'
_TaskManager=_A
_ImportManager=_A
_DisplayManager=_A
_DatabaseManager=_A
_DecoratorManager=DecoratorManager
_CommandStorageManager=_A
_ValueCacheDatabaseManager=_A
_PersistentCacheDatabasManager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _TaskManager;global _ImportManager;global _DisplayManager;global _CommandStorageManager;global _DatabaseManager;global _ValueCacheDatabaseManager;global _PersistentCacheDatabasManager;from..library import command_storage_manager as A,database_manager as B,display_manager as C,import_manager as D,persistent_cache_database_manager as E,task_manager as F,value_cache_database_manager as G;_TaskManager=F.TaskManager;_DisplayManager=C.DisplayManager;_DatabaseManager=B.DatabaseManager;_ValueCacheDatabaseManager=G.ValueCacheDatabaseManager;_PersistentCacheDatabasManager=E.PersistentCacheDatabasManager;_ImportManager=D.ImportManager;_CommandStorageManager=A.CommandStorageManager;_handle_dynamic_imports=lambda:_A
class CommandWorkflowManager:
	__slots__='_command_storage_manager','_task_manager','_import_manager','_display_manager','_database_manager','_value_cache_database_manager','_persistent_cache_database_manager'
	def __init__(A):_handle_dynamic_imports();A._command_storage_manager=_ImportManager.read_singleton(_CommandStorageManager);A._display_manager=_ImportManager.read_singleton(_DisplayManager);A._task_manager=_ImportManager.read_singleton(_TaskManager);A._import_manager=_ImportManager.read_singleton(_ImportManager);A._database_manager=_ImportManager.read_singleton(_DatabaseManager);A._value_cache_database_manager=_ImportManager.read_singleton(_ValueCacheDatabaseManager);A._persistent_cache_database_manager=_ImportManager.read_singleton(_PersistentCacheDatabasManager);A._command_storage_manager.add_commands(((A._command_storage_manager.read_command_name('workflow_run'),A.run_command_workflow_run),(A._command_storage_manager.read_command_name('workflow_list_selections'),A.run_command_workflow_list_selections)))
	@_DecoratorManager.command_decorator
	def run_command_workflow_run(self,**D):
		A=self
		if not D:return _B
		def I(workflow_target):
			K=workflow_target
			if not K:return _B
			C=M.get(K,{})
			if not C:return _B
			N=A._value_cache_database_manager.read_object_is_enabled_value(C)
			if not N:return _B
			O=A._value_cache_database_manager.read_is_object_operating_system_included(C)
			if not O:return _B
			P=A._value_cache_database_manager.read_object_scripts(C);E=A._value_cache_database_manager.read_object_delay_value(C);E=E if E>=0 else 0;H=A._value_cache_database_manager.read_object_filesystem_path_value(C)
			if not H:H=L
			A._import_manager.time_delay(value=E)
			for B in P:
				if not B:continue
				Q=A._value_cache_database_manager.read_object_is_enabled_value(B)
				if not Q:continue
				R=A._value_cache_database_manager.read_is_object_operating_system_included(B)
				if not R:continue
				D=A._value_cache_database_manager.read_object_run_value(B)
				if not D:continue
				S=A._value_cache_database_manager.read_object_process_value(B);T=A._value_cache_database_manager.read_object_argument(B);F=A._value_cache_database_manager.read_object_delay_value(B);F=F if F>=0 else 0;A._import_manager.time_delay(value=F);A._task_manager.navigate_via_filesystem_path(H)
				if D in J:J[D](**T)
				elif D in G:I(D)
				else:U=A._import_manager.run_command(script_process=S,command=D);A._import_manager.log_cache_info_to_file(message=f"{U}")
			return True
		A._task_manager.run_task_common_setup();A._task_manager.run_task_workflow_setup();A._task_manager.run_task_filesystem_clean_exclude_setup();A._task_manager.run_task_filesystem_clean_include_setup();B=D.get('targets',[])
		if not B or len(B)<1:return _B
		L=A._value_cache_database_manager.read_root_filesystem_path();J=A._command_storage_manager.read_commands();M=A._value_cache_database_manager.read_configuration_workspace_data_workflow_selection();G=A._value_cache_database_manager.read_workflow_selection()
		for C in B:
			if not C or C not in G:continue
			I(G[C])
		return True
	@_DecoratorManager.command_decorator
	def run_command_workflow_list_selections(self,**D):
		A=self;A._task_manager.run_task_common_setup();A._task_manager.run_task_workflow_setup();B={};C=A._value_cache_database_manager.read_workflow_selection()or{}
		if C:B['selections']=C
		if not B:return _B
		A._display_manager.display_tree_object(value=B);return True