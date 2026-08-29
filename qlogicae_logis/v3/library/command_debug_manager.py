from __future__ import annotations
K=tuple
A=None
from typing import Any
from..library.decorator_manager import DecoratorManager as L
__all__='CommandDebugManager'
C=A
B=A
D=A
E=A
F=A
G=A
H=A
I=L
def J():global J;global C;global B;global D;global E;global F;global G;global H;from..library import command_storage_manager as I,database_manager as K,display_manager as L,import_manager as M,persistent_cache_database_manager as N,task_manager as O,value_cache_database_manager as P;C=O.TaskManager;B=M.ImportManager;E=K.DatabaseManager;D=L.DisplayManager;G=P.ValueCacheDatabaseManager;F=I.CommandStorageManager;H=N.PersistentCacheDatabasManager;J=lambda:A
class M:
	__slots__='_command_storage_manager','_task_manager','_import_manager','_database_manager','_decorator_manager','_value_cache_database_manager','_display_manager','_persistent_cache_database_manager'
	def __init__(A):J();A._command_storage_manager=B.read_singleton(F);A._decorator_manager=B.read_singleton(I);A._database_manager=B.read_singleton(E);A._task_manager=B.read_singleton(C);A._import_manager=B.read_singleton(B);A._value_cache_database_manager=B.read_singleton(G);A._display_manager=B.read_singleton(D);A._persistent_cache_database_manager=B.read_singleton(H);A._command_storage_manager.add_commands(((A._command_storage_manager.read_command_name('debug_view_value_cache'),A.run_command_debug_view_value_cache),(A._command_storage_manager.read_command_name('debug_view_disk_cache'),A.run_command_debug_view_disk_cache)))
	@I.command_decorator
	def run_command_debug_view_value_cache(self,**D):
		A=self;A._task_manager.run_task_full_debug_value_cache_setup();B=D.get('key_paths',[])
		if len(B)<1:A._display_manager.display_tree_object(value=A._value_cache_database_manager.read_any_value(K()))
		else:
			for C in B:
				if not C:continue
				A._display_manager.display_tree_object(value=A._value_cache_database_manager.read_any_value(K(C.split('.'))))
		return True
	@I.command_decorator
	def run_command_debug_view_disk_cache(self,**C):A=self;A._task_manager.run_task_full_debug_disk_cache_setup();B=A._persistent_cache_database_manager.read_all_values();A._display_manager.display_tree_object(value=B);return True