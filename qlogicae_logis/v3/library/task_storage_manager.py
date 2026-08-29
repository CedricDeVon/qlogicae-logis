from __future__ import annotations
D=True
C=False
from typing import Any
__all__='TaskStorageManager'
A=None
def B():global B;global A;from..library import import_manager as C;A=C.ImportManager;B=lambda:None
class E:
	__slots__='_tasks','_import_manager'
	def __init__(C):B();C._tasks={};C._import_manager=A.read_singleton(A)
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
		if not name:return C
		del A._tasks[name];return D
	def is_executed(A,label=''):B=f"{label}";E=A._tasks.get(B,C);A._tasks[B]=D;return E
	def reset_all_task_executed(A):
		for(B,E)in A._tasks.items():A._tasks[B]=C
		return D