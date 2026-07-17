from pathlib import Path

import typer

from qlogicae_logis.v1 import (
    cli_manager,
    file_io_manager,
    file_log_manager,
    filesystem_manager,
    log_manager,
    macros_manager,
    value_cache_manager,
    workspace_filesystem_manager,
    workspace_manager,
)
from qlogicae_logis.v1.target_cache_value import TargetCacheValue

app_template = typer.Typer()
app_template_filesystem = typer.Typer()
app_template_filesystem_list = typer.Typer()

app_template.add_typer(
    app_template_filesystem,
    name="filesystem",
    help="Apply filesystem templates.",
)
app_template_filesystem.add_typer(
    app_template_filesystem_list,
    name="list",
    help="Show lists.",
)


def handle_loading() -> bool:
    cli_manager.singleton.render_progress_bar({})

    return True


@app_template_filesystem_list.command(
    name="selections", help="Show a list of template filesystem selections."
)
def selections() -> bool:
    file_log_manager.singleton.log_info("'template filesystem selections' - start")

    handle_loading()

    default_workspace_selections = list(
        value_cache_manager.singleton.get_one_value(
            ["default-workspace-selections"],
            output_type=TargetCacheValue.DEFINED,
        )
        or {}
    )
    default_workspace_selections.sort()
    group_workspace_selections = list(
        value_cache_manager.singleton.get_one_value(
            ["group-workspace-selections"],
            output_type=TargetCacheValue.DEFINED,
        )
        or {}
    )
    group_workspace_selections.sort()
    project_workspace_selections = list(
        value_cache_manager.singleton.get_one_value(
            ["project-workspace-selections"],
            output_type=TargetCacheValue.DEFINED,
        )
        or {}
    )
    project_workspace_selections.sort()
    for current_workspace_selection in default_workspace_selections:
        cli_manager.singleton.render_one(
            f"[red]base <- {current_workspace_selection}[/]"
        )

    for current_workspace_selection in group_workspace_selections:
        cli_manager.singleton.render_one(
            f"[yellow]group <- {current_workspace_selection}[/]"
        )

    for current_workspace_selection in project_workspace_selections:
        cli_manager.singleton.render_one(
            f"[green]project <- {current_workspace_selection}[/]"
        )

    file_log_manager.singleton.log_info("'template filesystem selections' - complete")
    workspace_manager.singleton.shutdown()

    return True


@app_template_filesystem.command(name="apply", help="Apply filesystem templates.")
def apply(
    targets: list[str] = typer.Argument(
        ...,
        help="List of workspace targets.",
    ),
) -> bool:
    file_log_manager.singleton.log_info("'template filesystem apply' - start")

    handle_loading()
    is_enabled = (
        value_cache_manager.singleton.get_one_value(
            [
                "workspace",
                "data",
                "selection",
                "is-enabled",
            ],
            output_type=TargetCacheValue.ANY,
        )
        or {}
    )
    is_enabled_value = is_enabled["value"] if "value" in is_enabled else True
    is_enabled_is_override = (
        is_enabled["is-override"] if "is-override" in is_enabled else False
    )

    if is_enabled_is_override and not is_enabled_value:
        log_manager.singleton.log_warning(
            "'template filesystem apply' - workspace property 'data.selection.is-enabled.value' is set to 'false'"
        )

        return False

    workspace_selections = (
        value_cache_manager.singleton.get_one_value(
            ["workspace-selections"],
            output_type=TargetCacheValue.DEFINED,
        )
        or {}
    )
    project_workspace_selections = (
        value_cache_manager.singleton.get_one_value(
            ["project-workspace-selections"],
            output_type=TargetCacheValue.DEFINED,
        )
        or {}
    )
    group_workspace_selections = (
        value_cache_manager.singleton.get_one_value(
            ["group-workspace-selections"],
            output_type=TargetCacheValue.DEFINED,
        )
        or {}
    )

    current_root_full_path = value_cache_manager.singleton.get_one_value(
        ["current-root-full-path"],
        output_type=TargetCacheValue.FOLDER_PATH,
    )

    filesystem_manager.singleton.clean_filesystem_path(
        f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem"
    )

    for current_target in targets:
        if current_target not in workspace_selections:
            log_manager.singleton.log_warning(
                f"'template filesystem apply' - selection '{current_target}' is not found within either workspace properties 'data.selection.project.targets', and 'data.selection.group.targets'"
            )
            continue

        if current_target == "all":
            handle_target_root()
            handle_target_group()
            handle_target_project()

        elif current_target == "root":
            handle_target_root()

        elif current_target == "group":
            handle_target_group()

        elif current_target == "project":
            handle_target_project()

        elif current_target in group_workspace_selections:
            handle_target_group_selection(current_target)

        elif current_target in project_workspace_selections:
            handle_target_project_selection(current_target)

    filesystem_manager.singleton.clean_filesystem_path(
        f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem"
    )

    file_log_manager.singleton.log_info("'template filesystem apply' - complete")
    workspace_manager.singleton.shutdown()

    return True


