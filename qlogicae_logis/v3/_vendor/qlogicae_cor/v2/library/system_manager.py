from __future__ import annotations
_A=None
__all__='SystemManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from pathlib import Path
_os=_A
_platform=_A
_path=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _os;global _platform;global _path;import os,pathlib as A,platform as B;_os=os;_platform=B;_path=A.Path;_handle_dynamic_imports=lambda:_A
class SystemManager:
	__slots__='_original_executing_console_filesystem_path',
	def __init__(A):_handle_dynamic_imports();A._original_executing_console_filesystem_path=f"{_path.cwd().resolve()}"
	@property
	def original_executing_console_filesystem_path(self):return self._original_executing_console_filesystem_path
	@property
	def current_executing_script_filesystem_path(self):return f"{_path(__file__).resolve()}"
	@property
	def current_executing_console_filesystem_path(self):return f"{_path.cwd().resolve()}"
	@current_executing_console_filesystem_path.setter
	def current_executing_console_filesystem_path(self,filesystem_path):
		A=_path(filesystem_path).expanduser().resolve()
		if not A.exists():raise ValueError(f"directory '{A}' does not exist")
		if not A.is_dir():raise ValueError(f"'{A}' is not a directory")
		_os.chdir(A)
	@property
	def operating_system_name(self):A=_platform.system();return A
	@property
	def operating_system_architecture(self):A=_platform.machine();return A