from __future__ import annotations
_A=False
from typing import Any
__all__='TaskStorageManager'
_ImportManager=None
def _handle_dynamic_imports():global _handle_dynamic_imports;global _ImportManager;from..library import import_manager as A;_ImportManager=A.ImportManager;_handle_dynamic_imports=lambda:None
class TaskStorageManager:
	__slots__='_tasks','_import_manager'
	def __init__(A):_handle_dynamic_imports();A._tasks={};A._import_manager=_ImportManager.read_singleton(_ImportManager)
	def read_tasks(A):return A._tasks
	def read_task(A,name):
		if not name:return{}
		return A._tasks[name]
	def write_task(B,name,value):
		A=value
		if not name or not A:return
		B._tasks[name]=A
	def write_tasks(B,value):
		A=value
		if not A:return
		B._tasks=A
	def remove_task(A,name):
		if not name:return _A
		del A._tasks[name];return True
	def is_executed(A,label=''):B=f"{label}";C=A._tasks.get(B,_A);A._tasks[B]=True;return C
	def reset_all_task_executed(A):
		for(B,C)in A._tasks.items():A._tasks[B]=_A
		return True