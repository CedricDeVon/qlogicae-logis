from __future__ import annotations
_B=True
_A=None
__all__='AsynchronousManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:import asyncio,threading;from collections.abc import Callable,Coroutine,Iterable;from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor;from typing import ParamSpec,TypeVar;P=ParamSpec('P');T=TypeVar('T')
_asyncio=_A
_threading=_A
_partial=_A
_ProcessPoolExecutor=_A
_ThreadPoolExecutor=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _asyncio;global _threading;global _partial;global _ProcessPoolExecutor;global _ThreadPoolExecutor;import asyncio as A,threading as B;from concurrent.futures import ProcessPoolExecutor as C,ThreadPoolExecutor as D;from functools import partial as E;_asyncio=A;_threading=B;_partial=E;_ProcessPoolExecutor=C;_ThreadPoolExecutor=D;_handle_dynamic_imports=lambda:_A
class AsynchronousManager:
	__slots__='_thread_executor','_process_executor'
	def __init__(A):_handle_dynamic_imports();A._thread_executor=_A;A._process_executor=_A
	@property
	def thread_executor(self):
		A=self
		if A._thread_executor is _A:A._thread_executor=_ThreadPoolExecutor()
		return A._thread_executor
	@property
	def process_executor(self):
		A=self
		if A._process_executor is _A:A._process_executor=_ProcessPoolExecutor()
		return A._process_executor
	async def run_thread(E,A,*B,**C):D=await _asyncio.to_thread(A,*B,**C);return D
	async def run_thread_pool(A,B,*C,**D):E=_asyncio.get_running_loop();F=await E.run_in_executor(A.thread_executor,_partial(B,*C,**D));return F
	async def run_process_pool(A,B,*C,**D):E=_asyncio.get_running_loop();F=await E.run_in_executor(A.process_executor,_partial(B,*C,**D));return F
	async def gather(C,*A,return_exceptions=False):B=await _asyncio.gather(*A,return_exceptions=return_exceptions);return B
	async def wait(D,*A,timeout=_A):B={_asyncio.create_task(A)for A in A};C=await _asyncio.wait(B,timeout=timeout);return C
	def create_task(B,coroutine,name=_A):A=_asyncio.create_task(coroutine,name=name);return A
	async def timeout(B,coroutine,seconds):A=await _asyncio.wait_for(coroutine,timeout=seconds);return A
	async def map_thread(A,function,*B):C=await _asyncio.gather(*(A.run_thread(function,*B)for B in zip(*B,strict=_B)));return C
	async def map_thread_pool(A,function,*B):C=await _asyncio.gather(*(A.run_thread_pool(function,*B)for B in zip(*B,strict=_B)));return C
	async def map_process_pool(A,function,*B):C=await _asyncio.gather(*(A.run_process_pool(function,*B)for B in zip(*B,strict=_B)));return C
	def create_thread(E,B,*C,daemon=False,start=_B,**D):
		A=_threading.Thread(target=B,args=C,kwargs=D,daemon=daemon)
		if start:A.start()
		return A
	def shutdown(A,*,wait=_B):
		if A._thread_executor is not _A:A._thread_executor.shutdown(wait=wait);A._thread_executor=_A
		if A._process_executor is not _A:A._process_executor.shutdown(wait=wait);A._process_executor=_A
	def __enter__(A):return A
	def __exit__(A,exc_type,exc,traceback):A.shutdown()