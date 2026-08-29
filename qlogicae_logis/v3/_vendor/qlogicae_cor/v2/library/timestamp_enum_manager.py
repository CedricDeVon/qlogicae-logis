from __future__ import annotations
_A=None
__all__='TimestampEnumManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from.enum_conversion_value import EnumConversionValue
_EnumConversionValue=_A
_Timestamp=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _EnumConversionValue;global _Timestamp;from.enum_conversion_value import EnumConversionValue as A;from.timestamp import Timestamp as B;_EnumConversionValue=A;_Timestamp=B;_handle_dynamic_imports=lambda:_A
class TimestampEnumManager:
	def __init__(A):_handle_dynamic_imports()
	def convert_value(D,input_type,output_type=_A):
		C='iso_date_string';B=input_type;A=output_type
		if A is _A:A=_EnumConversionValue.STRING
		match A:
			case _EnumConversionValue.STRING:
				match B:
					case _Timestamp.ISO_DATE_STRING:return C
					case _Timestamp.ISO_FILESYSTEM_STRING:return'iso_filesystem_string'
					case _:return C
			case _EnumConversionValue.ENUM:
				match B.lower():
					case'local':return _Timestamp.ISO_DATE_STRING
					case'iso_filesystem_string':return _Timestamp.ISO_FILESYSTEM_STRING
					case _:return _Timestamp.NONE
			case _:return _EnumConversionValue.NONE