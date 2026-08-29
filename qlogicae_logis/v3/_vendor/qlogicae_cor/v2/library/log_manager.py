from __future__ import annotations
E=None
__all__='LogManager',
from typing import TYPE_CHECKING as H,Any
if H:from.log_options import LogOptions
B=E
C=E
D=E
F=E
A=E
def G():global G;global B;global C;global D;global F;global A;import logging as H;from.console_log_manager import ConsoleLogManager as I;from.file_log_manager import FileLogManager as J;from.log_options_manager import LogOptionsManager as K;from.singleton_manager import SingletonManager as L;B=H;C=I;D=J;F=K;A=L;G=lambda:E
class I:
	__slots__='_file_log_manager','_console_log_manager','_log_options_manager'
	def __init__(B):G();B._file_log_manager=A.get_singleton(D);B._console_log_manager=A.get_singleton(C);B._log_options_manager=A.get_singleton(F)
	def log(B,message,console_options,file_options):A=message;B._console_log_manager.log(A,console_options);B._file_log_manager.log(A,file_options);return A
	def log_debug(E,message):return E.log(message,E._log_options_manager.generate_modified_defaults(A.get_singleton(C).options,log_level=B.DEBUG),E._log_options_manager.generate_modified_defaults(A.get_singleton(D).options,log_level=B.DEBUG))
	def log_info(E,message):return E.log(message,E._log_options_manager.generate_modified_defaults(A.get_singleton(C).options,log_level=B.INFO),E._log_options_manager.generate_modified_defaults(A.get_singleton(D).options,log_level=B.INFO))
	def log_warning(E,message):return E.log(message,E._log_options_manager.generate_modified_defaults(A.get_singleton(C).options,log_level=B.WARNING),E._log_options_manager.generate_modified_defaults(A.get_singleton(D).options,log_level=B.WARNING))
	def log_error(E,message):return E.log(message,E._log_options_manager.generate_modified_defaults(A.get_singleton(C).options,log_level=B.ERROR),E._log_options_manager.generate_modified_defaults(A.get_singleton(D).options,log_level=B.ERROR))
	def log_critical(E,message):return E.log(message,E._log_options_manager.generate_modified_defaults(A.get_singleton(C).options,log_level=B.CRITICAL),E._log_options_manager.generate_modified_defaults(A.get_singleton(D).options,log_level=B.CRITICAL))
	def shutdown(A):A._file_log_manager.shutdown();return True