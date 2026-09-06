from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from typing import Any, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

__all__ = (
    "DecoratorManager"
)

_LogManager: Any = None
_ImportManager: Any = None
_DatabaseManager: Any = None
_TaskStorageManager: Any = None
_ValueCacheDatabaseManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _LogManager
    global _ImportManager
    global _DatabaseManager
    global _TaskStorageManager
    global _ValueCacheDatabaseManager

    from ..library import (
        database_manager,
        import_manager,
        log_manager,
        task_storage_manager,
        value_cache_database_manager,
    )

    _TaskStorageManager = (
        task_storage_manager
            .TaskStorageManager
    )
    _DatabaseManager = (
        database_manager
            .DatabaseManager
    )
    _ValueCacheDatabaseManager = (
        value_cache_database_manager
            .ValueCacheDatabaseManager
    )
    _LogManager = (
        log_manager
            .LogManager
    )
    _ImportManager = (
        import_manager
            .ImportManager
    )
    _handle_dynamic_imports = lambda: None

class DecoratorManager:
    __slots__ = ()

    @staticmethod
    def single_task_decorator(
        callback: Callable[P, R],
    ) -> Any:
        _handle_dynamic_imports()

        @wraps(callback)
        def wrapper(
            self: Any,
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> Any:
            task_storage_manager = (
                _ImportManager.read_singleton(
                    _TaskStorageManager
                )
            )
            database_manager = (
                _ImportManager.read_singleton(
                    _DatabaseManager
                )
            )
            value_cache_database_manager = (
                _ImportManager.read_singleton(
                    _ValueCacheDatabaseManager
                )
            )
            log_manager = (
                _ImportManager.read_singleton(
                    _LogManager
                )
            )

            if task_storage_manager.is_executed(label=callback):
                return True

            log_manager.log_debug_method_start(
                reference=callback
            )

            result: Any = True
            if database_manager.read_debug_is_enabled():
                value_cache_database_manager.write_debug_snapshot_execution_timestamp_start(
                    label=callback
                )
                result = callback(
                    self,
                    *args,
                    **kwargs,
                )
                value_cache_database_manager.write_debug_snapshot_execution_timestamp_complete(
                    label=callback
                )
                log_manager.log_debug_snapshot_execution(
                    callback=callback
                )
            else:
                result = callback(
                    self,
                    *args,
                    **kwargs,
                )

            if not result:
                log_manager.log_debug_method_interrupted(
                    reference=callback
                )
                return result

            log_manager.log_debug_method_complete(
                reference=callback
            )

            return result

        return wrapper

    @staticmethod
    def multi_task_decorator(
        callback: Callable[P, R],
    ) -> Any:
        _handle_dynamic_imports()

        @wraps(callback)
        def wrapper(
            self: Any,
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> Any:
            log_manager = (
                _ImportManager.read_singleton(
                    _LogManager
                )
            )
            database_manager = (
                _ImportManager.read_singleton(
                    _DatabaseManager
                )
            )
            value_cache_database_manager = (
                _ImportManager.read_singleton(
                    _ValueCacheDatabaseManager
                )
            )

            log_manager.log_debug_method_start(
                reference=callback
            )

            result: Any = True
            if database_manager.read_debug_is_enabled():
                value_cache_database_manager.write_debug_snapshot_execution_timestamp_start(
                    label=callback
                )
                result = callback(
                    self,
                    *args,
                    **kwargs,
                )
                value_cache_database_manager.write_debug_snapshot_execution_timestamp_complete(
                    label=callback
                )
                log_manager.log_debug_snapshot_execution(
                    callback=callback
                )
            else:
                result = callback(
                    self,
                    *args,
                    **kwargs,
                )

            if not result:
                log_manager.log_debug_method_interrupted(
                    reference=callback
                )
                return result


            log_manager.log_debug_method_complete(
                reference=callback
            )

            return result

        return wrapper
