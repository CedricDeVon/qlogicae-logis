from __future__ import annotations
C=property
B=None
__all__='TimeManager',
from typing import TYPE_CHECKING as J,Any
if J:from.time_unit import TimeUnit
E=B
F=B
D=B
G=B
A=B
H=B
def I():global I;global E;global F;global D;global G;global A;global H;import time;from datetime import date,datetime as C;from.singleton_manager import SingletonManager as J;from.time_unit import TimeUnit as K;from.time_zone_manager import TimeZoneManager as L;E=time;F=date;D=C;G=J;A=K;H=L;I=lambda:B
class K:
	__slots__='_TIME_UNIT_TO_NANOSECONDS','_time_zone_manager'
	def __init__(B):I();B._TIME_UNIT_TO_NANOSECONDS={A.NANOSECOND:1.,A.MICROSECOND:1e3,A.MILLISECOND:1e6,A.SECOND:1e9,A.MINUTE:6e10,A.HOUR:36e11,A.DAY:864e11,A.WEEK:6048e11,A.MONTH:2629746e9,A.YEAR:3.1556952e16,A.DECADE:3.1556952e17,A.CENTURY:3.1556952e18,A.MILLENNIUM:3.1556952e19};B._time_zone_manager=G.get_singleton(H)
	@C
	def current_iso8601_date(self):A=F.today().strftime('%Y-%m-%d');return A
	@C
	def current_nanosecond(self):A=E.time_ns();return A
	@C
	def current_microsecond(self):return self.current_nanosecond//1000
	@C
	def current_millisecond(self):return self.current_nanosecond//1000000
	@C
	def current_second(self):A=D.now(self._time_zone_manager.selected_time_zone).second;return A
	@C
	def current_minute(self):A=D.now(self._time_zone_manager.selected_time_zone).minute;return A
	@C
	def current_hour(self):A=D.now(self._time_zone_manager.selected_time_zone).hour;return A
	@C
	def current_day(self):A=D.now(self._time_zone_manager.selected_time_zone).day;return A
	@C
	def current_week(self):A=D.now().isocalendar().week;return A
	@C
	def current_month(self):A=D.now(self._time_zone_manager.selected_time_zone).month;return A
	@C
	def current_year(self):A=D.now(self._time_zone_manager.selected_time_zone).year;return A
	@C
	def current_decade(self):return self.current_year//10
	@C
	def current_century(self):return(self.current_year-1)//100+1
	@C
	def current_millenium(self):return(self.current_year-1)//1000+1
	def calculate_elapsed_time(D,start,time_unit=B):
		C=time_unit
		if C is B:C=A.SECOND
		return D.convert_time_unit(E.time_ns()-start,A.NANOSECOND,C)
	def calculate_duration_time(D,start,end,time_unit=B):
		C=time_unit
		if C is B:C=A.SECOND
		return D.convert_time_unit(end-start,A.NANOSECOND,C)
	def convert_time_unit(E,value,input_time_unit=B,output_time_unit=B):
		F=value;D=output_time_unit;C=input_time_unit
		if C is B:C=A.SECOND
		if D is B:D=A.SECOND
		if C is D:return float(F)
		G=F*E._TIME_UNIT_TO_NANOSECONDS[C];return G/E._TIME_UNIT_TO_NANOSECONDS[D]