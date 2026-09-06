from __future__ import annotations

from typing import Any

__all__ = (
    "LogManager"
)

_ImportManager: Any = None
_DisplayManager: Any = None
_DatabaseManager: Any = None
_ValueCacheDatabaseManager: Any = None


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _ImportManager
    global _DisplayManager
    global _DatabaseManager
    global _ValueCacheDatabaseManager

    from ..library import (
        database_manager,
        display_manager,
        import_manager,
        value_cache_database_manager,
    )

    _DisplayManager = (
        display_manager.DisplayManager
    )
    _DatabaseManager = (
        database_manager.DatabaseManager
    )
    _ValueCacheDatabaseManager = (
        value_cache_database_manager.ValueCacheDatabaseManager
    )
    _ImportManager = (
        import_manager
            .ImportManager
    )

    _handle_dynamic_imports = lambda: None

class LogManager:
    __slots__ = (
        "_import_manager",
        "_display_manager",
        "_database_manager",
        "_value_cache_database_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._display_manager = (
            _ImportManager.read_singleton(
                _DisplayManager
            )
        )
        self._import_manager = (
            _ImportManager.read_singleton(
                _ImportManager
            )
        )
        self._database_manager = (
            _ImportManager.read_singleton(
                _DatabaseManager
            )
        )
        self._value_cache_database_manager = (
            _ImportManager.read_singleton(
                _ValueCacheDatabaseManager
            )
        )

    def log_debug_method_start(self, **kwargs: Any) -> bool:
        if not kwargs:
            return False

        reference = kwargs.get(
            "reference",
            ""
        )
        message = "start"
        if reference:
            message = f"{reference} | {message}"

        self._import_manager.log_cache_debug_to_file(
            message=message
        )

        return True

    def log_debug_method_interrupted(self, **kwargs: Any) -> bool:
        if not kwargs:
            return False

        reference = kwargs.get(
            "reference",
            ""
        )
        message = "interrupted"
        if reference:
            message = f"{reference} | {message}"

        self._import_manager.log_cache_warning_to_file(
            message=message
        )

        return True

    def log_debug_method_complete(self, **kwargs: Any) -> bool:
        if not kwargs:
            return False

        reference = kwargs.get(
            "reference",
            ""
        )
        message = "complete"
        if reference:
            message = f"{reference} | {message}"

        self._import_manager.log_cache_debug_to_file(
            message=message
        )

        return True

    def log_debug_snapshot_execution(self, **kwargs: Any) -> bool:
        if not kwargs:
            return False

        callback = kwargs.get(
            "callback",
            ""
        )
        snapshot_execution_data = (
            self._value_cache_database_manager
                .read_debug_snapshot_execution(
                    label=callback
                )
        )
        message = f"{callback} | {snapshot_execution_data}"

        self._import_manager.log_cache_debug_to_file(
            message=message
        )

        return True

    def log_display_warning(self, **kwargs: Any) -> bool:
        if not kwargs:
            return False

        reference = kwargs.get(
            "reference",
            ""
        )
        message = kwargs.get(
            "message",
            ""
        )

        console_message = (
            message
        )
        file_message = ""
        if reference:
            file_message = f"{reference} | {message}"

        self._import_manager.log_warning_to_console(
            message=console_message
        )
        self._import_manager.log_warning_to_file(
            message=file_message
        )

        return True

