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

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _ImportManager
    global _DatabaseManager
    global _TaskStorageManager
    global _ValueCacheDatabaseManager

    from ..library import (
        database_manager,
        import_manager,
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
            import_manager = (
                _ImportManager.read_singleton(
                    _ImportManager
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

            if task_storage_manager.is_executed(label=callback):
                return True

            import_manager.log_cache_info_to_file(
                message=f"{callback} - start"
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
                message = (
                    f"{callback} - "
                    f"{
                        value_cache_database_manager
                            .read_debug_snapshot_execution(label=callback)
                    }"
                )
                import_manager.log_cache_debug_to_file(
                    message=message
                )
            else:
                result = callback(
                    self,
                    *args,
                    **kwargs,
                )

            if not result:
                import_manager.log_cache_info_to_file(
                    message=f"{callback} - skip"
                )
                return result


            import_manager.log_cache_info_to_file(
                message=f"{callback} - complete"
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
            import_manager = (
                _ImportManager.read_singleton(
                    _ImportManager
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

            import_manager.log_cache_info_to_file(
                message=f"{callback} - start"
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
                message = (
                    f"{callback} - "
                    f"{
                        value_cache_database_manager
                            .read_debug_snapshot_execution(
                                label=callback
                            )
                    }"
                )
                import_manager.log_cache_debug_to_file(
                    message=message
                )
            else:
                result = callback(
                    self,
                    *args,
                    **kwargs,
                )

            if not result:
                import_manager.log_cache_info_to_file(
                    message=f"{callback} - skip"
                )
                return result


            import_manager.log_cache_info_to_file(
                message=f"{callback} - complete"
            )

            return result

        return wrapper

    @staticmethod
    def command_decorator(
        callback: Callable[P, R],
    ) -> Any:
        _handle_dynamic_imports()

        @wraps(callback)
        def wrapper(
            self: Any,
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> Any:
            import_manager = (
                _ImportManager.read_singleton(
                    _ImportManager
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

            import_manager.log_cache_info_to_file(
                message=f"{callback} - start"
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
                message = (
                    f"{callback} - "
                    f"{
                        value_cache_database_manager
                            .read_debug_snapshot_execution(label=callback)
                    }"
                )
                import_manager.log_cache_debug_to_file(
                    message=message
                )
            else:
                result = callback(
                    self,
                    *args,
                    **kwargs,
                )

            if not result:
                import_manager.log_cache_info_to_file(
                    message=f"{callback} - skip"
                )
                return result


            import_manager.log_cache_info_to_file(
                message=f"{callback} - complete"
            )

            return result

        return wrapper
