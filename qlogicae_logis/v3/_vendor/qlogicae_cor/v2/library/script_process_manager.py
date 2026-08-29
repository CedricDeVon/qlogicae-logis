from __future__ import annotations
I=ValueError
H=property
A=None
__all__='ScriptProcessManager',
from typing import TYPE_CHECKING as J,Any
if J:from subprocess import CompletedProcess;from.script_process import ScriptProcess
D=A
C=A
E=A
F=A
B=A
def G():global G;global D;global C;global E;global F;global B;import shlex,subprocess as H;from.script_process import ScriptProcess as I;from.singleton_manager import SingletonManager as J;from.text_encoding_manager import TextEncodingManager as K;D=shlex;C=H;E=J;F=K;B=I;G=lambda:A
class K:
	__slots__='_selected_script_process','_valid_script_processes','_text_encoding_manager'
	def __init__(A):B='shell';G();A._text_encoding_manager=E.get_singleton(F);A._selected_script_process=B;A._valid_script_processes={B,'subprocess'}
	@H
	def selected_script_process(self):return self._selected_script_process
	@selected_script_process.setter
	def selected_script_process(self,value):
		A=value
		if A not in self._valid_script_processes:return
		self._selected_script_process=A
	@H
	def valid_script_processes(self):return self._valid_script_processes
	def execute_command(K,command,script_process_type=A):
		H=True;F=script_process_type;E=command
		if F is A:F=B.SUBPROCESS
		if not E:raise I('commands cannot be empty')
		J=K._text_encoding_manager.selected_encoding;G:0
		match F:
			case B.SHELL:G=C.run(E,encoding=J,text=H,shell=H)
			case B.SUBPROCESS:G=C.run(D.split(E),encoding=J,text=H)
			case _:raise I('unsupported script process value')
		return G