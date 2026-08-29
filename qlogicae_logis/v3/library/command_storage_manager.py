from __future__ import annotations
B=True
A=False
from typing import Any
__all__='CommandStorageManager'
def C():global C;C=lambda:None
class D:
	__slots__='_commands'
	def __init__(A):C();A._commands={}
	def read_command_name(B,value):
		A=value
		if not A:return''
		return f"command-{A.replace("_","-")}"
	def read_commands(A):return A._commands
	def write_commands(B,value):
		A=value
		if not A:return
		B._commands=A
	def add_command(D,name,callback):
		C=callback
		if not name or not C:return A
		D._commands[name]=C;return B
	def add_commands(F,items):
		C=items
		if not C:return A
		for(D,E)in C:
			if not D or not E:continue
			F._commands[D]=E
		return B
	def run_command(C,name):
		if not name:return A
		C._commands[name]();return B
	def read_command(B,name):
		if not name:return A
		return B._commands[name]
	def write_command(B,name,value):
		A=value
		if not name or not A:return
		B._commands[name]=A
	def remove_command(C,name):
		if not name:return A
		del C._commands[name];return B