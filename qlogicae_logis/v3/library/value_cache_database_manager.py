from __future__ import annotations
_AH='outputis-enabled'
_AG='architecture'
_AF='vertical-count'
_AE='is-skipped'
_AD='indent-count'
_AC='maximum-depth'
_AB='highlight-2'
_AA='highlight-1'
_A9='value-cache'
_A8='is-modified'
_A7='current-executing-console-filesystem-path'
_A6='previous-executing-console-filesystem-path'
_A5='initial-executing-console-filesystem-path'
_A4='current-executing-script-filesystem-path'
_A3='selection-filesystem-path'
_A2='root-filesystem-path'
_A1='current-year'
_A0='current-date'
_z='current-timestamp'
_y='memory'
_x='duration'
_w='complete'
_v='reset'
_u='operating-system-architecture'
_t='operating-system-name'
_s='time-zone'
_r='configuration'
_q='alias'
_p='private'
_o='public'
_n='cache'
_m='workflow'
_l='template'
_k='project'
_j='default'
_i='override'
_h='count'
_g='compression'
_f='filesystem-path'
_e='include'
_d='exclude'
_c='after'
_b='before'
_a='static'
_Z=False
_Y=None
_X='group'
_W='clean'
_V='filesystem'
_U='is-verbose'
_T='timestamp'
_S='raw'
_R='file'
_Q='macros'
_P='cleanup'
_O='export'
_N='data'
_M='selection'
_L='plugin'
_K='workspace'
_J='command'
_I='operating-system'
_H='targets'
_G='log'
_F='style'
_E='display'
_D='is-enabled'
_C='console'
_B=True
_A='value'
from typing import Any
__all__='ValueCacheDatabaseManager'
_TaskManager=_Y
_ImportManager=_Y
_DatabaseManager=_Y
_CommandStorageManager=_Y
def _handle_dynamic_imports():global _handle_dynamic_imports;global _TaskManager;global _ImportManager;global _DatabaseManager;global _CommandStorageManager;from..library import database_manager as A,import_manager as B,task_manager as C;_TaskManager=C.TaskManager;_ImportManager=B.ImportManager;_DatabaseManager=A.DatabaseManager;_handle_dynamic_imports=lambda:_Y
class ValueCacheDatabaseManager:
	__slots__='_import_manager','_database_manager'
	def __init__(A):_handle_dynamic_imports();A._import_manager=_ImportManager.read_singleton(_ImportManager);A._database_manager=_ImportManager.read_singleton(_DatabaseManager)
	def read_default_clean_included(B):A={};return A
	def read_default_clean_excluded(A):B=A._import_manager.read_filesystem_entity_parents(target_path=A.read_root_filesystem_path());return B
	def read_key_path(A,key_path):return*A._database_manager.read_root_key_path(),*key_path
	def read_debug_snapshot_key_path(A,key_path):return*A._database_manager.read_root_key_path(),'debug','snapshot',*key_path
	def read_debug_snapshot_value(A,key_path):B=A._import_manager.read_any_value_via_value_cache(key_path=A.read_debug_snapshot_key_path(key_path))or{};return B
	def write_debug_snapshot_value(A,key_path,value):B=A._import_manager.write_any_value_via_value_cache(key_path=A.read_debug_snapshot_key_path(key_path),value=value);return B
	def read_configuration_workspace_data_key_path(A,key_path):return*A._database_manager.read_root_key_path(),_r,_K,_N,*key_path
	def read_configuration_workspace_data_value(A,key_path):B=A._import_manager.read_any_value_via_value_cache(key_path=A.read_configuration_workspace_data_key_path(key_path))or{};return B
	def write_configuration_workspace_data_value(A,key_path,value):B=A._import_manager.write_any_value_via_value_cache(key_path=A.read_configuration_workspace_data_key_path(key_path),value=value);return B
	def read_configuration_workspace_raw_key_path(A,key_path):return*A._database_manager.read_root_key_path(),_r,_K,_S,*key_path
	def read_configuration_workspace_raw_value(A,key_path):B=A._import_manager.read_any_value_via_value_cache(key_path=A.read_configuration_workspace_raw_key_path(key_path))or{};return B
	def write_configuration_workspace_raw_value(A,key_path,value):B=A._import_manager.write_any_value_via_value_cache(key_path=A.read_configuration_workspace_raw_key_path(key_path),value=value);return B
	def read_any_value(A,key_path):B=A._import_manager.read_any_value_via_value_cache(key_path=A.read_key_path(key_path))or{};return B
	def write_any_value(A,key_path,value):B=A._import_manager.write_any_value_via_value_cache(key_path=A.read_key_path(key_path),value=value);return B
	def remove_any_value(A,key_path):B=A._import_manager.remove_one_value_via_value_cache(key_path=A.read_key_path(key_path));return B
	def read_debug_snapshot_execution(A,label=''):
		if not A._database_manager.read_debug_is_enabled():return{}
		B=A.read_debug_snapshot_value((f"{label}",_T));return B
	def write_debug_snapshot_execution(A,label='',data=_Y):
		if not A._database_manager.read_debug_is_enabled():return _B
		A.write_debug_snapshot_value((f"{label}",_T),data or{});return _B
	def read_debug_snapshot_execution_timestamp_start(A,label=''):
		if not A._database_manager.read_debug_is_enabled():return 0
		B=A.read_debug_snapshot_value((f"{label}",_T,'start',_A));return B
	def write_debug_snapshot_execution_timestamp_start(A,label=''):
		if not A._database_manager.read_debug_is_enabled():return _B
		A.write_debug_snapshot_value((f"{label}",_T,'start',_A),A._import_manager.read_current_nanosecond());return _B
	def read_debug_snapshot_execution_timestamp_complete(A,label=''):
		if not A._database_manager.read_debug_is_enabled():return 0
		B=A.read_debug_snapshot_value((f"{label}",_T,_w,_A));return B
	def write_debug_snapshot_execution_timestamp_complete(A,label=''):
		B=label
		if not A._database_manager.read_debug_is_enabled():return _B
		A.write_debug_snapshot_value((f"{B}",_T,_w,_A),A._import_manager.read_current_nanosecond());A.write_debug_snapshot_execution_timestamp_duration(label=B);return _B
	def read_debug_snapshot_execution_timestamp_duration(A,label=''):
		if not A._database_manager.read_debug_is_enabled():return .0
		B=A.read_debug_snapshot_value((f"{label}",_T,_x,_A));return B
	def write_debug_snapshot_execution_timestamp_duration(A,label=''):
		B=label
		if not A._database_manager.read_debug_is_enabled():return _B
		C=(A.read_debug_snapshot_execution_timestamp_complete(label=B)-A.read_debug_snapshot_execution_timestamp_start(label=B))/1000000;A.write_debug_snapshot_value((f"{B}",_T,_x,_A),C);return _B
	def read_debug_snapshot_execution_memory(A,label=''):
		if not A._database_manager.read_debug_is_enabled():return{}
		B=A.read_debug_snapshot_value((f"{label}",_y));return B
	def write_debug_snapshot_execution_memory(A,label=''):
		if not A._database_manager.read_debug_is_enabled():return _B
		B=A._import_manager.snapshot_memory_usage();A.write_debug_snapshot_value((f"{label}",_y),B);return _B
	def read_current_timestamp(A):B=A.read_any_value((_z,_A))or 0;return B
	def write_current_timestamp(A):A.write_any_value((_z,_A),A._import_manager.read_current_nanosecond());return _B
	def read_time_zone_name(A):B=A.read_any_value((_s,_A))or'';return B
	def write_time_zone_name(A,value):A.write_any_value((_s,_A),value);return _B
	def write_default_time_zone_name(A):A.write_any_value((_s,_A),'local');return _B
	def read_operating_system_name(A):B=A.read_any_value((_t,_A))or A._import_manager.read_operating_system_name();return B
	def write_operating_system_name(A,value):A.write_any_value((_t,_A),value);return _B
	def write_default_operating_system_name(A):A.write_any_value((_t,_A),A._import_manager.read_operating_system_name());return _B
	def read_operating_system_architecture(A):B=A.read_any_value((_u,_A))or A._import_manager.read_operating_system_architecture();return B
	def write_operating_system_architecture(A,value):A.write_any_value((_u,_A),value);return _B
	def write_default_operating_system_architecture(A):A.write_any_value((_u,_A),A._import_manager.read_operating_system_architecture());return _B
	def read_current_date(A):B=A.read_any_value((_A0,_A))or'1970';return B
	def write_current_date(A):A.write_any_value((_A0,_A),A._import_manager.read_current_iso8601_date());return _B
	def read_current_year(A):B=A.read_any_value((_A1,_A))or 0;return B
	def write_current_year(A):A.write_any_value((_A1,_A),A._import_manager.read_current_year());return _B
	def read_root_filesystem_path(A):B=A.read_any_value((_A2,_A));return B
	def write_root_filesystem_path(A):A.write_any_value((_A2,_A),A._import_manager.read_original_executing_console_filesystem_path());return _B
	def read_selection_filesystem_path(A):B=A.read_any_value((_A3,_A));return B
	def write_selection_filesystem_path(A):A.write_any_value((_A3,_A),f"{A._import_manager.read_original_executing_console_filesystem_path()}/selection");return _B
	def read_current_executing_script_filesystem_path(A):B=A.read_any_value((_A4,_A));return B
	def write_current_executing_script_filesystem_path(A,value):A.write_any_value((_A4,_A),value);return _B
	def read_initial_executing_console_filesystem_path(A):B=A.read_any_value((_A5,_A));return B
	def write_initial_executing_console_filesystem_path(A,value):A.write_any_value((_A5,_A),value);return _B
	def read_previous_executing_console_filesystem_path(A):B=A.read_any_value((_A6,_A));return B
	def write_previous_executing_console_filesystem_path(A,value):A.write_any_value((_A6,_A),value);return _B
	def read_original_executing_console_filesystem_path(A):B=A.read_any_value((_A7,_A));return B
	def write_current_executing_console_filesystem_path(A,value):A.write_any_value((_A7,_A),value);return _B
	def read_configuration_workspace(A,accessibility_type):B=A.read_configuration_workspace_raw_value((accessibility_type,))or{};return B
	def write_configuration_workspace(A,accessibility_type,value):A.write_configuration_workspace_raw_value((accessibility_type,),value);return _B
	def remove_configuration_workspace(A):A.remove_any_value((_r,_K,_S));return _B
	def read_configuration_workspace_data(A,accessibility_type,key_path):B=A.read_configuration_workspace_raw_value((accessibility_type,key_path,_N,_A))or{};return B
	def write_configuration_workspace_rdata(A,accessibility_type,key_path,value):A.write_configuration_workspace_raw_value((accessibility_type,key_path,_N,_A),value);return _B
	def read_is_configuration_workspace_modified(A):B=A.read_configuration_workspace_raw_value((_A8,_A));return B
	def write_is_configuration_workspace_modified(A,value):A.write_configuration_workspace_raw_value((_A8,_A),value);return _B
	def read_configuration_workspace_file_count(A,accessibility_type):B=A.read_configuration_workspace_raw_value((_h,accessibility_type,_A));return B
	def write_configuration_workspace_file_count(A,accessibility_type,value):A.write_configuration_workspace_raw_value((_h,accessibility_type,_A),value);return _B
	def read_merged_configuration_workspace_data(A):B=A.read_configuration_workspace_data_value(())or{};return B
	def write_merged_configuration_workspace_data(A,value):A.write_configuration_workspace_data_value((),value);return _B
	def read_configuration_workspace_data_macros_static_value_cache_targets(A):B=A.read_configuration_workspace_data_value((_Q,_a,_A9,_H))or{};return B
	def write_configuration_workspace_data_macros_static_value_cache_targets(A,value):A.write_configuration_workspace_data_value((_Q,_a,_A9,_H),value);return _B
	def read_configuration_workspace_data_macros_static_file_targets(A):B=A.read_configuration_workspace_data_value((_Q,_a,_R,_H))or{};return B
	def write_configuration_workspace_data_macros_static_file_targets(A,value):A.write_configuration_workspace_data_value((_Q,_a,_R,_H),value);return _B
	def read_configuration_workspace_data_plugin_import_is_enabled_value(A):B=A.read_configuration_workspace_data_value((_L,'import',_D))or{};return bool(B.get(_A,_B))
	def write_configuration_workspace_data_plugin_import_is_enabled_value(A,value):A.write_configuration_workspace_data_value((_L,'import',_D,_A),value);return _B
	def read_configuration_workspace_data_display_console_is_enabled_value(A):B=A.read_configuration_workspace_data_value((_E,_C,_D))or{};return bool(B.get(_A,_B))
	def write_configuration_workspace_data_display_console_is_enabled_value(A,value):A.write_configuration_workspace_data_value((_E,_C,_D,_A),value);return _B
	def read_configuration_workspace_data_display_console_style(A):B=A.read_configuration_workspace_data_value((_E,_C,_F));return B
	def write_configuration_workspace_data_display_console_style(A,value):A.write_configuration_workspace_data_value((_E,_C,_F),value);return _B
	def read_configuration_workspace_data_display_console_style_reset_value(A):B=A.read_configuration_workspace_data_value((_E,_C,_F,_v))or{};return str(B.get(_A,_v))
	def write_configuration_workspace_data_display_console_style_reset_value(A,value):A.write_configuration_workspace_data_value((_E,_C,_F,_v,_A),value);return _B
	def read_configuration_workspace_data_display_console_style_base_1_value(A):B=A.read_configuration_workspace_data_value((_E,_C,_F,'base-1'))or{};return str(B.get(_A,''))
	def write_configuration_workspace_data_display_console_style_base_1_value(A,value):A.write_configuration_workspace_data_value((_E,_C,_F,'base-1',_A),value);return _B
	def read_configuration_workspace_data_display_console_style_base_2_value(A):B=A.read_configuration_workspace_data_value((_E,_C,_F,'base-2'))or{};return str(B.get(_A,'grey'))
	def write_configuration_workspace_data_display_console_style_base_2_value(A,value):A.write_configuration_workspace_data_value((_E,_C,_F,'base-2',_A),value);return _B
	def read_configuration_workspace_data_display_console_style_highlight_1_value(A):B=A.read_configuration_workspace_data_value((_E,_C,_F,_AA))or{};return str(B.get(_A,'green'))
	def write_configuration_workspace_data_display_console_style_highlight_1_value(A,value):A.write_configuration_workspace_data_value((_E,_C,_F,_AA,_A),value);return _B
	def read_configuration_workspace_data_display_console_style_highlight_2_value(A):B=A.read_configuration_workspace_data_value((_E,_C,_F,_AB))or{};return str(B.get(_A,'green'))
	def write_configuration_workspace_data_display_console_style_highlight_2_value(A,value):A.write_configuration_workspace_data_value((_E,_C,_F,_AB,_A),value);return _B
	def read_configuration_workspace_data_display_console_style_maximum_depth_value(A):B=A.read_configuration_workspace_data_value((_E,_C,_F,_AC))or{};return B.get(_A,_Y)
	def write_configuration_workspace_data_display_console_style_maximum_depth_value(A,value):A.write_configuration_workspace_data_value((_E,_C,_F,_AC,_A),value);return _B
	def read_configuration_workspace_data_display_console_style_indent_count_value(A):B=A.read_configuration_workspace_data_value((_E,_C,_F,_AD))or{};return int(B.get(_A,4))
	def write_configuration_workspace_data_display_console_style_indent_count_value(A,value):A.write_configuration_workspace_data_value((_E,_C,_F,_AD,_A),value);return _B
	def read_configuration_workspace_data_display_console_style_is_skipped_value(A):B=A.read_configuration_workspace_data_value((_E,_C,_F,_AE))or{};return bool(B.get(_A,_B))
	def write_configuration_workspace_data_display_console_style_is_skipped_value(A,value):A.write_configuration_workspace_data_value((_E,_C,_F,_AE,_A),value);return _B
	def read_configuration_workspace_data_display_console_style_vertical_count_value(A):B=A.read_configuration_workspace_data_value((_E,_C,_F,_AF))or{};return int(B.get(_A,0))
	def write_configuration_workspace_data_display_console_style_vertical_count_value(A,value):A.write_configuration_workspace_data_value((_E,_C,_F,_AF,_A),value);return _B
	def read_configuration_workspace_data_time_zone_value(A):B=A.read_configuration_workspace_data_value(('time','zone'))or{};return str(B.get(_A,'local'))
	def write_configuration_workspace_data_time_zone_value(A,value):A.write_configuration_workspace_data_value(('time','zone',_A),value);return _B
	def read_configuration_workspace_data_operating_system_name_value(A):B=A.read_configuration_workspace_data_value((_I,'name'))or{};return str(B.get(_A,A._import_manager.read_operating_system_name()))
	def write_configuration_workspace_data_operating_system_name_value(A,value):A.write_configuration_workspace_data_value((_I,'name',_A),value);return _B
	def read_configuration_workspace_data_operating_system_value(A):B=A.read_configuration_workspace_data_value((_I,))or{};return str(B.get(_A,f"{A._import_manager.read_operating_system_name()}-{A._import_manager.read_operating_system_architecture()}"))
	def write_configuration_workspace_data_operating_system_value(A,value):A.write_configuration_workspace_data_value((_I,_A),value);return _B
	def read_configuration_workspace_data_operating_system_architecture_value(A):B=A.read_configuration_workspace_data_value((_I,_AG))or{};return str(B.get(_A,A._import_manager.read_operating_system_architecture()))
	def write_configuration_workspace_data_operating_system_architecture_value(A,value):A.write_configuration_workspace_data_value((_I,_AG,_A),value);return _B
	def read_configuration_workspace_data_log_is_enabled_value(A):B=A.read_configuration_workspace_data_value((_G,_D))or{};return bool(B.get(_A,_B))
	def write_configuration_workspace_data_log_is_enabled_value(A,value):A.write_configuration_workspace_data_value((_G,_D,_A),value);return _B
	def read_configuration_workspace_data_log_is_enabled_override(A):B=A.read_configuration_workspace_data_value((_G,_D))or{};return bool(B.get(_i,_Z))
	def write_configuration_workspace_data_log_is_enabled_override(A,value):A.write_configuration_workspace_data_value((_G,_D,_i),value);return _B
	def read_configuration_workspace_data_log_is_verbose_value(A):B=A.read_configuration_workspace_data_value((_G,_U))or{};return bool(B.get(_A,_B))
	def write_configuration_workspace_data_log_is_verbose_value(A,value):A.write_configuration_workspace_data_value((_G,_U,_A),value);return _B
	def read_configuration_workspace_data_log_is_verbose_override(A):B=A.read_configuration_workspace_data_value((_G,_U))or{};return bool(B.get(_i,_Z))
	def write_configuration_workspace_data_log_is_verbose_override(A,value):A.write_configuration_workspace_data_value((_G,_U,_i),value);return _B
	def read_configuration_workspace_data_log_file_is_enabled_value(A):B=A.read_configuration_workspace_data_value((_G,_R,_D))or{};return bool(B.get(_A,_B))
	def write_configuration_workspace_data_log_file_is_enabled_value(A,value):A.write_configuration_workspace_data_value((_G,_R,_D,_A),value);return _B
	def read_configuration_workspace_data_log_file_is_verbose_value(A):B=A.read_configuration_workspace_data_value((_G,_R,_U))or{};return bool(B.get(_A,_B))
	def write_configuration_workspace_data_log_file_is_verbose_value(A,value):A.write_configuration_workspace_data_value((_G,_R,_U,_A),value);return _B
	def read_configuration_workspace_data_log_file_targets(A):B=A.read_configuration_workspace_data_value((_G,_R))or{};return B.get(_H,{})
	def write_configuration_workspace_data_log_file_targets(A,value):A.write_configuration_workspace_data_value((_G,_R,_H),value);return _B
	def read_configuration_workspace_data_log_console_is_enabled_value(A):B=A.read_configuration_workspace_data_value((_G,_C,_D))or{};return bool(B.get(_A,_B))
	def write_configuration_workspace_data_log_console_is_enabled_value(A,value):A.write_configuration_workspace_data_value((_G,_C,_D,_A),value);return _B
	def read_configuration_workspace_data_log_console_is_verbose_value(A):B=A.read_configuration_workspace_data_value((_G,_C,_U))or{};return bool(B.get(_A,_Z))
	def write_configuration_workspace_data_log_console_is_verbose_value(A,value):A.write_configuration_workspace_data_value((_G,_C,_U,_A),value);return _B
	def read_configuration_workspace_data_log_default_file_output_is_enabled_value(A):B=A.read_configuration_workspace_data_value((_G,_j,_R,_AH))or{};return bool(B.get(_A,_B))
	def write_configuration_workspace_data_log_default_file_output_is_enabled_value(A,value):A.write_configuration_workspace_data_value((_G,_j,_R,_AH,_A),value);return _B
	def read_configuration_workspace_data_command_filesystem_clean_exclude_targets(A):B=A.read_configuration_workspace_data_value((_J,_V,_W,_d))or{};return tuple(B.get(_H,tuple()))
	def write_configuration_workspace_data_command_filesystem_clean_exclude_targets(A,value):A.write_configuration_workspace_data_value((_J,_V,_W,_d,_H),value);return _B
	def read_configuration_workspace_data_command_filesystem_clean_include_selection(A):B=A.read_configuration_workspace_data_value((_J,_V,_W,_e))or{};return B.get(_M,{})
	def write_configuration_workspace_data_command_filesystem_clean_include_selection(A,value):A.write_configuration_workspace_data_value((_J,_V,_W,_e,_M),value);return _B
	def read_configuration_workspace_data_workspace_project_selection(A):B=A.read_configuration_workspace_data_value((_K,_k))or{};return B.get(_M,{})
	def write_configuration_workspace_data_workspace_project_selection(A,value):A.write_configuration_workspace_data_value((_K,_k,_M),value);return _B
	def read_configuration_workspace_data_workspace_group_selection(A):B=A.read_configuration_workspace_data_value((_K,_X))or{};return B.get(_M,{})
	def write_configuration_workspace_data_workspace_group_selection(A,value):A.write_configuration_workspace_data_value((_K,_X,_M),value);return _B
	def read_configuration_workspace_data_export_group(A):B=A.read_configuration_workspace_data_value((_J,_O))or{};return B.get(_X,{})
	def write_configuration_export_data_export_group(A,value):A.write_configuration_workspace_data_value((_J,_O,_X),value);return _B
	def read_configuration_workspace_data_export_selection(A):B=A.read_configuration_workspace_data_value((_J,_O))or{};return B.get(_M,{})
	def write_configuration_workspace_data_export_selection(A,value):A.write_configuration_workspace_data_value((_J,_O,_M),value);return _B
	def read_con_wor_data_export_cleanup_before_is_enabled_value(A):B=A.read_configuration_workspace_data_value((_J,_O,_P,_b,_D))or{};return bool(B.get(_A,_B))
	def write_con_wor_data_export_cleanup_before_is_enabled_value(A,value):A.write_configuration_workspace_data_value((_J,_O,_P,_b,_D,_A),value);return _B
	def read_con_wor_data_export_cleanup_after_is_enabled_value(A):B=A.read_configuration_workspace_data_value((_J,_O,_P,_c,_D))or{};return bool(B.get(_A,_B))
	def write_con_wor_data_export_cleanup_after_is_enabled_value(A,value):A.write_configuration_workspace_data_value((_J,_O,_P,_c,_D,_A),value);return _B
	def read_con_wor_data_template_cleanup_before_is_enabled_value(A):B=A.read_configuration_workspace_data_value((_J,_l,_P,_b,_D))or{};return bool(B.get(_A,_B))
	def write_con_wor_data_template_cleanup_before_is_enabled_value(A,value):A.write_configuration_workspace_data_value((_J,_l,_P,_b,_D,_A),value);return _B
	def read_con_wor_data_template_cleanup_after_is_enabled_value(A):B=A.read_configuration_workspace_data_value((_J,_l,_P,_c,_D))or{};return bool(B.get(_A,_B))
	def write_con_wor_data_template_cleanup_after_is_enabled_value(A,value):A.write_configuration_workspace_data_value((_J,_l,_P,_c,_D,_A),value);return _B
	def read_configuration_workspace_data_workflow_selection(A):B=A.read_configuration_workspace_data_value((_m,))or{};return B.get(_M,{})
	def write_configuration_workspace_data_workflow_selection(A,value):A.write_configuration_workspace_data_value((_m,_M),value);return _B
	def read_con_wor_data_cache_cleanup_before_is_enabled_value(A):B=A.read_configuration_workspace_data_value((_n,_P,_b,_D))or{};return bool(B.get(_A,_Z))
	def write_con_wor_data_cache_cleanup_before_is_enabled_value(A,value):A.write_configuration_workspace_data_value((_n,_P,_b,_D,_A),value);return _B
	def read_con_wor_data_cache_cleanup_after_is_enabled_value(A):B=A.read_configuration_workspace_data_value((_n,_P,_c,_D))or{};return bool(B.get(_A,_Z))
	def write_con_wor_data_cache_cleanup_after_is_enabled_value(A,value):A.write_configuration_workspace_data_value((_n,_P,_c,_D,_A),value);return _B
	def read_macros(A):B=A.read_any_value((_Q,))or{};return B
	def write_macros(A,value):A.write_any_value((_Q,),value);return _B
	def read_public_configuration_workspace(A):B=A.read_configuration_workspace(_o)or{};return B
	def write_public_configuration_workspace(A,value):A.write_configuration_workspace(_o,value);return _B
	def read_private_configuration_workspace(A):B=A.read_configuration_workspace(_p)or{};return B
	def write_private_configuration_workspace(A,value):A.write_configuration_workspace(_p,value);return _B
	def read_plugin_raw(A,accessibility_type):B=A.read_any_value((_L,_S,accessibility_type))or{};return B
	def write_plugin_raw(A,accessibility_type,value):A.write_any_value((_L,_S,accessibility_type),value);return _B
	def remove_plugin_raw(A):A.remove_any_value((_L,_S));return _B
	def read_plugin_raw_data(A,accessibility_type,key_path):B=A.read_any_value((_L,_S,accessibility_type,key_path,_N,_A))or{};return B
	def write_plugin_raw_data(A,accessibility_type,key_path,value):A.write_any_value((_L,_S,accessibility_type,key_path,_N,_A),value);return _B
	def read_plugin_public_raw(A):B=A.read_plugin_raw(_o)or{};return B
	def write_plugin_public_raw(A,value):A.write_plugin_raw(_o,value);return _B
	def read_plugin_private_raw(A):B=A.read_plugin_raw(_p)or{};return B
	def write_plugin_private_raw(A,value):A.write_plugin_raw(_p,value);return _B
	def read_plugin_raw_file_count(A,accessibility_type):B=A.read_any_value((_L,_S,_h,accessibility_type,_A));return B
	def write_plugin_raw_file_count(A,accessibility_type,value):A.write_any_value((_L,_S,_h,accessibility_type,_A),value);return _B
	def read_plugin_data_macros_static_targets(A):B=A.read_any_value((_L,_N,_Q,_a,_H))or{};return B
	def write_plugin_data_macros_static_targets(A,value):A.write_any_value((_L,_N,_Q,_a,_H),value);return _B
	def read_plugin_data_macros_dynamic_targets(A):B=A.read_any_value((_L,_N,_Q,'dynamic',_H))or{};return B
	def write_plugin_data_macros_dynamic_targets(A,value):A.write_any_value((_L,_N,_Q,'dynamic',_H),value);return _B
	def read_plugin_data(A):B=A.read_any_value((_L,_N))or{};return B
	def write_plugin_data(A,value):A.write_any_value((_L,_N),value);return _B
	def read_default_object_macros_values(C,data):
		A={}
		if not data:return A
		for B in data:A[B]={_A:C.read_any_value((B,_A))}
		return A
	def read_filesystem_clean_excluded(A):B=A.read_any_value((_V,_W))or{};return set(B.get('excluded',set()))
	def write_filesystem_clean_excluded(A,value):A.write_any_value((_V,_W,'excluded'),value);return _B
	def read_filesystem_clean_included(A):B=A.read_any_value((_V,_W))or{};return B.get('included',{})
	def write_filesystem_clean_included(A,value):A.write_any_value((_V,_W,'included'),value);return _B
	def read_workspace_group(A):B=A.read_any_value((_K,))or{};return B.get(_X,{})
	def write_workspace_group(A,value):A.write_any_value((_K,_X),value);return _B
	def read_workspace_project(A):B=A.read_any_value((_K,))or{};return B.get(_k,{})
	def write_workspace_project(A,value):A.write_any_value((_K,_k),value);return _B
	def read_workspace_default(A):B=A.read_any_value((_K,))or{};return B.get(_j,{})
	def write_workspace_default(A,value):A.write_any_value((_K,_j),value);return _B
	def read_workspace_all(A):B=A.read_any_value((_K,))or{};return B.get('all',{})
	def write_workspace_all(A,value):A.write_any_value((_K,'all'),value);return _B
	def read_export_selection(A):B=A.read_any_value((_O,))or{};return B.get(_M,{})
	def write_export_selection(A,value):A.write_any_value((_O,_M),value);return _B
	def read_export_group(A):B=A.read_any_value((_O,))or{};return B.get(_X,{})
	def write_export_group(A,value):A.write_any_value((_O,_X),value);return _B
	def read_workflow_selection(A):B=A.read_any_value((_m,))or{};return B.get(_M,{})
	def write_workflow_selection(A,value):A.write_any_value((_m,_M),value);return _B
	def read_object_macros(B,data):
		A={}
		if not data:return A
		A=B.read_object_macros_values(data);return A
	def read_object_filesystem_values(C,data):
		B=set()
		if not data:return B
		for A in data:
			if not A or _f not in A:continue
			if A and _I in A and not C.read_is_object_operating_system_included(A[_I]):continue
			A=A[_f]
			if not A or _A not in A:continue
			A=A[_A];B.add(A)
		return B
	def read_object_macros_values(C,data):
		B={}
		if not data:return B
		for(D,A)in data.items():
			if not A or _A not in A:continue
			if A and _I in A and not C.read_is_object_operating_system_included(A[_I]):continue
			B[D]=A[_A]
			if A and _q in A:
				E=C.read_object_alias_item_values(A[_q])
				for F in E:B[F]=A[_A]
		return B
	def read_object_selections(D,data):
		B={}
		if not data:return B
		for(C,A)in data.items():
			if A and _I in A and not D.read_is_object_operating_system_included(A[_I]):continue
			B[C]=C
			if A and _q in A:
				E=D.read_object_alias_item_values(A[_q])
				for F in E:B[F]=C
		return B
	def read_object_filesystem_pattern_values(C,data):
		B=set()
		if not data:return B
		for A in data:
			if not A or _f not in A:continue
			if A and _I in A and not C.read_is_object_operating_system_included(A[_I]):continue
			D=A[_f]
			if _A not in D:continue
			E=D[_A];F=C.read_object_pattern_value(A)
			if F:
				G=C._import_manager.read_filesystem_via_pattern(filesystem_path=E,pattern=F)
				for H in G:B.add(f"{H}")
			B.add(E)
		return B
	def read_object_pattern_values(C,data):
		B=set()
		if not data:return B
		for A in data:
			if A and _I in A and not C.read_is_object_operating_system_included(A[_I]):continue
			D=C.read_object_pattern_value(A)
			if not D:continue
			B.add(D)
		return B
	def read_object_exclude_filesystem_path_values(A,data):return A.read_object_filesystem_pattern_values(data)
	def read_object_include_filesystem_path_values(C,data):
		A={}
		if not data:return A
		for(D,B)in data.items():
			if _H not in B:continue
			A[D]=C.read_object_filesystem_pattern_values(B[_H])
		return A
	def read_object_command_filesystem_clean_included(A,data):B=A.read_object_selections(data);return B
	def read_object_alias_item_values(C,data):
		A=set()
		for(B,D)in data.items():A.add(B)
		return A
	def read_object_system_is_include(C,data):
		A=set()
		for(B,D)in data.items():A.add(B)
		return A
	def read_object_pattern_value(B,data):A=data.get('pattern',{}).get(_A,'');return A
	def read_object_selection(B,data):A=data.get(_M,{});return A
	def read_object_output_targets(B,data):A=data.get('output',{}).get(_H,[]);return A
	def read_object_input_exclude_targets(B,data):A=data.get('input',{}).get(_d,{}).get(_H,[]);return A
	def read_object_input_include_targets(B,data):A=data.get('input',{}).get(_e,{}).get(_H,[]);return A
	def read_object_is_enabled_value(B,data):A=data.get(_D,{}).get(_A,_B);return A
	def read_object_filesystem_path_value(B,data):A=data.get(_f,{}).get(_A,'');return A
	def read_object_argument(B,data):A=data.get('argument',{});return A
	def read_object_process_value(B,data):A=data.get('process',{}).get(_A,'shell');return A
	def read_object_run_value(B,data):A=data.get('run',{}).get(_A,'');return A
	def read_object_delay_value(B,data):A=data.get('delay',{}).get(_A,0);return A
	def read_object_scripts(B,data):A=data.get('scripts',[]);return A
	def read_object_compression_format_value(B,data):A=data.get(_g,{}).get('format',{}).get(_A,'zip');return A
	def read_object_compression_type_value(B,data):A=data.get(_g,{}).get('type',{}).get(_A,'deflated');return A
	def read_object_compression_level_value(B,data):A=data.get(_g,{}).get('level',{}).get(_A,6);return A
	def read_object_compression_is_zip_64_allowed_value(B,data):A=data.get(_g,{}).get('is-zip-64-allowed',{}).get(_A,_B);return A
	def read_object_compression_is_timestamp_strict_value(B,data):A=data.get(_g,{}).get('is-timestamp-strict',{}).get(_A,_B);return A
	def read_is_object_operating_system_included(B,data):
		A=data
		if not A or _e not in A and _d not in A:return _B
		D=B.read_operating_system_name();E=B.read_operating_system_architecture();C=f"{D}-{E}";F=A.get(_e,{});G=A.get(_d,{})
		if C in G:return _Z
		if C in F:return _B
		return _Z
	def read_file_data(A,data,metadata):return{_N:data,'metadata':metadata}or{}