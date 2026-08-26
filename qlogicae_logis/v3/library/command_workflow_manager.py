from __future__ import annotations

from typing import Any

from ..library.decorator_manager import DecoratorManager

__all__ = (
    "CommandWorkflowManager"
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
                self._task_manager.setup_command_name("workflow_run"),
                self.run_command_workflow_run,
            ),
            (
                self._task_manager.setup_command_name("workflow_list_selections"),
                self.run_command_workflow_list_selections,
            ),
        ))

    @_DecoratorManager.command_decorator
    def run_command_workflow_run(
        self,
        **kwargs: Any
    ) -> bool:
        # def handle_workflow_run_target(target: str) -> bool:
        #     return True

        # self._task_manager.run_task_common_setup()
        # self._task_manager.run_task_workflow_setup()
        # self._task_manager.run_task_filesystem_clean_exclude_setup()
        # self._task_manager.run_task_filesystem_clean_include_setup()

        # targets = kwargs.get('targets', [])
        # if len(targets) < 1:
        #     return False

        # root_filesystem_path = (
        #     self._value_cache_database_manager
        #         .read_root_filesystem_path()
        # )
        # commands = (
        #     self._command_storage_manager
        #         .read_commands()
        # )
        # workspace_data_workflow = (
        #     self._value_cache_database_manager
        #         .read_configuration_workspace_data_workflow_selection()
        # )
        # workflow_selections = (
        #     self._value_cache_database_manager
        #         .read_workflow_selection()
        # )

        # for target in targets:
        #     if not target or target not in workflow_selections:
        #         continue

        #     handle_workflow_run_target(
        #         workspace_data_workflow[target]
        #     )

        return True

    @_DecoratorManager.command_decorator
    def run_command_workflow_list_selections(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()
        self._task_manager.run_task_workflow_setup()

        value = {}
        workflow_selections = (
            self._value_cache_database_manager
                .read_workflow_selection()
        ) or {}
        if workflow_selections:
            value["selections"] = workflow_selections

        if not value:
            return False

        self._display_manager.display_tree_object(
            value=value,
        )

        return True
