from __future__ import annotations
H=True
G=None
B=staticmethod
from collections.abc import Callable
from functools import wraps as D
from typing import Any,ParamSpec as J,TypeVar as K
L=J('P')
M=K('R')
__all__='DecoratorManager'
A=G
E=G
I=G
F=G
def C():global C;global A;global E;global I;global F;from..library import database_manager as B,import_manager as D,task_storage_manager as H,value_cache_database_manager as J;I=H.TaskStorageManager;E=B.DatabaseManager;F=J.ValueCacheDatabaseManager;A=D.ImportManager;C=lambda:G
class N:
	__slots__=()
	@B
	def single_use_method_decorator(callback):
		B=callback;C()
		@D(B)
		def E(self,*C,**D):
			E=A.read_singleton(I)
			if E.is_executed(label=B):return H
			F=B(self,*C,**D);return F
		return E
	@B
	def debug_method_decorator(callback):
		B=callback;C()
		@D(B)
		def G(self,*D,**G):
			I=A.read_singleton(A);J=A.read_singleton(E);C=A.read_singleton(F)
			if J.read_debug_is_enabled():C.write_debug_snapshot_execution_timestamp_start(label=B);H=B(self,*D,**G);C.write_debug_snapshot_execution_timestamp_complete(label=B);K=f"{B} - {C.read_debug_snapshot_execution(label=B)}";I.log_cache_debug_to_file(message=K)
			else:H=B(self,*D,**G)
			return H
		return G
	@B
	def log_method_decorator(callback):
		B=callback;C()
		@D(B)
		def E(self,*E,**F):
			C=A.read_singleton(A);C.log_cache_info_to_file(message=f"{B} - start");D=B(self,*E,**F)
			if not D:C.log_cache_info_to_file(message=f"{B} - skip");return D
			C.log_cache_info_to_file(message=f"{B} - complete");return D
		return E
	@B
	def single_task_decorator(callback):
		B=callback;C()
		@D(B)
		def G(self,*J,**K):
			L=A.read_singleton(I);D=A.read_singleton(A);M=A.read_singleton(E);G=A.read_singleton(F)
			if L.is_executed(label=B):return H
			D.log_cache_info_to_file(message=f"{B} - start");C=H
			if M.read_debug_is_enabled():G.write_debug_snapshot_execution_timestamp_start(label=B);C=B(self,*J,**K);G.write_debug_snapshot_execution_timestamp_complete(label=B);N=f"{B} - {G.read_debug_snapshot_execution(label=B)}";D.log_cache_debug_to_file(message=N)
			else:C=B(self,*J,**K)
			if not C:D.log_cache_info_to_file(message=f"{B} - skip");return C
			D.log_cache_info_to_file(message=f"{B} - complete");return C
		return G
	@B
	def multi_task_decorator(callback):
		B=callback;C()
		@D(B)
		def G(self,*I,**J):
			D=A.read_singleton(A);K=A.read_singleton(E);G=A.read_singleton(F);D.log_cache_info_to_file(message=f"{B} - start");C=H
			if K.read_debug_is_enabled():G.write_debug_snapshot_execution_timestamp_start(label=B);C=B(self,*I,**J);G.write_debug_snapshot_execution_timestamp_complete(label=B);L=f"{B} - {G.read_debug_snapshot_execution(label=B)}";D.log_cache_debug_to_file(message=L)
			else:C=B(self,*I,**J)
			if not C:D.log_cache_info_to_file(message=f"{B} - skip");return C
			D.log_cache_info_to_file(message=f"{B} - complete");return C
		return G
	@B
	def command_decorator(callback):
		B=callback;C()
		@D(B)
		def G(self,*I,**J):
			D=A.read_singleton(A);K=A.read_singleton(E);G=A.read_singleton(F);D.log_cache_info_to_file(message=f"{B} - start");C=H
			if K.read_debug_is_enabled():G.write_debug_snapshot_execution_timestamp_start(label=B);C=B(self,*I,**J);G.write_debug_snapshot_execution_timestamp_complete(label=B);L=f"{B} - {G.read_debug_snapshot_execution(label=B)}";D.log_cache_debug_to_file(message=L)
			else:C=B(self,*I,**J)
			if not C:D.log_cache_info_to_file(message=f"{B} - skip");return C
			D.log_cache_info_to_file(message=f"{B} - complete");return C
		return G