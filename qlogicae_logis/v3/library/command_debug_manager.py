from __future__ import annotations

from typing import Any

from ..library.decorator_manager import DecoratorManager

__all__ = (
    "CommandDebugManager"
)

_TaskManager: Any = None
_ImportManager: Any = None
_DisplayManager: Any = None
_DatabaseManager: Any = None
_CommandStorageManager: Any = None
_ValueCacheDatabaseManager: Any = None
_PersistentCacheDatabasManager: Any = None
_DecoratorManager = DecoratorManager


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _TaskManager
    global _ImportManager
    global _DisplayManager
    global _DatabaseManager
    global _CommandStorageManager
    global _ValueCacheDatabaseManager
    global _PersistentCacheDatabasManager


    from ..library import (
        command_storage_manager,
        database_manager,
        display_manager,
        import_manager,
        persistent_cache_database_manager,
        task_manager,
        value_cache_database_manager,
    )

    _TaskManager = (
        task_manager
            .TaskManager
    )
    _ImportManager = (
        import_manager
            .ImportManager
    )
    _DatabaseManager = (
        database_manager.DatabaseManager
    )
    _DisplayManager = (
        display_manager.DisplayManager
    )
    _ValueCacheDatabaseManager = (
        value_cache_database_manager.ValueCacheDatabaseManager
    )
    _CommandStorageManager = (
        command_storage_manager
            .CommandStorageManager
    )
    _PersistentCacheDatabasManager = (
        persistent_cache_database_manager.PersistentCacheDatabasManager
    )

    _handle_dynamic_imports = lambda: None

class CommandDebugManager:
    __slots__ = (
        "_command_storage_manager",
        "_task_manager",
        "_import_manager",
        "_database_manager",
        "_value_cache_database_manager",
        "_display_manager",
        "_persistent_cache_database_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._command_storage_manager = _ImportManager.read_singleton(
            _CommandStorageManager
        )

        self._database_manager = (
            _ImportManager.read_singleton(
                _DatabaseManager
            )
        )
        self._task_manager = (
            _ImportManager.read_singleton(
                _TaskManager
            )
        )
        self._import_manager = (
            _ImportManager.read_singleton(
                _ImportManager
            )
        )
        self._value_cache_database_manager = (
            _ImportManager.read_singleton(
                _ValueCacheDatabaseManager
            )
        )
        self._display_manager = (
            _ImportManager.read_singleton(
                _DisplayManager
            )
        )
        self._persistent_cache_database_manager = (
            _ImportManager.read_singleton(
                _PersistentCacheDatabasManager
            )
        )

        self._command_storage_manager.add_commands((
            (
                self._command_storage_manager
                    .read_command_name("debug_view_value_cache"),
                self.run_command_debug_view_value_cache,
            ),
            (
                self._command_storage_manager
                    .read_command_name("debug_view_disk_cache"),
                self.run_command_debug_view_disk_cache,
            ),
        ))

    @_DecoratorManager.command_decorator
    def run_command_debug_view_value_cache(self, **kwargs: Any) -> bool:
        self._task_manager.run_task_full_debug_value_cache_setup()

        key_paths = kwargs.get("key_paths", [])

        if len(key_paths) < 1:
            self._display_manager.display_tree_object(
                value=self._value_cache_database_manager.read_any_value(
                    tuple()
                ),
            )

        else:
            for target in key_paths:
                if not target:
                    continue

                self._display_manager.display_tree_object(
                    value=self._value_cache_database_manager.read_any_value(
                        tuple(target.split("."))
                    ),
                )

        return True

    @_DecoratorManager.command_decorator
    def run_command_debug_view_disk_cache(self, **kwargs: Any) -> bool:
        self._task_manager.run_task_full_debug_disk_cache_setup()

        value = self._persistent_cache_database_manager.read_all_values()

        self._display_manager.display_tree_object(
            value=value,
        )

        return True


