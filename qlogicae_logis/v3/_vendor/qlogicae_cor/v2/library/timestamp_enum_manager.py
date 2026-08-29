from __future__ import annotations
C=None
__all__='TimestampEnumManager',
from typing import TYPE_CHECKING as E,Any
if E:from.enum_conversion_value import EnumConversionValue
B=C
A=C
def D():global D;global B;global A;from.enum_conversion_value import EnumConversionValue as E;from.timestamp import Timestamp as F;B=E;A=F;D=lambda:C
class F:
	def __init__(A):D()
	def convert_value(G,input_type,output_type=C):
		F='iso_date_string';E=input_type;D=output_type
		if D is C:D=B.STRING
		match D:
			case B.STRING:
				match E:
					case A.ISO_DATE_STRING:return F
					case A.ISO_FILESYSTEM_STRING:return'iso_filesystem_string'
					case _:return F
			case B.ENUM:
				match E.lower():
					case'local':return A.ISO_DATE_STRING
					case'iso_filesystem_string':return A.ISO_FILESYSTEM_STRING
					case _:return A.NONE
			case _:return B.NONE