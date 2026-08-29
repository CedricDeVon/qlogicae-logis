from __future__ import annotations
_H='timestamp_modified'
_G='public'
_F='private'
_E='project'
_D='all'
_C='arguments must not be null'
_B=None
_A='value'
from typing import Any
__all__='DatabaseManager'
_utility_data=_B
_ImportManager=_B
_utility_metadata=_B
def _handle_dynamic_imports():global _handle_dynamic_imports;global _utility_data;global _ImportManager;global _utility_metadata;from..library import import_manager as B;from..project.configuration import utility as A;_utility_data=A.DATA;_utility_metadata=A.METADATA;_ImportManager=B.ImportManager;_handle_dynamic_imports=lambda:_B
class DatabaseManager:
	__slots__='_import_manager',
	def __init__(A):_handle_dynamic_imports();A._import_manager=_ImportManager.read_singleton(_ImportManager)
	def read_default_static_value_cache_macros(A):return{'current-date','current-year','time-zone','operating-system-name','operating-system-architecture','current-timestamp','root-filesystem-path','selection-filesystem-path'}
	def read_default_dynamic_value_cache_macros(A):return{}
	def read_default_template_types(A):return'filesystem',
	def read_default_filesystem_accessibility_types(A):return _F,_G
	def read_default_data_file_extensions(A):return A.read_default_yaml_data_file_extensions()|A.read_default_json_data_file_extensions()|A.read_default_python_data_file_extensions()
	def read_default_yaml_data_file_extensions(A):return{'.yaml','.yml'}
	def read_default_json_data_file_extensions(A):return{'.json'}
	def read_default_python_data_file_extensions(A):return{'.py'}
	def read_default_plugin_file_extensions(A):return{'.py'}
	def read_default_groups(A):return{_D:_D}
	def read_default_selection_targets(C):B='group';A='root';return{A:A,B:B,_E:_E}
	def read_none(A):return'none'
	def read_not_a_number(A):return'nan'
	def read_redacted(A):return'redacted'
	def read_expunged(A):return'expunged'
	def read_company_project_major_version(A,delimeter):B=delimeter;return f"{A.read_company_name()}{B}{A.read_project_name()}{B}{A.read_active_major_version_label()}"
	def read_root_key_path(A):return f"{A.read_company_name()}",f"{A.read_project_name()}",f"{A.read_active_major_version_label()}"
	def read_debug_is_enabled(B):A=_utility_data.get('debug',{}).get('is-enabled',{}).get(_A,False);return A
	def read_company_name(B):A=_utility_data.get('company-name',{}).get(_A,'company');return A
	def read_project_name(B):A=_utility_data.get('project-name',{}).get(_A,_E);return A
	def read_company_project_name(A):B=f"{A.read_company_name()}-{A.read_project_name()}";return B
	def read_active_major_version_label(B):A=_utility_data.get('active-major-version-label',{}).get(_A,'v0');return A
	def read_root_workspace_filesystem_path(A):return f"{A._import_manager.read_original_executing_console_filesystem_path()}/.{A.read_company_project_major_version("/")}"
	def read_root_plugin_filesystem_path(A,scope_selection):return f"{A.read_root_workspace_filesystem_path()}/{scope_selection}/plugin"
	def read_default_log_output_filesystem_paths(A):return{f"{A.read_root_workspace_filesystem_path()}/private/temporary/log/{A._import_manager.read_current_iso8601_date()}.log"}
	def read_default_export_groups(B):A={_D};return{A:A for A in A}
	def read_object_filtered_export_included(F,targets,patterns):
		B=patterns;A=targets
		if not A or not B:return A
		C=set()
		for D in B:
			if not D:continue
			for E in A:
				if D in E:continue
				C.add(E)
		return C
	def read_default_disk_cache_output_file_path(A):B=A.read_root_workspace_filesystem_path();C=A._import_manager.read_current_iso8601_date();return f"{B}/private/temporary/cache/disk/{C}.db"
	def read_default_cache_disk_output_folder_path(A):B=A.read_root_workspace_filesystem_path();return f"{B}/private/temporary/cache/disk"
	def read_temporary_template_output_filesystem_path(A):B=A.read_root_workspace_filesystem_path();return f"{B}/private/temporary/template"
	def read_temporary_export_output_filesystem_path(A):B=A.read_root_workspace_filesystem_path();return f"{B}/private/temporary/export"
	def read_temporary_export_targets_source_filesystem_path(B,target):
		A=target
		if not A:raise ValueError(_C)
		C=B.read_root_workspace_filesystem_path();return f"{C}/private/temporary/export/targets/{A}"
	def read_temporary_export_targets_output_filesystem_path(C,target,relative_path):
		B=relative_path;A=target
		if not A or not B:raise ValueError(_C)
		D=C.read_root_workspace_filesystem_path();return f"{D}/private/temporary/export/targets/{A}/{B}"
	def read_configuration_workspace_filesystem_path(B,accessibility_type):
		A=accessibility_type
		if not A:raise ValueError(_C)
		C=B.read_root_workspace_filesystem_path();return f"{C}/{A}/configuration/workspace"
	def read_configuration_workspace_base_file_paths(C,accessibility_type):
		B=accessibility_type
		if not B:raise ValueError(_C)
		A=C.read_configuration_workspace_filesystem_path(B);return f"{A}/root",f"{A}/project/project",f"{A}/group/group"
	def read_configuration_workspace_base_folder_paths(C,accessibility_type):
		A=accessibility_type
		if not A:raise ValueError(_C)
		B=C.read_configuration_workspace_filesystem_path(A);return f"{B}/group/selection",f"{B}/project/selection"
	def read_file_metadata(B,filesystem_path):
		A=filesystem_path
		if not A:raise ValueError(_C)
		return{_H:{_A:B._import_manager.read_filesystem_modification_timestamp(value=A)}}
	def read_object_property_timestamp_modified_value(B,data):A=data.get(_H,{}).get(_A,_B);return A
	def read_object_selection_origins(A,data):
		if not data:raise ValueError(_C)
		return{A for(B,A)in data.items()}
	def read_plugin_data(D,module):C='macros';B='command';A=module;A={B:A.command if hasattr(A,B)else _B,C:A.macros if hasattr(A,C)else _B};return A
	def read_default_export_selections(B):A=B.read_company_project_major_version('-');C={f"{A}",f"{A}-public",f"{A}-private"};return{A:A for A in C}
	def read_default_export_selection_data(E):
		I='include';H='output';G='input';D='targets';A='filesystem-path';L=E._import_manager.read_original_executing_console_filesystem_path();B=f".{E.read_company_project_major_version("/")}";C=E.read_company_project_major_version('-');J={A:{_A:f"{B}/public"}};K=[{A:{_A:f"{B}/.gitignore"}},{A:{_A:f"{B}/private/.gitignore"}},{A:{_A:f"{B}/private/configuration"}},{A:{_A:f"{B}/private/plugin"}},{A:{_A:f"{B}/private/template"}}]
		def F(tag=''):
			B=tag
			if B:B=f"-{B}"
			return{D:[{A:{_A:f"{L}/{C}{B}"}}]}
		M={f"{C}":{G:{I:{D:[J,*K]}},H:F()},f"{C}-public":{G:{I:{D:[J]}},H:F(_G)},f"{C}-private":{G:{I:{D:[*K]}},H:F(_F)}};return M
	def read_configuration_workspace_data_file(A,file_path):
		B=file_path
		if not B:return{}
		C={};D=A._import_manager.read_file_suffix(value=B)
		if D in A.read_default_yaml_data_file_extensions():C=A._import_manager.read_yaml_file(file_path=B)or{}
		elif D in A.read_default_json_data_file_extensions():C=A._import_manager.read_json_file(file_path=B)or{}
		elif D in A.read_default_python_data_file_extensions():C=A._import_manager.read_python_file(file_path=B)or{}
		return C