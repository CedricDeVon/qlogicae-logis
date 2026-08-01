from __future__ import annotations

from typing import Any

# if TYPE_CHECKING:
#     pass

_SingletonManager: Any = None
_ValueCacheManager: Any = None
_ConsoleDatabaseManager: Any = None
_ConsoleSystemManager: Any = None
_SystemManager: Any = None
_TimeManager: Any = None
_TargetCacheValue: Any = None
_Path: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _SingletonManager
    global _ValueCacheManager
    global _ConsoleDatabaseManager
    global _ConsoleSystemManager
    global _SystemManager
    global _TimeManager
    global _TargetCacheValue
    global _Path

    from pathlib import Path

    from qlogicae_cor.v1.library import (
        singleton_manager,
        system_manager,
        target_cache_value,
        time_manager,
        value_cache_manager,
    )

    from qlogicae_logis.v2.library import (
        console_database_manager,
        console_system_manager,
    )

    _Path = Path
    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _ValueCacheManager = (
        value_cache_manager.ValueCacheManager
    )
    _ConsoleDatabaseManager = (
        console_database_manager.ConsoleDatabaseManager
    )
    _ConsoleSystemManager = (
        console_system_manager.ConsoleSystemManager
    )
    _SystemManager = (
        system_manager.SystemManager
    )
    _TimeManager = (
        time_manager.TimeManager
    )
    _TargetCacheValue = (
        target_cache_value.TargetCacheValue
    )

    _handle_dynamic_imports = lambda: None


class ConsoleTaskManager:
    __slots__ = ("_tasks")

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._tasks: dict[str, Any] = {
            "task_handle_timestamp_console_execution_start_setup":
                self.handle_timestamp_console_execution_start_setup,
            "task_handle_current_root_workspace_filesystem_paths_setup":
                self.handle_current_root_workspace_filesystem_paths_setup,
            "task_handle_executing_console_filesystem_paths_setup":
                self.handle_executing_console_filesystem_paths_setup,
            "task_handle_navigate_to_root_workspace":
                self.handle_navigate_to_root_workspace,
            "task_handle_navigate_to_filesystem_path":
                self.handle_navigate_to_filesystem_path,
            "task_handle_timestamp_console_execution_end_setup":
                self.handle_timestamp_console_execution_end_setup,
        }

    @property
    def tasks(self) -> dict[str, Any]:
        return self._tasks

    def handle_shutdown(self) -> bool:
        return True

    def handle_value_cache(self) -> bool:
        self.handle_timestamp_console_execution_start_setup()

        self.handle_current_root_workspace_filesystem_paths_setup()
        self.handle_executing_console_filesystem_paths_setup()
        self.handle_navigate_to_root_workspace()

        self.handle_timestamp_console_execution_end_setup()

        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).display_all_items()

        return True

    def handle_timestamp_console_execution_start_setup(
        self,
    ) -> bool:
        _SingletonManager.get_singleton(
            _ConsoleDatabaseManager
        ).setup_timestamp_setup_execution_start()

        return True

    def handle_timestamp_console_execution_end_setup(
        self,
    ) -> bool:
        _SingletonManager.get_singleton(
            _ConsoleDatabaseManager
        ).setup_timestamp_setup_execution_complete()

        return True

    def handle_current_root_workspace_filesystem_paths_setup(
        self,
    ) -> bool:
        _SingletonManager.get_singleton(
            _ConsoleDatabaseManager
        ).setup_current_root_workspace_filesystem_path()

        return True

    def handle_executing_console_filesystem_paths_setup(
        self,
    ) -> bool:
        _console_database_manager = _SingletonManager.get_singleton(
            _ConsoleDatabaseManager
        )
        _console_system_manager = _SingletonManager.get_singleton(
            _ConsoleSystemManager
        )

        _console_database_manager.current_executing_script_filesystem_path = (
            _console_system_manager.current_executing_script_filesystem_path
        )
        _console_database_manager.initial_executing_console_filesystem_path = (
            _console_database_manager.current_root_workspace_filesystem_path
        )
        _console_database_manager.previous_executing_console_filesystem_path = (
            _console_database_manager.initial_executing_console_filesystem_path
        )
        _console_database_manager.current_executing_console_filesystem_path = (
            _console_database_manager.initial_executing_console_filesystem_path
        )

        return True

    def handle_navigate_to_root_workspace(
        self,
    ) -> bool:
        _console_database_manager = _SingletonManager.get_singleton(
            _ConsoleDatabaseManager
        )

        self.handle_navigate_to_filesystem_path(
            _console_database_manager.current_root_workspace_filesystem_path
        )

        return True

    def handle_navigate_to_filesystem_path(
        self,
        filesystem_path: str
    ) -> bool:
        _console_database_manager = _SingletonManager.get_singleton(
            _ConsoleDatabaseManager
        )
        _system_manager = _SingletonManager.get_singleton(
            _SystemManager
        )

        _console_database_manager.previous_executing_console_filesystem_path = (
            _console_database_manager.current_executing_console_filesystem_path
        )
        _console_database_manager.current_executing_console_filesystem_path = (
            filesystem_path
        )
        _system_manager.current_executing_console_filesystem_path = (
            filesystem_path
        )

        return True

