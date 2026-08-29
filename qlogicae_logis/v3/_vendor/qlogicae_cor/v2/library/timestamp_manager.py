from __future__ import annotations
A=None
__all__='TimestampManager',
from typing import TYPE_CHECKING as G,Any
if G:from.time_unit import TimeUnit;from.timestamp import Timestamp
H=A
I=A
J=A
C=A
B=A
E=A
D=A
def F():global F;global H;global I;global J;global C;global B;global E;global D;import time;from datetime import UTC,datetime as G;from.singleton_manager import SingletonManager as K;from.time_unit import TimeUnit as L;from.time_zone_manager import TimeZoneManager as M;from.timestamp import Timestamp as N;H=time;I=UTC;J=G;C=K;B=L;E=M;D=N;F=lambda:A
class K:
	__slots__='_time_zone_manager',
	def __init__(A):F();A._time_zone_manager=C.get_singleton(E)
	def generate_current_timestamp(N,timestamp=A,time_unit=A):
		L=time_unit;K=timestamp
		if K is A:K=D.ISO_DATE_STRING
		if L is A:L=B.NANOSECOND
		F=H.time_ns();G=J.fromtimestamp(F/1000000000,N._time_zone_manager.selected_time_zone)
		match L:
			case B.NONE|B.SECOND:E=''
			case B.MILLISECOND:E=f".{F//1000000%1000:03d}"
			case B.MICROSECOND:E=f".{F//1000%1000000:06d}"
			case B.NANOSECOND:E=f".{F%1000000000:09d}"
			case _:E=''
		if G.tzinfo is I:C='Z'
		else:
			C=G.strftime('%z')
			if C:C=f"{C[:-2]}:{C[-2:]}"
		match K:
			case D.ISO_DATE_STRING:M=G.strftime('%Y-%m-%dT%H:%M:%S')
			case D.ISO_FILESYSTEM_STRING:M=G.strftime('%Y-%m-%dT%H-%M-%S');C=C.replace(':','-')
			case _:return''
		return''.join((M,E,C))