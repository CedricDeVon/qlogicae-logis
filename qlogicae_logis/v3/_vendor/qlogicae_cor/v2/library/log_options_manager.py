from __future__ import annotations
_A=None
__all__='LogOptionsManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from.log_options import LogOptions
_logging=_A
_LogOptions=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _logging;global _LogOptions;import logging as A;from.log_options import LogOptions as B;_logging=A;_LogOptions=B;_handle_dynamic_imports=lambda:_A
class LogOptionsManager:
	def __init__(A):_handle_dynamic_imports()
	def generate_modified_defaults(D,default_log_options,log_level=_A):
		B=log_level;A=default_log_options
		if B is _A:B=_logging.DEBUG
		C=_LogOptions(is_enabled=A.is_enabled,is_verbose_enabled=A.is_verbose_enabled,log_level=B,stack_level=A.stack_level);return C