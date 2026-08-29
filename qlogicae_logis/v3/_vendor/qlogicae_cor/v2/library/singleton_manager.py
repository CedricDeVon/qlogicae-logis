from collections.abc import Callable
from typing import Any,TypeVar,cast
__all__='SingletonManager',
Type=TypeVar('Type')
class SingletonManager:
	_singletons:dict[Callable[[],Any],Any]={};_singleton_arrays:dict[Callable[[],Any],list[Any]]={}
	@classmethod
	def reset(A):A._singletons.clear();A._singleton_arrays.clear();return True
	@classmethod
	def get_singleton(C,constructor):
		B=constructor;A=C._singletons.get(B)
		if A is None:A=B();C._singletons[B]=A
		return A
	@classmethod
	def get_singleton_from_pool(D,constructor,instance_count,index):
		C=instance_count;B=constructor
		if C<=0:raise ValueError('something went wrong here')
		A=D._singleton_arrays.get(B)
		if A is None:A=[B()for A in range(C)];D._singleton_arrays[B]=A
		return cast(Type,A[abs(index)%C])