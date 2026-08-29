from __future__ import annotations
B=None
__all__='ConsoleLogManager',
from typing import TYPE_CHECKING as H,Any
if H:from.log_options import LogOptions
A=B
C=B
D=B
E=B
F=B
def G():global G;global A;global C;global D;global E;global F;import logging as H;from.log_format import LogFormat as I;from.log_options import LogOptions as J;from.log_options_manager import LogOptionsManager as K;from.singleton_manager import SingletonManager as L;A=H;C=I;D=J;E=K;F=L;G=lambda:B
class I:
	__slots__='_logger','_options','_log_options_manager'
	def __init__(B):G();B._log_options_manager=F.get_singleton(E);B._logger=A.getLogger('console-logger');B._logger.setLevel(A.DEBUG);B._logger.propagate=False;B._logger.handlers.clear();H=A.StreamHandler();H.setFormatter(C());B._logger.addHandler(H);B._options=D()
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
	def log_debug(B,message):return B.log(message,B._log_options_manager.generate_modified_defaults(B._options,log_level=A.DEBUG))
	def log_info(B,message):return B.log(message,B._log_options_manager.generate_modified_defaults(B._options,log_level=A.INFO))
	def log_warning(B,message):return B.log(message,B._log_options_manager.generate_modified_defaults(B._options,log_level=A.WARNING))
	def log_error(B,message):return B.log(message,B._log_options_manager.generate_modified_defaults(B._options,log_level=A.ERROR))
	def log_critical(B,message):return B.log(message,B._log_options_manager.generate_modified_defaults(B._options,log_level=A.CRITICAL))