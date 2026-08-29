_A=True
import logging
from dataclasses import dataclass
__all__='LogOptions',
@dataclass(frozen=_A,slots=_A)
class LogOptions:is_enabled:bool=_A;is_verbose_enabled:bool=_A;log_level:int=logging.DEBUG;stack_level:int=3