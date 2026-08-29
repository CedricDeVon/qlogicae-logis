from __future__ import annotations
C=None
__all__='TimeZoneEnumManager',
from typing import TYPE_CHECKING as G,Any
if G:from.enum_conversion_value import EnumConversionValue
D=C
E=C
B=C
A=C
def F():global F;global D;global E;global B;global A;from datetime import UTC,datetime as G;from.enum_conversion_value import EnumConversionValue as H;from.time_zone import TimeZone as I;D=G;E=UTC;B=H;A=I;F=lambda:C
class H:
	def __init__(A):F()
	def convert_value(I,input_type,output_type=C):
		H='local';G=output_type;F=input_type
		if G is C:G=B.STRING
		match G:
			case B.STRING:
				match F:
					case A.LOCAL:return H
					case A.UTC:return'utc'
					case A.CUSTOM:return'custom'
					case _:return H
			case B.ENUM:
				match str(F).lower():
					case'local':return A.LOCAL
					case'utc':return A.UTC
					case'custom':return A.CUSTOM
					case _:return A.LOCAL
			case B.CUSTOM:
				match str(F).lower():
					case'local':return D.now().astimezone().tzinfo
					case'utc':return E
					case'custom':return D.now().astimezone().tzinfo
					case _:return D.now().astimezone().tzinfo
			case _:return B.NONE