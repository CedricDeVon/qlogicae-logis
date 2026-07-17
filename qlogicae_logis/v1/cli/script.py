import time

import typer

from qlogicae_logis.v1 import (
    cli_manager,
    console_log_manager,
    file_log_manager,
    log_manager,
    script_process_enum_manager,
    script_process_manager,
    system_manager,
    value_cache_manager,
    workspace_manager,
)
from qlogicae_logis.v1.enum_conversion_output import EnumConversionOutput
from qlogicae_logis.v1.target_cache_value import TargetCacheValue

app_script = typer.Typer()
app_script_list = typer.Typer()
app_script.add_typer(
    app_script_list,
    name="list",
    help="Show list information.",
)


def handle_loading():
    cli_manager.singleton.render_progress_bar({})


@app_script.command(name="run", help="Run script selections.")
def run(
    targets: list[str] = typer.Argument(
        ...,
        help="List of scripts.",
    ),
) -> bool:
    file_log_manager.singleton.log_info("'script run' - start")

    handle_loading()
    script_data = (
        value_cache_manager.singleton.get_one_value(
            ["workspace", "data", "script"],
            output_type=TargetCacheValue.ANY,
        )
        or {}
    )
    script_data_is_enabled = (
        script_data["is-enabled"] if "is-enabled" in script_data else {}
    )
    script_data_is_enabled_value = (
        script_data_is_enabled["value"] if "value" in script_data_is_enabled else True
    )
    script_data_is_override_enabled = (
        script_data_is_enabled["is-override"]
        if "is-override" in script_data_is_enabled
        else False
    )
    if script_data_is_override_enabled and not script_data_is_enabled_value:
        log_manager.singleton.log_warning(
            "'script run' - workspace property 'data.script.is-enabled.value' is set to 'false'"
        )
        workspace_manager.singleton.shutdown()
        return True

    script_data_targets = script_data["targets"] if "targets" in script_data else {}
    for current_target in targets:
        if current_target not in script_data_targets:
            log_manager.singleton.log_warning(
                f"'script run' - workspace property 'data.script.targets.{current_target}' does not exist"
            )
            continue

        handle_targets(current_target)

    file_log_manager.singleton.log_info("'script run' - complete")
    workspace_manager.singleton.shutdown()

    return True


@app_script_list.command(name="selections", help="Show a list of defined scripts.")
def selections() -> bool:
    file_log_manager.singleton.log_info("'script selections' - start")

    handle_loading()
    script_data_targets = list(
        value_cache_manager.singleton.get_one_value(
            ["workspace", "data", "script", "targets"],
            output_type=TargetCacheValue.ANY,
        )
        or {}
    )
    script_data_targets.sort()

    for script_selection in script_data_targets:
        cli_manager.singleton.render_one(f"[green]{script_selection}[/]")

    file_log_manager.singleton.log_info("'script selections' - complete")
    workspace_manager.singleton.shutdown()

    return True


