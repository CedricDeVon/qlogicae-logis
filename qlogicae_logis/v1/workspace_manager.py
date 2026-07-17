from __future__ import annotations

from collections.abc import Callable
from copy import deepcopy
from pathlib import Path
from typing import Any

from qlogicae_cor.v1.abstract_manager import AbstractManager

from qlogicae_logis.v1 import (
    console_log_manager,
    file_io_manager,
    file_log_manager,
    filesystem_manager,
    log_manager,
    macros_manager,
    system_manager,
    time_manager,
    time_zone_enum_manager,
    value_cache_manager,
    workspace_filesystem_manager,
    workspace_system_manager,
)
from qlogicae_logis.v1.filesystem_manager import (
    FileEntityFileSystemTreeSetupOptions,
    FolderEntityFileSystemTreeSetupOptions,
)
from qlogicae_logis.v1.log_options import LogOptions
from qlogicae_logis.v1.target_cache_value import TargetCacheValue
from qlogicae_logis.v1.workspace_manager_configurations import (
    WorkspaceManagerConfigurations,
)


class WorkspaceManager(AbstractManager[WorkspaceManagerConfigurations]):
    def __init__(self) -> None:
        super().__init__(WorkspaceManagerConfigurations())

    @property
    def current_elapsed_console_execution_start(self) -> float:
        console_execution_start = value_cache_manager.singleton.get_one_value(
            ["timestamp-console-execution-start"],
            output_type=TargetCacheValue.DEFINED,
        )

        return time_manager.singleton.calculate_elapsed_time(
            start=console_execution_start
        )

    def handle(self, callback: Callable[[None], None]) -> bool:
        self.setup()

        callback()

        self.shutdown()

        return True

    def setup(self) -> bool:
        self.handle_timestamp_console_execution_start_setup()
        self.handle_current_root_filesystem_paths_setup()
        self.handle_executing_console_filesystem_paths_setup()
        self.handle_current_root_filesystem_navigation_setup()
        self.handle_workspace_base_filesystem_replenishment_setup()
        self.handle_workspace_configuration_file_data_extraction_setup()
        self.handle_workspace_selection_setup()
        self.handle_workspace_selection_filesystem_replenishment_setup()
        self.handle_value_cache_macros_setup()
        self.handle_macros_parsing_setup()
        self.handle_logs_setup()

        return True

    def shutdown(self) -> bool:
        log_manager.singleton.shutdown()

        return True

    def debug_value_cache(self) -> bool:
        self.setup()

        self.handle_toolset_configuration_file_data_extraction_setup()
        self.handle_toolset_configuration_data_setup()
        self.handle_clean_scripts_setup()

        value_cache_manager.singleton.display_all_items()

        return True

    def handle_timestamp_console_execution_start_setup(self) -> bool:
        value_cache_manager.singleton.set_one_value(
            ["timestamp-console-execution-start"],
            time_manager.singleton.current_nanosecond,
        )

        return True

    def handle_timestamp_console_execution_end_setup(self) -> bool:
        value_cache_manager.singleton.set_one_value(
            ["timestamp-console-execution-end"],
            time_manager.singleton.current_nanosecond,
        )

        return True

    def handle_current_root_filesystem_paths_setup(self) -> bool:
        value_cache_manager.singleton.set_one_value(
            ["current-root-full-path"],
            workspace_filesystem_manager.singleton.root_workspace_filesystem_path,
            output_type=TargetCacheValue.FOLDER_PATH,
        )

        return True

    def handle_executing_console_filesystem_paths_setup(self) -> bool:
        current_root_full_path = value_cache_manager.singleton.get_one_value(
            ["current-root-full-path"],
            output_type=TargetCacheValue.FOLDER_PATH,
        )
        value_cache_manager.singleton.set_one_value(
            ["original-executing-console-full-path"],
            system_manager.singleton.current_executing_console_filesystem_path,
            output_type=TargetCacheValue.FOLDER_PATH,
        )
        value_cache_manager.singleton.set_one_value(
            ["current-executing-console-full-path"],
            current_root_full_path,
            output_type=TargetCacheValue.FOLDER_PATH,
        )

        return True

    def handle_current_root_filesystem_navigation_setup(self) -> bool:
        workspace_system_manager.singleton.navigate_to_root()

        return True

    def handle_workspace_base_filesystem_replenishment_setup(self) -> bool:
        current_root_full_path = value_cache_manager.singleton.get_one_value(
            ["current-root-full-path"],
            output_type=TargetCacheValue.FOLDER_PATH,
        )

        workspace_gitignore_file = FileEntityFileSystemTreeSetupOptions(
            name=".gitignore", content="private/**/*"
        )

        configuration_workspace_root_file = FileEntityFileSystemTreeSetupOptions(
            name="root.yaml", content="data:\n\nmetadata:\n"
        )

        configuration_workspace_group_file = FileEntityFileSystemTreeSetupOptions(
            name="group.yaml", content="data:\n\nmetadata:\n"
        )

        configuration_workspace_project_file = FileEntityFileSystemTreeSetupOptions(
            name="project.yaml", content="data:\n\nmetadata:\n"
        )

        configuration_workspace_sub_tree = FolderEntityFileSystemTreeSetupOptions(
            name="configuration",
            entities=[
                FolderEntityFileSystemTreeSetupOptions(
                    name="workspace",
                    entities=[
                        FolderEntityFileSystemTreeSetupOptions(
                            name="group",
                            entities=[
                                FolderEntityFileSystemTreeSetupOptions(
                                    name="selection", entities=[]
                                ),
                                configuration_workspace_group_file,
                            ],
                        ),
                        FolderEntityFileSystemTreeSetupOptions(
                            name="project",
                            entities=[
                                FolderEntityFileSystemTreeSetupOptions(
                                    name="selection", entities=[]
                                ),
                                configuration_workspace_project_file,
                            ],
                        ),
                        configuration_workspace_root_file,
                    ],
                ),
            ],
        )

        template_workspace_sub_tree = FolderEntityFileSystemTreeSetupOptions(
            name="template",
            entities=[
                FolderEntityFileSystemTreeSetupOptions(
                    name="all",
                    entities=[
                        FolderEntityFileSystemTreeSetupOptions(
                            name="filesystem",
                            entities=[],
                        )
                    ],
                ),
                FolderEntityFileSystemTreeSetupOptions(
                    name="group",
                    entities=[
                        FolderEntityFileSystemTreeSetupOptions(
                            name="filesystem",
                            entities=[],
                        ),
                        FolderEntityFileSystemTreeSetupOptions(
                            name="selection",
                            entities=[],
                        ),
                    ],
                ),
                FolderEntityFileSystemTreeSetupOptions(
                    name="project",
                    entities=[
                        FolderEntityFileSystemTreeSetupOptions(
                            name="filesystem",
                            entities=[],
                        ),
                        FolderEntityFileSystemTreeSetupOptions(
                            name="selection",
                            entities=[],
                        ),
                    ],
                ),
                FolderEntityFileSystemTreeSetupOptions(
                    name="root",
                    entities=[
                        FolderEntityFileSystemTreeSetupOptions(
                            name="filesystem",
                            entities=[],
                        )
                    ],
                ),
            ],
        )

        temporary_workspace_sub_tree = FolderEntityFileSystemTreeSetupOptions(
            name="temporary",
            entities=[
                FolderEntityFileSystemTreeSetupOptions(
                    name="intermediate",
                    entities=[
                        FolderEntityFileSystemTreeSetupOptions(
                            name="filesystem",
                            entities=[],
                        )
                    ],
                ),
                FolderEntityFileSystemTreeSetupOptions(
                    name="log",
                    entities=[],
                ),
            ],
        )

        root_filesystem_tree = FolderEntityFileSystemTreeSetupOptions(
            entities=[
                FolderEntityFileSystemTreeSetupOptions(
                    name="workspace",
                    entities=[
                        FolderEntityFileSystemTreeSetupOptions(
                            name="private",
                            entities=[
                                configuration_workspace_sub_tree,
                                template_workspace_sub_tree,
                                temporary_workspace_sub_tree,
                            ],
                        ),
                        FolderEntityFileSystemTreeSetupOptions(
                            name="public",
                            entities=[
                                configuration_workspace_sub_tree,
                                template_workspace_sub_tree,
                            ],
                        ),
                        workspace_gitignore_file,
                    ],
                ),
                FolderEntityFileSystemTreeSetupOptions(
                    name="selection",
                    entities=[],
                ),
            ]
        )

        filesystem_manager.singleton.setup_filesystem_tree(
            current_root_full_path, root_filesystem_tree
        )

    def handle_workspace_selection_filesystem_replenishment_setup(self) -> bool:
        current_root_full_path = value_cache_manager.singleton.get_one_value(
            ["current-root-full-path"],
            output_type=TargetCacheValue.FOLDER_PATH,
        )
        project_workspace_selections = value_cache_manager.singleton.get_one_value(
            ["project-workspace-selections"], output_type=TargetCacheValue.DEFINED
        )
        group_workspace_selections = value_cache_manager.singleton.get_one_value(
            ["group-workspace-selections"], output_type=TargetCacheValue.DEFINED
        )

        filesystem_sub_tree = FolderEntityFileSystemTreeSetupOptions(
            name="filesystem",
            entities=[],
        )

        for current_scope in ["private", "public"]:
            for current_workspace_selection in project_workspace_selections:
                target_filesystem_sub_tree = FolderEntityFileSystemTreeSetupOptions(
                    entities=[
                        FolderEntityFileSystemTreeSetupOptions(
                            name="workspace",
                            entities=[
                                FolderEntityFileSystemTreeSetupOptions(
                                    name=current_scope,
                                    entities=[
                                        FolderEntityFileSystemTreeSetupOptions(
                                            name="configuration",
                                            entities=[
                                                FolderEntityFileSystemTreeSetupOptions(
                                                    name="workspace",
                                                    entities=[
                                                        FolderEntityFileSystemTreeSetupOptions(
                                                            name="project",
                                                            entities=[
                                                                FolderEntityFileSystemTreeSetupOptions(
                                                                    name="selection",
                                                                    entities=[
                                                                        FileEntityFileSystemTreeSetupOptions(
                                                                            name=f"{current_workspace_selection}.yaml",
                                                                            content="data:\n\nmetadata:\n",
                                                                        )
                                                                    ],
                                                                )
                                                            ],
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                        FolderEntityFileSystemTreeSetupOptions(
                                            name="template",
                                            entities=[
                                                FolderEntityFileSystemTreeSetupOptions(
                                                    name="project",
                                                    entities=[
                                                        FolderEntityFileSystemTreeSetupOptions(
                                                            name="selection",
                                                            entities=[
                                                                FolderEntityFileSystemTreeSetupOptions(
                                                                    name=current_workspace_selection,
                                                                    entities=[
                                                                        filesystem_sub_tree
                                                                    ],
                                                                )
                                                            ],
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                    ],
                                )
                            ],
                        )
                    ]
                )
                filesystem_manager.singleton.setup_filesystem_tree(
                    current_root_full_path, target_filesystem_sub_tree
                )

            for current_workspace_selection in group_workspace_selections:
                target_filesystem_sub_tree = FolderEntityFileSystemTreeSetupOptions(
                    entities=[
                        FolderEntityFileSystemTreeSetupOptions(
                            name="workspace",
                            entities=[
                                FolderEntityFileSystemTreeSetupOptions(
                                    name=current_scope,
                                    entities=[
                                        FolderEntityFileSystemTreeSetupOptions(
                                            name="configuration",
                                            entities=[
                                                FolderEntityFileSystemTreeSetupOptions(
                                                    name="workspace",
                                                    entities=[
                                                        FolderEntityFileSystemTreeSetupOptions(
                                                            name="group",
                                                            entities=[
                                                                FolderEntityFileSystemTreeSetupOptions(
                                                                    name="selection",
                                                                    entities=[
                                                                        FileEntityFileSystemTreeSetupOptions(
                                                                            name=f"{current_workspace_selection}.yaml",
                                                                            content="data:\n\nmetadata:\n",
                                                                        )
                                                                    ],
                                                                )
                                                            ],
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                        FolderEntityFileSystemTreeSetupOptions(
                                            name="template",
                                            entities=[
                                                FolderEntityFileSystemTreeSetupOptions(
                                                    name="group",
                                                    entities=[
                                                        FolderEntityFileSystemTreeSetupOptions(
                                                            name="selection",
                                                            entities=[
                                                                FolderEntityFileSystemTreeSetupOptions(
                                                                    name=current_workspace_selection,
                                                                    entities=[
                                                                        filesystem_sub_tree
                                                                    ],
                                                                )
                                                            ],
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                    ],
                                )
                            ],
                        )
                    ]
                )
                filesystem_manager.singleton.setup_filesystem_tree(
                    current_root_full_path, target_filesystem_sub_tree
                )

        return True

    def handle_workspace_configuration_file_data_extraction_setup(self) -> bool:
        current_root_full_path = value_cache_manager.singleton.get_one_value(
            ["current-root-full-path"],
            output_type=TargetCacheValue.FOLDER_PATH,
        )

        workspace_data = {}
        workspace_filesystem_paths = []
        scope_selecions = ["private", "public"]
        for current_scope_selection in scope_selecions:
            configuration_workspace_filesystem_path = f"{current_root_full_path}/workspace/{current_scope_selection}/configuration/workspace"
            configuration_workspace_target_filesystem_paths = [
                Path(f"{configuration_workspace_filesystem_path}/root.yaml"),
                Path(f"{configuration_workspace_filesystem_path}/project/project.yaml"),
                Path(f"{configuration_workspace_filesystem_path}/group/group.yaml"),
            ]
            workspace_filesystem_paths = [
                *workspace_filesystem_paths,
                *configuration_workspace_target_filesystem_paths,
            ]
            for (
                current_configuration_workpsace_target_filesystem_path
            ) in configuration_workspace_target_filesystem_paths:
                if not current_configuration_workpsace_target_filesystem_path.is_file():
                    continue

                with Path.open(
                    current_configuration_workpsace_target_filesystem_path.resolve(),
                    encoding=file_io_manager.singleton.file_encoding,
                ) as current_file:
                    raw_data = workspace_filesystem_manager.singleton.read_file(
                        current_file
                    )
                    workspace_data = self.handle_deep_merging(
                        workspace_data,
                        raw_data,
                    )

            configuration_workspace_target_filesystem_paths = [
                Path(f"{configuration_workspace_filesystem_path}/group/selection"),
                Path(f"{configuration_workspace_filesystem_path}/project/selection"),
            ]
            for (
                current_configuration_workpsace_target_filesystem_path
            ) in configuration_workspace_target_filesystem_paths:
                extracted_target_filesystem_paths = (
                    current_configuration_workpsace_target_filesystem_path.iterdir()
                )

                if not current_configuration_workpsace_target_filesystem_path.is_dir():
                    continue

                for (
                    current_extracted_target_filesystem_path
                ) in extracted_target_filesystem_paths:
                    if not current_extracted_target_filesystem_path.is_file():
                        continue

                    workspace_filesystem_paths.append(
                        current_extracted_target_filesystem_path
                    )
                    with Path.open(
                        current_extracted_target_filesystem_path.resolve(),
                        encoding=file_io_manager.singleton.file_encoding,
                    ) as current_file:
                        raw_data = workspace_filesystem_manager.singleton.read_file(
                            current_file
                        )
                        workspace_data = self.handle_deep_merging(
                            workspace_data,
                            raw_data,
                        )

        value_cache_manager.singleton.set_one_value(
            ["workspace"],
            workspace_data,
            output_type=TargetCacheValue.DEFINED,
        )
        value_cache_manager.singleton.set_one_value(
            ["workspace-configuration-filesystem-paths"],
            workspace_filesystem_paths,
            output_type=TargetCacheValue.DEFINED,
        )

    def handle_value_cache_macros_setup(self) -> bool:
        current_root_full_path = value_cache_manager.singleton.get_one_value(
            ["current-root-full-path"],
            output_type=TargetCacheValue.FOLDER_PATH,
        )

        value_cache_manager.singleton.set_one_value(
            ["current-root-selection-full-path"],
            f"{current_root_full_path}/selection",
            output_type=TargetCacheValue.FOLDER_PATH,
        )

        time_zone = (
            value_cache_manager.singleton.get_one_value(
                ["workspace", "data", "time", "zone", "value"],
                output_type=TargetCacheValue.ANY,
            )
            or "local"
        )

        time_manager.singleton.current_time_zone = (
            time_zone_enum_manager.singleton.convert_from_string_to_timezone(time_zone)
        )

        value_cache_manager.singleton.set_one_value(
            ["current-date"], time_manager.singleton.current_iso8601_date
        )

        value_cache_manager.singleton.set_one_value(
            ["current-year"], time_manager.singleton.current_year
        )

        return True

    def handle_macros_parsing_setup(self) -> bool:
        workspace_data = value_cache_manager.singleton.get_one_value(
            ["workspace"],
            output_type=TargetCacheValue.ANY,
        )

        value_cache_macros = {
            "current-date",
            "current-year",
            "current-root-full-path",
            "current-root-selection-full-path",
        }

        value_cache_macros = value_cache_macros | {
            key
            for key, _value in (
                value_cache_manager.singleton.get_one_value(
                    [
                        "workspace",
                        "data",
                        "macros",
                        "value-cache",
                        "targets",
                    ],
                    output_type=TargetCacheValue.ANY,
                )
                or {}
            ).items()
        }

        file_macros = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "macros",
                    "file",
                    "targets",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        )

        resolved_macros = {
            key: f"{
                value_cache_manager.singleton.get_one_value(
                    [key],
                    output_type=TargetCacheValue.ANY,
                )
            }"
            for key in value_cache_macros
        } | {key: f"{item['value']}" for key, item in file_macros.items()} or {}

        resolved_macros = macros_manager.singleton.resolve_many(resolved_macros) or {}

        value_cache_manager.singleton.set_one_value(
            ["workspace-macros"],
            resolved_macros,
            output_type=TargetCacheValue.DEFINED,
        )

        value_cache_manager.singleton.set_one_value(
            ["workspace"],
            macros_manager.singleton.parse_many(workspace_data, resolved_macros),
            output_type=TargetCacheValue.DEFINED,
        )

        return True

    def handle_logs_setup(self) -> bool:
        current_root_full_path = value_cache_manager.singleton.get_one_value(
            ["current-root-full-path"],
            output_type=TargetCacheValue.FOLDER_PATH,
        )
        current_date = value_cache_manager.singleton.get_one_value(
            ["current-date"],
            output_type=TargetCacheValue.DEFINED,
        )
        log_file_targets = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "log",
                    "file",
                    "targets",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or []
        )
        temporary_log_file_targets = []
        for item in log_file_targets:
            if "full-path" in item:
                temporary_log_file_targets.append(item["full-path"])

        log_file_targets = [
            *temporary_log_file_targets,
            f"{current_root_full_path}/workspace/private/temporary/log/{current_date}.log",
        ]
        is_logging_enabled = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "log",
                    "is-enabled",
                    "value",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or False
        )
        is_logging_verbose_enabled = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "log",
                    "is-verbose",
                    "value",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or False
        )
        is_logging_override_enabled = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "log",
                    "is-enabled",
                    "is-override",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or False
        )
        is_logging_verbose_override_enabled = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "log",
                    "is-verbose",
                    "is-override",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or False
        )
        is_log_file_enabled = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "log",
                    "file",
                    "is-enabled",
                    "value",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or True
        )

        file_log_manager.singleton.options = LogOptions(
            is_enabled=is_logging_enabled
            if is_logging_override_enabled
            else is_log_file_enabled,
            is_verbose_enabled=is_logging_verbose_enabled
            if is_logging_verbose_override_enabled
            else (
                value_cache_manager.singleton.get_one_value(
                    [
                        "workspace",
                        "data",
                        "log",
                        "file",
                        "is-verbose",
                        "value",
                    ],
                    output_type=TargetCacheValue.ANY,
                )
                or True
            ),
        )
        console_log_manager.singleton.options = LogOptions(
            is_enabled=is_logging_enabled
            if is_logging_override_enabled
            else (
                value_cache_manager.singleton.get_one_value(
                    [
                        "workspace",
                        "data",
                        "log",
                        "console",
                        "is-enabled",
                        "value",
                    ],
                    output_type=TargetCacheValue.ANY,
                )
                or True
            ),
            is_verbose_enabled=is_logging_verbose_enabled
            if is_logging_verbose_override_enabled
            else (
                value_cache_manager.singleton.get_one_value(
                    [
                        "workspace",
                        "data",
                        "log",
                        "console",
                        "is-verbose",
                        "value",
                    ],
                    output_type=TargetCacheValue.ANY,
                )
                or False
            ),
        )

        if (
            is_logging_enabled
            if is_logging_override_enabled
            else is_log_file_enabled or False
        ):
            for current_log_file_target in log_file_targets:
                file_log_manager.singleton.add_file_output(current_log_file_target)

        return True

    def handle_toolset_configuration_file_data_extraction_setup(self) -> bool:
        original_executing_console_full_path = (
            value_cache_manager.singleton.get_one_value(
                ["original-executing-console-full-path"],
                output_type=TargetCacheValue.FOLDER_PATH,
            )
        )

        target_filesystem_paths = (
            Path(
                f"{original_executing_console_full_path}/project/configuration"
            ).iterdir()
            or {}
        )
        for current_configuration_file in target_filesystem_paths:
            if not current_configuration_file.is_file():
                continue

            with Path.open(
                current_configuration_file.resolve(),
                encoding=file_io_manager.singleton.file_encoding,
            ) as current_file:
                raw_data = workspace_filesystem_manager.singleton.read_file(
                    current_file
                )

                value_cache_manager.singleton.set_one_value(
                    [
                        f"qlogicae-logis/project/configuration/{current_configuration_file.name}-raw"
                    ],
                    (({} if raw_data is None else raw_data) or {}),
                    output_type=TargetCacheValue.DEFINED,
                )
                value_cache_manager.singleton.set_one_value(
                    [
                        f"qlogicae-logis/project/configuration/{current_configuration_file.name}-full-path"
                    ],
                    current_configuration_file.resolve(),
                    output_type=TargetCacheValue.FILE_PATH,
                )

    def handle_toolset_configuration_data_setup(self) -> bool:
        toolset_about_raw_data = (
            value_cache_manager.singleton.get_one_value(
                [
                    "qlogicae-logis/project/configuration/about.json-raw",
                    "data",
                ],
                output_type=TargetCacheValue.DEFINED,
            )
            or {}
        )

        toolset_about = {}
        toolset_about_table = {}
        for key, item in toolset_about_raw_data.items():
            if "name" not in item:
                continue

            if "value" not in item:
                toolset_about[key] = item
                toolset_about[key]["value"] = "None"

            else:
                toolset_about[key] = item

                if "is-tabular" not in item or item["is-tabular"]:
                    toolset_about_table[key] = item

        value_cache_manager.singleton.set_one_value(
            ["toolset-about"],
            toolset_about,
            output_type=TargetCacheValue.DEFINED,
        )
        value_cache_manager.singleton.set_one_value(
            ["toolset-about-table"],
            toolset_about_table,
            output_type=TargetCacheValue.DEFINED,
        )

        return True

    def handle_workspace_selection_setup(self) -> bool:
        project_workspace_selections = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "selection",
                    "project",
                    "targets",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        ).items()

        group_workspace_selections = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "selection",
                    "group",
                    "targets",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        ).items()

        default_workspace_selection_set = {"all", "root", "group", "project"}

        project_workspace_selection_set = set(
            key for key, _value in project_workspace_selections
        )
        group_workspace_selection_set = set(
            key for key, _value in group_workspace_selections
        )

        value_cache_manager.singleton.set_one_value(
            ["default-workspace-selections"], default_workspace_selection_set
        )
        value_cache_manager.singleton.set_one_value(
            ["project-workspace-selections"], project_workspace_selection_set
        )
        value_cache_manager.singleton.set_one_value(
            ["group-workspace-selections"], group_workspace_selection_set
        )

        value_cache_manager.singleton.set_one_value(
            ["workspace-selections"],
            default_workspace_selection_set
            | project_workspace_selection_set
            | group_workspace_selection_set,
        )

        return True

    def handle_clean_scripts_setup(self) -> bool:
        current_root_full_path = value_cache_manager.singleton.get_one_value(
            ["current-root-full-path"],
            output_type=TargetCacheValue.FOLDER_PATH,
        )
        current_root_selection_full_path = value_cache_manager.singleton.get_one_value(
            ["current-root-selection-full-path"],
            output_type=TargetCacheValue.FOLDER_PATH,
        )
        project_workspace_selections = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "selection",
                    "project",
                    "targets",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        )

        clean_include_targets = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "script",
                    "clean",
                    "include",
                    "targets",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        )

        clean_exclude_targets = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "script",
                    "clean",
                    "exclude",
                    "targets",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or []
        )
        clean_exclude_targets = (
            {
                item["full-path"] if "full-path" in item else ""
                for item in clean_exclude_targets
            }
            | {
                f"{current_root_full_path}",
                f"{current_root_full_path}/workspace",
                f"{current_root_selection_full_path}",
            }
            | {
                f"{item['full-path']}"
                if "full-path" in item
                else current_root_full_path
                for _key, item in project_workspace_selections.items()
            }
        )

        value_cache_manager.singleton.set_one_value(
            ["clean-include-selections"], clean_include_targets
        )

        value_cache_manager.singleton.set_one_value(
            ["clean-exclude-selections"], clean_exclude_targets
        )

        return True

    def handle_deep_merging(
        self,
        left: Any,
        right: Any,
    ) -> Any:
        if left is None:
            return deepcopy(right)

        if right is None:
            return deepcopy(left)

        if isinstance(left, dict) and isinstance(right, dict):
            result = deepcopy(left)

            for key, value in right.items():
                if key in result:
                    result[key] = self.handle_deep_merging(
                        result[key],
                        value,
                    )
                else:
                    result[key] = deepcopy(value)

            return result

        if isinstance(left, list) and isinstance(right, list):
            return deepcopy(left) + deepcopy(right)

        return deepcopy(right)

    def handle_cli_argument_set_invalid(self, cli_arguments: Any) -> bool:
        log_manager.singleton.log_info(
            f"'{cli_arguments}' is not an existing cli option set"
        )

        return True


singleton = WorkspaceManager()
