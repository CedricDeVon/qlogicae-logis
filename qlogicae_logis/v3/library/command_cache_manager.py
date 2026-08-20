from __future__ import annotations

from typing import Any

__all__ = (
    "CommandCacheManager"
)

_TaskManager: Any = None
_ImportManager: Any = None
_DatabaseManager: Any = None
_CommandStorageManager: Any = None


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _TaskManager
    global _ImportManager
    global _DatabaseManager
    global _CommandStorageManager

    from ..library import (
        command_storage_manager,
        database_manager,
        import_manager,
        task_manager,
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
    _CommandStorageManager = (
        command_storage_manager
            .CommandStorageManager
    )

    _handle_dynamic_imports = lambda: None

class CommandCacheManager:
    __slots__ = (
        "_command_storage_manager",
        "_task_manager",
        "_import_manager",
        "_database_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._command_storage_manager = _ImportManager.get_singleton(
            _CommandStorageManager
        )

        self._task_manager = (
            _ImportManager.get_singleton(
                _TaskManager
            )
        )

        self._database_manager = (
            _ImportManager.get_singleton(
                _DatabaseManager
            )
        )

        self._import_manager = (
            _ImportManager.get_singleton(
                _ImportManager
            )
        )

        self._command_storage_manager.add_commands((
            (
                self._task_manager.setup_command_name("cache_view_disk"),
                self.run_command_cache_view_disk,
            ),
            (
                self._task_manager.setup_command_name("cache_view_value"),
                self.run_command_cache_view_value,
            ),
            (
                self._task_manager.setup_command_name("cache_clear_disk"),
                self.run_command_cache_clear_disk,
            ),
            (
                self._task_manager.setup_command_name("cache_clear_value"),
                self.run_command_cache_clear_value,
            ),
        ))

    def run_command_cache_view_disk(self, **kwargs: Any) -> bool:
        print(kwargs)

        return True

    def run_command_cache_view_value(self, **kwargs: Any) -> bool:
        print(kwargs)

        return True

    def run_command_cache_clear_disk(self, **kwargs: Any) -> bool:
        self._task_manager.run_task_full_debug_disk_cache()

        self._import_manager.clean_filesystem_path(
            path=(
                self._database_manager
                    .read_default_cache_disk_output_folder_path()
            )
        )

        return True

    def run_command_cache_clear_value(self, **kwargs: Any) -> bool:
        self._import_manager.clear_all_values_via_value_cache()

        return True

