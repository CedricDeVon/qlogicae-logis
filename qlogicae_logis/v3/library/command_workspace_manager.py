from __future__ import annotations
_D='targets'
_C=True
_B=None
_A=False
from typing import Any
from..library.decorator_manager import DecoratorManager
__all__='CommandWorkspaceManager'
_TaskManager=_B
_ImportManager=_B
_DisplayManager=_B
_DatabaseManager=_B
_DecoratorManager=DecoratorManager
_CommandStorageManager=_B
_ValueCacheDatabaseManager=_B
_PersistentCacheDatabasManager=_B
_FileEntityFileSystemTreeSetupOptions=_B
_FolderEntityFileSystemTreeSetupOptions=_B
def _handle_dynamic_imports():global _handle_dynamic_imports;global _TaskManager;global _ImportManager;global _DisplayManager;global _CommandStorageManager;global _DatabaseManager;global _ValueCacheDatabaseManager;global _PersistentCacheDatabasManager;global _FileEntityFileSystemTreeSetupOptions;global _FolderEntityFileSystemTreeSetupOptions;from.._vendor.qlogicae_cor.v2.library import file_entity_filesystem_tree_setup_options as A,folder_entity_filesystem_tree_setup_options as B;from..library import command_storage_manager as C,database_manager as D,display_manager as E,import_manager as F,persistent_cache_database_manager as G,task_manager as H,value_cache_database_manager as I;_TaskManager=H.TaskManager;_DisplayManager=E.DisplayManager;_DatabaseManager=D.DatabaseManager;_ValueCacheDatabaseManager=I.ValueCacheDatabaseManager;_PersistentCacheDatabasManager=G.PersistentCacheDatabasManager;_ImportManager=F.ImportManager;_CommandStorageManager=C.CommandStorageManager;_FileEntityFileSystemTreeSetupOptions=A.FileEntityFileSystemTreeSetupOptions;_FolderEntityFileSystemTreeSetupOptions=B.FolderEntityFileSystemTreeSetupOptions;_handle_dynamic_imports=lambda:_B
class CommandWorkspaceManager:
	__slots__='_command_storage_manager','_task_manager','_import_manager','_display_manager','_database_manager','_value_cache_database_manager','_persistent_cache_database_manager'
	def __init__(A):_handle_dynamic_imports();A._command_storage_manager=_ImportManager.read_singleton(_CommandStorageManager);A._display_manager=_ImportManager.read_singleton(_DisplayManager);A._task_manager=_ImportManager.read_singleton(_TaskManager);A._import_manager=_ImportManager.read_singleton(_ImportManager);A._database_manager=_ImportManager.read_singleton(_DatabaseManager);A._value_cache_database_manager=_ImportManager.read_singleton(_ValueCacheDatabaseManager);A._persistent_cache_database_manager=_ImportManager.read_singleton(_PersistentCacheDatabasManager);A._command_storage_manager.add_commands(((A._command_storage_manager.read_command_name('workspace_export'),A.run_command_workspace_export),(A._command_storage_manager.read_command_name('workspace_import'),A.run_command_workspace_import),(A._command_storage_manager.read_command_name('workspace_setup'),A.run_command_workspace_setup),(A._command_storage_manager.read_command_name('workspace_replenish'),A.run_command_workspace_replenish),(A._command_storage_manager.read_command_name('workspace_install'),A.run_command_workspace_install),(A._command_storage_manager.read_command_name('workspace_list_exports'),A.run_command_workspace_list_exports)))
	@_DecoratorManager.command_decorator
	def run_command_workspace_export(self,**G):
		A=self
		if not G:return _A
		def H(target):
			E=target
			if not E or E not in D:return _A
			F=D[E];G=A._value_cache_database_manager.read_object_is_enabled_value(F)
			if not G:return _A
			I=A._value_cache_database_manager.read_object_is_enabled_value(F)
			for B in I:
				if not B:continue
				if B in D:H(B)
				elif B in L:C(B)
			return _C
		def C(target):
			K='output';J='input';E=target;B=L.get(E,{})
			if E in M:
				if not B:B=M.get(E,{})
			S=A._value_cache_database_manager.read_object_is_enabled_value(B)
			if not S:return _A
			G=A._value_cache_database_manager.read_object_input_exclude_targets(B);G=A._value_cache_database_manager.read_object_pattern_values(G);C=A._value_cache_database_manager.read_object_input_include_targets(B);C=A._value_cache_database_manager.read_object_filesystem_pattern_values(C);C=A._database_manager.read_object_filtered_export_included(C,G);H=A._value_cache_database_manager.read_object_output_targets(B);H=A._value_cache_database_manager.read_object_filesystem_values(H);T=A._value_cache_database_manager.read_object_compression_format_value(B);U=A._value_cache_database_manager.read_object_compression_type_value(B);V=A._value_cache_database_manager.read_object_compression_level_value(B);W=A._value_cache_database_manager.read_object_compression_is_zip_64_allowed_value(B);X=A._value_cache_database_manager.read_object_compression_is_timestamp_strict_value(B);N=[];O=f"{F}/{E}"
			for I in C:
				if not I:continue
				Y=f"{R}/{I}";Z=f"{O}/{I}";N.append({J:Y,K:Z})
			for D in N:
				if not D or J not in D or K not in D:continue
				P=D.get(J,'');Q=D.get(K,'')
				if not P or not Q:continue
				A._import_manager.copy_filesystem_paths(source_path=P,target_paths=(Q,))
			for a in H:b=f"{a}.{T}";A._import_manager.compress(source=O,destination=b,mode='w',compression=U,compresslevel=V,allowZip64=W,strict_timestamps=X)
			return _C
		A._task_manager.run_task_common_setup();A._task_manager.run_task_export_group_setup();A._task_manager.run_task_export_selection_setup();A._task_manager.run_task_filesystem_clean_exclude_setup();A._task_manager.run_task_filesystem_clean_include_setup();I=G.get(_D,[])
		if len(I)<1:return _A
		R=A._value_cache_database_manager.read_root_filesystem_path();D=A._value_cache_database_manager.read_configuration_workspace_data_export_group();L=A._value_cache_database_manager.read_configuration_workspace_data_export_selection();K=A._value_cache_database_manager.read_con_wor_data_export_cleanup_before_is_enabled_value();N=A._value_cache_database_manager.read_con_wor_data_export_cleanup_after_is_enabled_value();J=A._value_cache_database_manager.read_export_group();E=A._value_cache_database_manager.read_export_selection();O=A._database_manager.read_object_selection_origins(E);M=A._database_manager.read_default_export_selection_data();F=A._database_manager.read_temporary_export_output_filesystem_path()
		if K:A._task_manager.run_task_safe_clean_filesystem_path(target_path=F)
		for B in I:
			if not B:continue
			if B=='all':
				for P in O:C(P)
			elif B in J:H(J[B])
			elif B in E:C(E[B])
		if N:A._task_manager.run_task_safe_clean_filesystem_path(target_path=F)
		return _C
	@_DecoratorManager.command_decorator
	def run_command_workspace_import(self,**A):
		if not A:return _A
		self._task_manager.run_task_common_setup();B=A.get('input_path','');C=A.get('output_path','')
		if not B or not C:return _A
		self._import_manager.uncompress_zip(archive_path=B,destination_path=C);return _C
	@_DecoratorManager.command_decorator
	def run_command_workspace_replenish(self,**i):
		U='.gitignore';T='filesystem';P='workspace';O='configuration';I='template';H='project';G='group';F='selection';A=self;A._task_manager.run_task_common_setup();A._task_manager.run_task_workspace_group_setup();A._task_manager.run_task_workspace_project_setup();J=A._value_cache_database_manager.read_root_filesystem_path();V={A for(B,A)in A._value_cache_database_manager.read_workspace_project().items()};W={A for(B,A)in A._value_cache_database_manager.read_workspace_group().items()};X=A._database_manager.read_default_filesystem_accessibility_types();K=A._database_manager.read_company_name();L=A._database_manager.read_project_name();M=A._database_manager.read_active_major_version_label();D='';B=_FolderEntityFileSystemTreeSetupOptions(name=T,entities=[]);Y=_FileEntityFileSystemTreeSetupOptions(name=U,content='private/**/*');Z=_FileEntityFileSystemTreeSetupOptions(name=U,content='*');a=_FileEntityFileSystemTreeSetupOptions(name='root.yaml',content=D);b=_FileEntityFileSystemTreeSetupOptions(name='group.yaml',content=D);c=_FileEntityFileSystemTreeSetupOptions(name='project.yaml',content=D);C=_FolderEntityFileSystemTreeSetupOptions(name=F,entities=[]);B=_FolderEntityFileSystemTreeSetupOptions(name=T,entities=[]);d=_FolderEntityFileSystemTreeSetupOptions(name='target',entities=[]);e=_FolderEntityFileSystemTreeSetupOptions(name='log',entities=[]);f=_FolderEntityFileSystemTreeSetupOptions(name='cache',entities=[_FolderEntityFileSystemTreeSetupOptions(name='disk',entities=[])]);Q=_FolderEntityFileSystemTreeSetupOptions(name=O,entities=[_FolderEntityFileSystemTreeSetupOptions(name=P,entities=[_FolderEntityFileSystemTreeSetupOptions(name=G,entities=[C,b]),_FolderEntityFileSystemTreeSetupOptions(name=H,entities=[C,c]),a])]);R=_FolderEntityFileSystemTreeSetupOptions(name=I,entities=[_FolderEntityFileSystemTreeSetupOptions(name='all',entities=[B]),_FolderEntityFileSystemTreeSetupOptions(name=G,entities=[C,B]),_FolderEntityFileSystemTreeSetupOptions(name=H,entities=[C,B]),_FolderEntityFileSystemTreeSetupOptions(name='root',entities=[B])]);g=_FolderEntityFileSystemTreeSetupOptions(name='temporary',entities=[_FolderEntityFileSystemTreeSetupOptions(name='export',entities=[d]),_FolderEntityFileSystemTreeSetupOptions(name=I,entities=[B]),e,f]);h=_FolderEntityFileSystemTreeSetupOptions(entities=[_FolderEntityFileSystemTreeSetupOptions(name=f".{K}",entities=[_FolderEntityFileSystemTreeSetupOptions(name=L,entities=[_FolderEntityFileSystemTreeSetupOptions(name=M,entities=[_FolderEntityFileSystemTreeSetupOptions(name='private',entities=[Q,R,g,Z]),_FolderEntityFileSystemTreeSetupOptions(name='public',entities=[Q,R]),Y])])]),C]);A._import_manager.setup_filesystem_tree(root_path=J,tree=h)
		for S in X:
			for E in V:N=_FolderEntityFileSystemTreeSetupOptions(entities=[_FolderEntityFileSystemTreeSetupOptions(name=f".{K}",entities=[_FolderEntityFileSystemTreeSetupOptions(name=L,entities=[_FolderEntityFileSystemTreeSetupOptions(name=M,entities=[_FolderEntityFileSystemTreeSetupOptions(name=S,entities=[_FolderEntityFileSystemTreeSetupOptions(name=O,entities=[_FolderEntityFileSystemTreeSetupOptions(name=P,entities=[_FolderEntityFileSystemTreeSetupOptions(name=H,entities=[_FolderEntityFileSystemTreeSetupOptions(name=F,entities=[_FileEntityFileSystemTreeSetupOptions(name=f"{E}.yaml",content=D)])])])]),_FolderEntityFileSystemTreeSetupOptions(name=I,entities=[_FolderEntityFileSystemTreeSetupOptions(name=H,entities=[_FolderEntityFileSystemTreeSetupOptions(name=F,entities=[_FolderEntityFileSystemTreeSetupOptions(name=E,entities=[B])])])])])])])])]);A._import_manager.setup_filesystem_tree(root_path=J,tree=N)
			for E in W:N=_FolderEntityFileSystemTreeSetupOptions(entities=[_FolderEntityFileSystemTreeSetupOptions(name=f".{K}",entities=[_FolderEntityFileSystemTreeSetupOptions(name=L,entities=[_FolderEntityFileSystemTreeSetupOptions(name=M,entities=[_FolderEntityFileSystemTreeSetupOptions(name=S,entities=[_FolderEntityFileSystemTreeSetupOptions(name=O,entities=[_FolderEntityFileSystemTreeSetupOptions(name=P,entities=[_FolderEntityFileSystemTreeSetupOptions(name=G,entities=[_FolderEntityFileSystemTreeSetupOptions(name=F,entities=[_FileEntityFileSystemTreeSetupOptions(name=f"{E}.yaml",content=D)])])])]),_FolderEntityFileSystemTreeSetupOptions(name=I,entities=[_FolderEntityFileSystemTreeSetupOptions(name=G,entities=[_FolderEntityFileSystemTreeSetupOptions(name=F,entities=[_FolderEntityFileSystemTreeSetupOptions(name=E,entities=[B])])])])])])])]),C]);A._import_manager.setup_filesystem_tree(root_path=J,tree=N)
		return _C
	@_DecoratorManager.command_decorator
	def run_command_workspace_list_exports(self,**E):
		A=self;A._task_manager.run_task_common_setup();A._task_manager.run_task_export_group_setup();A._task_manager.run_task_export_selection_setup();B={};C=A._value_cache_database_manager.read_export_group()or{}
		if C:B['groups']=C
		D=A._value_cache_database_manager.read_export_selection()or{}
		if D:B['selections']=D
		if not B:return _A
		A._display_manager.display_tree_object(value=B);return _C
	@_DecoratorManager.command_decorator
	def run_command_workspace_setup(self,**A):self._task_manager.run_task_common_setup();return _C
	@_DecoratorManager.command_decorator
	def run_command_workspace_install(self,**E):
		A=self
		if not E:return _A
		def F(target):
			E=target
			if not E or E not in D:return _A
			B=I.get(E,{}).get('installation',{})
			if not B:return _A
			J=A._value_cache_database_manager.read_object_is_enabled_value(B)
			if not J:return _A
			K=A._value_cache_database_manager.read_is_object_operating_system_included(B)
			if not K:return _A
			F=A._value_cache_database_manager.read_object_filesystem_path_value(B)
			if not F:return _A
			L=A._value_cache_database_manager.read_object_scripts(B);M=A._value_cache_database_manager.read_object_delay_value(B);A._import_manager.time_delay(value=M);A._task_manager.navigate_via_filesystem_path(F)
			for C in L:
				if not C:continue
				N=A._value_cache_database_manager.read_object_is_enabled_value(C)
				if not N:continue
				O=A._value_cache_database_manager.read_is_object_operating_system_included(C)
				if not O:continue
				G=A._value_cache_database_manager.read_object_run_value(C)
				if not G:continue
				P=A._value_cache_database_manager.read_object_process_value(C);Q=A._value_cache_database_manager.read_object_delay_value(C);A._import_manager.time_delay(value=Q);R=A._import_manager.run_command(script_process=P,command=G);A._import_manager.log_cache_info_to_file(message=f"{R}")
			A._task_manager.navigate_via_filesystem_path(H);return _C
		A._task_manager.run_task_common_setup();A._task_manager.run_task_workspace_default_setup();A._task_manager.run_task_workspace_group_setup();A._task_manager.run_task_workspace_project_setup();A._task_manager.run_task_filesystem_clean_exclude_setup();A._task_manager.run_task_filesystem_clean_include_setup();B=E.get(_D,[])
		if not B or len(B)<1:return _A
		H=A._value_cache_database_manager.read_root_filesystem_path();I=A._value_cache_database_manager.read_configuration_workspace_data_workspace_project_selection();D=A._value_cache_database_manager.read_workspace_project()
		for C in B:
			if not C or C not in D:continue
			F(D.get(C,''))
		return _C