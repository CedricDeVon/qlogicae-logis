from __future__ import annotations
_E='public'
_D='private'
_C=False
_B=None
_A=True
from typing import Any,ParamSpec,TypeVar
from..library.decorator_manager import DecoratorManager
P=ParamSpec('P')
R=TypeVar('R')
__all__='TaskManager'
_ImportManager=_B
_DatabaseManager=_B
_TaskStorageManager=_B
_DecoratorManager=DecoratorManager
_ValueCacheDatabaseManager=_B
_PersistentCacheDatabasManager=_B
def _handle_dynamic_imports():global _handle_dynamic_imports;global _ImportManager;global _DatabaseManager;global _TaskStorageManager;global _ValueCacheDatabaseManager;global _PersistentCacheDatabasManager;from..library import database_manager as A,import_manager as B,persistent_cache_database_manager as C,task_storage_manager as D,value_cache_database_manager as E;_ImportManager=B.ImportManager;_DatabaseManager=A.DatabaseManager;_ValueCacheDatabaseManager=E.ValueCacheDatabaseManager;_TaskStorageManager=D.TaskStorageManager;_PersistentCacheDatabasManager=C.PersistentCacheDatabasManager;_handle_dynamic_imports=lambda:_B
class TaskManager:
	__slots__='_import_manager','_database_manager','_task_storage_manager','_value_cache_database_manager','_persistent_cache_database_manager'
	def __init__(A):_handle_dynamic_imports();A._import_manager=_ImportManager.read_singleton(_ImportManager);A._database_manager=_ImportManager.read_singleton(_DatabaseManager);A._value_cache_database_manager=_ImportManager.read_singleton(_ValueCacheDatabaseManager);A._persistent_cache_database_manager=_ImportManager.read_singleton(_PersistentCacheDatabasManager);A._task_storage_manager=_ImportManager.read_singleton(_TaskStorageManager)
	@_DecoratorManager.single_task_decorator
	def run_task_system_values(self):A=self;A._value_cache_database_manager.write_current_timestamp();A._value_cache_database_manager.write_current_date();A._value_cache_database_manager.write_current_year();A._value_cache_database_manager.write_default_time_zone_name();A._value_cache_database_manager.write_default_operating_system_name();A._value_cache_database_manager.write_default_operating_system_architecture();return _A
	@_DecoratorManager.single_task_decorator
	def run_task_root_filesystem_path(self):self._value_cache_database_manager.write_root_filesystem_path();return _A
	@_DecoratorManager.single_task_decorator
	def run_task_selection_filesystem_path(self):self._value_cache_database_manager.write_selection_filesystem_path();return _A
	@_DecoratorManager.single_task_decorator
	def run_task_executing_console_filesystem_paths(self):A=self;A._value_cache_database_manager.write_initial_executing_console_filesystem_path(A._import_manager.read_original_executing_console_filesystem_path());A._value_cache_database_manager.write_previous_executing_console_filesystem_path(A._value_cache_database_manager.read_initial_executing_console_filesystem_path());A._value_cache_database_manager.write_current_executing_console_filesystem_path(A._value_cache_database_manager.read_initial_executing_console_filesystem_path());return _A
	@_DecoratorManager.single_task_decorator
	def run_task_disk_cache_output_folder_path(self):self._import_manager.setup_filesystem_tree_path(target_path=self._database_manager.read_default_cache_disk_output_folder_path());return _A
	@_DecoratorManager.single_task_decorator
	def run_task_disk_cache_output_file_path(self):self._import_manager.write_database_path_via_disk_cache(self._database_manager.read_default_disk_cache_output_file_path());return _A
	@_DecoratorManager.single_task_decorator
	def run_task_disk_cache_startup(self):self._import_manager.open_via_disk_cache();return _A
	@_DecoratorManager.single_task_decorator
	def run_task_disk_cache_refresh(self):
		for A in range(5):self._persistent_cache_database_manager.write_refresh_data({})
		return _A
	@_DecoratorManager.single_task_decorator
	def run_task_initial_console_filesystem_path(self):self.navigate_via_root_filesystem_path();return _A
	@_DecoratorManager.single_task_decorator
	def navigate_via_root_filesystem_path(self):self.navigate_via_filesystem_path(self._value_cache_database_manager.read_root_filesystem_path());return _A
	@_DecoratorManager.multi_task_decorator
	def navigate_via_filesystem_path(self,filesystem_path):
		B=filesystem_path;A=self
		if not B:return _C
		A._value_cache_database_manager.write_previous_executing_console_filesystem_path(A._value_cache_database_manager.read_original_executing_console_filesystem_path());A._import_manager.write_current_executing_console_filesystem_path(filesystem_path=B);A._value_cache_database_manager.write_current_executing_console_filesystem_path(B);return _A
	@_DecoratorManager.multi_task_decorator
	def run_task_configuration_workspace(self,accessibility_type):
		C=accessibility_type;A=self
		if not C:return _C
		G=A._value_cache_database_manager.read_is_configuration_workspace_modified()or _C;M=A._database_manager.read_default_data_file_extensions();E={};H={};N=A._database_manager.read_configuration_workspace_base_file_paths(C);O=A._database_manager.read_configuration_workspace_base_folder_paths(C)
		for I in N:
			for P in M:
				B=f"{I}{P}"
				if not A._import_manager.is_file_path_valid(value=B):continue
				D=A._database_manager.read_file_metadata(B);F=A._persistent_cache_database_manager.read_configuration_workspace_metadata(C,B);J=A._database_manager.read_object_property_timestamp_modified_value(D)or 1;K=A._database_manager.read_object_property_timestamp_modified_value(F)or 2
				if K!=J:E=A._database_manager.read_configuration_workspace_data_file(B);A._persistent_cache_database_manager.write_configuration_workspace_data(C,B,E);A._persistent_cache_database_manager.write_configuration_workspace_metadata(C,B,D);G=_A
				else:E=A._persistent_cache_database_manager.read_configuration_workspace_data(C,B);D=F
				H[B]=A._value_cache_database_manager.read_file_data(E,D)
		for I in O:
			if not A._import_manager.is_folder_path_valid(value=I):continue
			Q=A._import_manager.read_child_folder_paths(value=I)
			for B in Q:
				B=f"{B}"
				if A._import_manager.is_file_path_valid(value=B)and A._import_manager.read_file_suffix(value=B)in M:
					D=A._database_manager.read_file_metadata(B);F=A._persistent_cache_database_manager.read_configuration_workspace_metadata(C,B);J=A._database_manager.read_object_property_timestamp_modified_value(D)or 1;K=A._database_manager.read_object_property_timestamp_modified_value(F)or 2
					if K!=J:E=A._database_manager.read_configuration_workspace_data_file(B);A._persistent_cache_database_manager.write_configuration_workspace_data(C,B,E);A._persistent_cache_database_manager.write_configuration_workspace_metadata(C,B,D);G=_A
					else:E=A._persistent_cache_database_manager.read_configuration_workspace_data(C,B);D=F
					H[B]=A._value_cache_database_manager.read_file_data(E,D)
		L=len(H);R=A._persistent_cache_database_manager.read_configuration_workspace_file_count(C)
		if L!=R:A._persistent_cache_database_manager.write_configuration_workspace_file_count(C,L);G=_A
		A._value_cache_database_manager.write_is_configuration_workspace_modified(G);A._value_cache_database_manager.write_configuration_workspace_file_count(C,L);A._value_cache_database_manager.write_configuration_workspace(C,H);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_private_configuration_workspace_extraction(self):self.run_task_configuration_workspace(_D);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_public_configuration_workspace_extraction(self):self.run_task_configuration_workspace(_E);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_configuration_workspace_object_merging(self):
		A=self;C=A._value_cache_database_manager.read_is_configuration_workspace_modified()or _C
		if C:
			B={};D=A._value_cache_database_manager.read_private_configuration_workspace()|A._value_cache_database_manager.read_public_configuration_workspace()
			for(F,E)in D.items():B=A._import_manager.object_deep_merge(left=B,right=E.get('data',{}))
			A._persistent_cache_database_manager.write_merged_configuration_workspace_data(B);A._value_cache_database_manager.write_merged_configuration_workspace_data(B)
		else:A._value_cache_database_manager.write_merged_configuration_workspace_data(A._persistent_cache_database_manager.read_merged_configuration_workspace_data())
		A._value_cache_database_manager.remove_configuration_workspace();return _A
	def run_task_plugins(A,accessibility_type):
		C=accessibility_type
		if not A._value_cache_database_manager.read_configuration_workspace_data_plugin_import_is_enabled_value():A._value_cache_database_manager.write_plugin_raw(C,{});return _A
		D={};F=f"{A._database_manager.read_root_plugin_filesystem_path(C)}";E=A._import_manager.read_python_filesystem_paths(path=f"{F}")
		if len(E)<1:A._value_cache_database_manager.write_plugin_raw(C,D);return _A
		for B in E:
			if not B:continue
			B=f"{B}";D[B]=A._database_manager.read_plugin_data(A._import_manager.read_python_file(file_path=B))
		A._value_cache_database_manager.write_plugin_raw(C,D);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_private_plugin_extraction(self):self.run_task_plugins(_D);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_public_plugin_extraction(self):self.run_task_plugins(_E);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_plugin_object_merging(self):
		A=self;C=A._value_cache_database_manager.read_plugin_private_raw()|A._value_cache_database_manager.read_plugin_public_raw();B={}
		for(E,D)in C.items():B=A._import_manager.object_deep_merge(left=B,right=D)
		A._value_cache_database_manager.write_plugin_data(B);A._value_cache_database_manager.remove_plugin_raw();return _A
	@_DecoratorManager.single_task_decorator
	def run_task_static_macros_extraction(self):A=self;B={};C=A._value_cache_database_manager.read_default_object_macros_values(A._database_manager.read_default_static_value_cache_macros());D=A._value_cache_database_manager.read_configuration_workspace_data_macros_static_value_cache_targets();E=A._value_cache_database_manager.read_configuration_workspace_data_macros_static_file_targets();F=A._value_cache_database_manager.read_plugin_data_macros_static_targets();B=C|D|E|F;A._value_cache_database_manager.write_macros(B);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_static_macros_object_merging(self):A=self;B=A._value_cache_database_manager.read_macros();B=A._value_cache_database_manager.read_object_macros(B);A._value_cache_database_manager.write_macros(B);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_static_macros_resolution(self):A=self;B=A._value_cache_database_manager.read_macros();B=A._import_manager.macros_resolve_many(values=B);A._value_cache_database_manager.write_macros(B);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_dynamic_macros_resolution(self):A=self;D=A._value_cache_database_manager.read_macros();B=A._value_cache_database_manager.read_default_object_macros_values(A._database_manager.read_default_dynamic_value_cache_macros());B=A._value_cache_database_manager.read_object_macros(B);C=A._value_cache_database_manager.read_plugin_data_macros_dynamic_targets();C=A._value_cache_database_manager.read_object_macros(C);A._value_cache_database_manager.write_macros(D|B|C);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_configuration_workspace_macros_resolution(self):A=self;C=A._value_cache_database_manager.read_macros();B=A._value_cache_database_manager.read_merged_configuration_workspace_data();B=A._import_manager.macros_parse_many(values=B,resolved=C);A._value_cache_database_manager.write_merged_configuration_workspace_data(B);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_console_logging_setup(self):A=self;D=A._value_cache_database_manager.read_configuration_workspace_data_log_is_enabled_value();E=A._value_cache_database_manager.read_configuration_workspace_data_log_is_enabled_override();F=A._value_cache_database_manager.read_configuration_workspace_data_log_is_verbose_value();G=A._value_cache_database_manager.read_configuration_workspace_data_log_is_verbose_override();B=A._value_cache_database_manager.read_configuration_workspace_data_log_console_is_enabled_value();C=A._value_cache_database_manager.read_configuration_workspace_data_log_console_is_verbose_value();B=D if E else B;C=F if G else C;A._import_manager.setup_console_log_settings(is_enabled=B,is_verbose=C);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_file_logging_setup(self):
		A=self;E=A._value_cache_database_manager.read_configuration_workspace_data_log_is_enabled_value();F=A._value_cache_database_manager.read_configuration_workspace_data_log_is_enabled_override();G=A._value_cache_database_manager.read_configuration_workspace_data_log_is_verbose_value();H=A._value_cache_database_manager.read_configuration_workspace_data_log_is_verbose_override();C=A._value_cache_database_manager.read_configuration_workspace_data_log_file_is_enabled_value();D=A._value_cache_database_manager.read_configuration_workspace_data_log_file_is_verbose_value();B=A._value_cache_database_manager.read_configuration_workspace_data_log_file_targets();I=A._value_cache_database_manager.read_configuration_workspace_data_log_default_file_output_is_enabled_value();J=A._database_manager.read_default_log_output_filesystem_paths();C=E if F else C;D=G if H else D;B=A._value_cache_database_manager.read_object_filesystem_values(B)
		if I:B=J|B
		A._import_manager.setup_file_log_settings(is_enabled=C,is_verbose=D,file_outputs=B);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_file_logging_shutdown(self):self._import_manager.log_shutdown();return _A
	@_DecoratorManager.single_task_decorator
	def run_task_filesystem_values(self):A=self;A._value_cache_database_manager.write_time_zone_name(A._value_cache_database_manager.read_configuration_workspace_data_time_zone_value());A._value_cache_database_manager.write_operating_system_name(A._value_cache_database_manager.read_configuration_workspace_data_operating_system_name_value());A._value_cache_database_manager.write_operating_system_architecture(A._value_cache_database_manager.read_configuration_workspace_data_operating_system_architecture_value());return _A
	@_DecoratorManager.single_task_decorator
	def run_task_workflow_setup(self):A=self;B=A._value_cache_database_manager.read_object_selections(A._value_cache_database_manager.read_configuration_workspace_data_workflow_selection());A._value_cache_database_manager.write_workflow_selection(B);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_export_group_setup(self):A=self;B=A._value_cache_database_manager.read_object_selections(A._value_cache_database_manager.read_configuration_workspace_data_export_group())|A._database_manager.read_default_export_groups();A._value_cache_database_manager.write_export_group(B);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_export_selection_setup(self):A=self;B=A._value_cache_database_manager.read_object_selections(A._value_cache_database_manager.read_configuration_workspace_data_export_selection())|A._database_manager.read_default_export_selections();A._value_cache_database_manager.write_export_selection(B);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_workspace_group_setup(self):A=self;B=A._value_cache_database_manager.read_object_selections(A._value_cache_database_manager.read_configuration_workspace_data_workspace_group_selection())|A._database_manager.read_default_groups();A._value_cache_database_manager.write_workspace_group(B);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_workspace_project_setup(self):A=self;B=A._value_cache_database_manager.read_object_selections(A._value_cache_database_manager.read_configuration_workspace_data_workspace_project_selection());A._value_cache_database_manager.write_workspace_project(B);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_workspace_default_setup(self):A=self._database_manager.read_default_selection_targets();self._value_cache_database_manager.write_workspace_default(A);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_filesystem_clean_exclude_setup(self):A=self;B=A._value_cache_database_manager.read_default_clean_excluded();C=A._value_cache_database_manager.read_object_exclude_filesystem_path_values(A._value_cache_database_manager.read_configuration_workspace_data_command_filesystem_clean_exclude_targets())|B;A._value_cache_database_manager.write_filesystem_clean_excluded(C);return _A
	@_DecoratorManager.single_task_decorator
	def run_task_filesystem_clean_include_setup(self):A=self;B=A._value_cache_database_manager.read_default_clean_included();C=A._value_cache_database_manager.read_object_command_filesystem_clean_included(A._value_cache_database_manager.read_configuration_workspace_data_command_filesystem_clean_include_selection())|B;A._value_cache_database_manager.write_filesystem_clean_included(C);return _A
	@_DecoratorManager.multi_task_decorator
	def run_task_disk_cache_shutdown(self):self._import_manager.close_via_disk_cache();return _A
	@_DecoratorManager.multi_task_decorator
	def run_task_disk_cache_cleanup_before(self):
		A=self._value_cache_database_manager.read_con_wor_data_cache_cleanup_before_is_enabled_value()
		if A:self._import_manager.clear_all_values_via_disk_cache()
		return _A
	@_DecoratorManager.multi_task_decorator
	def run_task_disk_cache_cleanup_after(self):
		A=self._value_cache_database_manager.read_con_wor_data_cache_cleanup_after_is_enabled_value()
		if A:self._import_manager.clear_all_values_via_disk_cache()
		return _A
	@_DecoratorManager.multi_task_decorator
	def run_task_value_cache_cleanup(self):return _A
	@_DecoratorManager.multi_task_decorator
	def run_task_closing_console_execution_navigation_setup(self):self.navigate_via_filesystem_path(self._value_cache_database_manager.read_root_filesystem_path());return _A
	@_DecoratorManager.multi_task_decorator
	def run_task_task_storage_shutdown(self):self._task_storage_manager.reset_all_task_executed();return _A
	@_DecoratorManager.multi_task_decorator
	def run_task_system_setup(self):A=self;A.run_task_system_values();A.run_task_root_filesystem_path();A.run_task_selection_filesystem_path();A.run_task_executing_console_filesystem_paths();A.run_task_initial_console_filesystem_path();A.run_task_disk_cache_output_folder_path();A.run_task_disk_cache_output_file_path();A.run_task_disk_cache_startup();A.run_task_disk_cache_cleanup_before();A.run_task_disk_cache_refresh();return _A
	@_DecoratorManager.multi_task_decorator
	def run_task_common_setup(self):A=self;A.run_task_system_setup();A.run_task_private_configuration_workspace_extraction();A.run_task_public_configuration_workspace_extraction();A.run_task_private_plugin_extraction();A.run_task_public_plugin_extraction();A.run_task_configuration_workspace_object_merging();A.run_task_filesystem_values();A.run_task_plugin_object_merging();A.run_task_static_macros_extraction();A.run_task_static_macros_object_merging();A.run_task_static_macros_resolution();A.run_task_dynamic_macros_resolution();A.run_task_configuration_workspace_macros_resolution();A.run_task_console_logging_setup();return _A
	@_DecoratorManager.multi_task_decorator
	def run_task_full_debug_value_cache_setup(self):A=self;A.run_task_common_setup();A.run_task_filesystem_clean_exclude_setup();A.run_task_filesystem_clean_include_setup();A.run_task_workflow_setup();A.run_task_workspace_default_setup();A.run_task_workspace_project_setup();A.run_task_workspace_group_setup();A.run_task_export_selection_setup();A.run_task_export_group_setup();return _A
	@_DecoratorManager.multi_task_decorator
	def run_task_full_debug_disk_cache_setup(self):self.run_task_system_setup();return _A
	@_DecoratorManager.multi_task_decorator
	def run_task_full_shutdown(self):A=self;A.run_task_closing_console_execution_navigation_setup();A.run_task_disk_cache_cleanup_after();A.run_task_disk_cache_shutdown();A.run_task_file_logging_setup();A.run_task_file_logging_shutdown();A.run_task_value_cache_cleanup();return _A
	@_DecoratorManager.multi_task_decorator
	def run_task_safe_clean_filesystem_path(self,target_path):
		B=target_path;A=self
		if not B:return _C
		A.run_task_filesystem_clean_exclude_setup();C=A._value_cache_database_manager.read_filesystem_clean_excluded()or{}
		if B in C:return _C
		A._import_manager.clean_filesystem_path(target_path=B);return _A
	@_DecoratorManager.multi_task_decorator
	def run_task_reboot_common_setup(self):A=self;A.run_task_full_shutdown();A.run_task_task_storage_shutdown();A.run_task_common_setup();return _A