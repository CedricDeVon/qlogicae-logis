from __future__ import annotations

from typing import Any

_time: Any = None
_LogManager: Any = None
_SystemManager: Any = None
_DatabaseManager: Any = None
_SingletonManager: Any = None
_EnumConversionValue: Any = None
_ScriptProcessManager: Any = None
_CommandStorageManager: Any = None
_ConsoleDisplayManager: Any = None
_CommandUtilityManager: Any = None
_ScriptProcessEnumManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _time
    global _LogManager
    global _SystemManager
    global _DatabaseManager
    global _SingletonManager
    global _EnumConversionValue
    global _ScriptProcessManager
    global _CommandStorageManager
    global _ConsoleDisplayManager
    global _CommandUtilityManager
    global _ScriptProcessEnumManager

    import time

    from qlogicae_cor.v1.library import (
        console_display_manager,
        enum_conversion_value,
        script_process_enum_manager,
        script_process_manager,
        singleton_manager,
        system_manager,
    )

    from qlogicae_logis.v2.library import (
        command_storage_manager,
        command_utility_manager,
        database_manager,
        log_manager,
    )

    _time = time
    _LogManager = (
        log_manager.LogManager
    )
    _SystemManager = (
        system_manager.SystemManager
    )
    _DatabaseManager = (
        database_manager.DatabaseManager
    )
    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _EnumConversionValue = (
        enum_conversion_value.EnumConversionValue
    )
    _CommandStorageManager = (
        command_storage_manager.CommandStorageManager
    )
    _ConsoleDisplayManager = (
        console_display_manager.ConsoleDisplayManager
    )
    _ScriptProcessManager = (
        script_process_manager.ScriptProcessManager
    )
    _CommandUtilityManager = (
        command_utility_manager.CommandUtilityManager
    )
    _ScriptProcessEnumManager = (
        script_process_enum_manager.ScriptProcessEnumManager
    )

    _handle_dynamic_imports = lambda: None

class CommandWorkflowManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()

    def run_command_workflow_list_selections(self) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )
        console_display_manager = _SingletonManager.get_singleton(
            _ConsoleDisplayManager
        )

        workflow_selections = list(
            database_manager.workflow_selections
        )

        workflow_selections.sort()

        console_display_manager.render_one_component(
            "\n".join(
                (
                    f"[green]{item}[/]"
                    for item
                    in workflow_selections
                ),
            )
        )

        return True

    def run_command_workflow_run(
        self,
        **kwargs: Any,
    ) -> bool:
        def handle_workflow_run_target(target_name: str) -> bool:
            if target_name not in workspace_data_workflow_selection:
                log_manager.full_log_warning(
                    f"workspace property "
                    f"'data.workflow.selection.{target_name}' "
                    "does not exist"
                )
                return False

            workflow_selection_data = workspace_data_workflow_selection[target_name]
            workflow_selection_data_is_enabled = (
                workflow_selection_data["is-enabled"]
                if workflow_selection_data and "is-enabled" in workflow_selection_data
                else {}
            )
            workflow_selection_data_is_enabled_value = (
                workflow_selection_data_is_enabled["value"]
                if workflow_selection_data_is_enabled
                and "value" in workflow_selection_data_is_enabled
                else True
            )
            if (
                not workflow_selection_data_is_enabled_value
            ):
                log_manager.full_log_warning(
                    f"workspace property "
                    f"'data.workflow.selection.{target_name}."
                    "is-enabled.value' has been set to 'false'"
                )
                return False

            workflow_selection_data_scripts = (
                workflow_selection_data["scripts"]
                if workflow_selection_data and "scripts"
                    in workflow_selection_data
                else []
            ) or []
            if not len(workflow_selection_data_scripts):
                log_manager.full_log_warning(
                    f"workspace property "
                    f"'data.workflow.targets.{target_name}.scripts' "
                    "is an empty list"
                )
                return False

            # workflow_data_name = (
            #     workspace_data_workflow["name"]
            #     if workspace_data_workflow and "name" in workspace_data_workflow
            #     else {}
            # ) or {}
            # workflow_data_name_value = (
            #     workflow_data_name["value"]
            #     if workflow_data_name
            #     and "value" in workflow_data_name
            #     else "Workflow Selection"
            # ) or "Workflow Selection"

            workflow_data_delay = (
                workspace_data_workflow["delay"]
                if workspace_data_workflow and "delay" in workspace_data_workflow
                else {}
            ) or {}
            workflow_data_delay_value = (
                workflow_data_delay["value"]
                if workflow_data_delay
                and "value" in workflow_data_delay
                and workflow_data_delay["value"] >= 0
                else 0
            )
            workflow_data_process = (
                workspace_data_workflow["process"]
                if workspace_data_workflow and "process" in workspace_data_workflow
                else {}
            ) or {}
            workflow_data_process_value = (
                workflow_data_process["value"]
                if workflow_data_process and "value"
                    in workflow_data_process
                else script_process_manager.selected_script_process
            ) or script_process_manager.selected_script_process
            workflow_data_process_override = (
                workflow_data_process["override"]
                if workflow_data_process and "override" in workflow_data_process
                else False
            )

            workflow_data_is_atomic = (
                workspace_data_workflow["is-atomic"]
                if workspace_data_workflow and "is-atomic" in workspace_data_workflow
                else {}
            ) or {}
            workflow_data_is_atomic_value = (
                workflow_data_is_atomic["value"]
                if workflow_data_is_atomic and "value"
                    in workflow_data_is_atomic
                else True
            )
            workflow_data_is_atomic_override = (
                workflow_data_is_atomic["override"]
                if workflow_data_is_atomic and "override" in workflow_data_is_atomic
                else False
            )

            workflow_selection_data_enter_full_path = (
                workflow_selection_data["enter-filesystem-path"]
                if workflow_selection_data and "enter-filesystem-path"
                    in workflow_selection_data
                else {}
            ) or {}
            workflow_selection_data_enter_full_path_value = (
                workflow_selection_data_enter_full_path["value"]
                if workflow_selection_data_enter_full_path
                and "value" in workflow_selection_data_enter_full_path
                else root_filesystem_path
            ) or root_filesystem_path

            if workflow_data_delay_value and workflow_data_delay_value > 0:
                _time.sleep(workflow_data_delay_value)

            for command in workflow_selection_data_scripts:
                if "run" not in command:
                    log_manager.full_log_warning(
                        f"a command within the '{target_name}'"
                        "workflow does not have a 'run' property"
                    )
                    return False

                current_command_is_enabled = (
                    command["is-enabled"]
                    if command
                    and "is-enabled" in command
                    else {}
                ) or {}
                current_command_is_enabled_value = (
                    current_command_is_enabled["value"]
                    if current_command_is_enabled
                    and "value" in current_command_is_enabled
                    else True
                )
                current_run = command["run"]
                current_run_value = (
                    current_run["value"]
                    if current_run and "value" in current_run else (
                        None
                    )
                )

                if not current_command_is_enabled_value or not current_run_value:
                    log_manager.full_log_warning(
                        f"workspace property "
                        f"'data.workflow.targets.{target_name}.scripts."
                        f"'{current_run}'' has been set "
                        "to 'false'"
                    )
                    return False

                # command_name = (
                #     command["name"]
                #     if command and "name" in command
                #     else {}
                # ) or {}
                # command_name_value = (
                #     command_name["value"]
                #     if command_name
                #     and "value" in command_name
                #     else "Selection Command"
                # ) or "Selection Command"

                current_args = (
                    command["argument"]
                    if command and "argument" in command else {}
                ) or {}
                current_process = (
                    command["process"]
                    if command and "process" in command else {}
                ) or {}
                current_process_value = (
                    current_process["value"]
                    if current_process
                    and "value" in current_process
                    else script_process_manager.selected_script_process
                ) or script_process_manager.selected_script_process
                if workflow_data_process_override:
                    current_process_value = (
                        workflow_data_process_value
                    )

                current_run_is_atomic = (
                    current_run["is-atomic"]
                    if current_run and "is-atomic" in current_run
                    else {}
                ) or {}
                current_run_is_atomic_value = (
                    current_run_is_atomic["value"]
                    if current_run_is_atomic and "value"
                        in current_run_is_atomic
                    else True
                )

                current_run_delay = (
                    command["delay"]
                    if command
                    and "delay" in command
                    else {}
                ) or {}
                current_run_delay_value = (
                    current_run_delay["value"]
                    if current_run_delay
                    and "value" in current_run_delay
                    and current_run_delay["value"] >= 0
                    else 0
                ) or 0
                current_process_value = (
                    script_process_enum_manager.convert_value(
                        current_process_value,
                        _EnumConversionValue.ENUM
                    )
                )
                if current_run_delay_value and current_run_delay_value > 0:
                    _time.sleep(current_run_delay_value)

                v = workflow_selection_data_enter_full_path_value
                system_manager.current_executing_console_filesystem_path = v

                if current_run_value in commands:
                    commands[current_run_value](**current_args)

                elif current_run_value in workspace_data_workflow_selection:
                    handle_workflow_run_target(current_run_value)

                else:
                    cli_output = script_process_manager.execute_command(
                        current_run_value,
                        script_process_type=current_process_value,
                    )

                    if (
                        workflow_data_is_atomic_value
                        if workflow_data_is_atomic_override
                        else current_run_is_atomic_value
                    ):
                        if (
                            current_process_value == (
                                script_process_manager.selected_script_process
                            )
                            and cli_output.returncode
                        ):
                            return False

                    log_manager.file_log_info(
                        cli_output
                    )

            return True

        targets = kwargs.get('targets', [])

        log_manager = _SingletonManager.get_singleton(
            _LogManager
        )
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )
        workspace_data_workflow_is_enabled_value = (
            database_manager
                .workspace_data_workflow_is_enabled_value
        )
        if not workspace_data_workflow_is_enabled_value:
            log_manager.full_log_warning(
                "workspace property "
                "'data.workflow.is-enabled.value' has been "
                "set to 'false'"
            )
            return False

        command_storage_manager = _SingletonManager.get_singleton(
            _CommandStorageManager
        )
        command_utility_manager = _SingletonManager.get_singleton(
            _CommandUtilityManager
        )
        system_manager = _SingletonManager.get_singleton(
            _SystemManager
        )
        script_process_manager = _SingletonManager.get_singleton(
            _ScriptProcessManager
        )
        script_process_enum_manager = _SingletonManager.get_singleton(
            _ScriptProcessEnumManager
        )

        root_filesystem_path = (
            database_manager
                .root_filesystem_path
        )
        commands = (
            command_storage_manager.commands
        )
        workspace_data_workflow = (
            database_manager
                .workspace_data_workflow
        )
        workspace_data_workflow_selections = (
            database_manager
                .workflow_selections
        )
        workspace_data_workflow_selection = (
            database_manager
                .workspace_data_workflow_selection
        )
        workspace_data_macros_default_on_parse_is_enabled_value = (
            database_manager
                .workspace_data_macros_default_on_parse_is_enabled_value
        )
        if workspace_data_macros_default_on_parse_is_enabled_value:
            workspace_data_workflow_selection = (
                command_utility_manager.parse_many(
                    workspace_data_workflow_selection,
                )
            )

        for target in targets:
            if target not in workspace_data_workflow_selections:
                log_manager.full_log_warning(
                    "workspace property "
                    f"'data.workflow.selection.{target}' "
                    "script does not exist"
                )
                continue

            handle_workflow_run_target(target)

        return True


    def run_command_workflow_setup(
        self,
    ) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        workspace_data_workflow_selection = (
            database_manager
                .workspace_data_workflow_selection
        )

        database_manager.workflow_selections = {
            key
            for key, _value in workspace_data_workflow_selection.items()
            if key
        }

        return True