def handle_target_root():
    file_log_manager.singleton.log_info(
        "'template filesystem apply' - 'root' setup execution start"
    )

    current_root_full_path = value_cache_manager.singleton.get_one_value(
        ["current-root-full-path"],
        output_type=TargetCacheValue.FOLDER_PATH,
    )

    for current_scope_name in workspace_filesystem_manager.singleton.scope_selections:
        filesystem_manager.singleton.copy_filesystem_path(
            f"{current_root_full_path}/workspace/{current_scope_name}/template/all/filesystem",
            f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem/root",
        )
        filesystem_manager.singleton.copy_filesystem_path(
            f"{current_root_full_path}/workspace/{current_scope_name}/template/root/filesystem",
            f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem/root",
        )

    handle_filesystem_parsing(
        f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem/root"
    )
    filesystem_manager.singleton.copy_filesystem_path(
        f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem/root",
        current_root_full_path,
    )
    file_log_manager.singleton.log_info(
        "'template filesystem apply' - 'root' setup execution complete"
    )

    return True


def handle_target_group():
    file_log_manager.singleton.log_info(
        "'template filesystem apply' - 'group' setup execution start"
    )

    group_workspace_selections = (
        value_cache_manager.singleton.get_one_value(
            ["group-workspace-selections"],
            output_type=TargetCacheValue.DEFINED,
        )
        or {}
    )

    for group_name in group_workspace_selections:
        handle_target_group_selection(group_name)

    file_log_manager.singleton.log_info(
        "'template filesystem apply' - 'group' setup execution complete"
    )

    return True


def handle_target_group_selection(group_name):
    file_log_manager.singleton.log_info(
        f"'template filesystem apply' - '{group_name}' setup execution start"
    )

    current_root_full_path = value_cache_manager.singleton.get_one_value(
        ["current-root-full-path"],
        output_type=TargetCacheValue.FOLDER_PATH,
    )

    group_targets = value_cache_manager.singleton.get_one_value(
        [
            "workspace",
            "data",
            "selection",
            "group",
            "targets",
            group_name,
            "targets",
        ],
        output_type=TargetCacheValue.DEFINED,
    )
    project_workspace_selections = (
        value_cache_manager.singleton.get_one_value(
            ["project-workspace-selections"],
            output_type=TargetCacheValue.DEFINED,
        )
        or {}
    )
    group_workspace_selections = (
        value_cache_manager.singleton.get_one_value(
            ["group-workspace-selections"],
            output_type=TargetCacheValue.DEFINED,
        )
        or {}
    )

    for current_scope_name in workspace_filesystem_manager.singleton.scope_selections:
        filesystem_manager.singleton.copy_filesystem_path(
            f"{current_root_full_path}/workspace/{current_scope_name}/template/all/filesystem",
            f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem/{group_name}",
        )
        filesystem_manager.singleton.copy_filesystem_path(
            f"{current_root_full_path}/workspace/{current_scope_name}/template/group/filesystem",
            f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem/{group_name}",
        )
        filesystem_manager.singleton.copy_filesystem_path(
            f"{current_root_full_path}/workspace/{
                current_scope_name
            }/template/group/selection/{group_name}/filesystem",
            f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem/{group_name}",
        )

    handle_filesystem_parsing(
        f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem/{group_name}"
    )

    for current_target in group_targets:
        if current_target in project_workspace_selections:
            filesystem_manager.singleton.copy_filesystem_path(
                f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem/{group_name}",
                f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem/{current_target}",
            )
            handle_target_project_selection(current_target)

        elif current_target in group_workspace_selections:
            handle_target_group_selection(current_target)

    file_log_manager.singleton.log_info(
        f"'template filesystem apply' - '{group_name}' setup execution complete"
    )

    return True


