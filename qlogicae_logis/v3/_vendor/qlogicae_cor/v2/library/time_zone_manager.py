from __future__ import annotations
F=property
A=None
__all__='TimeZoneManager',
from typing import TYPE_CHECKING as G,Any
if G:from datetime import tzinfo
B=A
C=A
D=A
def E():global E;global B;global C;global D;from.enum_conversion_value import EnumConversionValue as F;from.singleton_manager import SingletonManager as G;from.time_zone_enum_manager import TimeZoneEnumManager as H;B=F;C=G;D=H;E=lambda:A
class H:
	__slots__='_selected_time_zone_type','_valid_time_zone_types','_time_zone_enum_manager'
	def __init__(A):B='local';E();A._time_zone_enum_manager=C.get_singleton(D);A._selected_time_zone_type=B;A._valid_time_zone_types={B,'utc'}
	@F
	def selected_time_zone_type(self):return self._selected_time_zone_type
	@selected_time_zone_type.setter
	def selected_time_zone_type(self,value):
		B=value;A=self
		if B not in A._valid_time_zone_types:raise ValueError(f"time zones must include the followwing: {A._valid_time_zone_types}")
		A._selected_time_zone_type=B
	@F
	def selected_time_zone(self):A=self._time_zone_enum_manager.convert_value(self._selected_time_zone_type,B.CUSTOM);return A