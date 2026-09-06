from __future__ import annotations

__all__ = (
    "LogFormat",
)

import logging
from typing import Any

_SingletonManager: Any = None
_TimestampManager: Any = None


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _logging
    global _SingletonManager
    global _TimestampManager

    from .singleton_manager import SingletonManager
    from .timestamp_manager import TimestampManager

    _SingletonManager = (
        SingletonManager
    )
    _TimestampManager = (
        TimestampManager
    )

    _handle_dynamic_imports = lambda: None


class LogFormat(logging.Formatter):
    def __init__(self) -> None:
        _handle_dynamic_imports()

    def format_log_color(
        self,
        message: str,
        log_level: int,
    ) -> str:        
        match log_level:
            case logging.INFO:
                message = f"{message}"

            case logging.DEBUG:
                message = f"\x1b[35m{message}\x1b[0m"

            case logging.WARNING:
                message = f"\x1b[33m{message}\x1b[0m"

            case logging.ERROR:
                message = f"\x1b[31m{message}\x1b[0m"

            case _:
                message = f"{message}"

        return message

    def format(
        self,
        record: logging.LogRecord,
    ) -> str:
        timestamp: str = (
            _SingletonManager.get_singleton(
                _TimestampManager,
            ).generate_current_timestamp()
        )

        value: str = (
            f"[ {timestamp} ] [ {record.levelname} ] - {record.getMessage()}"
        )
        value = (
            self.format_log_color(
                value,
                record.levelno
            )
        )

        return value
