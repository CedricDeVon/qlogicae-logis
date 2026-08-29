from __future__ import annotations
AV='included'
AU='excluded'
AT='dynamic'
AS='outputis-enabled'
AR='architecture'
AQ='vertical-count'
AP='is-skipped'
AO='indent-count'
AN='maximum-depth'
AM='highlight-2'
AL='highlight-1'
AK='base-2'
AJ='base-1'
AI='import'
AH='value-cache'
AG='is-modified'
AF='current-executing-console-filesystem-path'
AE='previous-executing-console-filesystem-path'
AD='initial-executing-console-filesystem-path'
AC='current-executing-script-filesystem-path'
AB='selection-filesystem-path'
AA='root-filesystem-path'
A9='current-year'
A8='current-date'
A7='current-timestamp'
A6='memory'
A5='duration'
A4='complete'
A2='reset'
A1='operating-system-architecture'
A0='operating-system-name'
z='time-zone'
y='configuration'
v='alias'
u='private'
t='public'
s='cache'
r='workflow'
q='template'
p='project'
o='default'
n='override'
m='count'
l='compression'
k='filesystem-path'
j='include'
i='exclude'
g='after'
f='before'
e='static'
d=False
c=None
b=set
a='group'
Z='clean'
Y='filesystem'
X='is-verbose'
W='timestamp'
V='raw'
U=str
T='file'
S='macros'
R='cleanup'
Q='export'
P='data'
O='selection'
N='plugin'
M=''
L='workspace'
K='command'
J='operating-system'
I='targets'
H=bool
G='log'
F='style'
E='display'
D='is-enabled'
C='console'
B=True
A='value'
from typing import Any
__all__='ValueCacheDatabaseManager'
A3=c
h=c
w=c
AW=c
def x():global x;global A3;global h;global w;global AW;from..library import database_manager as A,import_manager as B,task_manager as C;A3=C.TaskManager;h=B.ImportManager;w=A.DatabaseManager;x=lambda:c
class AX:
	__slots__='_import_manager','_database_manager'
	def __init__(A):x();A._import_manager=h.read_singleton(h);A._database_manager=h.read_singleton(w)
	def read_default_clean_included(B):A={};return A
	def read_default_clean_excluded(A):B=A._import_manager.read_filesystem_entity_parents(target_path=A.read_root_filesystem_path());return B
	def read_key_path(A,key_path):return*A._database_manager.read_root_key_path(),*key_path
	def read_debug_snapshot_key_path(A,key_path):return*A._database_manager.read_root_key_path(),'debug','snapshot',*key_path
	def read_debug_snapshot_value(A,key_path):B=A._import_manager.read_any_value_via_value_cache(key_path=A.read_debug_snapshot_key_path(key_path))or{};return B
	def write_debug_snapshot_value(A,key_path,value):B=A._import_manager.write_any_value_via_value_cache(key_path=A.read_debug_snapshot_key_path(key_path),value=value);return B
	def read_configuration_workspace_data_key_path(A,key_path):return*A._database_manager.read_root_key_path(),y,L,P,*key_path
	def read_configuration_workspace_data_value(A,key_path):B=A._import_manager.read_any_value_via_value_cache(key_path=A.read_configuration_workspace_data_key_path(key_path))or{};return B
	def write_configuration_workspace_data_value(A,key_path,value):B=A._import_manager.write_any_value_via_value_cache(key_path=A.read_configuration_workspace_data_key_path(key_path),value=value);return B
	def read_configuration_workspace_raw_key_path(A,key_path):return*A._database_manager.read_root_key_path(),y,L,V,*key_path
	def read_configuration_workspace_raw_value(A,key_path):B=A._import_manager.read_any_value_via_value_cache(key_path=A.read_configuration_workspace_raw_key_path(key_path))or{};return B
	def write_configuration_workspace_raw_value(A,key_path,value):B=A._import_manager.write_any_value_via_value_cache(key_path=A.read_configuration_workspace_raw_key_path(key_path),value=value);return B
	def read_any_value(A,key_path):B=A._import_manager.read_any_value_via_value_cache(key_path=A.read_key_path(key_path))or{};return B
	def write_any_value(A,key_path,value):B=A._import_manager.write_any_value_via_value_cache(key_path=A.read_key_path(key_path),value=value);return B
	def remove_any_value(A,key_path):B=A._import_manager.remove_one_value_via_value_cache(key_path=A.read_key_path(key_path));return B
	def read_debug_snapshot_execution(A,label=M):
		if not A._database_manager.read_debug_is_enabled():return{}
		B=A.read_debug_snapshot_value((f"{label}",W));return B
	def write_debug_snapshot_execution(A,label=M,data=c):
		if not A._database_manager.read_debug_is_enabled():return B
		A.write_debug_snapshot_value((f"{label}",W),data or{});return B
	def read_debug_snapshot_execution_timestamp_start(B,label=M):
		if not B._database_manager.read_debug_is_enabled():return 0
		C=B.read_debug_snapshot_value((f"{label}",W,'start',A));return C
	def write_debug_snapshot_execution_timestamp_start(C,label=M):
		if not C._database_manager.read_debug_is_enabled():return B
		C.write_debug_snapshot_value((f"{label}",W,'start',A),C._import_manager.read_current_nanosecond());return B
	def read_debug_snapshot_execution_timestamp_complete(B,label=M):
		if not B._database_manager.read_debug_is_enabled():return 0
		C=B.read_debug_snapshot_value((f"{label}",W,A4,A));return C
	def write_debug_snapshot_execution_timestamp_complete(C,label=M):
		D=label
		if not C._database_manager.read_debug_is_enabled():return B
		C.write_debug_snapshot_value((f"{D}",W,A4,A),C._import_manager.read_current_nanosecond());C.write_debug_snapshot_execution_timestamp_duration(label=D);return B
	def read_debug_snapshot_execution_timestamp_duration(B,label=M):
		if not B._database_manager.read_debug_is_enabled():return .0
		C=B.read_debug_snapshot_value((f"{label}",W,A5,A));return C
	def write_debug_snapshot_execution_timestamp_duration(C,label=M):
		D=label
		if not C._database_manager.read_debug_is_enabled():return B
		E=(C.read_debug_snapshot_execution_timestamp_complete(label=D)-C.read_debug_snapshot_execution_timestamp_start(label=D))/1000000;C.write_debug_snapshot_value((f"{D}",W,A5,A),E);return B
	def read_debug_snapshot_execution_memory(A,label=M):
		if not A._database_manager.read_debug_is_enabled():return{}
		B=A.read_debug_snapshot_value((f"{label}",A6));return B
	def write_debug_snapshot_execution_memory(A,label=M):
		if not A._database_manager.read_debug_is_enabled():return B
		C=A._import_manager.snapshot_memory_usage();A.write_debug_snapshot_value((f"{label}",A6),C);return B
	def read_current_timestamp(B):C=B.read_any_value((A7,A))or 0;return C
	def write_current_timestamp(C):C.write_any_value((A7,A),C._import_manager.read_current_nanosecond());return B
	def read_time_zone_name(B):C=B.read_any_value((z,A))or M;return C
	def write_time_zone_name(C,value):C.write_any_value((z,A),value);return B
	def write_default_time_zone_name(C):C.write_any_value((z,A),'local');return B
	def read_operating_system_name(B):C=B.read_any_value((A0,A))or B._import_manager.read_operating_system_name();return C
	def write_operating_system_name(C,value):C.write_any_value((A0,A),value);return B
	def write_default_operating_system_name(C):C.write_any_value((A0,A),C._import_manager.read_operating_system_name());return B
	def read_operating_system_architecture(B):C=B.read_any_value((A1,A))or B._import_manager.read_operating_system_architecture();return C
	def write_operating_system_architecture(C,value):C.write_any_value((A1,A),value);return B
	def write_default_operating_system_architecture(C):C.write_any_value((A1,A),C._import_manager.read_operating_system_architecture());return B
	def read_current_date(B):C=B.read_any_value((A8,A))or'1970';return C
	def write_current_date(C):C.write_any_value((A8,A),C._import_manager.read_current_iso8601_date());return B
	def read_current_year(B):C=B.read_any_value((A9,A))or 0;return C
	def write_current_year(C):C.write_any_value((A9,A),C._import_manager.read_current_year());return B
	def read_root_filesystem_path(B):C=B.read_any_value((AA,A));return C
	def write_root_filesystem_path(C):C.write_any_value((AA,A),C._import_manager.read_original_executing_console_filesystem_path());return B
	def read_selection_filesystem_path(B):C=B.read_any_value((AB,A));return C
	def write_selection_filesystem_path(C):C.write_any_value((AB,A),f"{C._import_manager.read_original_executing_console_filesystem_path()}/selection");return B
	def read_current_executing_script_filesystem_path(B):C=B.read_any_value((AC,A));return C
	def write_current_executing_script_filesystem_path(C,value):C.write_any_value((AC,A),value);return B
	def read_initial_executing_console_filesystem_path(B):C=B.read_any_value((AD,A));return C
	def write_initial_executing_console_filesystem_path(C,value):C.write_any_value((AD,A),value);return B
	def read_previous_executing_console_filesystem_path(B):C=B.read_any_value((AE,A));return C
	def write_previous_executing_console_filesystem_path(C,value):C.write_any_value((AE,A),value);return B
	def read_original_executing_console_filesystem_path(B):C=B.read_any_value((AF,A));return C
	def write_current_executing_console_filesystem_path(C,value):C.write_any_value((AF,A),value);return B
	def read_configuration_workspace(A,accessibility_type):B=A.read_configuration_workspace_raw_value((accessibility_type,))or{};return B
	def write_configuration_workspace(A,accessibility_type,value):A.write_configuration_workspace_raw_value((accessibility_type,),value);return B
	def remove_configuration_workspace(A):A.remove_any_value((y,L,V));return B
	def read_configuration_workspace_data(B,accessibility_type,key_path):C=B.read_configuration_workspace_raw_value((accessibility_type,key_path,P,A))or{};return C
	def write_configuration_workspace_rdata(C,accessibility_type,key_path,value):C.write_configuration_workspace_raw_value((accessibility_type,key_path,P,A),value);return B
	def read_is_configuration_workspace_modified(B):C=B.read_configuration_workspace_raw_value((AG,A));return C
	def write_is_configuration_workspace_modified(C,value):C.write_configuration_workspace_raw_value((AG,A),value);return B
	def read_configuration_workspace_file_count(B,accessibility_type):C=B.read_configuration_workspace_raw_value((m,accessibility_type,A));return C
	def write_configuration_workspace_file_count(C,accessibility_type,value):C.write_configuration_workspace_raw_value((m,accessibility_type,A),value);return B
	def read_merged_configuration_workspace_data(A):B=A.read_configuration_workspace_data_value(())or{};return B
	def write_merged_configuration_workspace_data(A,value):A.write_configuration_workspace_data_value((),value);return B
	def read_configuration_workspace_data_macros_static_value_cache_targets(A):B=A.read_configuration_workspace_data_value((S,e,AH,I))or{};return B
	def write_configuration_workspace_data_macros_static_value_cache_targets(A,value):A.write_configuration_workspace_data_value((S,e,AH,I),value);return B
	def read_configuration_workspace_data_macros_static_file_targets(A):B=A.read_configuration_workspace_data_value((S,e,T,I))or{};return B
	def write_configuration_workspace_data_macros_static_file_targets(A,value):A.write_configuration_workspace_data_value((S,e,T,I),value);return B
	def read_configuration_workspace_data_plugin_import_is_enabled_value(C):E=C.read_configuration_workspace_data_value((N,AI,D))or{};return H(E.get(A,B))
	def write_configuration_workspace_data_plugin_import_is_enabled_value(C,value):C.write_configuration_workspace_data_value((N,AI,D,A),value);return B
	def read_configuration_workspace_data_display_console_is_enabled_value(F):G=F.read_configuration_workspace_data_value((E,C,D))or{};return H(G.get(A,B))
	def write_configuration_workspace_data_display_console_is_enabled_value(F,value):F.write_configuration_workspace_data_value((E,C,D,A),value);return B
	def read_configuration_workspace_data_display_console_style(A):B=A.read_configuration_workspace_data_value((E,C,F));return B
	def write_configuration_workspace_data_display_console_style(A,value):A.write_configuration_workspace_data_value((E,C,F),value);return B
	def read_configuration_workspace_data_display_console_style_reset_value(B):D=B.read_configuration_workspace_data_value((E,C,F,A2))or{};return U(D.get(A,A2))
	def write_configuration_workspace_data_display_console_style_reset_value(D,value):D.write_configuration_workspace_data_value((E,C,F,A2,A),value);return B
	def read_configuration_workspace_data_display_console_style_base_1_value(B):D=B.read_configuration_workspace_data_value((E,C,F,AJ))or{};return U(D.get(A,M))
	def write_configuration_workspace_data_display_console_style_base_1_value(D,value):D.write_configuration_workspace_data_value((E,C,F,AJ,A),value);return B
	def read_configuration_workspace_data_display_console_style_base_2_value(B):D=B.read_configuration_workspace_data_value((E,C,F,AK))or{};return U(D.get(A,'grey'))
	def write_configuration_workspace_data_display_console_style_base_2_value(D,value):D.write_configuration_workspace_data_value((E,C,F,AK,A),value);return B
	def read_configuration_workspace_data_display_console_style_highlight_1_value(B):D=B.read_configuration_workspace_data_value((E,C,F,AL))or{};return U(D.get(A,'green'))
	def write_configuration_workspace_data_display_console_style_highlight_1_value(D,value):D.write_configuration_workspace_data_value((E,C,F,AL,A),value);return B
	def read_configuration_workspace_data_display_console_style_highlight_2_value(B):D=B.read_configuration_workspace_data_value((E,C,F,AM))or{};return U(D.get(A,'green'))
	def write_configuration_workspace_data_display_console_style_highlight_2_value(D,value):D.write_configuration_workspace_data_value((E,C,F,AM,A),value);return B
	def read_configuration_workspace_data_display_console_style_maximum_depth_value(B):D=B.read_configuration_workspace_data_value((E,C,F,AN))or{};return D.get(A,c)
	def write_configuration_workspace_data_display_console_style_maximum_depth_value(D,value):D.write_configuration_workspace_data_value((E,C,F,AN,A),value);return B
	def read_configuration_workspace_data_display_console_style_indent_count_value(B):D=B.read_configuration_workspace_data_value((E,C,F,AO))or{};return int(D.get(A,4))
	def write_configuration_workspace_data_display_console_style_indent_count_value(D,value):D.write_configuration_workspace_data_value((E,C,F,AO,A),value);return B
	def read_configuration_workspace_data_display_console_style_is_skipped_value(D):G=D.read_configuration_workspace_data_value((E,C,F,AP))or{};return H(G.get(A,B))
	def write_configuration_workspace_data_display_console_style_is_skipped_value(D,value):D.write_configuration_workspace_data_value((E,C,F,AP,A),value);return B
	def read_configuration_workspace_data_display_console_style_vertical_count_value(B):D=B.read_configuration_workspace_data_value((E,C,F,AQ))or{};return int(D.get(A,0))
	def write_configuration_workspace_data_display_console_style_vertical_count_value(D,value):D.write_configuration_workspace_data_value((E,C,F,AQ,A),value);return B
	def read_configuration_workspace_data_time_zone_value(B):C=B.read_configuration_workspace_data_value(('time','zone'))or{};return U(C.get(A,'local'))
	def write_configuration_workspace_data_time_zone_value(C,value):C.write_configuration_workspace_data_value(('time','zone',A),value);return B
	def read_configuration_workspace_data_operating_system_name_value(B):C=B.read_configuration_workspace_data_value((J,'name'))or{};return U(C.get(A,B._import_manager.read_operating_system_name()))
	def write_configuration_workspace_data_operating_system_name_value(C,value):C.write_configuration_workspace_data_value((J,'name',A),value);return B
	def read_configuration_workspace_data_operating_system_value(B):C=B.read_configuration_workspace_data_value((J,))or{};return U(C.get(A,f"{B._import_manager.read_operating_system_name()}-{B._import_manager.read_operating_system_architecture()}"))
	def write_configuration_workspace_data_operating_system_value(C,value):C.write_configuration_workspace_data_value((J,A),value);return B
	def read_configuration_workspace_data_operating_system_architecture_value(B):C=B.read_configuration_workspace_data_value((J,AR))or{};return U(C.get(A,B._import_manager.read_operating_system_architecture()))
	def write_configuration_workspace_data_operating_system_architecture_value(C,value):C.write_configuration_workspace_data_value((J,AR,A),value);return B
	def read_configuration_workspace_data_log_is_enabled_value(C):E=C.read_configuration_workspace_data_value((G,D))or{};return H(E.get(A,B))
	def write_configuration_workspace_data_log_is_enabled_value(C,value):C.write_configuration_workspace_data_value((G,D,A),value);return B
	def read_configuration_workspace_data_log_is_enabled_override(A):B=A.read_configuration_workspace_data_value((G,D))or{};return H(B.get(n,d))
	def write_configuration_workspace_data_log_is_enabled_override(A,value):A.write_configuration_workspace_data_value((G,D,n),value);return B
	def read_configuration_workspace_data_log_is_verbose_value(C):D=C.read_configuration_workspace_data_value((G,X))or{};return H(D.get(A,B))
	def write_configuration_workspace_data_log_is_verbose_value(C,value):C.write_configuration_workspace_data_value((G,X,A),value);return B
	def read_configuration_workspace_data_log_is_verbose_override(A):B=A.read_configuration_workspace_data_value((G,X))or{};return H(B.get(n,d))
	def write_configuration_workspace_data_log_is_verbose_override(A,value):A.write_configuration_workspace_data_value((G,X,n),value);return B
	def read_configuration_workspace_data_log_file_is_enabled_value(C):E=C.read_configuration_workspace_data_value((G,T,D))or{};return H(E.get(A,B))
	def write_configuration_workspace_data_log_file_is_enabled_value(C,value):C.write_configuration_workspace_data_value((G,T,D,A),value);return B
	def read_configuration_workspace_data_log_file_is_verbose_value(C):D=C.read_configuration_workspace_data_value((G,T,X))or{};return H(D.get(A,B))
	def write_configuration_workspace_data_log_file_is_verbose_value(C,value):C.write_configuration_workspace_data_value((G,T,X,A),value);return B
	def read_configuration_workspace_data_log_file_targets(A):B=A.read_configuration_workspace_data_value((G,T))or{};return B.get(I,{})
	def write_configuration_workspace_data_log_file_targets(A,value):A.write_configuration_workspace_data_value((G,T,I),value);return B
	def read_configuration_workspace_data_log_console_is_enabled_value(E):F=E.read_configuration_workspace_data_value((G,C,D))or{};return H(F.get(A,B))
	def write_configuration_workspace_data_log_console_is_enabled_value(E,value):E.write_configuration_workspace_data_value((G,C,D,A),value);return B
	def read_configuration_workspace_data_log_console_is_verbose_value(B):D=B.read_configuration_workspace_data_value((G,C,X))or{};return H(D.get(A,d))
	def write_configuration_workspace_data_log_console_is_verbose_value(D,value):D.write_configuration_workspace_data_value((G,C,X,A),value);return B
	def read_configuration_workspace_data_log_default_file_output_is_enabled_value(C):D=C.read_configuration_workspace_data_value((G,o,T,AS))or{};return H(D.get(A,B))
	def write_configuration_workspace_data_log_default_file_output_is_enabled_value(C,value):C.write_configuration_workspace_data_value((G,o,T,AS,A),value);return B
	def read_configuration_workspace_data_command_filesystem_clean_exclude_targets(A):B=A.read_configuration_workspace_data_value((K,Y,Z,i))or{};return tuple(B.get(I,tuple()))
	def write_configuration_workspace_data_command_filesystem_clean_exclude_targets(A,value):A.write_configuration_workspace_data_value((K,Y,Z,i,I),value);return B
	def read_configuration_workspace_data_command_filesystem_clean_include_selection(A):B=A.read_configuration_workspace_data_value((K,Y,Z,j))or{};return B.get(O,{})
	def write_configuration_workspace_data_command_filesystem_clean_include_selection(A,value):A.write_configuration_workspace_data_value((K,Y,Z,j,O),value);return B
	def read_configuration_workspace_data_workspace_project_selection(A):B=A.read_configuration_workspace_data_value((L,p))or{};return B.get(O,{})
	def write_configuration_workspace_data_workspace_project_selection(A,value):A.write_configuration_workspace_data_value((L,p,O),value);return B
	def read_configuration_workspace_data_workspace_group_selection(A):B=A.read_configuration_workspace_data_value((L,a))or{};return B.get(O,{})
	def write_configuration_workspace_data_workspace_group_selection(A,value):A.write_configuration_workspace_data_value((L,a,O),value);return B
	def read_configuration_workspace_data_export_group(A):B=A.read_configuration_workspace_data_value((K,Q))or{};return B.get(a,{})
	def write_configuration_export_data_export_group(A,value):A.write_configuration_workspace_data_value((K,Q,a),value);return B
	def read_configuration_workspace_data_export_selection(A):B=A.read_configuration_workspace_data_value((K,Q))or{};return B.get(O,{})
	def write_configuration_workspace_data_export_selection(A,value):A.write_configuration_workspace_data_value((K,Q,O),value);return B
	def read_con_wor_data_export_cleanup_before_is_enabled_value(C):E=C.read_configuration_workspace_data_value((K,Q,R,f,D))or{};return H(E.get(A,B))
	def write_con_wor_data_export_cleanup_before_is_enabled_value(C,value):C.write_configuration_workspace_data_value((K,Q,R,f,D,A),value);return B
	def read_con_wor_data_export_cleanup_after_is_enabled_value(C):E=C.read_configuration_workspace_data_value((K,Q,R,g,D))or{};return H(E.get(A,B))
	def write_con_wor_data_export_cleanup_after_is_enabled_value(C,value):C.write_configuration_workspace_data_value((K,Q,R,g,D,A),value);return B
	def read_con_wor_data_template_cleanup_before_is_enabled_value(C):E=C.read_configuration_workspace_data_value((K,q,R,f,D))or{};return H(E.get(A,B))
	def write_con_wor_data_template_cleanup_before_is_enabled_value(C,value):C.write_configuration_workspace_data_value((K,q,R,f,D,A),value);return B
	def read_con_wor_data_template_cleanup_after_is_enabled_value(C):E=C.read_configuration_workspace_data_value((K,q,R,g,D))or{};return H(E.get(A,B))
	def write_con_wor_data_template_cleanup_after_is_enabled_value(C,value):C.write_configuration_workspace_data_value((K,q,R,g,D,A),value);return B
	def read_configuration_workspace_data_workflow_selection(A):B=A.read_configuration_workspace_data_value((r,))or{};return B.get(O,{})
	def write_configuration_workspace_data_workflow_selection(A,value):A.write_configuration_workspace_data_value((r,O),value);return B
	def read_con_wor_data_cache_cleanup_before_is_enabled_value(B):C=B.read_configuration_workspace_data_value((s,R,f,D))or{};return H(C.get(A,d))
	def write_con_wor_data_cache_cleanup_before_is_enabled_value(C,value):C.write_configuration_workspace_data_value((s,R,f,D,A),value);return B
	def read_con_wor_data_cache_cleanup_after_is_enabled_value(B):C=B.read_configuration_workspace_data_value((s,R,g,D))or{};return H(C.get(A,d))
	def write_con_wor_data_cache_cleanup_after_is_enabled_value(C,value):C.write_configuration_workspace_data_value((s,R,g,D,A),value);return B
	def read_macros(A):B=A.read_any_value((S,))or{};return B
	def write_macros(A,value):A.write_any_value((S,),value);return B
	def read_public_configuration_workspace(A):B=A.read_configuration_workspace(t)or{};return B
	def write_public_configuration_workspace(A,value):A.write_configuration_workspace(t,value);return B
	def read_private_configuration_workspace(A):B=A.read_configuration_workspace(u)or{};return B
	def write_private_configuration_workspace(A,value):A.write_configuration_workspace(u,value);return B
	def read_plugin_raw(A,accessibility_type):B=A.read_any_value((N,V,accessibility_type))or{};return B
	def write_plugin_raw(A,accessibility_type,value):A.write_any_value((N,V,accessibility_type),value);return B
	def remove_plugin_raw(A):A.remove_any_value((N,V));return B
	def read_plugin_raw_data(B,accessibility_type,key_path):C=B.read_any_value((N,V,accessibility_type,key_path,P,A))or{};return C
	def write_plugin_raw_data(C,accessibility_type,key_path,value):C.write_any_value((N,V,accessibility_type,key_path,P,A),value);return B
	def read_plugin_public_raw(A):B=A.read_plugin_raw(t)or{};return B
	def write_plugin_public_raw(A,value):A.write_plugin_raw(t,value);return B
	def read_plugin_private_raw(A):B=A.read_plugin_raw(u)or{};return B
	def write_plugin_private_raw(A,value):A.write_plugin_raw(u,value);return B
	def read_plugin_raw_file_count(B,accessibility_type):C=B.read_any_value((N,V,m,accessibility_type,A));return C
	def write_plugin_raw_file_count(C,accessibility_type,value):C.write_any_value((N,V,m,accessibility_type,A),value);return B
	def read_plugin_data_macros_static_targets(A):B=A.read_any_value((N,P,S,e,I))or{};return B
	def write_plugin_data_macros_static_targets(A,value):A.write_any_value((N,P,S,e,I),value);return B
	def read_plugin_data_macros_dynamic_targets(A):B=A.read_any_value((N,P,S,AT,I))or{};return B
	def write_plugin_data_macros_dynamic_targets(A,value):A.write_any_value((N,P,S,AT,I),value);return B
	def read_plugin_data(A):B=A.read_any_value((N,P))or{};return B
	def write_plugin_data(A,value):A.write_any_value((N,P),value);return B
	def read_default_object_macros_values(D,data):
		B={}
		if not data:return B
		for C in data:B[C]={A:D.read_any_value((C,A))}
		return B
	def read_filesystem_clean_excluded(A):B=A.read_any_value((Y,Z))or{};return b(B.get(AU,b()))
	def write_filesystem_clean_excluded(A,value):A.write_any_value((Y,Z,AU),value);return B
	def read_filesystem_clean_included(A):B=A.read_any_value((Y,Z))or{};return B.get(AV,{})
	def write_filesystem_clean_included(A,value):A.write_any_value((Y,Z,AV),value);return B
	def read_workspace_group(A):B=A.read_any_value((L,))or{};return B.get(a,{})
	def write_workspace_group(A,value):A.write_any_value((L,a),value);return B
	def read_workspace_project(A):B=A.read_any_value((L,))or{};return B.get(p,{})
	def write_workspace_project(A,value):A.write_any_value((L,p),value);return B
	def read_workspace_default(A):B=A.read_any_value((L,))or{};return B.get(o,{})
	def write_workspace_default(A,value):A.write_any_value((L,o),value);return B
	def read_workspace_all(A):B=A.read_any_value((L,))or{};return B.get('all',{})
	def write_workspace_all(A,value):A.write_any_value((L,'all'),value);return B
	def read_export_selection(A):B=A.read_any_value((Q,))or{};return B.get(O,{})
	def write_export_selection(A,value):A.write_any_value((Q,O),value);return B
	def read_export_group(A):B=A.read_any_value((Q,))or{};return B.get(a,{})
	def write_export_group(A,value):A.write_any_value((Q,a),value);return B
	def read_workflow_selection(A):B=A.read_any_value((r,))or{};return B.get(O,{})
	def write_workflow_selection(A,value):A.write_any_value((r,O),value);return B
	def read_object_macros(B,data):
		A={}
		if not data:return A
		A=B.read_object_macros_values(data);return A
	def read_object_filesystem_values(D,data):
		C=b()
		if not data:return C
		for B in data:
			if not B or k not in B:continue
			if B and J in B and not D.read_is_object_operating_system_included(B[J]):continue
			B=B[k]
			if not B or A not in B:continue
			B=B[A];C.add(B)
		return C
	def read_object_macros_values(D,data):
		C={}
		if not data:return C
		for(E,B)in data.items():
			if not B or A not in B:continue
			if B and J in B and not D.read_is_object_operating_system_included(B[J]):continue
			C[E]=B[A]
			if B and v in B:
				F=D.read_object_alias_item_values(B[v])
				for G in F:C[G]=B[A]
		return C
	def read_object_selections(D,data):
		B={}
		if not data:return B
		for(C,A)in data.items():
			if A and J in A and not D.read_is_object_operating_system_included(A[J]):continue
			B[C]=C
			if A and v in A:
				E=D.read_object_alias_item_values(A[v])
				for F in E:B[F]=C
		return B
	def read_object_filesystem_pattern_values(D,data):
		C=b()
		if not data:return C
		for B in data:
			if not B or k not in B:continue
			if B and J in B and not D.read_is_object_operating_system_included(B[J]):continue
			E=B[k]
			if A not in E:continue
			F=E[A];G=D.read_object_pattern_value(B)
			if G:
				H=D._import_manager.read_filesystem_via_pattern(filesystem_path=F,pattern=G)
				for I in H:C.add(f"{I}")
			C.add(F)
		return C
	def read_object_pattern_values(C,data):
		B=b()
		if not data:return B
		for A in data:
			if A and J in A and not C.read_is_object_operating_system_included(A[J]):continue
			D=C.read_object_pattern_value(A)
			if not D:continue
			B.add(D)
		return B
	def read_object_exclude_filesystem_path_values(A,data):return A.read_object_filesystem_pattern_values(data)
	def read_object_include_filesystem_path_values(C,data):
		A={}
		if not data:return A
		for(D,B)in data.items():
			if I not in B:continue
			A[D]=C.read_object_filesystem_pattern_values(B[I])
		return A
	def read_object_command_filesystem_clean_included(A,data):B=A.read_object_selections(data);return B
	def read_object_alias_item_values(C,data):
		A=b()
		for(B,D)in data.items():A.add(B)
		return A
	def read_object_system_is_include(C,data):
		A=b()
		for(B,D)in data.items():A.add(B)
		return A
	def read_object_pattern_value(C,data):B=data.get('pattern',{}).get(A,M);return B
	def read_object_selection(B,data):A=data.get(O,{});return A
	def read_object_output_targets(B,data):A=data.get('output',{}).get(I,[]);return A
	def read_object_input_exclude_targets(B,data):A=data.get('input',{}).get(i,{}).get(I,[]);return A
	def read_object_input_include_targets(B,data):A=data.get('input',{}).get(j,{}).get(I,[]);return A
	def read_object_is_enabled_value(E,data):C=data.get(D,{}).get(A,B);return C
	def read_object_filesystem_path_value(C,data):B=data.get(k,{}).get(A,M);return B
	def read_object_argument(B,data):A=data.get('argument',{});return A
	def read_object_process_value(C,data):B=data.get('process',{}).get(A,'shell');return B
	def read_object_run_value(C,data):B=data.get('run',{}).get(A,M);return B
	def read_object_delay_value(C,data):B=data.get('delay',{}).get(A,0);return B
	def read_object_scripts(B,data):A=data.get('scripts',[]);return A
	def read_object_compression_format_value(C,data):B=data.get(l,{}).get('format',{}).get(A,'zip');return B
	def read_object_compression_type_value(C,data):B=data.get(l,{}).get('type',{}).get(A,'deflated');return B
	def read_object_compression_level_value(C,data):B=data.get(l,{}).get('level',{}).get(A,6);return B
	def read_object_compression_is_zip_64_allowed_value(D,data):C=data.get(l,{}).get('is-zip-64-allowed',{}).get(A,B);return C
	def read_object_compression_is_timestamp_strict_value(D,data):C=data.get(l,{}).get('is-timestamp-strict',{}).get(A,B);return C
	def read_is_object_operating_system_included(C,data):
		A=data
		if not A or j not in A and i not in A:return B
		E=C.read_operating_system_name();F=C.read_operating_system_architecture();D=f"{E}-{F}";G=A.get(j,{});H=A.get(i,{})
		if D in H:return d
		if D in G:return B
		return d
	def read_file_data(A,data,metadata):return{P:data,'metadata':metadata}or{}