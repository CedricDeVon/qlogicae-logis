B=classmethod
from collections.abc import Callable as C
from typing import Any as A,TypeVar as D,cast
__all__='SingletonManager',
E=D('Type')
class F:
	_singletons:dict[C[[],A],A]={};_singleton_arrays:dict[C[[],A],list[A]]={}
	@B
	def reset(self):self._singletons.clear();self._singleton_arrays.clear();return True
	@B
	def get_singleton(self,constructor):
		B=constructor;A=self._singletons.get(B)
		if A is None:A=B();self._singletons[B]=A
		return A
	@B
	def get_singleton_from_pool(self,constructor,instance_count,index):
		C=instance_count;B=constructor
		if C<=0:raise ValueError('something went wrong here')
		A=self._singleton_arrays.get(B)
		if A is None:A=[B()for A in range(C)];self._singleton_arrays[B]=A
		return cast(E,A[abs(index)%C])