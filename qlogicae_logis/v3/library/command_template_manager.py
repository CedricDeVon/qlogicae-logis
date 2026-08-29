from __future__ import annotations
E='all'
G=True
F=False
A=None
from typing import Any
from..library.decorator_manager import DecoratorManager as N
__all__='CommandTemplateManager'
C=A
B=A
D=A
H=A
M=N
I=A
J=A
K=A
def L():global L;global C;global B;global D;global H;global I;global J;global K;from..library import command_storage_manager as E,database_manager as F,display_manager as G,import_manager as M,persistent_cache_database_manager as N,task_manager as O,value_cache_database_manager as P;C=O.TaskManager;D=G.DisplayManager;H=F.DatabaseManager;J=P.ValueCacheDatabaseManager;K=N.PersistentCacheDatabasManager;B=M.ImportManager;I=E.CommandStorageManager;L=lambda:A
class O:
	__slots__='_command_storage_manager','_task_manager','_import_manager','_display_manager','_database_manager','_value_cache_database_manager','_persistent_cache_database_manager'
	def __init__(A):L();A._command_storage_manager=B.read_singleton(I);A._display_manager=B.read_singleton(D);A._task_manager=B.read_singleton(C);A._import_manager=B.read_singleton(B);A._database_manager=B.read_singleton(H);A._value_cache_database_manager=B.read_singleton(J);A._persistent_cache_database_manager=B.read_singleton(K);A._command_storage_manager.add_commands(((A._command_storage_manager.read_command_name('template_apply'),A.run_command_template_apply),(A._command_storage_manager.read_command_name('template_list_selections'),A.run_command_template_list_selections)))
	@M.command_decorator
	def run_command_template_apply(self,**K):
		T='root';S='targets';A=self
		if not K:return F
		def M():
			B=f"{D}/root/filesystem"
			for E in Q:
				if not E:continue
				F=f"{C}/{E}/template/all/filesystem";H=f"{C}/{E}/template/root/filesystem";A._import_manager.setup_filesystem_tree_paths(target_paths=(F,H,B));A._import_manager.copy_filesystem_path(source_path=F,target_path=B);A._import_manager.copy_filesystem_path(source_path=H,target_path=B)
			A._import_manager.macros_parse_filesystem(filesystem_path=B,workspace_macros=P);A._import_manager.copy_filesystem_path(source_path=B,target_path=V);return G
		def L():
			for A in I:
				if not A:continue
				N(A)
			return G
		def R():
			for A in H:
				if not A:continue
				O(A)
			return G
		def N(group_target):
			K=group_target
			if not K:return F
			R=X.get(K,{})
			if not R:return F
			Y=set(R.get(S,{}));B=f"{D}/group/selection/{K}/filesystem"
			for L in Q:
				if not L:continue
				U=f"{C}/{L}/template/all/filesystem";V=f"{C}/{L}/template/group/filesystem";W=f"{C}/{L}/template/group/selection/{K}/filesystem";A._import_manager.setup_filesystem_tree_paths(target_paths=(U,V,W,B));A._import_manager.copy_filesystem_path(source_path=U,target_path=B);A._import_manager.copy_filesystem_path(source_path=V,target_path=B);A._import_manager.copy_filesystem_path(source_path=W,target_path=B)
			A._import_manager.macros_parse_filesystem(filesystem_path=B,workspace_macros=P)
			for E in Y:
				if not E:continue
				if E==T:J=f"{D}/root/filesystem";A._import_manager.copy_filesystem_path(source_path=B,target_path=J);M()
				elif E in H:J=f"{D}/project/selection/{E}/filesystem";A._import_manager.copy_filesystem_path(source_path=B,target_path=J);O(E)
				elif E in I:J=f"{D}/group/selection/{E}/filesystem";A._import_manager.copy_filesystem_path(source_path=B,target_path=J);N(E)
			return G
		def O(project_target):
			E=project_target
			if not E:return F
			I=U.get(E,{})
			if not I:return F
			J=I.get('filesystem-path',{}).get('value','')
			if not J:return F
			B=f"{D}/project/selection/{E}/filesystem"
			for H in Q:
				if not H:continue
				K=f"{C}/{H}/template/all/filesystem";L=f"{C}/{H}/template/project/filesystem";M=f"{C}/{H}/template/project/selection/{E}/filesystem";A._import_manager.setup_filesystem_tree_paths(target_paths=(K,L,M,B));A._import_manager.copy_filesystem_path(source_path=K,target_path=B);A._import_manager.copy_filesystem_path(source_path=L,target_path=B);A._import_manager.copy_filesystem_path(source_path=M,target_path=B)
			A._import_manager.macros_parse_filesystem(filesystem_path=B,workspace_macros=P);A._import_manager.copy_filesystem_path(source_path=B,target_path=J);return G
		A._task_manager.run_task_common_setup();A._task_manager.run_task_workspace_default_setup();A._task_manager.run_task_workspace_group_setup();A._task_manager.run_task_workspace_project_setup();A._task_manager.run_task_filesystem_clean_exclude_setup();A._task_manager.run_task_filesystem_clean_include_setup();J=K.get(S,[E])
		if not J or len(J)<1:J=[E]
		P=A._value_cache_database_manager.read_macros();Q=A._database_manager.read_default_filesystem_accessibility_types();U=A._value_cache_database_manager.read_configuration_workspace_data_workspace_project_selection();H=A._value_cache_database_manager.read_workspace_project();H=A._database_manager.read_object_selection_origins(H);X=A._value_cache_database_manager.read_configuration_workspace_data_workspace_group_selection();I=A._value_cache_database_manager.read_workspace_group();I=A._database_manager.read_object_selection_origins(I);V=A._value_cache_database_manager.read_root_filesystem_path();C=A._database_manager.read_root_workspace_filesystem_path();D=A._database_manager.read_temporary_template_output_filesystem_path();W=A._value_cache_database_manager.read_con_wor_data_template_cleanup_before_is_enabled_value();Y=A._value_cache_database_manager.read_con_wor_data_template_cleanup_after_is_enabled_value()
		if W:A._task_manager.run_task_safe_clean_filesystem_path(target_path=D)
		for B in J:
			if not B:continue
			if B==E:M();L();R()
			elif B==T:M()
			elif B=='group':L()
			elif B=='project':R()
			elif B in I:N(B)
			elif B in H:O(B)
		if Y:A._task_manager.run_task_safe_clean_filesystem_path(target_path=D)
		return G
	@M.command_decorator
	def run_command_template_list_selections(self,**J):
		A=self;A._task_manager.run_task_common_setup();A._task_manager.run_task_workspace_default_setup();A._task_manager.run_task_workspace_group_setup();A._task_manager.run_task_workspace_project_setup();B={};C=A._value_cache_database_manager.read_workspace_default()or{}
		if C:B['defaults']=C
		D=A._value_cache_database_manager.read_workspace_project()or{}
		if D:B['projects']=D
		H=A._value_cache_database_manager.read_workspace_group()or{}
		if H:B['groups']=H
		I=A._value_cache_database_manager.read_workspace_all()or{}
		if I:B[E]=I
		if not B:return F
		A._display_manager.display_tree_object(value=B);return G