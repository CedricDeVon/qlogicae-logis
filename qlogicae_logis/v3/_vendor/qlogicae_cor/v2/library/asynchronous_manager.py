from __future__ import annotations
K=False
J=property
I=zip
C=True
A=None
__all__='AsynchronousManager',
from typing import TYPE_CHECKING as L,Any
if L:import asyncio,threading;from collections.abc import Callable,Coroutine,Iterable;from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor;from typing import ParamSpec as M,TypeVar as N;O=M('P');P=N('T')
B=A
E=A
D=A
F=A
G=A
def H():global H;global B;global E;global D;global F;global G;import asyncio as C,threading as I;from concurrent.futures import ProcessPoolExecutor as J,ThreadPoolExecutor as K;from functools import partial as L;B=C;E=I;D=L;F=J;G=K;H=lambda:A
class Q:
	__slots__='_thread_executor','_process_executor'
	def __init__(B):H();B._thread_executor=A;B._process_executor=A
	@J
	def thread_executor(self):
		B=self
		if B._thread_executor is A:B._thread_executor=G()
		return B._thread_executor
	@J
	def process_executor(self):
		B=self
		if B._process_executor is A:B._process_executor=F()
		return B._process_executor
	async def run_thread(F,A,*C,**D):E=await B.to_thread(A,*C,**D);return E
	async def run_thread_pool(A,C,*E,**F):G=B.get_running_loop();H=await G.run_in_executor(A.thread_executor,D(C,*E,**F));return H
	async def run_process_pool(A,C,*E,**F):G=B.get_running_loop();H=await G.run_in_executor(A.process_executor,D(C,*E,**F));return H
	async def gather(D,*A,return_exceptions=K):C=await B.gather(*A,return_exceptions=return_exceptions);return C
	async def wait(E,*A,timeout=A):C={B.create_task(A)for A in A};D=await B.wait(C,timeout=timeout);return D
	def create_task(C,coroutine,name=A):A=B.create_task(coroutine,name=name);return A
	async def timeout(C,coroutine,seconds):A=await B.wait_for(coroutine,timeout=seconds);return A
	async def map_thread(A,function,*D):E=await B.gather(*(A.run_thread(function,*B)for B in I(*D,strict=C)));return E
	async def map_thread_pool(A,function,*D):E=await B.gather(*(A.run_thread_pool(function,*B)for B in I(*D,strict=C)));return E
	async def map_process_pool(A,function,*D):E=await B.gather(*(A.run_process_pool(function,*B)for B in I(*D,strict=C)));return E
	def create_thread(F,B,*C,daemon=K,start=C,**D):
		A=E.Thread(target=B,args=C,kwargs=D,daemon=daemon)
		if start:A.start()
		return A
	def shutdown(B,*,wait=C):
		if B._thread_executor is not A:B._thread_executor.shutdown(wait=wait);B._thread_executor=A
		if B._process_executor is not A:B._process_executor.shutdown(wait=wait);B._process_executor=A
	def __enter__(A):return A
	def __exit__(A,exc_type,exc,traceback):A.shutdown()