from __future__ import annotations
_B=True
_A=None
__all__='TimerManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from.time_unit import TimeUnit
_SingletonManager=_A
_TimeManager=_A
_TimeUnit=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _SingletonManager;global _TimeManager;global _TimeUnit;from.singleton_manager import SingletonManager as A;from.time_manager import TimeManager as B;from.time_unit import TimeUnit as C;_SingletonManager=A;_TimeManager=B;_TimeUnit=C;_handle_dynamic_imports=lambda:_A
class TimerManager:
	__slots__='_start_timestamp','_stop_timestamp'
	def __init__(A):_handle_dynamic_imports();A._time_manager=_SingletonManager.get_singleton(_TimeManager);A._start_timestamp=0;A._stop_timestamp=0
	@property
	def start_timestamp(self):return self._start_timestamp
	@property
	def stop_timestamp(self):return self._stop_timestamp
	def start_time(A):A._start_timestamp=A._time_manager.current_nanosecond;return _B
	def stop_time(A):A._stop_timestamp=A._time_manager.current_nanosecond;return _B
	def clear_time(A):A._start_timestamp=0;A._stop_timestamp=0;return _B
	def reset_time(A):A._start_timestamp=A._time_manager.current_nanosecond;A._stop_timestamp=0;return _B
	def calculate_elapsed_time(A,time_unit=_A):
		B=time_unit
		if B is _A:B=_TimeUnit.SECOND
		C=A._time_manager.convert_time_unit(A._time_manager.current_nanosecond-A._start_timestamp,output_time_unit=B);return C
	def calculate_duration_time(A,time_unit=_A):
		B=time_unit
		if B is _A:B=_TimeUnit.SECOND
		C=A._time_manager.convert_time_unit(A._stop_timestamp-A._start_timestamp,output_time_unit=B);return C