from __future__ import annotations
M=tuple
E=True
D=None
A=False
from typing import Any
from..library.decorator_manager import DecoratorManager as N
__all__='CommandFilesystemManager'
F=D
B=D
G=D
H=D
C=N
I=D
J=D
K=D
def L():global L;global F;global B;global G;global I;global H;global J;global K;from..library import command_storage_manager as A,database_manager as C,display_manager as E,import_manager as M,persistent_cache_database_manager as N,task_manager as O,value_cache_database_manager as P;F=O.TaskManager;G=E.DisplayManager;H=C.DatabaseManager;J=P.ValueCacheDatabaseManager;K=N.PersistentCacheDatabasManager;B=M.ImportManager;I=A.CommandStorageManager;L=lambda:D
class O:
	__slots__='_command_storage_manager','_task_manager','_import_manager','_display_manager','_database_manager','_value_cache_database_manager','_persistent_cache_database_manager'
	def __init__(A):L();A._command_storage_manager=B.read_singleton(I);A._display_manager=B.read_singleton(G);A._task_manager=B.read_singleton(F);A._import_manager=B.read_singleton(B);A._database_manager=B.read_singleton(H);A._value_cache_database_manager=B.read_singleton(J);A._persistent_cache_database_manager=B.read_singleton(K);A._command_storage_manager.add_commands(((A._command_storage_manager.read_command_name('filesystem_copy'),A.run_command_filesystem_copy),(A._command_storage_manager.read_command_name('filesystem_move'),A.run_command_filesystem_move),(A._command_storage_manager.read_command_name('filesystem_rename'),A.run_command_filesystem_rename),(A._command_storage_manager.read_command_name('filesystem_tree_setup'),A.run_command_filesystem_tree_setup),(A._command_storage_manager.read_command_name('filesystem_clean_path'),A.run_command_filesystem_clean_path),(A._command_storage_manager.read_command_name('filesystem_clean_selection'),A.run_command_filesystem_clean_selection),(A._command_storage_manager.read_command_name('filesystem_clean_list_included'),A.run_command_filesystem_clean_list_included),(A._command_storage_manager.read_command_name('filesystem_clean_list_excluded'),A.run_command_filesystem_clean_list_excluded)))
	@C.command_decorator
	def run_command_filesystem_copy(self,**B):
		if not B:return A
		self._task_manager.run_task_common_setup();C=self._import_manager.copy_filesystem_paths(**B);return C
	@C.command_decorator
	def run_command_filesystem_move(self,**B):
		if not B:return A
		self._task_manager.run_task_common_setup();C=self._import_manager.move_filesystem_path(**B);return C
	@C.command_decorator
	def run_command_filesystem_rename(self,**B):
		if not B:return A
		self._task_manager.run_task_common_setup();C=self._import_manager.rename_filesystem_entity(**B);return C
	@C.command_decorator
	def run_command_filesystem_tree_setup(self,**B):
		if not B:return A
		self._task_manager.run_task_common_setup();C=self._import_manager.setup_filesystem_tree_paths(**B);return C
	@C.command_decorator
	def run_command_filesystem_clean_path(self,**D):
		B=self
		if not D:return A
		B._task_manager.run_task_common_setup();B._task_manager.run_task_filesystem_clean_exclude_setup();F=D.get('target_paths',M())
		if len(F)<1:return A
		G=B._value_cache_database_manager.read_filesystem_clean_excluded()or{}
		for C in F:
			if not C or C in G:continue
			B._import_manager.clean_filesystem_paths(target_paths=(C,))
		return E
	@C.command_decorator
	def run_command_filesystem_clean_selection(self,**F):
		I='targets';B=self
		if not F:return A
		B._task_manager.run_task_common_setup();B._task_manager.run_task_filesystem_clean_include_setup();B._task_manager.run_task_filesystem_clean_exclude_setup();J=F.get(I,M());K=B._value_cache_database_manager.read_configuration_workspace_data_command_filesystem_clean_include_selection()or{};G=B._value_cache_database_manager.read_filesystem_clean_included()or{};L=B._value_cache_database_manager.read_filesystem_clean_excluded()or{}
		for C in J:
			if not C or C not in G:continue
			H=K.get(G.get(C,''),'')
			if not H:continue
			N=B._value_cache_database_manager.read_object_filesystem_pattern_values(H.get(I,{}))
			for D in N:
				if not D or D in L:continue
				B._import_manager.clean_filesystem_paths(target_paths=(D,))
		return E
	@C.command_decorator
	def run_command_filesystem_clean_list_included(self,**F):
		B=self;B._task_manager.run_task_common_setup();B._task_manager.run_task_filesystem_clean_include_setup();C={};D=B._value_cache_database_manager.read_filesystem_clean_included()or{}
		if D:C['included']=D
		if not C:return A
		B._display_manager.display_tree_object(value=C);return E
	@C.command_decorator
	def run_command_filesystem_clean_list_excluded(self,**F):
		B=self;B._task_manager.run_task_common_setup();B._task_manager.run_task_filesystem_clean_exclude_setup();C={};D=B._value_cache_database_manager.read_filesystem_clean_excluded()or{}
		if D:C['excluded']=D
		if not C:return A
		B._display_manager.display_tree_object(value=C);return E