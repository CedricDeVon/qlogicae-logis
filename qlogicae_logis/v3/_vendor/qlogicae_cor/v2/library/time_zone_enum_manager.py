from __future__ import annotations
_A=None
__all__='TimeZoneEnumManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from.enum_conversion_value import EnumConversionValue
_datetime=_A
_UTC=_A
_EnumConversionValue=_A
_TimeZone=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _datetime;global _UTC;global _EnumConversionValue;global _TimeZone;from datetime import UTC,datetime as A;from.enum_conversion_value import EnumConversionValue as B;from.time_zone import TimeZone as C;_datetime=A;_UTC=UTC;_EnumConversionValue=B;_TimeZone=C;_handle_dynamic_imports=lambda:_A
class TimeZoneEnumManager:
	def __init__(A):_handle_dynamic_imports()
	def convert_value(D,input_type,output_type=_A):
		C='local';B=output_type;A=input_type
		if B is _A:B=_EnumConversionValue.STRING
		match B:
			case _EnumConversionValue.STRING:
				match A:
					case _TimeZone.LOCAL:return C
					case _TimeZone.UTC:return'utc'
					case _TimeZone.CUSTOM:return'custom'
					case _:return C
			case _EnumConversionValue.ENUM:
				match str(A).lower():
					case'local':return _TimeZone.LOCAL
					case'utc':return _TimeZone.UTC
					case'custom':return _TimeZone.CUSTOM
					case _:return _TimeZone.LOCAL
			case _EnumConversionValue.CUSTOM:
				match str(A).lower():
					case'local':return _datetime.now().astimezone().tzinfo
					case'utc':return _UTC
					case'custom':return _datetime.now().astimezone().tzinfo
					case _:return _datetime.now().astimezone().tzinfo
			case _:return _EnumConversionValue.NONE