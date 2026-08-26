from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from typing import Any, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

__all__ = (
    "DecoratorManager"
)

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports

    _handle_dynamic_imports = lambda: None


class DecoratorManager:
    __slots__ = ()

    def __init__(self) -> None:
        pass

    @staticmethod
    def single_use_method_decorator(
        callback: Callable[P, R],
    ) -> Any:
        _handle_dynamic_imports()

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
        _handle_dynamic_imports()

        @wraps(callback)
        def wrapper(
            self: Any,
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> Any:
            if self._database_manager.read_debug_is_enabled():
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
                message = (
                    f"{callback} - "
                    f"{
                        self._value_cache_database_manager
                            .read_debug_snapshot_execution(label=callback)
                    }"
                )
                self._import_manager.log_cache_debug_to_file(
                    message=message
                )
            else:
                result = callback(
                    self,
                    *args,
                    **kwargs,
                )

            return result

        return wrapper

    @staticmethod
    def log_method_decorator(
        callback: Callable[P, R],
    ) -> Any:
        _handle_dynamic_imports()

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
        _handle_dynamic_imports()

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

            result: Any = True
            if self._database_manager.read_debug_is_enabled():
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
                message = (
                    f"{callback} - "
                    f"{
                        self._value_cache_database_manager
                            .read_debug_snapshot_execution(label=callback)
                    }"
                )
                self._import_manager.log_cache_debug_to_file(
                    message=message
                )
            else:
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
            self._import_manager.log_cache_info_to_file(
                message=f"{callback} - start"
            )

            result: Any = True
            if self._database_manager.read_debug_is_enabled():
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
                message = (
                    f"{callback} - "
                    f"{
                        self._value_cache_database_manager
                            .read_debug_snapshot_execution(label=callback)
                    }"
                )
                self._import_manager.log_cache_debug_to_file(
                    message=message
                )
            else:
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
            self._import_manager.log_cache_info_to_file(
                message=f"{callback} - start"
            )

            result: Any = True
            if self._database_manager.read_debug_is_enabled():
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
                message = (
                    f"{callback} - "
                    f"{
                        self._value_cache_database_manager
                            .read_debug_snapshot_execution(label=callback)
                    }"
                )
                self._import_manager.log_cache_debug_to_file(
                    message=message
                )
            else:
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
