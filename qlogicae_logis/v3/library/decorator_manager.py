from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from typing import Any, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


__all__ = (
    "DecoratorManager"
)

_ImportManager: Any = None
_DatabaseManager: Any = None
_TaskStorageManager: Any = None
_ValueCacheDatabaseManager: Any = None
_PersistentCacheDatabasManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _ImportManager
    global _DatabaseManager
    global _TaskStorageManager
    global _ValueCacheDatabaseManager
    global _PersistentCacheDatabasManager

    from ..library import (
        database_manager,
        import_manager,
        persistent_cache_database_manager,
        task_storage_manager,
        value_cache_database_manager,
    )

    _ImportManager = (
        import_manager.ImportManager
    )
    _DatabaseManager = (
        database_manager.DatabaseManager
    )
    _ValueCacheDatabaseManager = (
        value_cache_database_manager.ValueCacheDatabaseManager
    )
    _TaskStorageManager = (
        task_storage_manager.TaskStorageManager
    )
    _PersistentCacheDatabasManager = (
        persistent_cache_database_manager.PersistentCacheDatabasManager
    )

    _handle_dynamic_imports = lambda: None


class DecoratorManager:
    __slots__ = (
        "_import_manager",
        "_database_manager",
        "_task_storage_manager",
        "_value_cache_database_manager",
        "_persistent_cache_database_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._import_manager = (
            _ImportManager.get_singleton(
                _ImportManager
            )
        )
        self._database_manager = (
            _ImportManager.get_singleton(
                _DatabaseManager
            )
        )
        self._value_cache_database_manager = (
            _ImportManager.get_singleton(
                _ValueCacheDatabaseManager
            )
        )
        self._persistent_cache_database_manager = (
            _ImportManager.get_singleton(
                _PersistentCacheDatabasManager
            )
        )
        self._task_storage_manager = (
            _ImportManager.get_singleton(
                _TaskStorageManager
            )
        )

    @staticmethod
    def single_use_method_decorator(
        callback: Callable[P, R],
    ) -> Any:
        @wraps(callback)
        def wrapper(
            self: Any,
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> Any:
            if self._task_storage_manager.is_executed(label=callback):
                return True

            result = callback(
                self,
                *args,
                **kwargs,
            )

            return result

        return wrapper

    @staticmethod
    def debug_method_decorator(
        callback: Callable[P, R],
    ) -> Any:
        @wraps(callback)
        def wrapper(
            self: Any,
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> Any:
            self._value_cache_database_manager.write_debug_snapshot_execution_timestamp_start(
                label=callback
            )

            result = callback(
                self,
                *args,
                **kwargs,
            )

            self._value_cache_database_manager.write_debug_snapshot_execution_timestamp_complete(
                label=callback
            )

            return result

        return wrapper

    @staticmethod
    def log_method_decorator(
        callback: Callable[P, R],
    ) -> Any:
        @wraps(callback)
        def wrapper(
            self: Any,
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> Any:
            self._import_manager.log_cache_info_to_file(
                message=f"{callback} - start"
            )

            result = callback(
                self,
                *args,
                **kwargs,
            )
            if not result:
                self._import_manager.log_cache_info_to_file(
                    message=f"{callback} - skip"
                )
                return result

            self._import_manager.log_cache_info_to_file(
                message=f"{callback} - complete"
            )

            return result

        return wrapper

    @staticmethod
    def single_task_decorator(
        callback: Callable[P, R],
    ) -> Any:
        @wraps(callback)
        def wrapper(
            self: Any,
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> Any:
            if self._task_storage_manager.is_executed(label=callback):
                return True

            self._import_manager.log_cache_info_to_file(
                message=f"{callback} - start"
            )

            self._value_cache_database_manager.write_debug_snapshot_execution_timestamp_start(
                label=callback
            )
            result = callback(
                self,
                *args,
                **kwargs,
            )
            self._value_cache_database_manager.write_debug_snapshot_execution_timestamp_complete(
                label=callback
            )

            if not result:
                self._import_manager.log_cache_info_to_file(
                    message=f"{callback} - skip"
                )
                return result


            self._import_manager.log_cache_info_to_file(
                message=f"{callback} - complete"
            )

            return result

        return wrapper

    @staticmethod
    def multi_task_decorator(
        callback: Callable[P, R],
    ) -> Any:
        @wraps(callback)
        def wrapper(
            self: Any,
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> Any:
            self._import_manager.log_cache_info_to_file(
                message=f"{callback} - start"
            )

            self._value_cache_database_manager.write_debug_snapshot_execution_timestamp_start(
                label=callback
            )
            result = callback(
                self,
                *args,
                **kwargs,
            )
            self._value_cache_database_manager.write_debug_snapshot_execution_timestamp_complete(
                label=callback
            )

            if not result:
                self._import_manager.log_cache_info_to_file(
                    message=f"{callback} - skip"
                )
                return result


            self._import_manager.log_cache_info_to_file(
                message=f"{callback} - complete"
            )

            return result

        return wrapper
