from __future__ import annotations
C=None
__all__='ScriptProcessEnumManager',
from typing import TYPE_CHECKING as E,Any
if E:from.enum_conversion_value import EnumConversionValue
B=C
A=C
def D():global D;global B;global A;from.enum_conversion_value import EnumConversionValue as E;from.script_process import ScriptProcess as F;B=E;A=F;D=lambda:C
class F:
	def __init__(A):D()
	def convert_value(F,input_type,output_type=C):
		E=input_type;D=output_type
		if D is C:D=B.STRING
		match D:
			case B.STRING:
				match E:
					case A.SHELL:return'shell'
					case A.SUBPROCESS:return'subprocess'
					case _:return'none'
			case B.ENUM:
				match str(E).lower():
					case'shell':return A.SHELL
					case'subprocess':return A.SUBPROCESS
					case _:return A.SUBPROCESS
			case _:return B.NONE