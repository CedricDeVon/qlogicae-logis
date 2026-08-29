from __future__ import annotations
N='key_paths'
M=tuple
L=False
D=True
A=None
from typing import Any
from.decorator_manager import DecoratorManager as O
__all__='CommandDatabaseManager'
E=A
B=A
F=A
G=A
C=O
H=A
I=A
J=A
def K():global K;global E;global B;global F;global H;global G;global I;global J;from.import command_storage_manager as C,database_manager as D,display_manager as L,import_manager as M,persistent_cache_database_manager as N,task_manager as O,value_cache_database_manager as P;E=O.TaskManager;F=L.DisplayManager;G=D.DatabaseManager;I=P.ValueCacheDatabaseManager;J=N.PersistentCacheDatabasManager;B=M.ImportManager;H=C.CommandStorageManager;K=lambda:A
class P:
	__slots__='_command_storage_manager','_task_manager','_import_manager','_display_manager','_database_manager','_value_cache_database_manager','_persistent_cache_database_manager'
	def __init__(A):K();A._command_storage_manager=B.read_singleton(H);A._display_manager=B.read_singleton(F);A._task_manager=B.read_singleton(E);A._import_manager=B.read_singleton(B);A._database_manager=B.read_singleton(G);A._value_cache_database_manager=B.read_singleton(I);A._persistent_cache_database_manager=B.read_singleton(J);A._command_storage_manager.add_commands(((A._command_storage_manager.read_command_name('cache_view_disk'),A.run_command_database_view_disk),(A._command_storage_manager.read_command_name('cache_view_value'),A.run_command_database_view_value),(A._command_storage_manager.read_command_name('cache_clear_disk'),A.run_command_database_clear_disk),(A._command_storage_manager.read_command_name('cache_clear_value'),A.run_command_database_clear_value)))
	@C.command_decorator
	def run_command_database_view_disk(self,**C):
		A=self
		if not C:return L
		A._task_manager.run_task_full_debug_disk_cache_setup();E=C.get(N,[]);F=A._persistent_cache_database_manager.read_all_values()
		if len(E)<1:A._display_manager.display_tree_object(value=F)
		else:
			for G in E:
				if not G:continue
				for B in F:
					if not B:continue
					if B['key']==G:A._display_manager.display_tree_object(value=B)
		return D
	@C.command_decorator
	def run_command_database_view_value(self,**B):
		A=self
		if not B:return L
		C=B.get(N,[])
		if len(C)<1:A._display_manager.display_tree_object(value=A._value_cache_database_manager.read_any_value(M()))
		else:
			for E in C:
				if not E:continue
				A._display_manager.display_tree_object(value=A._value_cache_database_manager.read_any_value(M(E.split('.'))))
		return D
	@C.command_decorator
	def run_command_database_clear_disk(self,**C):
		A=self;A._task_manager.run_task_full_debug_disk_cache_setup();B=A._database_manager.read_default_cache_disk_output_folder_path()or''
		if not B:return L
		A._import_manager.clean_filesystem_paths(target_paths=(B,));return D
	@C.command_decorator
	def run_command_database_clear_value(self,**A):self._import_manager.clear_all_values_via_value_cache();return D