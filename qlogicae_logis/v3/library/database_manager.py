from __future__ import annotations
O='timestamp_modified'
N='.py'
M='public'
L='private'
K=hasattr
I='project'
H='all'
D='arguments must not be null'
C=None
B=ValueError
A='value'
from typing import Any
__all__='DatabaseManager'
E=C
F=C
J=C
def G():global G;global E;global F;global J;from..library import import_manager as B;from..project.configuration import utility as A;E=A.DATA;J=A.METADATA;F=B.ImportManager;G=lambda:C
class P:
	__slots__='_import_manager',
	def __init__(A):G();A._import_manager=F.read_singleton(F)
	def read_default_static_value_cache_macros(A):return{'current-date','current-year','time-zone','operating-system-name','operating-system-architecture','current-timestamp','root-filesystem-path','selection-filesystem-path'}
	def read_default_dynamic_value_cache_macros(A):return{}
	def read_default_template_types(A):return'filesystem',
	def read_default_filesystem_accessibility_types(A):return L,M
	def read_default_data_file_extensions(A):return A.read_default_yaml_data_file_extensions()|A.read_default_json_data_file_extensions()|A.read_default_python_data_file_extensions()
	def read_default_yaml_data_file_extensions(A):return{'.yaml','.yml'}
	def read_default_json_data_file_extensions(A):return{'.json'}
	def read_default_python_data_file_extensions(A):return{N}
	def read_default_plugin_file_extensions(A):return{N}
	def read_default_groups(A):return{H:H}
	def read_default_selection_targets(C):B='group';A='root';return{A:A,B:B,I:I}
	def read_none(A):return'none'
	def read_not_a_number(A):return'nan'
	def read_redacted(A):return'redacted'
	def read_expunged(A):return'expunged'
	def read_company_project_major_version(A,delimeter):B=delimeter;return f"{A.read_company_name()}{B}{A.read_project_name()}{B}{A.read_active_major_version_label()}"
	def read_root_key_path(A):return f"{A.read_company_name()}",f"{A.read_project_name()}",f"{A.read_active_major_version_label()}"
	def read_debug_is_enabled(C):B=E.get('debug',{}).get('is-enabled',{}).get(A,False);return B
	def read_company_name(C):B=E.get('company-name',{}).get(A,'company');return B
	def read_project_name(C):B=E.get('project-name',{}).get(A,I);return B
	def read_company_project_name(A):B=f"{A.read_company_name()}-{A.read_project_name()}";return B
	def read_active_major_version_label(C):B=E.get('active-major-version-label',{}).get(A,'v0');return B
	def read_root_workspace_filesystem_path(A):return f"{A._import_manager.read_original_executing_console_filesystem_path()}/.{A.read_company_project_major_version("/")}"
	def read_root_plugin_filesystem_path(A,scope_selection):return f"{A.read_root_workspace_filesystem_path()}/{scope_selection}/plugin"
	def read_default_log_output_filesystem_paths(A):return{f"{A.read_root_workspace_filesystem_path()}/private/temporary/log/{A._import_manager.read_current_iso8601_date()}.log"}
	def read_default_export_groups(B):A={H};return{A:A for A in A}
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
	def read_temporary_export_targets_source_filesystem_path(C,target):
		A=target
		if not A:raise B(D)
		E=C.read_root_workspace_filesystem_path();return f"{E}/private/temporary/export/targets/{A}"
	def read_temporary_export_targets_output_filesystem_path(E,target,relative_path):
		C=relative_path;A=target
		if not A or not C:raise B(D)
		F=E.read_root_workspace_filesystem_path();return f"{F}/private/temporary/export/targets/{A}/{C}"
	def read_configuration_workspace_filesystem_path(C,accessibility_type):
		A=accessibility_type
		if not A:raise B(D)
		E=C.read_root_workspace_filesystem_path();return f"{E}/{A}/configuration/workspace"
	def read_configuration_workspace_base_file_paths(E,accessibility_type):
		C=accessibility_type
		if not C:raise B(D)
		A=E.read_configuration_workspace_filesystem_path(C);return f"{A}/root",f"{A}/project/project",f"{A}/group/group"
	def read_configuration_workspace_base_folder_paths(E,accessibility_type):
		A=accessibility_type
		if not A:raise B(D)
		C=E.read_configuration_workspace_filesystem_path(A);return f"{C}/group/selection",f"{C}/project/selection"
	def read_file_metadata(E,filesystem_path):
		C=filesystem_path
		if not C:raise B(D)
		return{O:{A:E._import_manager.read_filesystem_modification_timestamp(value=C)}}
	def read_object_property_timestamp_modified_value(D,data):B=data.get(O,{}).get(A,C);return B
	def read_object_selection_origins(A,data):
		if not data:raise B(D)
		return{A for(B,A)in data.items()}
	def read_plugin_data(E,module):D='macros';B='command';A=module;A={B:A.command if K(A,B)else C,D:A.macros if K(A,D)else C};return A
	def read_default_export_selections(B):A=B.read_company_project_major_version('-');C={f"{A}",f"{A}-public",f"{A}-private"};return{A:A for A in C}
	def read_default_export_selection_data(F):
		J='include';I='output';H='input';E='targets';B='filesystem-path';O=F._import_manager.read_original_executing_console_filesystem_path();C=f".{F.read_company_project_major_version("/")}";D=F.read_company_project_major_version('-');K={B:{A:f"{C}/public"}};N=[{B:{A:f"{C}/.gitignore"}},{B:{A:f"{C}/private/.gitignore"}},{B:{A:f"{C}/private/configuration"}},{B:{A:f"{C}/private/plugin"}},{B:{A:f"{C}/private/template"}}]
		def G(tag=''):
			C=tag
			if C:C=f"-{C}"
			return{E:[{B:{A:f"{O}/{D}{C}"}}]}
		P={f"{D}":{H:{J:{E:[K,*N]}},I:G()},f"{D}-public":{H:{J:{E:[K]}},I:G(M)},f"{D}-private":{H:{J:{E:[*N]}},I:G(L)}};return P
	def read_configuration_workspace_data_file(A,file_path):
		B=file_path
		if not B:return{}
		C={};D=A._import_manager.read_file_suffix(value=B)
		if D in A.read_default_yaml_data_file_extensions():C=A._import_manager.read_yaml_file(file_path=B)or{}
		elif D in A.read_default_json_data_file_extensions():C=A._import_manager.read_json_file(file_path=B)or{}
		elif D in A.read_default_python_data_file_extensions():C=A._import_manager.read_python_file(file_path=B)or{}
		return C