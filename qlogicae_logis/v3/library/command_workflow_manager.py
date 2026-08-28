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
        def handle_workflow_run_target(
            workflow_target: str
        ) -> bool:
            if not workflow_target:
                return False

            workflow_selection = (
                data_workflow.get(
                    workflow_target,
                    {}
                )
            )

            if not workflow_selection:
                return False

            workflow_selection_data_is_enabled_value = (
                workflow_selection
                    .get("is-enabled", {})
                    .get("value", True)
            )
            if not workflow_selection_data_is_enabled_value:
                return False

            is_operating_system_included = (
                self._value_cache_database_manager
                    .read_is_object_operating_system_included(
                        workflow_selection
                    )
            )
            if not is_operating_system_included:
                return False

            workflow_selection_scripts = (
                workflow_selection
                    .get("scripts", {})
            )
            workflow_selection_delay_value = (
                workflow_selection
                    .get("delay", {})
                    .get("value", 0)
            )
            workflow_selection_delay_value = (
                workflow_selection_delay_value
                if workflow_selection_delay_value >= 0
                else 0
            )
            workflow_selection_is_atmoic_value = (
                workflow_selection
                    .get("is-atmoic", {})
                    .get("value", False)
            )
            workflow_selection_filesystem_path_value = (
                workflow_selection
                    .get("filesystem-path", {})
                    .get("value", root_filesystem_path)
            )

            self._import_manager.time_delay(
                value=workflow_selection_delay_value
            )

            for workflow_selection_script in workflow_selection_scripts:
                if not workflow_selection_script:
                    continue

                workflow_selection_script_is_enabled_value = (
                    workflow_selection_script
                        .get("is-enabled", {})
                        .get("value", True)
                )
                if not workflow_selection_script_is_enabled_value:
                    continue

                workflow_selection_script_is_operating_system_included = (
                    self._value_cache_database_manager
                        .read_is_object_operating_system_included(
                            workflow_selection_script
                        )
                )
                if not workflow_selection_script_is_operating_system_included:
                    continue

                workflow_selection_script_run_value = (
                    workflow_selection_script
                        .get("run", {})
                        .get("value", "")
                )
                if not workflow_selection_script_run_value:
                    continue

                workflow_selection_script_process_value = (
                    workflow_selection_script
                        .get("process", {})
                        .get("value", "shell")
                )

                workflow_selection_script_argument = (
                    workflow_selection_script
                        .get("argument", {})
                )

                workflow_selection_script_delay_value = (
                    workflow_selection_script
                        .get("delay", {})
                        .get("value", 0)
                )
                workflow_selection_script_delay_value = (
                    workflow_selection_script_delay_value
                    if workflow_selection_script_delay_value >= 0
                    else 0
                )

                self._import_manager.time_delay(
                    value=workflow_selection_script_delay_value
                )

                self._task_manager.navigate_via_filesystem_path(
                    workflow_selection_filesystem_path_value
                )

                if workflow_selection_script_run_value in commands:
                    commands[workflow_selection_script_run_value](**workflow_selection_script_argument)

                elif workflow_selection_script_run_value in data_workflow_selections:
                    handle_workflow_run_target(
                        workflow_selection_script_run_value
                    )

                else:
                    cli_output = {}
                    if workflow_selection_script_process_value == "shell":
                        cli_output = self._import_manager.run_shell_command(
                            command=workflow_selection_script_run_value
                        )

                    elif workflow_selection_script_process_value == "subprocess":
                        cli_output = self._import_manager.run_subprocess_command(
                            command=workflow_selection_script_run_value
                        )

            return True

        self._task_manager.run_task_common_setup()
        self._task_manager.run_task_workflow_setup()
        self._task_manager.run_task_filesystem_clean_exclude_setup()
        self._task_manager.run_task_filesystem_clean_include_setup()

        targets = kwargs.get('targets', [])
        if not targets or len(targets) < 1:
            return False

        root_filesystem_path = (
            self._value_cache_database_manager
                .read_root_filesystem_path()
        )
        commands = (
            self._command_storage_manager
                .read_commands()
        )
        data_workflow = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_workflow_selection()
        )
        data_workflow_selections = (
            self._value_cache_database_manager
                .read_workflow_selection()
        )
        workflow_selections = (
            self._database_manager
                .read_object_selection_origins(
                    data_workflow_selections
                )
        )

        for target in targets:
            if not target or target not in data_workflow_selections:
                continue

            handle_workflow_run_target(
                data_workflow_selections[target]
            )

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
