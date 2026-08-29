from __future__ import annotations
_A=None
__all__='ScriptProcessEnumManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from.enum_conversion_value import EnumConversionValue
_EnumConversionValue=_A
_ScriptProcess=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _EnumConversionValue;global _ScriptProcess;from.enum_conversion_value import EnumConversionValue as A;from.script_process import ScriptProcess as B;_EnumConversionValue=A;_ScriptProcess=B;_handle_dynamic_imports=lambda:_A
class ScriptProcessEnumManager:
	def __init__(A):_handle_dynamic_imports()
	def convert_value(C,input_type,output_type=_A):
		B=input_type;A=output_type
		if A is _A:A=_EnumConversionValue.STRING
		match A:
			case _EnumConversionValue.STRING:
				match B:
					case _ScriptProcess.SHELL:return'shell'
					case _ScriptProcess.SUBPROCESS:return'subprocess'
					case _:return'none'
			case _EnumConversionValue.ENUM:
				match str(B).lower():
					case'shell':return _ScriptProcess.SHELL
					case'subprocess':return _ScriptProcess.SUBPROCESS
					case _:return _ScriptProcess.SUBPROCESS
			case _:return _EnumConversionValue.NONE