from __future__ import annotations

from typing import Any

_Path: Any = None
_chain: Any = None
_repeat: Any = None
_Callable: Any = None
_LogManager: Any = None
_SystemManager: Any = None
_DatabaseManager: Any = None
_SingletonManager: Any = None
_FilesystemManager: Any = None
_DataFileIoManager: Any = None
_ThreadPoolExecutor: Any = None
_ObjectMergeManager: Any = None
_ConsoleDisplayManager: Any = None
_CommandUtilityManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _Path
    global _chain
    global _repeat
    global _Callable
    global _LogManager
    global _SystemManager
    global _DatabaseManager
    global _SingletonManager
    global _FilesystemManager
    global _DataFileIoManager
    global _ThreadPoolExecutor
    global _ObjectMergeManager
    global _ConsoleDisplayManager
    global _CommandUtilityManager

    from collections.abc import Callable
    from concurrent.futures import ThreadPoolExecutor
    from itertools import chain, repeat
    from pathlib import Path

    from qlogicae_cor.v1.library import (
        console_display_manager,
        data_file_io_manager,
        filesystem_manager,
        object_merge_manager,
        singleton_manager,
        system_manager,
    )

    from qlogicae_logis.v2.library import (
        command_utility_manager,
        database_manager,
        log_manager,
    )

    _Path = Path
    _chain = chain
    _repeat = repeat
    _Callable = Callable
    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _ObjectMergeManager = (
        object_merge_manager.ObjectMergeManager
    )
    _DataFileIoManager = (
        data_file_io_manager.DataFileIoManager
    )
    _SystemManager = (
        system_manager.SystemManager
    )
    _ThreadPoolExecutor = (
        ThreadPoolExecutor
    )
    _DatabaseManager = (
        database_manager.DatabaseManager
    )
    _LogManager = (
        log_manager.LogManager
    )
    _FilesystemManager = (
        filesystem_manager.FilesystemManager
    )
    _ConsoleDisplayManager = console_display_manager.ConsoleDisplayManager
    _CommandUtilityManager = (
        command_utility_manager.CommandUtilityManager
    )

    _handle_dynamic_imports = lambda: None

class CommandTemplateManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()

    def run_command_template_list_selections(self) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )
        console_display_manager = _SingletonManager.get_singleton(
            _ConsoleDisplayManager
        )

        workspace_selection_base = list(
            database_manager.workspace_selection_base
        )
        workspace_selection_group = list(
            database_manager.workspace_selection_group
        )
        workspace_selection_project = list(
            database_manager.workspace_selection_project
        )

        workspace_selection_base.sort()
        workspace_selection_group.sort()
        workspace_selection_project.sort()

        console_display_manager.render_one_component(
            "\n".join(
                _chain(
                    (
                        f"[red]base <- {item}[/]"
                        for item
                        in workspace_selection_base
                    ),
                    (
                        f"[yellow]group <- {item}[/]"
                        for item
                        in workspace_selection_group
                    ),
                    (
                        f"[green]project <- {item}[/]"
                        for item
                        in workspace_selection_project
                    ),
                )
            )
        )

        return True

    def run_command_template_apply(
        self,
        **kwargs: Any,
    ) -> bool:
        def handle_target_root() -> bool:
            log_manager.file_log_info(
                "'root' setup execution start"
            )

            copy_tasks: list[tuple[_Path, _Path]] = []
            for scope in default_filesystem_accessibility_types:
                for template_type in default_template_types:
                    destination = (
                        _Path(temporary_template_output_filesystem_path)
                        / template_type
                        / "root"
                    )

                    copy_tasks.extend(
                        [
                            (
                                _Path(root_workspace_filesystem_path)
                                / scope
                                / "template"
                                / "all"
                                / template_type,
                                destination,
                            ),
                            (
                                _Path(root_workspace_filesystem_path)
                                / scope
                                / "template"
                                / "root"
                                / template_type,
                                destination,
                            ),
                        ]
                    )

            def copy_task(task: tuple[_Path, _Path]) -> None:
                filesystem_manager.copy_filesystem_path(
                    task[0],
                    task[1],
                )

            with _ThreadPoolExecutor(
                max_workers=min(32, len(copy_tasks) or 1),
            ) as executor:
                tuple(executor.map(copy_task, copy_tasks))

            parse_paths = [
                _Path(temporary_template_output_filesystem_path)
                / "filesystem" / "root",
                _Path(temporary_template_output_filesystem_path)
                / "fragment" / "root",
            ]

            with _ThreadPoolExecutor(max_workers=2) as executor:
                tuple(
                    executor.map(
                        command_utility_manager.parse_filesystem,
                        parse_paths,
                    )
                )

            filesystem_manager.copy_filesystem_path(
                _Path(temporary_template_output_filesystem_path)
                / "filesystem" / "root",
                root_filesystem_path,
            )

            fragment_root = (
                _Path(temporary_template_output_filesystem_path)
                / "fragment"
                / "root"
            )

            relative_paths = [
                path.relative_to(fragment_root)
                for path in fragment_root.rglob("*")
                if path.is_file()
            ]

            def merge_fragment(relative_path: _Path) -> None:
                source_path = fragment_root / relative_path
                target_path = (
                    _Path(root_filesystem_path)
                    / relative_path
                )

                source_data = (
                    data_file_io_manager.read_file(source_path)
                )

                target_data = (
                    data_file_io_manager.read_file(target_path)
                )

                merged = (
                    object_merge_manager.deep_merge_fragments(
                        target_data,
                        source_data,
                    )
                )

                data_file_io_manager.write_file(
                    target_path,
                    merged,
                )

            with _ThreadPoolExecutor(
                max_workers=min(32, len(relative_paths) or 1),
            ) as executor:
                tuple(
                    executor.map(
                        merge_fragment,
                        relative_paths,
                    )
                )

            log_manager.file_log_info(
                "'root' setup execution complete"
            )

            return True


        def handle_target_group() -> bool:
            log_manager.file_log_info(
                "'group' "
                "setup execution start"
            )

            with _ThreadPoolExecutor(
                max_workers=min(32, len(workspace_selection_group) or 1),
            ) as executor:
                tuple(
                    executor.map(
                        handle_target_group_selection,
                        workspace_selection_group,
                    )
                )

            log_manager.file_log_info(
                "'group' "
                "setup execution complete"
            )

            return True


        def handle_target_group_selection(group_name: str) -> bool:
            log_manager.file_log_info(
                f"'{group_name}' "
                "setup execution start"
            )

            group_targets = (
                database_manager
                    .setup_workspace_data_selection_group_targets_name(
                        group_name
                    )
            )

            for (
                current_scope_name
            ) in default_filesystem_accessibility_types:
                for current_template_type in default_template_types:
                    filesystem_manager.copy_filesystem_path(
                        f"{root_workspace_filesystem_path}/{current_scope_name}/template/all/{current_template_type}",
                        f"{temporary_template_output_filesystem_path}/{current_template_type}/{group_name}",
                    )
                    filesystem_manager.copy_filesystem_path(
                        f"{root_workspace_filesystem_path}/{current_scope_name}/template/group/{current_template_type}",
                        f"{temporary_template_output_filesystem_path}/{current_template_type}/{group_name}",
                    )
                    filesystem_manager.copy_filesystem_path(
                        f"{root_workspace_filesystem_path}/{
                            current_scope_name
                        }/template/group/selection/{group_name}/{
                            current_template_type
                        }",
                        f"{temporary_template_output_filesystem_path}/{current_template_type}/{group_name}",
                    )

            for current_template_type in default_template_types:
                command_utility_manager.parse_filesystem(
                    f"{temporary_template_output_filesystem_path}/{current_template_type}/{group_name}"
                )

            for current_target in group_targets:
                if current_target in workspace_selection_project:
                    filesystem_manager.copy_filesystem_path(
                        f"{temporary_template_output_filesystem_path}/filesystem/{group_name}",
                        f"{temporary_template_output_filesystem_path}/filesystem/{current_target}",
                    )
                    handle_target_project_selection(current_target)

                elif current_target == "root":
                    filesystem_manager.copy_filesystem_path(
                        f"{temporary_template_output_filesystem_path}/filesystem/{group_name}",
                        f"{temporary_template_output_filesystem_path}/filesystem/root",
                    )
                    handle_target_root()

                elif current_target in workspace_selection_group:
                    handle_target_group_selection(current_target)


            log_manager.file_log_info(
                f"'{group_name}' "
                "setup execution complete"
            )

            return True

        def handle_target_project() -> bool:
            log_manager.file_log_info(
                "'project' "
                "setup execution start"
            )

            with _ThreadPoolExecutor(
                max_workers=min(32, len(workspace_selection_project) or 1),
            ) as executor:
                tuple(
                    executor.map(
                        handle_target_project_selection,
                        workspace_selection_project,
                    )
                )

            log_manager.file_log_info(
                "'project' "
                "setup execution complete"
            )

            return True

        def handle_target_project_selection(project_name: str) -> bool:
            log_manager.file_log_info(
                f"'{project_name}' "
                "setup execution start"
            )

            selection_project_target_full_paths = (
                database_manager
                    .setup_workspace_data_selection_project_targets_name_filesystem_path_value(
                        project_name
                    )
            )
            selection_project_target_full_paths = (
                command_utility_manager
                    .parse_many(
                        selection_project_target_full_paths
                    )
            )

            for (
                current_scope_name
            ) in default_filesystem_accessibility_types:
                for current_template_type in default_template_types:
                    filesystem_manager.copy_filesystem_path(
                        f"{root_workspace_filesystem_path}/{current_scope_name}/template/all/{current_template_type}",
                        f"{temporary_template_output_filesystem_path}/{current_template_type}/{project_name}",
                    )
                    filesystem_manager.copy_filesystem_path(
                        f"{root_workspace_filesystem_path}/{current_scope_name}/template/project/{current_template_type}",
                        f"{temporary_template_output_filesystem_path}/{current_template_type}/{project_name}",
                    )
                    filesystem_manager.copy_filesystem_path(
                        f"{root_workspace_filesystem_path}/{
                            current_scope_name
                        }/template/project/selection/{project_name}/{
                            current_template_type
                        }",
                        f"{temporary_template_output_filesystem_path}/{current_template_type}/{project_name}",
                    )

            for current_template_type in default_template_types:
                command_utility_manager.parse_filesystem(
                    f"{temporary_template_output_filesystem_path}/{current_template_type}/{project_name}"
                )

            filesystem_manager.copy_filesystem_path(
                f"{temporary_template_output_filesystem_path}/filesystem/{project_name}",
                selection_project_target_full_paths,
            )

            template_fragment_root = _Path(
                f"{temporary_template_output_filesystem_path}/fragment/{project_name}"
            )
            relative_file_paths = [
                current_relative_file_path.relative_to(template_fragment_root)
                for current_relative_file_path in template_fragment_root.rglob("*")
                if current_relative_file_path.is_file()
            ]
            for file in relative_file_paths:
                source_path = _Path(
                    f"{temporary_template_output_filesystem_path}/fragment/{project_name}/{file}"
                )
                source_data = data_file_io_manager.read_file(
                    source_path
                )
                target_path = _Path(f"{root_filesystem_path}/{file}")
                target_data = target_data = (
                    data_file_io_manager.read_file(target_path)
                )
                output_data = (
                    object_merge_manager.deep_merge_fragments(
                        target_data,
                        source_data,
                    )
                )
                data_file_io_manager.write_file(
                    target_path, output_data
                )

            log_manager.file_log_info(
                f"'{project_name}' "
                "setup execution complete"
            )

            return True

        targets: Any = kwargs.get("targets", ["all"])

        log_manager = _SingletonManager.get_singleton(
            _LogManager
        )
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )
        workspace_data_command_template_is_enabled_value = (
            database_manager
                .workspace_data_command_template_is_enabled_value
        )

        if not workspace_data_command_template_is_enabled_value:
            log_manager.full_log_warning(
                "workspace property "
                "'data.selection.is-enabled.value' may be set to 'false'"
            )
            return False

        command_utility_manager = _SingletonManager.get_singleton(
            _CommandUtilityManager
        )
        filesystem_manager = _SingletonManager.get_singleton(
            _FilesystemManager
        )
        object_merge_manager = _SingletonManager.get_singleton(
            _ObjectMergeManager
        )
        data_file_io_manager = _SingletonManager.get_singleton(
            _DataFileIoManager
        )

        default_filesystem_accessibility_types = (
            command_utility_manager
                .default_filesystem_accessibility_types
        )
        workspace_selection_all = (
            database_manager
                .workspace_selection_all
        )
        workspace_selection_project = (
            database_manager
                .workspace_selection_project
        )
        workspace_selection_group = (
            database_manager
                .workspace_selection_group
        )
        default_template_types = (
            command_utility_manager
                .default_template_types
        )
        root_filesystem_path = (
            database_manager
                .root_filesystem_path
        )
        root_workspace_filesystem_path = (
            command_utility_manager
                .setup_root_workspace_filesystem_path()
        )
        temporary_template_output_filesystem_path = (
            command_utility_manager
                .setup_temporary_template_output_filesystem_path()
        )
        workspace_data_command_template_cleanup_is_enabled_value = (
            database_manager
                .workspace_data_command_template_cleanup_is_enabled_value
        )

        if workspace_data_command_template_cleanup_is_enabled_value:
            filesystem_manager.clean_filesystem_path(
                temporary_template_output_filesystem_path
            )

        tasks: list[Any] = []

        for target in targets:
            if (
                not target
                or target not in workspace_selection_all
            ):
                log_manager.full_log_warning(
                    f"selection "
                    f"'{target}' does not exist within either "
                    "workspace properties "
                    "'data.selection.project.target', or "
                    "'data.selection.group.target'"
                )
                return False

            if target == "all":
                tasks.extend(
                    [
                        (handle_target_root,),
                        (handle_target_group,),
                        (handle_target_project,),
                    ]
                )

            elif target == "root":
                tasks.append((handle_target_root,))

            elif target == "group":
                tasks.append((handle_target_group,))

            elif target == "project":
                tasks.append((handle_target_project,))

            elif target in workspace_selection_group:
                tasks.append(
                    (
                        handle_target_group_selection,
                        target,
                    )
                )

            elif target in workspace_selection_project:
                tasks.append(
                    (
                        handle_target_project_selection,
                        target,
                    )
                )

        for task in tasks:
            if len(task) == 1:
                task[0]()
            else:
                task[0](task[1])

        if workspace_data_command_template_cleanup_is_enabled_value:
            filesystem_manager.clean_filesystem_path(
                temporary_template_output_filesystem_path
            )

        return True
