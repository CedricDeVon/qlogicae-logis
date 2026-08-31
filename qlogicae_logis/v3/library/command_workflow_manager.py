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
                self._command_storage_manager
                    .read_command_name("workflow_run"),
                self.run_command_workflow_run,
            ),
            (
                self._command_storage_manager
                    .read_command_name("workflow_list_selections"),
                self.run_command_workflow_list_selections,
            ),
        ))

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
                self._value_cache_database_manager
                    .read_object_is_enabled_value(
                        workflow_selection
                    )
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
                self._value_cache_database_manager
                    .read_object_scripts(
                        workflow_selection
                    )
            )
            workflow_selection_delay_value = (
                self._value_cache_database_manager
                    .read_object_delay_value(
                        workflow_selection
                    )
            )
            workflow_selection_delay_value = (
                workflow_selection_delay_value
                if workflow_selection_delay_value >= 0
                else 0
            )
            workflow_selection_is_atomic_value = (
                self._value_cache_database_manager
                    .read_object_is_atomic_value(
                        workflow_selection
                    )
            )
            workflow_selection_filesystem_path_value = (
                self._value_cache_database_manager
                    .read_object_filesystem_path_value(
                        workflow_selection
                    )
            )
            if not workflow_selection_filesystem_path_value:
                workflow_selection_filesystem_path_value = (
                    root_filesystem_path
                )


            self._import_manager.time_delay(
                value=workflow_selection_delay_value
            )

            self._task_manager.navigate_via_filesystem_path(
                workflow_selection_filesystem_path_value
            )

            for workflow_selection_script in workflow_selection_scripts:
                if not workflow_selection_script:
                    continue

                workflow_selection_script_is_enabled_value = (
                    self._value_cache_database_manager
                        .read_object_is_enabled_value(
                            workflow_selection_script
                        )
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
                    self._value_cache_database_manager
                        .read_object_run_value(
                            workflow_selection_script
                        )
                )
                if not workflow_selection_script_run_value:
                    continue

                workflow_selection_script_process_value = (
                    self._value_cache_database_manager
                        .read_object_process_value(
                            workflow_selection_script
                        )
                )

                workflow_selection_script_argument = (
                    self._value_cache_database_manager
                        .read_object_argument(
                            workflow_selection_script
                        )
                )

                workflow_selection_script_delay_value = (
                    self._value_cache_database_manager
                        .read_object_delay_value(
                            workflow_selection_script
                        )
                )
                workflow_selection_script_delay_value = (
                    workflow_selection_script_delay_value
                    if workflow_selection_script_delay_value >= 0
                    else 0
                )
                workflow_selection_script_filesystem_path_value = (
                    self._value_cache_database_manager
                        .read_object_filesystem_path_value(
                            workflow_selection_script
                        )
                )
                if not workflow_selection_script_filesystem_path_value:
                    workflow_selection_script_filesystem_path_value = (
                        workflow_selection_filesystem_path_value
                    )

                self._import_manager.time_delay(
                    value=workflow_selection_script_delay_value
                )

                self._task_manager.navigate_via_filesystem_path(
                    workflow_selection_script_filesystem_path_value
                )

                cli_output_returncode: Any = 0
                if workflow_selection_script_run_value in commands:
                    cli_output_returncode = (
                        commands[workflow_selection_script_run_value](**workflow_selection_script_argument)
                    )
                    if (
                        not cli_output_returncode and
                        workflow_selection_is_atomic_value
                    ):
                        return False

                elif workflow_selection_script_run_value in data_workflow_selections:
                    cli_output_returncode = (
                        handle_workflow_run_target(
                            workflow_selection_script_run_value
                        )
                    )
                    if (
                        not cli_output_returncode and
                        workflow_selection_is_atomic_value
                    ):
                        return False

                else:
                    cli_output = (
                        self._import_manager.run_command(
                            script_process=workflow_selection_script_process_value,
                            command=workflow_selection_script_run_value,
                        )
                    )
                    self._import_manager.log_cache_info_to_file(
                        message=f"{cli_output}"
                    )
                    cli_output_returncode = (
                        getattr(cli_output, "returncode", None)
                    )
                    if (
                        cli_output_returncode and
                        workflow_selection_is_atomic_value
                    ):
                        return False

            return True

        self._task_manager.run_task_common_setup()
        self._task_manager.run_task_workflow_setup()
        self._task_manager.run_task_filesystem_clean_exclude_setup()
        self._task_manager.run_task_filesystem_clean_include_setup()

        if not kwargs:
            self._import_manager.log_cache_warning_to_file(
                message="invalid arguments"
            )
            return False

        targets = kwargs.get('targets', [])
        if not targets or len(targets) < 1:
            self._import_manager.log_cache_warning_to_file(
                message="no targets selected"
            )
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

        for target in targets:
            if not target or target not in data_workflow_selections:
                self._import_manager.log_cache_warning_to_file(
                    message=f"'{target}' is not a valid workflow"
                )
                continue

            handle_workflow_run_target(
                data_workflow_selections[target]
            )

        return True

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