def handle_targets(target_name: str) -> bool:
    file_log_manager.singleton.log_info(
        f"'script run' - '{target_name}' script execution start"
    )

    script_data = (
        value_cache_manager.singleton.get_one_value(
            [
                "workspace",
                "data",
                "script",
            ],
            output_type=TargetCacheValue.ANY,
        )
        or {}
    )

    script_data_targets = script_data["targets"] if "targets" in script_data else {}
    if target_name not in script_data_targets:
        log_manager.singleton.log_warning(
            f"'script run' - workspace property 'data.script.targets.{target_name}' does not exist"
        )
        return False

    script_target_data = script_data_targets[target_name]
    script_target_data_is_enabled = (
        script_target_data["is-enabled"] if "is-enabled" in script_target_data else {}
    )
    script_target_data_is_enabled_value = (
        script_target_data_is_enabled["value"]
        if "value" in script_target_data_is_enabled
        else True
    )
    script_target_data_is_override_enabled = (
        script_target_data_is_enabled["is-override"]
        if "is-override" in script_target_data_is_enabled
        else False
    )
    if (
        script_target_data_is_override_enabled
        and not script_target_data_is_enabled_value
    ):
        log_manager.singleton.log_warning(
            f"'script run' - workspace property 'data.script.targets.{target_name}.is-enabled.value' is set to 'false'"
        )
        return False

    script_data_delay = script_data["delay"] if "delay" in script_data else {}
    script_data_delay_value = (
        script_data_delay["value"]
        if "value" in script_data_delay and script_data_delay["value"] >= 0
        else 0
    )
    script_data_process = script_data["process"] if "process" in script_data else {}
    script_data_process_value = (
        script_data_process["value"] if "value" in script_data_process else "subprocess"
    )
    script_data_process_is_override_enabled = (
        script_data_process["is-override"]
        if "is-override" in script_data_process
        else False
    )
    current_root_full_path = value_cache_manager.singleton.get_one_value(
        ["current-root-full-path"],
        output_type=TargetCacheValue.FOLDER_PATH,
    )
    script_target_data_commands = (
        script_target_data["commands"] if "commands" in script_target_data else []
    )
    script_target_data_enter_full_path = (
        script_target_data["enter-full-path"]
        if "enter-full-path" in script_target_data
        else current_root_full_path
    )
    if not len(script_target_data_commands):
        log_manager.singleton.log_warning(
            f"'script run' - workspace property 'data.script.targets.{target_name}.commands' is an empty list"
        )
        return False

    if script_data_delay_value:
        time.sleep(script_data_delay_value)

    for current_script_command in script_target_data_commands:
        if "run" not in current_script_command:
            log_manager.singleton.log_warning(
                f"'script run' - a command within the '{target_name}'"
                "script does not have a 'run' property"
            )
            continue

        current_script_command_is_enabled = (
            current_script_command["is-enabled"]
            if "is-enabled" in current_script_command
            else {}
        )
        current_script_command_is_enabled_value = (
            current_script_command_is_enabled["value"]
            if "value" in current_script_command_is_enabled
            else True
        )
        current_script_run_command = current_script_command["run"]
        if not current_script_command_is_enabled_value:
            log_manager.singleton.log_warning(
                f"'script run' - workspace property 'data.script.targets.{target_name}.commands.'{current_script_run_command}'' is set to 'false'"
            )
            continue

        current_script_process = (
            current_script_command["process"]
            if "process" in current_script_command
            else {}
        )
        current_script_process_value = (
            script_data_process_value
            if script_data_process_is_override_enabled
            else (
                current_script_process["value"]
                if "value" in current_script_process
                else "subprocess"
            )
        )
        current_script_run_command_delay = (
            current_script_run_command["delay"]
            if "delay" in current_script_run_command
            else {}
        )
        current_script_run_command_delay_value = (
            current_script_run_command_delay["value"]
            if "value" in current_script_run_command_delay
            and current_script_run_command_delay["value"] >= 0
            else 0
        )
        current_script_process_value = (
            script_process_enum_manager.singleton.convert_value(
                current_script_process_value, EnumConversionOutput.ENUM
            )
        )
        if current_script_run_command_delay_value:
            time.sleep(current_script_run_command_delay_value)

        system_manager.singleton.current_executing_console_filesystem_path = (
            script_target_data_enter_full_path
        )
        if current_script_run_command in script_data_targets:
            handle_targets(current_script_run_command)

        else:
            cli_output = script_process_manager.singleton.execute_command(
                current_script_run_command,
                script_process_type=current_script_process_value,
            )

            file_log_manager.singleton.log_info(cli_output)
            console_log_manager.singleton.log_info(
                cli_output.stdout or cli_output.stderr or ""
            )

    file_log_manager.singleton.log_info(
        f"'script run' - '{target_name}' script execution complete"
    )

    return True
