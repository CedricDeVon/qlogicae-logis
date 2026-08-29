from __future__ import annotations
G=ValueError
D=None
B=property
__all__='SystemManager',
from typing import TYPE_CHECKING as H,Any
if H:from pathlib import Path
E=D
C=D
A=D
def F():global F;global E;global C;global A;import os,pathlib as B,platform as G;E=os;C=G;A=B.Path;F=lambda:D
class I:
	__slots__='_original_executing_console_filesystem_path',
	def __init__(B):F();B._original_executing_console_filesystem_path=f"{A.cwd().resolve()}"
	@B
	def original_executing_console_filesystem_path(self):return self._original_executing_console_filesystem_path
	@B
	def current_executing_script_filesystem_path(self):return f"{A(__file__).resolve()}"
	@B
	def current_executing_console_filesystem_path(self):return f"{A.cwd().resolve()}"
	@current_executing_console_filesystem_path.setter
	def current_executing_console_filesystem_path(self,filesystem_path):
		B=A(filesystem_path).expanduser().resolve()
		if not B.exists():raise G(f"directory '{B}' does not exist")
		if not B.is_dir():raise G(f"'{B}' is not a directory")
		E.chdir(B)
	@B
	def operating_system_name(self):A=C.system();return A
	@B
	def operating_system_architecture(self):A=C.machine();return A