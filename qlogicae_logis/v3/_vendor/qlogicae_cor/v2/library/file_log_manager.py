from __future__ import annotations
N=False
C=True
A=None
__all__='FileLogManager',
import logging as O
from typing import TYPE_CHECKING as P,Any
if P:from.log_options import LogOptions
B=A
G=A
H=A
E=A
D=A
F=A
I=A
J=A
K=A
L=A
def M():global M;global B;global G;global H;global E;global D;global F;global I;global J;global K;global L;import logging as C,queue;from logging.handlers import QueueHandler as N,QueueListener as O;from pathlib import Path;from.log_format import LogFormat as P;from.log_options import LogOptions as Q;from.log_options_manager import LogOptionsManager as R;from.singleton_manager import SingletonManager as S;from.text_encoding_manager import TextEncodingManager as T;B=C;G=queue;H=N;E=O;D=Path;J=P;K=Q;L=R;F=S;I=T;M=lambda:A
class Q:
	__slots__='logger','file_handlers','log_queue','queue_handler','listener','_options','_cache','_log_options_manager','_text_encoding_manager'
	def __init__(A):M();A._log_options_manager=F.get_singleton(L);A._text_encoding_manager=F.get_singleton(I);A.logger=B.getLogger('file-logger');A.logger.setLevel(B.DEBUG);A.logger.propagate=N;A.logger.handlers.clear();A.file_handlers={};A.log_queue=G.Queue();A.queue_handler=H(A.log_queue);A.logger.addHandler(A.queue_handler);A.listener=E(A.log_queue);A.listener.start();A._options=K();A._cache=[]
	def cache_log(A,message,log_level=O.INFO):B=message;A._cache.append((B,A._log_options_manager.generate_modified_defaults(A._options,log_level=log_level)));return B
	def log_cached(A):
		for(B,D)in A._cache:A.log(B,D)
		A._cache.clear();return C
	@property
	def options(self):A=self._options;return A
	@options.setter
	def options(self,value):self._options=value
	def log(C,message,options):
		B=options;A=message
		if not B.is_enabled:return A
		if B.is_verbose_enabled:C.logger.log(B.log_level,str(A).strip(),stacklevel=B.stack_level)
		else:
			for E in C.file_handlers:
				with D.open(E,'a',encoding=C._text_encoding_manager.selected_encoding)as F:F.write(f"{str(A).strip()}\n")
		return A
	def log_debug(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(A._options,log_level=B.DEBUG))
	def log_info(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(A._options,log_level=B.INFO))
	def log_warning(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(A._options,log_level=B.WARNING))
	def log_error(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(A._options,log_level=B.ERROR))
	def log_critical(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(A._options,log_level=B.CRITICAL))
	def rebuild_listener(A):A.listener.stop();A.listener=E(A.log_queue,*A.file_handlers.values());A.listener.start();return C
	def add_file_output(A,file_path):
		E=D(file_path).resolve()
		if E in A.file_handlers:return N
		E.parent.mkdir(parents=C,exist_ok=C);F=B.FileHandler(E,encoding=A._text_encoding_manager.selected_encoding);F.setFormatter(J());A.file_handlers[E]=F;A.rebuild_listener();return C
	def remove_file_output(B,file_path):
		E=D(file_path).resolve();F=B.file_handlers.get(E)
		if F is A:return N
		F.close();del B.file_handlers[E];B.rebuild_listener();return C
	def clear_file_outputs(A):
		for B in A.file_handlers.values():B.close()
		A.file_handlers.clear();A.rebuild_listener();A._cache.clear();return C
	def shutdown(A):
		A.log_cached();A.listener.stop()
		for B in A.file_handlers.values():B.close()
		A.file_handlers.clear();return C