from __future__ import annotations
_B=True
_A=False
from typing import Any
__all__='CommandStorageManager'
def _handle_dynamic_imports():global _handle_dynamic_imports;_handle_dynamic_imports=lambda:None
class CommandStorageManager:
	__slots__='_commands'
	def __init__(A):_handle_dynamic_imports();A._commands={}
	def read_command_name(B,value):
		A=value
		if not A:return''
		return f"command-{A.replace("_","-")}"
	def read_commands(A):return A._commands
	def write_commands(B,value):
		A=value
		if not A:return
		B._commands=A
	def add_command(B,name,callback):
		A=callback
		if not name or not A:return _A
		B._commands[name]=A;return _B
	def add_commands(D,items):
		A=items
		if not A:return _A
		for(B,C)in A:
			if not B or not C:continue
			D._commands[B]=C
		return _B
	def run_command(A,name):
		if not name:return _A
		A._commands[name]();return _B
	def read_command(A,name):
		if not name:return _A
		return A._commands[name]
	def write_command(B,name,value):
		A=value
		if not name or not A:return
		B._commands[name]=A
	def remove_command(A,name):
		if not name:return _A
		del A._commands[name];return _B