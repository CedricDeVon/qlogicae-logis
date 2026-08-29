from __future__ import annotations
_A=None
__all__='EnumConversionValueEnumManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from.enum_conversion_value import EnumConversionValue
_enum_conversion_value=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _enum_conversion_value;from.enum_conversion_value import EnumConversionValue as A;_enum_conversion_value=A;_handle_dynamic_imports=lambda:_A
class EnumConversionValueEnumManager:
	def __init__(A):_handle_dynamic_imports()
	def convert_value(C,input_type,output_type=_A):
		B=input_type;A=output_type
		if A is _A:A=EnumConversionValue.STRING
		match A:
			case _enum_conversion_value.STRING:
				match B:
					case _enum_conversion_value.STRING:return'string'
					case _enum_conversion_value.ENUM:return'enum'
					case _enum_conversion_value.CUSTOM:return'custom'
					case _:return'none'
			case _enum_conversion_value.ENUM:
				match str(B).lower():
					case'string':return _enum_conversion_value.STRING
					case'none':return _enum_conversion_value.ENUM
					case'custom':return _enum_conversion_value.CUSTOM
					case _:return _enum_conversion_value.NONE
			case _:return _enum_conversion_value.NONE