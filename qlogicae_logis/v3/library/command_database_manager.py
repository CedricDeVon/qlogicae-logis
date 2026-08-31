from __future__ import annotations

from typing import Any

from .decorator_manager import DecoratorManager

__all__ = (
    "CommandDatabaseManager"
)

_TaskManager: Any = None
_ImportManager: Any = None
_DisplayManager: Any = None
_DatabaseManager: Any = None
_DecoratorManager = DecoratorManager
_CommandStorageManager: Any = None
_ValueCacheDatabaseManager: Any = None
_PersistentCacheDatabasManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _TaskManager
    global _ImportManager
    global _DisplayManager
    global _CommandStorageManager
    global _DatabaseManager
    global _ValueCacheDatabaseManager
    global _PersistentCacheDatabasManager

    from . import (
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
    _DisplayManager = (
        display_manager.DisplayManager
    )
    _DatabaseManager = (
        database_manager.DatabaseManager
    )
    _ValueCacheDatabaseManager = (
        value_cache_database_manager.ValueCacheDatabaseManager
    )
    _PersistentCacheDatabasManager = (
        persistent_cache_database_manager.PersistentCacheDatabasManager
    )
    _ImportManager = (
        import_manager
            .ImportManager
    )
    _CommandStorageManager = (
        command_storage_manager
            .CommandStorageManager
    )

    _handle_dynamic_imports = lambda: None

class CommandDatabaseManager:
    __slots__ = (
        "_command_storage_manager",
        "_task_manager",
        "_import_manager",
        "_display_manager",
        "_database_manager",
        "_value_cache_database_manager",
        "_persistent_cache_database_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._command_storage_manager = _ImportManager.read_singleton(
            _CommandStorageManager
        )
        self._display_manager = (
            _ImportManager.read_singleton(
                _DisplayManager
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
        self._persistent_cache_database_manager = (
            _ImportManager.read_singleton(
                _PersistentCacheDatabasManager
            )
        )
        self._command_storage_manager.add_commands((
            (
                self._command_storage_manager
                    .read_command_name("cache_view_disk"),
                self.run_command_database_view_disk,
            ),
            (
                self._command_storage_manager
                    .read_command_name("cache_view_value"),
                self.run_command_database_view_value,
            ),
            (
                self._command_storage_manager
                    .read_command_name("cache_clear_disk"),
                self.run_command_database_clear_disk,
            ),
            (
                self._command_storage_manager
                    .read_command_name("cache_clear_value"),
                self.run_command_database_clear_value,
            ),
        ))

    def run_command_database_view_disk(self, **kwargs: Any) -> bool:
        if not kwargs:
            self._import_manager.log_cache_warning_to_file(
                message="invalid arguments"
            )
            return False

        self._task_manager.run_task_full_debug_disk_cache_setup()

        key_paths = kwargs.get("key_paths", []) or []
        values = self._persistent_cache_database_manager.read_all_values()

        if len(key_paths) < 1:
            self._display_manager.display_tree_object(
                value=values,
            )

        else:
            for target in key_paths:
                if not target:
                    continue

                for value in values:
                    if not value:
                        continue

                    if value["key"] == target:
                        self._display_manager.display_tree_object(
                            value=value
                        )

        return True

    def run_command_database_view_value(self, **kwargs: Any) -> bool:
        if not kwargs:
            self._import_manager.log_cache_warning_to_file(
                message="invalid arguments"
            )
            return False

        key_paths = kwargs.get("key_paths", []) or []

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

    def run_command_database_clear_disk(self, **kwargs: Any) -> bool:
        self._task_manager.run_task_full_debug_disk_cache_setup()

        target_path = (
            self._database_manager
                .read_default_cache_disk_output_folder_path()
        ) or ""
        if not target_path:
            return False

        self._import_manager.clean_filesystem_paths(
            target_paths=(
                target_path,
            )
        )

        return True

    def run_command_database_clear_value(self, **kwargs: Any) -> bool:
        self._import_manager.clear_all_values_via_value_cache()

        return True

