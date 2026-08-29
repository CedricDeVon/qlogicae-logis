from __future__ import annotations
_A=None
__all__='TimeUnitEnumManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from.enum_conversion_value import EnumConversionValue
_EnumConversionValue=_A
_TimeUnit=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _EnumConversionValue;global _TimeUnit;from.enum_conversion_value import EnumConversionValue as A;from.time_unit import TimeUnit as B;_EnumConversionValue=A;_TimeUnit=B;_handle_dynamic_imports=lambda:_A
class TimeUnitEnumManager:
	def __init__(A):_handle_dynamic_imports()
	def convert_value(C,input_type,output_type=_A):
		B=input_type;A=output_type
		if A is _A:A=_EnumConversionValue.STRING
		match A:
			case _EnumConversionValue.STRING:
				match B:
					case _TimeUnit.NANOSECOND:return'nanosecond'
					case _TimeUnit.MICROSECOND:return'microsecond'
					case _TimeUnit.MILLISECOND:return'millisecond'
					case _TimeUnit.SECOND:return'second'
					case _TimeUnit.MINUTE:return'minute'
					case _TimeUnit.HOUR:return'hour'
					case _TimeUnit.DAY:return'day'
					case _TimeUnit.WEEK:return'week'
					case _TimeUnit.MONTH:return'month'
					case _TimeUnit.YEAR:return'year'
					case _TimeUnit.DECADE:return'decade'
					case _TimeUnit.CENTURY:return'century'
					case _TimeUnit.MILLENNIUM:return'millennium'
					case _:return'none'
			case _EnumConversionValue.ENUM:
				match str(B).lower():
					case'nanosecond'|'ns':return _TimeUnit.NANOSECOND
					case'microsecond'|'us':return _TimeUnit.MICROSECOND
					case'millisecond'|'ms':return _TimeUnit.MILLISECOND
					case'second'|'sec':return _TimeUnit.SECOND
					case'minute'|'min':return _TimeUnit.MINUTE
					case'hour'|'hr':return _TimeUnit.HOUR
					case'day'|'d':return _TimeUnit.DAY
					case'week'|'wk':return _TimeUnit.WEEK
					case'month'|'mon':return _TimeUnit.MONTH
					case'year'|'yr':return _TimeUnit.YEAR
					case'decade'|'deca':return _TimeUnit.DECADE
					case'century'|'cen':return _TimeUnit.CENTURY
					case'millennium'|'mil':return _TimeUnit.MILLENNIUM
					case _:return _TimeUnit.NONE
			case _:return _EnumConversionValue.NONE