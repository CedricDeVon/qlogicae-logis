from __future__ import annotations
L='public'
K='private'
G=False
D=None
A=True
from typing import Any,ParamSpec as M,TypeVar as N
from..library.decorator_manager import DecoratorManager as O
P=M('P')
Q=N('R')
__all__='TaskManager'
C=D
E=D
F=D
B=O
H=D
I=D
def J():global J;global C;global E;global F;global H;global I;from..library import database_manager as A,import_manager as B,persistent_cache_database_manager as G,task_storage_manager as K,value_cache_database_manager as L;C=B.ImportManager;E=A.DatabaseManager;H=L.ValueCacheDatabaseManager;F=K.TaskStorageManager;I=G.PersistentCacheDatabasManager;J=lambda:D
class R:
	__slots__='_import_manager','_database_manager','_task_storage_manager','_value_cache_database_manager','_persistent_cache_database_manager'
	def __init__(A):J();A._import_manager=C.read_singleton(C);A._database_manager=C.read_singleton(E);A._value_cache_database_manager=C.read_singleton(H);A._persistent_cache_database_manager=C.read_singleton(I);A._task_storage_manager=C.read_singleton(F)
	@B.single_task_decorator
	def run_task_system_values(self):B=self;B._value_cache_database_manager.write_current_timestamp();B._value_cache_database_manager.write_current_date();B._value_cache_database_manager.write_current_year();B._value_cache_database_manager.write_default_time_zone_name();B._value_cache_database_manager.write_default_operating_system_name();B._value_cache_database_manager.write_default_operating_system_architecture();return A
	@B.single_task_decorator
	def run_task_root_filesystem_path(self):self._value_cache_database_manager.write_root_filesystem_path();return A
	@B.single_task_decorator
	def run_task_selection_filesystem_path(self):self._value_cache_database_manager.write_selection_filesystem_path();return A
	@B.single_task_decorator
	def run_task_executing_console_filesystem_paths(self):B=self;B._value_cache_database_manager.write_initial_executing_console_filesystem_path(B._import_manager.read_original_executing_console_filesystem_path());B._value_cache_database_manager.write_previous_executing_console_filesystem_path(B._value_cache_database_manager.read_initial_executing_console_filesystem_path());B._value_cache_database_manager.write_current_executing_console_filesystem_path(B._value_cache_database_manager.read_initial_executing_console_filesystem_path());return A
	@B.single_task_decorator
	def run_task_disk_cache_output_folder_path(self):self._import_manager.setup_filesystem_tree_path(target_path=self._database_manager.read_default_cache_disk_output_folder_path());return A
	@B.single_task_decorator
	def run_task_disk_cache_output_file_path(self):self._import_manager.write_database_path_via_disk_cache(self._database_manager.read_default_disk_cache_output_file_path());return A
	@B.single_task_decorator
	def run_task_disk_cache_startup(self):self._import_manager.open_via_disk_cache();return A
	@B.single_task_decorator
	def run_task_disk_cache_refresh(self):
		for B in range(5):self._persistent_cache_database_manager.write_refresh_data({})
		return A
	@B.single_task_decorator
	def run_task_initial_console_filesystem_path(self):self.navigate_via_root_filesystem_path();return A
	@B.single_task_decorator
	def navigate_via_root_filesystem_path(self):self.navigate_via_filesystem_path(self._value_cache_database_manager.read_root_filesystem_path());return A
	@B.multi_task_decorator
	def navigate_via_filesystem_path(self,filesystem_path):
		C=filesystem_path;B=self
		if not C:return G
		B._value_cache_database_manager.write_previous_executing_console_filesystem_path(B._value_cache_database_manager.read_original_executing_console_filesystem_path());B._import_manager.write_current_executing_console_filesystem_path(filesystem_path=C);B._value_cache_database_manager.write_current_executing_console_filesystem_path(C);return A
	@B.multi_task_decorator
	def run_task_configuration_workspace(self,accessibility_type):
		D=accessibility_type;B=self
		if not D:return G
		I=B._value_cache_database_manager.read_is_configuration_workspace_modified()or G;O=B._database_manager.read_default_data_file_extensions();F={};J={};P=B._database_manager.read_configuration_workspace_base_file_paths(D);Q=B._database_manager.read_configuration_workspace_base_folder_paths(D)
		for K in P:
			for R in O:
				C=f"{K}{R}"
				if not B._import_manager.is_file_path_valid(value=C):continue
				E=B._database_manager.read_file_metadata(C);H=B._persistent_cache_database_manager.read_configuration_workspace_metadata(D,C);L=B._database_manager.read_object_property_timestamp_modified_value(E)or 1;M=B._database_manager.read_object_property_timestamp_modified_value(H)or 2
				if M!=L:F=B._database_manager.read_configuration_workspace_data_file(C);B._persistent_cache_database_manager.write_configuration_workspace_data(D,C,F);B._persistent_cache_database_manager.write_configuration_workspace_metadata(D,C,E);I=A
				else:F=B._persistent_cache_database_manager.read_configuration_workspace_data(D,C);E=H
				J[C]=B._value_cache_database_manager.read_file_data(F,E)
		for K in Q:
			if not B._import_manager.is_folder_path_valid(value=K):continue
			S=B._import_manager.read_child_folder_paths(value=K)
			for C in S:
				C=f"{C}"
				if B._import_manager.is_file_path_valid(value=C)and B._import_manager.read_file_suffix(value=C)in O:
					E=B._database_manager.read_file_metadata(C);H=B._persistent_cache_database_manager.read_configuration_workspace_metadata(D,C);L=B._database_manager.read_object_property_timestamp_modified_value(E)or 1;M=B._database_manager.read_object_property_timestamp_modified_value(H)or 2
					if M!=L:F=B._database_manager.read_configuration_workspace_data_file(C);B._persistent_cache_database_manager.write_configuration_workspace_data(D,C,F);B._persistent_cache_database_manager.write_configuration_workspace_metadata(D,C,E);I=A
					else:F=B._persistent_cache_database_manager.read_configuration_workspace_data(D,C);E=H
					J[C]=B._value_cache_database_manager.read_file_data(F,E)
		N=len(J);T=B._persistent_cache_database_manager.read_configuration_workspace_file_count(D)
		if N!=T:B._persistent_cache_database_manager.write_configuration_workspace_file_count(D,N);I=A
		B._value_cache_database_manager.write_is_configuration_workspace_modified(I);B._value_cache_database_manager.write_configuration_workspace_file_count(D,N);B._value_cache_database_manager.write_configuration_workspace(D,J);return A
	@B.single_task_decorator
	def run_task_private_configuration_workspace_extraction(self):self.run_task_configuration_workspace(K);return A
	@B.single_task_decorator
	def run_task_public_configuration_workspace_extraction(self):self.run_task_configuration_workspace(L);return A
	@B.single_task_decorator
	def run_task_configuration_workspace_object_merging(self):
		B=self;D=B._value_cache_database_manager.read_is_configuration_workspace_modified()or G
		if D:
			C={};E=B._value_cache_database_manager.read_private_configuration_workspace()|B._value_cache_database_manager.read_public_configuration_workspace()
			for(H,F)in E.items():C=B._import_manager.object_deep_merge(left=C,right=F.get('data',{}))
			B._persistent_cache_database_manager.write_merged_configuration_workspace_data(C);B._value_cache_database_manager.write_merged_configuration_workspace_data(C)
		else:B._value_cache_database_manager.write_merged_configuration_workspace_data(B._persistent_cache_database_manager.read_merged_configuration_workspace_data())
		B._value_cache_database_manager.remove_configuration_workspace();return A
	def run_task_plugins(B,accessibility_type):
		D=accessibility_type
		if not B._value_cache_database_manager.read_configuration_workspace_data_plugin_import_is_enabled_value():B._value_cache_database_manager.write_plugin_raw(D,{});return A
		E={};G=f"{B._database_manager.read_root_plugin_filesystem_path(D)}";F=B._import_manager.read_python_filesystem_paths(path=f"{G}")
		if len(F)<1:B._value_cache_database_manager.write_plugin_raw(D,E);return A
		for C in F:
			if not C:continue
			C=f"{C}";E[C]=B._database_manager.read_plugin_data(B._import_manager.read_python_file(file_path=C))
		B._value_cache_database_manager.write_plugin_raw(D,E);return A
	@B.single_task_decorator
	def run_task_private_plugin_extraction(self):self.run_task_plugins(K);return A
	@B.single_task_decorator
	def run_task_public_plugin_extraction(self):self.run_task_plugins(L);return A
	@B.single_task_decorator
	def run_task_plugin_object_merging(self):
		B=self;D=B._value_cache_database_manager.read_plugin_private_raw()|B._value_cache_database_manager.read_plugin_public_raw();C={}
		for(F,E)in D.items():C=B._import_manager.object_deep_merge(left=C,right=E)
		B._value_cache_database_manager.write_plugin_data(C);B._value_cache_database_manager.remove_plugin_raw();return A
	@B.single_task_decorator
	def run_task_static_macros_extraction(self):B=self;C={};D=B._value_cache_database_manager.read_default_object_macros_values(B._database_manager.read_default_static_value_cache_macros());E=B._value_cache_database_manager.read_configuration_workspace_data_macros_static_value_cache_targets();F=B._value_cache_database_manager.read_configuration_workspace_data_macros_static_file_targets();G=B._value_cache_database_manager.read_plugin_data_macros_static_targets();C=D|E|F|G;B._value_cache_database_manager.write_macros(C);return A
	@B.single_task_decorator
	def run_task_static_macros_object_merging(self):B=self;C=B._value_cache_database_manager.read_macros();C=B._value_cache_database_manager.read_object_macros(C);B._value_cache_database_manager.write_macros(C);return A
	@B.single_task_decorator
	def run_task_static_macros_resolution(self):B=self;C=B._value_cache_database_manager.read_macros();C=B._import_manager.macros_resolve_many(values=C);B._value_cache_database_manager.write_macros(C);return A
	@B.single_task_decorator
	def run_task_dynamic_macros_resolution(self):B=self;E=B._value_cache_database_manager.read_macros();C=B._value_cache_database_manager.read_default_object_macros_values(B._database_manager.read_default_dynamic_value_cache_macros());C=B._value_cache_database_manager.read_object_macros(C);D=B._value_cache_database_manager.read_plugin_data_macros_dynamic_targets();D=B._value_cache_database_manager.read_object_macros(D);B._value_cache_database_manager.write_macros(E|C|D);return A
	@B.single_task_decorator
	def run_task_configuration_workspace_macros_resolution(self):B=self;D=B._value_cache_database_manager.read_macros();C=B._value_cache_database_manager.read_merged_configuration_workspace_data();C=B._import_manager.macros_parse_many(values=C,resolved=D);B._value_cache_database_manager.write_merged_configuration_workspace_data(C);return A
	@B.single_task_decorator
	def run_task_console_logging_setup(self):B=self;E=B._value_cache_database_manager.read_configuration_workspace_data_log_is_enabled_value();F=B._value_cache_database_manager.read_configuration_workspace_data_log_is_enabled_override();G=B._value_cache_database_manager.read_configuration_workspace_data_log_is_verbose_value();H=B._value_cache_database_manager.read_configuration_workspace_data_log_is_verbose_override();C=B._value_cache_database_manager.read_configuration_workspace_data_log_console_is_enabled_value();D=B._value_cache_database_manager.read_configuration_workspace_data_log_console_is_verbose_value();C=E if F else C;D=G if H else D;B._import_manager.setup_console_log_settings(is_enabled=C,is_verbose=D);return A
	@B.single_task_decorator
	def run_task_file_logging_setup(self):
		B=self;F=B._value_cache_database_manager.read_configuration_workspace_data_log_is_enabled_value();G=B._value_cache_database_manager.read_configuration_workspace_data_log_is_enabled_override();H=B._value_cache_database_manager.read_configuration_workspace_data_log_is_verbose_value();I=B._value_cache_database_manager.read_configuration_workspace_data_log_is_verbose_override();D=B._value_cache_database_manager.read_configuration_workspace_data_log_file_is_enabled_value();E=B._value_cache_database_manager.read_configuration_workspace_data_log_file_is_verbose_value();C=B._value_cache_database_manager.read_configuration_workspace_data_log_file_targets();J=B._value_cache_database_manager.read_configuration_workspace_data_log_default_file_output_is_enabled_value();K=B._database_manager.read_default_log_output_filesystem_paths();D=F if G else D;E=H if I else E;C=B._value_cache_database_manager.read_object_filesystem_values(C)
		if J:C=K|C
		B._import_manager.setup_file_log_settings(is_enabled=D,is_verbose=E,file_outputs=C);return A
	@B.single_task_decorator
	def run_task_file_logging_shutdown(self):self._import_manager.log_shutdown();return A
	@B.single_task_decorator
	def run_task_filesystem_values(self):B=self;B._value_cache_database_manager.write_time_zone_name(B._value_cache_database_manager.read_configuration_workspace_data_time_zone_value());B._value_cache_database_manager.write_operating_system_name(B._value_cache_database_manager.read_configuration_workspace_data_operating_system_name_value());B._value_cache_database_manager.write_operating_system_architecture(B._value_cache_database_manager.read_configuration_workspace_data_operating_system_architecture_value());return A
	@B.single_task_decorator
	def run_task_workflow_setup(self):B=self;C=B._value_cache_database_manager.read_object_selections(B._value_cache_database_manager.read_configuration_workspace_data_workflow_selection());B._value_cache_database_manager.write_workflow_selection(C);return A
	@B.single_task_decorator
	def run_task_export_group_setup(self):B=self;C=B._value_cache_database_manager.read_object_selections(B._value_cache_database_manager.read_configuration_workspace_data_export_group())|B._database_manager.read_default_export_groups();B._value_cache_database_manager.write_export_group(C);return A
	@B.single_task_decorator
	def run_task_export_selection_setup(self):B=self;C=B._value_cache_database_manager.read_object_selections(B._value_cache_database_manager.read_configuration_workspace_data_export_selection())|B._database_manager.read_default_export_selections();B._value_cache_database_manager.write_export_selection(C);return A
	@B.single_task_decorator
	def run_task_workspace_group_setup(self):B=self;C=B._value_cache_database_manager.read_object_selections(B._value_cache_database_manager.read_configuration_workspace_data_workspace_group_selection())|B._database_manager.read_default_groups();B._value_cache_database_manager.write_workspace_group(C);return A
	@B.single_task_decorator
	def run_task_workspace_project_setup(self):B=self;C=B._value_cache_database_manager.read_object_selections(B._value_cache_database_manager.read_configuration_workspace_data_workspace_project_selection());B._value_cache_database_manager.write_workspace_project(C);return A
	@B.single_task_decorator
	def run_task_workspace_default_setup(self):B=self._database_manager.read_default_selection_targets();self._value_cache_database_manager.write_workspace_default(B);return A
	@B.single_task_decorator
	def run_task_filesystem_clean_exclude_setup(self):B=self;C=B._value_cache_database_manager.read_default_clean_excluded();D=B._value_cache_database_manager.read_object_exclude_filesystem_path_values(B._value_cache_database_manager.read_configuration_workspace_data_command_filesystem_clean_exclude_targets())|C;B._value_cache_database_manager.write_filesystem_clean_excluded(D);return A
	@B.single_task_decorator
	def run_task_filesystem_clean_include_setup(self):B=self;C=B._value_cache_database_manager.read_default_clean_included();D=B._value_cache_database_manager.read_object_command_filesystem_clean_included(B._value_cache_database_manager.read_configuration_workspace_data_command_filesystem_clean_include_selection())|C;B._value_cache_database_manager.write_filesystem_clean_included(D);return A
	@B.multi_task_decorator
	def run_task_disk_cache_shutdown(self):self._import_manager.close_via_disk_cache();return A
	@B.multi_task_decorator
	def run_task_disk_cache_cleanup_before(self):
		B=self._value_cache_database_manager.read_con_wor_data_cache_cleanup_before_is_enabled_value()
		if B:self._import_manager.clear_all_values_via_disk_cache()
		return A
	@B.multi_task_decorator
	def run_task_disk_cache_cleanup_after(self):
		B=self._value_cache_database_manager.read_con_wor_data_cache_cleanup_after_is_enabled_value()
		if B:self._import_manager.clear_all_values_via_disk_cache()
		return A
	@B.multi_task_decorator
	def run_task_value_cache_cleanup(self):return A
	@B.multi_task_decorator
	def run_task_closing_console_execution_navigation_setup(self):self.navigate_via_filesystem_path(self._value_cache_database_manager.read_root_filesystem_path());return A
	@B.multi_task_decorator
	def run_task_task_storage_shutdown(self):self._task_storage_manager.reset_all_task_executed();return A
	@B.multi_task_decorator
	def run_task_system_setup(self):B=self;B.run_task_system_values();B.run_task_root_filesystem_path();B.run_task_selection_filesystem_path();B.run_task_executing_console_filesystem_paths();B.run_task_initial_console_filesystem_path();B.run_task_disk_cache_output_folder_path();B.run_task_disk_cache_output_file_path();B.run_task_disk_cache_startup();B.run_task_disk_cache_cleanup_before();B.run_task_disk_cache_refresh();return A
	@B.multi_task_decorator
	def run_task_common_setup(self):B=self;B.run_task_system_setup();B.run_task_private_configuration_workspace_extraction();B.run_task_public_configuration_workspace_extraction();B.run_task_private_plugin_extraction();B.run_task_public_plugin_extraction();B.run_task_configuration_workspace_object_merging();B.run_task_filesystem_values();B.run_task_plugin_object_merging();B.run_task_static_macros_extraction();B.run_task_static_macros_object_merging();B.run_task_static_macros_resolution();B.run_task_dynamic_macros_resolution();B.run_task_configuration_workspace_macros_resolution();B.run_task_console_logging_setup();return A
	@B.multi_task_decorator
	def run_task_full_debug_value_cache_setup(self):B=self;B.run_task_common_setup();B.run_task_filesystem_clean_exclude_setup();B.run_task_filesystem_clean_include_setup();B.run_task_workflow_setup();B.run_task_workspace_default_setup();B.run_task_workspace_project_setup();B.run_task_workspace_group_setup();B.run_task_export_selection_setup();B.run_task_export_group_setup();return A
	@B.multi_task_decorator
	def run_task_full_debug_disk_cache_setup(self):self.run_task_system_setup();return A
	@B.multi_task_decorator
	def run_task_full_shutdown(self):B=self;B.run_task_closing_console_execution_navigation_setup();B.run_task_disk_cache_cleanup_after();B.run_task_disk_cache_shutdown();B.run_task_file_logging_setup();B.run_task_file_logging_shutdown();B.run_task_value_cache_cleanup();return A
	@B.multi_task_decorator
	def run_task_safe_clean_filesystem_path(self,target_path):
		C=target_path;B=self
		if not C:return G
		B.run_task_filesystem_clean_exclude_setup();D=B._value_cache_database_manager.read_filesystem_clean_excluded()or{}
		if C in D:return G
		B._import_manager.clean_filesystem_path(target_path=C);return A
	@B.multi_task_decorator
	def run_task_reboot_common_setup(self):B=self;B.run_task_full_shutdown();B.run_task_task_storage_shutdown();B.run_task_common_setup();return A