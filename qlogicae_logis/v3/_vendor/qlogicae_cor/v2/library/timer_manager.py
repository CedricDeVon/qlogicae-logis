from __future__ import annotations
G=property
C=True
A=None
__all__='TimerManager',
from typing import TYPE_CHECKING as H,Any
if H:from.time_unit import TimeUnit
D=A
E=A
B=A
def F():global F;global D;global E;global B;from.singleton_manager import SingletonManager as C;from.time_manager import TimeManager as G;from.time_unit import TimeUnit as H;D=C;E=G;B=H;F=lambda:A
class I:
	__slots__='_start_timestamp','_stop_timestamp'
	def __init__(A):F();A._time_manager=D.get_singleton(E);A._start_timestamp=0;A._stop_timestamp=0
	@G
	def start_timestamp(self):return self._start_timestamp
	@G
	def stop_timestamp(self):return self._stop_timestamp
	def start_time(A):A._start_timestamp=A._time_manager.current_nanosecond;return C
	def stop_time(A):A._stop_timestamp=A._time_manager.current_nanosecond;return C
	def clear_time(A):A._start_timestamp=0;A._stop_timestamp=0;return C
	def reset_time(A):A._start_timestamp=A._time_manager.current_nanosecond;A._stop_timestamp=0;return C
	def calculate_elapsed_time(C,time_unit=A):
		D=time_unit
		if D is A:D=B.SECOND
		E=C._time_manager.convert_time_unit(C._time_manager.current_nanosecond-C._start_timestamp,output_time_unit=D);return E
	def calculate_duration_time(C,time_unit=A):
		D=time_unit
		if D is A:D=B.SECOND
		E=C._time_manager.convert_time_unit(C._stop_timestamp-C._start_timestamp,output_time_unit=D);return E