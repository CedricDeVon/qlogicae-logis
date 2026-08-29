from __future__ import annotations
_A=None
__all__='TimestampManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from.time_unit import TimeUnit;from.timestamp import Timestamp
_time=_A
_UTC=_A
_datetime=_A
_SingletonManager=_A
_TimeUnit=_A
_TimeZoneManager=_A
_Timestamp=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _time;global _UTC;global _datetime;global _SingletonManager;global _TimeUnit;global _TimeZoneManager;global _Timestamp;import time;from datetime import UTC,datetime as A;from.singleton_manager import SingletonManager as B;from.time_unit import TimeUnit as C;from.time_zone_manager import TimeZoneManager as D;from.timestamp import Timestamp as E;_time=time;_UTC=UTC;_datetime=A;_SingletonManager=B;_TimeUnit=C;_TimeZoneManager=D;_Timestamp=E;_handle_dynamic_imports=lambda:_A
class TimestampManager:
	__slots__='_time_zone_manager',
	def __init__(A):_handle_dynamic_imports();A._time_zone_manager=_SingletonManager.get_singleton(_TimeZoneManager)
	def generate_current_timestamp(H,timestamp=_A,time_unit=_A):
		F=time_unit;E=timestamp
		if E is _A:E=_Timestamp.ISO_DATE_STRING
		if F is _A:F=_TimeUnit.NANOSECOND
		C=_time.time_ns();D=_datetime.fromtimestamp(C/1000000000,H._time_zone_manager.selected_time_zone)
		match F:
			case _TimeUnit.NONE|_TimeUnit.SECOND:B=''
			case _TimeUnit.MILLISECOND:B=f".{C//1000000%1000:03d}"
			case _TimeUnit.MICROSECOND:B=f".{C//1000%1000000:06d}"
			case _TimeUnit.NANOSECOND:B=f".{C%1000000000:09d}"
			case _:B=''
		if D.tzinfo is _UTC:A='Z'
		else:
			A=D.strftime('%z')
			if A:A=f"{A[:-2]}:{A[-2:]}"
		match E:
			case _Timestamp.ISO_DATE_STRING:G=D.strftime('%Y-%m-%dT%H:%M:%S')
			case _Timestamp.ISO_FILESYSTEM_STRING:G=D.strftime('%Y-%m-%dT%H-%M-%S');A=A.replace(':','-')
			case _:return''
		return''.join((G,B,A))