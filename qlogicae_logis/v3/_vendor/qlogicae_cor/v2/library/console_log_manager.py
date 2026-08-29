from __future__ import annotations
_A=None
__all__='ConsoleLogManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from.log_options import LogOptions
_logging=_A
_LogFormat=_A
_LogOptions=_A
_LogOptionsManager=_A
_SingletonManager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _logging;global _LogFormat;global _LogOptions;global _LogOptionsManager;global _SingletonManager;import logging as A;from.log_format import LogFormat as B;from.log_options import LogOptions as C;from.log_options_manager import LogOptionsManager as D;from.singleton_manager import SingletonManager as E;_logging=A;_LogFormat=B;_LogOptions=C;_LogOptionsManager=D;_SingletonManager=E;_handle_dynamic_imports=lambda:_A
class ConsoleLogManager:
	__slots__='_logger','_options','_log_options_manager'
	def __init__(A):_handle_dynamic_imports();A._log_options_manager=_SingletonManager.get_singleton(_LogOptionsManager);A._logger=_logging.getLogger('console-logger');A._logger.setLevel(_logging.DEBUG);A._logger.propagate=False;A._logger.handlers.clear();B=_logging.StreamHandler();B.setFormatter(_LogFormat());A._logger.addHandler(B);A._options=_LogOptions()
	@property
	def options(self):return self._options
	@options.setter
	def options(self,value):self._options=value
	def log(C,message,options):
		B=options;A=message
		if not B.is_enabled:return''
		A=str(A).strip()
		if B.is_verbose_enabled:C._logger.log(B.log_level,A,stacklevel=B.stack_level)
		else:print(A)
		return A
	def log_debug(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(A._options,log_level=_logging.DEBUG))
	def log_info(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(A._options,log_level=_logging.INFO))
	def log_warning(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(A._options,log_level=_logging.WARNING))
	def log_error(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(A._options,log_level=_logging.ERROR))
	def log_critical(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(A._options,log_level=_logging.CRITICAL))