from __future__ import annotations
_A=None
__all__='TimeZoneManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from datetime import tzinfo
_EnumConversionValue=_A
_SingletonManager=_A
_TimeZoneEnumManager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _EnumConversionValue;global _SingletonManager;global _TimeZoneEnumManager;from.enum_conversion_value import EnumConversionValue as A;from.singleton_manager import SingletonManager as B;from.time_zone_enum_manager import TimeZoneEnumManager as C;_EnumConversionValue=A;_SingletonManager=B;_TimeZoneEnumManager=C;_handle_dynamic_imports=lambda:_A
class TimeZoneManager:
	__slots__='_selected_time_zone_type','_valid_time_zone_types','_time_zone_enum_manager'
	def __init__(A):B='local';_handle_dynamic_imports();A._time_zone_enum_manager=_SingletonManager.get_singleton(_TimeZoneEnumManager);A._selected_time_zone_type=B;A._valid_time_zone_types={B,'utc'}
	@property
	def selected_time_zone_type(self):return self._selected_time_zone_type
	@selected_time_zone_type.setter
	def selected_time_zone_type(self,value):
		B=value;A=self
		if B not in A._valid_time_zone_types:raise ValueError(f"time zones must include the followwing: {A._valid_time_zone_types}")
		A._selected_time_zone_type=B
	@property
	def selected_time_zone(self):A=self._time_zone_enum_manager.convert_value(self._selected_time_zone_type,_EnumConversionValue.CUSTOM);return A