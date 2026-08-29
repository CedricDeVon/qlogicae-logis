from __future__ import annotations
B=None
__all__='EnumConversionValueEnumManager',
from typing import TYPE_CHECKING as D,Any
if D:from.enum_conversion_value import EnumConversionValue as E
A=B
def C():global C;global A;from.enum_conversion_value import EnumConversionValue as D;A=D;C=lambda:B
class F:
	def __init__(A):C()
	def convert_value(F,input_type,output_type=B):
		D=input_type;C=output_type
		if C is B:C=E.STRING
		match C:
			case A.STRING:
				match D:
					case A.STRING:return'string'
					case A.ENUM:return'enum'
					case A.CUSTOM:return'custom'
					case _:return'none'
			case A.ENUM:
				match str(D).lower():
					case'string':return A.STRING
					case'none':return A.ENUM
					case'custom':return A.CUSTOM
					case _:return A.NONE
			case _:return A.NONE