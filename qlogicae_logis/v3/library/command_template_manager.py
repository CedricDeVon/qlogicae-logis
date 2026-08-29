from __future__ import annotations
_D='all'
_C=True
_B=False
_A=None
from typing import Any
from..library.decorator_manager import DecoratorManager
__all__='CommandTemplateManager'
_TaskManager=_A
_ImportManager=_A
_DisplayManager=_A
_DatabaseManager=_A
_DecoratorManager=DecoratorManager
_CommandStorageManager=_A
_ValueCacheDatabaseManager=_A
_PersistentCacheDatabasManager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _TaskManager;global _ImportManager;global _DisplayManager;global _DatabaseManager;global _CommandStorageManager;global _ValueCacheDatabaseManager;global _PersistentCacheDatabasManager;from..library import command_storage_manager as A,database_manager as B,display_manager as C,import_manager as D,persistent_cache_database_manager as E,task_manager as F,value_cache_database_manager as G;_TaskManager=F.TaskManager;_DisplayManager=C.DisplayManager;_DatabaseManager=B.DatabaseManager;_ValueCacheDatabaseManager=G.ValueCacheDatabaseManager;_PersistentCacheDatabasManager=E.PersistentCacheDatabasManager;_ImportManager=D.ImportManager;_CommandStorageManager=A.CommandStorageManager;_handle_dynamic_imports=lambda:_A
class CommandTemplateManager:
	__slots__='_command_storage_manager','_task_manager','_import_manager','_display_manager','_database_manager','_value_cache_database_manager','_persistent_cache_database_manager'
	def __init__(A):_handle_dynamic_imports();A._command_storage_manager=_ImportManager.read_singleton(_CommandStorageManager);A._display_manager=_ImportManager.read_singleton(_DisplayManager);A._task_manager=_ImportManager.read_singleton(_TaskManager);A._import_manager=_ImportManager.read_singleton(_ImportManager);A._database_manager=_ImportManager.read_singleton(_DatabaseManager);A._value_cache_database_manager=_ImportManager.read_singleton(_ValueCacheDatabaseManager);A._persistent_cache_database_manager=_ImportManager.read_singleton(_PersistentCacheDatabasManager);A._command_storage_manager.add_commands(((A._command_storage_manager.read_command_name('template_apply'),A.run_command_template_apply),(A._command_storage_manager.read_command_name('template_list_selections'),A.run_command_template_list_selections)))
	@_DecoratorManager.command_decorator
	def run_command_template_apply(self,**H):
		Q='root';P='targets';A=self
		if not H:return _B
		def K():
			B=f"{D}/root/filesystem"
			for E in O:
				if not E:continue
				F=f"{C}/{E}/template/all/filesystem";G=f"{C}/{E}/template/root/filesystem";A._import_manager.setup_filesystem_tree_paths(target_paths=(F,G,B));A._import_manager.copy_filesystem_path(source_path=F,target_path=B);A._import_manager.copy_filesystem_path(source_path=G,target_path=B)
			A._import_manager.macros_parse_filesystem(filesystem_path=B,workspace_macros=N);A._import_manager.copy_filesystem_path(source_path=B,target_path=S);return _C
		def I():
			for A in G:
				if not A:continue
				L(A)
			return _C
		def J():
			for A in F:
				if not A:continue
				M(A)
			return _C
		def L(group_target):
			I=group_target
			if not I:return _B
			R=V.get(I,{})
			if not R:return _B
			W=set(R.get(P,{}));B=f"{D}/group/selection/{I}/filesystem"
			for J in O:
				if not J:continue
				S=f"{C}/{J}/template/all/filesystem";T=f"{C}/{J}/template/group/filesystem";U=f"{C}/{J}/template/group/selection/{I}/filesystem";A._import_manager.setup_filesystem_tree_paths(target_paths=(S,T,U,B));A._import_manager.copy_filesystem_path(source_path=S,target_path=B);A._import_manager.copy_filesystem_path(source_path=T,target_path=B);A._import_manager.copy_filesystem_path(source_path=U,target_path=B)
			A._import_manager.macros_parse_filesystem(filesystem_path=B,workspace_macros=N)
			for E in W:
				if not E:continue
				if E==Q:H=f"{D}/root/filesystem";A._import_manager.copy_filesystem_path(source_path=B,target_path=H);K()
				elif E in F:H=f"{D}/project/selection/{E}/filesystem";A._import_manager.copy_filesystem_path(source_path=B,target_path=H);M(E)
				elif E in G:H=f"{D}/group/selection/{E}/filesystem";A._import_manager.copy_filesystem_path(source_path=B,target_path=H);L(E)
			return _C
		def M(project_target):
			E=project_target
			if not E:return _B
			G=R.get(E,{})
			if not G:return _B
			H=G.get('filesystem-path',{}).get('value','')
			if not H:return _B
			B=f"{D}/project/selection/{E}/filesystem"
			for F in O:
				if not F:continue
				I=f"{C}/{F}/template/all/filesystem";J=f"{C}/{F}/template/project/filesystem";K=f"{C}/{F}/template/project/selection/{E}/filesystem";A._import_manager.setup_filesystem_tree_paths(target_paths=(I,J,K,B));A._import_manager.copy_filesystem_path(source_path=I,target_path=B);A._import_manager.copy_filesystem_path(source_path=J,target_path=B);A._import_manager.copy_filesystem_path(source_path=K,target_path=B)
			A._import_manager.macros_parse_filesystem(filesystem_path=B,workspace_macros=N);A._import_manager.copy_filesystem_path(source_path=B,target_path=H);return _C
		A._task_manager.run_task_common_setup();A._task_manager.run_task_workspace_default_setup();A._task_manager.run_task_workspace_group_setup();A._task_manager.run_task_workspace_project_setup();A._task_manager.run_task_filesystem_clean_exclude_setup();A._task_manager.run_task_filesystem_clean_include_setup();E=H.get(P,[_D])
		if not E or len(E)<1:E=[_D]
		N=A._value_cache_database_manager.read_macros();O=A._database_manager.read_default_filesystem_accessibility_types();R=A._value_cache_database_manager.read_configuration_workspace_data_workspace_project_selection();F=A._value_cache_database_manager.read_workspace_project();F=A._database_manager.read_object_selection_origins(F);V=A._value_cache_database_manager.read_configuration_workspace_data_workspace_group_selection();G=A._value_cache_database_manager.read_workspace_group();G=A._database_manager.read_object_selection_origins(G);S=A._value_cache_database_manager.read_root_filesystem_path();C=A._database_manager.read_root_workspace_filesystem_path();D=A._database_manager.read_temporary_template_output_filesystem_path();T=A._value_cache_database_manager.read_con_wor_data_template_cleanup_before_is_enabled_value();U=A._value_cache_database_manager.read_con_wor_data_template_cleanup_after_is_enabled_value()
		if T:A._task_manager.run_task_safe_clean_filesystem_path(target_path=D)
		for B in E:
			if not B:continue
			if B==_D:K();I();J()
			elif B==Q:K()
			elif B=='group':I()
			elif B=='project':J()
			elif B in G:L(B)
			elif B in F:M(B)
		if U:A._task_manager.run_task_safe_clean_filesystem_path(target_path=D)
		return _C
	@_DecoratorManager.command_decorator
	def run_command_template_list_selections(self,**G):
		A=self;A._task_manager.run_task_common_setup();A._task_manager.run_task_workspace_default_setup();A._task_manager.run_task_workspace_group_setup();A._task_manager.run_task_workspace_project_setup();B={};C=A._value_cache_database_manager.read_workspace_default()or{}
		if C:B['defaults']=C
		D=A._value_cache_database_manager.read_workspace_project()or{}
		if D:B['projects']=D
		E=A._value_cache_database_manager.read_workspace_group()or{}
		if E:B['groups']=E
		F=A._value_cache_database_manager.read_workspace_all()or{}
		if F:B[_D]=F
		if not B:return _B
		A._display_manager.display_tree_object(value=B);return _C