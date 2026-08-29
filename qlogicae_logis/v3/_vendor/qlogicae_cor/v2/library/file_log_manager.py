from __future__ import annotations
_C=False
_B=True
_A=None
__all__='FileLogManager',
import logging
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from.log_options import LogOptions
_logging=_A
_queue=_A
_QueueHandler=_A
_QueueListener=_A
_Path=_A
_SingletonManager=_A
_TextEncodingManager=_A
_LogFormat=_A
_LogOptions=_A
_LogOptionsManager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _logging;global _queue;global _QueueHandler;global _QueueListener;global _Path;global _SingletonManager;global _TextEncodingManager;global _LogFormat;global _LogOptions;global _LogOptionsManager;import logging as A,queue;from logging.handlers import QueueHandler as B,QueueListener as C;from pathlib import Path;from.log_format import LogFormat as D;from.log_options import LogOptions as E;from.log_options_manager import LogOptionsManager as F;from.singleton_manager import SingletonManager as G;from.text_encoding_manager import TextEncodingManager as H;_logging=A;_queue=queue;_QueueHandler=B;_QueueListener=C;_Path=Path;_LogFormat=D;_LogOptions=E;_LogOptionsManager=F;_SingletonManager=G;_TextEncodingManager=H;_handle_dynamic_imports=lambda:_A
class FileLogManager:
	__slots__='logger','file_handlers','log_queue','queue_handler','listener','_options','_cache','_log_options_manager','_text_encoding_manager'
	def __init__(A):_handle_dynamic_imports();A._log_options_manager=_SingletonManager.get_singleton(_LogOptionsManager);A._text_encoding_manager=_SingletonManager.get_singleton(_TextEncodingManager);A.logger=_logging.getLogger('file-logger');A.logger.setLevel(_logging.DEBUG);A.logger.propagate=_C;A.logger.handlers.clear();A.file_handlers={};A.log_queue=_queue.Queue();A.queue_handler=_QueueHandler(A.log_queue);A.logger.addHandler(A.queue_handler);A.listener=_QueueListener(A.log_queue);A.listener.start();A._options=_LogOptions();A._cache=[]
	def cache_log(A,message,log_level=logging.INFO):B=message;A._cache.append((B,A._log_options_manager.generate_modified_defaults(A._options,log_level=log_level)));return B
	def log_cached(A):
		for(B,C)in A._cache:A.log(B,C)
		A._cache.clear();return _B
	@property
	def options(self):A=self._options;return A
	@options.setter
	def options(self,value):self._options=value
	def log(C,message,options):
		B=options;A=message
		if not B.is_enabled:return A
		if B.is_verbose_enabled:C.logger.log(B.log_level,str(A).strip(),stacklevel=B.stack_level)
		else:
			for D in C.file_handlers:
				with _Path.open(D,'a',encoding=C._text_encoding_manager.selected_encoding)as E:E.write(f"{str(A).strip()}\n")
		return A
	def log_debug(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(A._options,log_level=_logging.DEBUG))
	def log_info(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(A._options,log_level=_logging.INFO))
	def log_warning(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(A._options,log_level=_logging.WARNING))
	def log_error(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(A._options,log_level=_logging.ERROR))
	def log_critical(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(A._options,log_level=_logging.CRITICAL))
	def rebuild_listener(A):A.listener.stop();A.listener=_QueueListener(A.log_queue,*A.file_handlers.values());A.listener.start();return _B
	def add_file_output(A,file_path):
		B=_Path(file_path).resolve()
		if B in A.file_handlers:return _C
		B.parent.mkdir(parents=_B,exist_ok=_B);C=_logging.FileHandler(B,encoding=A._text_encoding_manager.selected_encoding);C.setFormatter(_LogFormat());A.file_handlers[B]=C;A.rebuild_listener();return _B
	def remove_file_output(A,file_path):
		B=_Path(file_path).resolve();C=A.file_handlers.get(B)
		if C is _A:return _C
		C.close();del A.file_handlers[B];A.rebuild_listener();return _B
	def clear_file_outputs(A):
		for B in A.file_handlers.values():B.close()
		A.file_handlers.clear();A.rebuild_listener();A._cache.clear();return _B
	def shutdown(A):
		A.log_cached();A.listener.stop()
		for B in A.file_handlers.values():B.close()
		A.file_handlers.clear();return _B