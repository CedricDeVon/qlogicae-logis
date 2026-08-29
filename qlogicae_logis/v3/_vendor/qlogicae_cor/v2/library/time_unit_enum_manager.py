from __future__ import annotations
C=None
__all__='TimeUnitEnumManager',
from typing import TYPE_CHECKING as E,Any
if E:from.enum_conversion_value import EnumConversionValue
B=C
A=C
def D():global D;global B;global A;from.enum_conversion_value import EnumConversionValue as E;from.time_unit import TimeUnit as F;B=E;A=F;D=lambda:C
class F:
	def __init__(A):D()
	def convert_value(F,input_type,output_type=C):
		E=input_type;D=output_type
		if D is C:D=B.STRING
		match D:
			case B.STRING:
				match E:
					case A.NANOSECOND:return'nanosecond'
					case A.MICROSECOND:return'microsecond'
					case A.MILLISECOND:return'millisecond'
					case A.SECOND:return'second'
					case A.MINUTE:return'minute'
					case A.HOUR:return'hour'
					case A.DAY:return'day'
					case A.WEEK:return'week'
					case A.MONTH:return'month'
					case A.YEAR:return'year'
					case A.DECADE:return'decade'
					case A.CENTURY:return'century'
					case A.MILLENNIUM:return'millennium'
					case _:return'none'
			case B.ENUM:
				match str(E).lower():
					case'nanosecond'|'ns':return A.NANOSECOND
					case'microsecond'|'us':return A.MICROSECOND
					case'millisecond'|'ms':return A.MILLISECOND
					case'second'|'sec':return A.SECOND
					case'minute'|'min':return A.MINUTE
					case'hour'|'hr':return A.HOUR
					case'day'|'d':return A.DAY
					case'week'|'wk':return A.WEEK
					case'month'|'mon':return A.MONTH
					case'year'|'yr':return A.YEAR
					case'decade'|'deca':return A.DECADE
					case'century'|'cen':return A.CENTURY
					case'millennium'|'mil':return A.MILLENNIUM
					case _:return A.NONE
			case _:return B.NONE