from __future__ import annotations

from typing import Any

__all__ = (
    "CommandWorkflowManager"
)

_TaskManager: Any = None
_ImportManager: Any = None
_DisplayManager: Any = None
_DatabaseManager: Any = None
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

class CommandWorkflowManager:
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

        self._command_storage_manager = _ImportManager.get_singleton(
            _CommandStorageManager
        )

        self._display_manager = (
            _ImportManager.get_singleton(
                _DisplayManager
            )
        )
        self._task_manager = (
            _ImportManager.get_singleton(
                _TaskManager
            )
        )
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

        self._command_storage_manager.add_commands((
            (
                self._task_manager.setup_command_name("workflow_run"),
                self.run_command_workflow_run,
            ),
            (
                self._task_manager.setup_command_name("workflow_list_selections"),
                self.run_command_workflow_list_selections,
            ),
        ))

    def run_command_workflow_run(
        self,
        **kwargs: Any
    ) -> bool:
        return True

    def run_command_workflow_list_selections(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()    
        self._task_manager.run_task_workflow_setup()

        value = {}
        workflow_selection = (
            self._value_cache_database_manager.read_workflow_selection()
        ) or {}
        if workflow_selection:
            value["selections"] = workflow_selection

        if not value:
            return False

        maximum_depth = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_display_console_style_maximum_depth_value()
        )
        is_skipped = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_display_console_style_is_skipped_value()
        )
        indent_count = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_display_console_style_indent_count_value()
        )
        vertical_space_count = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_display_console_style_vertical_count_value()
        )
        self._display_manager.display_tree_object(
            value=value,
            maximum_depth=maximum_depth,
            is_skipped=is_skipped,
            indent_count=indent_count,
            vertical_space_count=vertical_space_count,
        )

        return True
