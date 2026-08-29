from __future__ import annotations
_A=None
__all__='TimeManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from.time_unit import TimeUnit
_time=_A
_date=_A
_datetime=_A
_SingletonManager=_A
_TimeUnit=_A
_TimeZoneManager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _time;global _date;global _datetime;global _SingletonManager;global _TimeUnit;global _TimeZoneManager;import time;from datetime import date,datetime as A;from.singleton_manager import SingletonManager as B;from.time_unit import TimeUnit as C;from.time_zone_manager import TimeZoneManager as D;_time=time;_date=date;_datetime=A;_SingletonManager=B;_TimeUnit=C;_TimeZoneManager=D;_handle_dynamic_imports=lambda:_A
class TimeManager:
	__slots__='_TIME_UNIT_TO_NANOSECONDS','_time_zone_manager'
	def __init__(A):_handle_dynamic_imports();A._TIME_UNIT_TO_NANOSECONDS={_TimeUnit.NANOSECOND:1.,_TimeUnit.MICROSECOND:1e3,_TimeUnit.MILLISECOND:1e6,_TimeUnit.SECOND:1e9,_TimeUnit.MINUTE:6e10,_TimeUnit.HOUR:36e11,_TimeUnit.DAY:864e11,_TimeUnit.WEEK:6048e11,_TimeUnit.MONTH:2629746e9,_TimeUnit.YEAR:3.1556952e16,_TimeUnit.DECADE:3.1556952e17,_TimeUnit.CENTURY:3.1556952e18,_TimeUnit.MILLENNIUM:3.1556952e19};A._time_zone_manager=_SingletonManager.get_singleton(_TimeZoneManager)
	@property
	def current_iso8601_date(self):A=_date.today().strftime('%Y-%m-%d');return A
	@property
	def current_nanosecond(self):A=_time.time_ns();return A
	@property
	def current_microsecond(self):return self.current_nanosecond//1000
	@property
	def current_millisecond(self):return self.current_nanosecond//1000000
	@property
	def current_second(self):A=_datetime.now(self._time_zone_manager.selected_time_zone).second;return A
	@property
	def current_minute(self):A=_datetime.now(self._time_zone_manager.selected_time_zone).minute;return A
	@property
	def current_hour(self):A=_datetime.now(self._time_zone_manager.selected_time_zone).hour;return A
	@property
	def current_day(self):A=_datetime.now(self._time_zone_manager.selected_time_zone).day;return A
	@property
	def current_week(self):A=_datetime.now().isocalendar().week;return A
	@property
	def current_month(self):A=_datetime.now(self._time_zone_manager.selected_time_zone).month;return A
	@property
	def current_year(self):A=_datetime.now(self._time_zone_manager.selected_time_zone).year;return A
	@property
	def current_decade(self):return self.current_year//10
	@property
	def current_century(self):return(self.current_year-1)//100+1
	@property
	def current_millenium(self):return(self.current_year-1)//1000+1
	def calculate_elapsed_time(B,start,time_unit=_A):
		A=time_unit
		if A is _A:A=_TimeUnit.SECOND
		return B.convert_time_unit(_time.time_ns()-start,_TimeUnit.NANOSECOND,A)
	def calculate_duration_time(B,start,end,time_unit=_A):
		A=time_unit
		if A is _A:A=_TimeUnit.SECOND
		return B.convert_time_unit(end-start,_TimeUnit.NANOSECOND,A)
	def convert_time_unit(C,value,input_time_unit=_A,output_time_unit=_A):
		D=value;B=output_time_unit;A=input_time_unit
		if A is _A:A=_TimeUnit.SECOND
		if B is _A:B=_TimeUnit.SECOND
		if A is B:return float(D)
		E=D*C._TIME_UNIT_TO_NANOSECONDS[A];return E/C._TIME_UNIT_TO_NANOSECONDS[B]