def handle_target_project():
    file_log_manager.singleton.log_info(
        "'template filesystem apply' - 'project' setup execution start"
    )

    project_workspace_selections = (
        value_cache_manager.singleton.get_one_value(
            ["project-workspace-selections"],
            output_type=TargetCacheValue.DEFINED,
        )
        or {}
    )

    for project_name in project_workspace_selections:
        handle_target_project_selection(project_name)

    file_log_manager.singleton.log_info(
        "'template filesystem apply' - 'project' setup execution complete"
    )

    return True


def handle_target_project_selection(project_name):
    file_log_manager.singleton.log_info(
        f"'template filesystem apply' - '{project_name}' setup execution start"
    )

    current_root_full_path = value_cache_manager.singleton.get_one_value(
        ["current-root-full-path"],
        output_type=TargetCacheValue.FOLDER_PATH,
    )

    selection_project_target_full_paths = value_cache_manager.singleton.get_one_value(
        [
            "workspace",
            "data",
            "selection",
            "project",
            "targets",
            project_name,
            "full-path",
        ],
        output_type=TargetCacheValue.DEFINED,
    )

    for current_scope_name in workspace_filesystem_manager.singleton.scope_selections:
        filesystem_manager.singleton.copy_filesystem_path(
            f"{current_root_full_path}/workspace/{current_scope_name}/template/all/filesystem",
            f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem/{project_name}",
        )
        filesystem_manager.singleton.copy_filesystem_path(
            f"{current_root_full_path}/workspace/{current_scope_name}/template/project/filesystem",
            f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem/{project_name}",
        )
        filesystem_manager.singleton.copy_filesystem_path(
            f"{current_root_full_path}/workspace/{
                current_scope_name
            }/template/project/selection/{project_name}/filesystem",
            f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem/{project_name}",
        )

    handle_filesystem_parsing(
        f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem/{project_name}"
    )
    filesystem_manager.singleton.copy_filesystem_path(
        f"{current_root_full_path}/workspace/private/temporary/intermediate/filesystem/{project_name}",
        selection_project_target_full_paths,
    )

    file_log_manager.singleton.log_info(
        f"'template filesystem apply' - '{project_name}' setup execution complete"
    )

    return True


def handle_filesystem_parsing(
    filesystem_path,
):
    workspace_macros = (
        value_cache_manager.singleton.get_one_value(
            ["workspace-macros"],
            output_type=TargetCacheValue.DEFINED,
        )
        or {}
    )

    root = Path(filesystem_path)

    for current_root, directories, files in root.walk(
        top_down=False,
    ):
        current_root = Path(current_root)

        for file_name in files:
            current_path = current_root / file_name

            try:
                file_data = current_path.read_text(
                    encoding=file_io_manager.singleton.file_encoding,
                )
            except UnicodeDecodeError:
                pass
            else:
                parsed_file_data = macros_manager.singleton.parse_one(
                    file_data,
                    workspace_macros,
                )

                if parsed_file_data != file_data:
                    current_path.write_text(
                        parsed_file_data,
                        encoding=file_io_manager.singleton.file_encoding,
                    )

            parsed_name = macros_manager.singleton.parse_one(
                current_path.name,
                workspace_macros,
            )

            if parsed_name != current_path.name:
                current_path = current_path.rename(
                    current_path.with_name(parsed_name),
                )

        for directory_name in directories:
            current_path = current_root / directory_name

            parsed_name = macros_manager.singleton.parse_one(
                current_path.name,
                workspace_macros,
            )

            if parsed_name != current_path.name:
                current_path.rename(
                    current_path.with_name(
                        parsed_name,
                    )
                )

    return True
