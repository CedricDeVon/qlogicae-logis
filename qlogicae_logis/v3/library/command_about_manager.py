from __future__ import annotations
B=None
from typing import Any
from..library.decorator_manager import DecoratorManager as J
__all__='CommandAboutManager'
C=B
A=B
D=B
E=B
K=J
F=B
G=B
H=B
def I():global I;global C;global A;global D;global F;global E;global G;global H;from..library import command_storage_manager as J,database_manager as K,display_manager as L,import_manager as M,persistent_cache_database_manager as N,task_manager as O,value_cache_database_manager as P;C=O.TaskManager;D=L.DisplayManager;E=K.DatabaseManager;G=P.ValueCacheDatabaseManager;H=N.PersistentCacheDatabasManager;A=M.ImportManager;F=J.CommandStorageManager;I=lambda:B
class L:
	__slots__='_command_storage_manager','_task_manager','_import_manager','_display_manager','_database_manager','_value_cache_database_manager','_persistent_cache_database_manager'
	def __init__(B):I();B._command_storage_manager=A.read_singleton(F);B._display_manager=A.read_singleton(D);B._task_manager=A.read_singleton(C);B._import_manager=A.read_singleton(A);B._database_manager=A.read_singleton(E);B._value_cache_database_manager=A.read_singleton(G);B._persistent_cache_database_manager=A.read_singleton(H);B._command_storage_manager.add_commands(((B._command_storage_manager.read_command_name('about_version'),B.run_command_about_version),))
	@K.command_decorator
	def run_command_about_version(self,**E):
		D=False;A=self;B=A._database_manager.read_company_project_name()
		if not B:return D
		C=A._import_manager.read_metadata_version(B)
		if not C:return D
		A._display_manager.display_highlight_value(value=C);return True