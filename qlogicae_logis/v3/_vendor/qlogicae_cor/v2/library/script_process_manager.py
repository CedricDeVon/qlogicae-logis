from __future__ import annotations
_A=None
__all__='ScriptProcessManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from subprocess import CompletedProcess;from.script_process import ScriptProcess
_shlex=_A
_subprocess=_A
_SingletonManager=_A
_TextEncodingManager=_A
_ScriptProcess=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _shlex;global _subprocess;global _SingletonManager;global _TextEncodingManager;global _ScriptProcess;import shlex,subprocess as A;from.script_process import ScriptProcess as B;from.singleton_manager import SingletonManager as C;from.text_encoding_manager import TextEncodingManager as D;_shlex=shlex;_subprocess=A;_SingletonManager=C;_TextEncodingManager=D;_ScriptProcess=B;_handle_dynamic_imports=lambda:_A
class ScriptProcessManager:
	__slots__='_selected_script_process','_valid_script_processes','_text_encoding_manager'
	def __init__(A):B='shell';_handle_dynamic_imports();A._text_encoding_manager=_SingletonManager.get_singleton(_TextEncodingManager);A._selected_script_process=B;A._valid_script_processes={B,'subprocess'}
	@property
	def selected_script_process(self):return self._selected_script_process
	@selected_script_process.setter
	def selected_script_process(self,value):
		A=value
		if A not in self._valid_script_processes:return
		self._selected_script_process=A
	@property
	def valid_script_processes(self):return self._valid_script_processes
	def execute_command(F,command,script_process_type=_A):
		D=True;B=script_process_type;A=command
		if B is _A:B=_ScriptProcess.SUBPROCESS
		if not A:raise ValueError('commands cannot be empty')
		E=F._text_encoding_manager.selected_encoding;C:0
		match B:
			case _ScriptProcess.SHELL:C=_subprocess.run(A,encoding=E,text=D,shell=D)
			case _ScriptProcess.SUBPROCESS:C=_subprocess.run(_shlex.split(A),encoding=E,text=D)
			case _:raise ValueError('unsupported script process value')
		return C