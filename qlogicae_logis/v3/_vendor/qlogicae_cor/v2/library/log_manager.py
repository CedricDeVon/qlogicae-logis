from __future__ import annotations
_A=None
__all__='LogManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from.log_options import LogOptions
_logging=_A
_ConsoleLogManager=_A
_FileLogManager=_A
_LogOptionsManager=_A
_SingletonManager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _logging;global _ConsoleLogManager;global _FileLogManager;global _LogOptionsManager;global _SingletonManager;import logging as A;from.console_log_manager import ConsoleLogManager as B;from.file_log_manager import FileLogManager as C;from.log_options_manager import LogOptionsManager as D;from.singleton_manager import SingletonManager as E;_logging=A;_ConsoleLogManager=B;_FileLogManager=C;_LogOptionsManager=D;_SingletonManager=E;_handle_dynamic_imports=lambda:_A
class LogManager:
	__slots__='_file_log_manager','_console_log_manager','_log_options_manager'
	def __init__(A):_handle_dynamic_imports();A._file_log_manager=_SingletonManager.get_singleton(_FileLogManager);A._console_log_manager=_SingletonManager.get_singleton(_ConsoleLogManager);A._log_options_manager=_SingletonManager.get_singleton(_LogOptionsManager)
	def log(B,message,console_options,file_options):A=message;B._console_log_manager.log(A,console_options);B._file_log_manager.log(A,file_options);return A
	def log_debug(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(_SingletonManager.get_singleton(_ConsoleLogManager).options,log_level=_logging.DEBUG),A._log_options_manager.generate_modified_defaults(_SingletonManager.get_singleton(_FileLogManager).options,log_level=_logging.DEBUG))
	def log_info(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(_SingletonManager.get_singleton(_ConsoleLogManager).options,log_level=_logging.INFO),A._log_options_manager.generate_modified_defaults(_SingletonManager.get_singleton(_FileLogManager).options,log_level=_logging.INFO))
	def log_warning(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(_SingletonManager.get_singleton(_ConsoleLogManager).options,log_level=_logging.WARNING),A._log_options_manager.generate_modified_defaults(_SingletonManager.get_singleton(_FileLogManager).options,log_level=_logging.WARNING))
	def log_error(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(_SingletonManager.get_singleton(_ConsoleLogManager).options,log_level=_logging.ERROR),A._log_options_manager.generate_modified_defaults(_SingletonManager.get_singleton(_FileLogManager).options,log_level=_logging.ERROR))
	def log_critical(A,message):return A.log(message,A._log_options_manager.generate_modified_defaults(_SingletonManager.get_singleton(_ConsoleLogManager).options,log_level=_logging.CRITICAL),A._log_options_manager.generate_modified_defaults(_SingletonManager.get_singleton(_FileLogManager).options,log_level=_logging.CRITICAL))
	def shutdown(A):A._file_log_manager.shutdown();return True