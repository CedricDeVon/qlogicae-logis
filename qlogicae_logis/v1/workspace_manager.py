from collections.abc import Callable
from pathlib import Path
from typing import Any
from concurrent.futures import ThreadPoolExecutor

from qlogicae_cor.v1.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1 import (
    console_log_manager,
    file_log_manager,
    filesystem_manager,
    log_manager,
    macros_manager,
    object_merge_manager,
    timestamp_manager,
    system_manager,
    time_manager,
    value_cache_manager,
    workspace_export_manager,
    workspace_filesystem_manager,
    workspace_system_manager,
)
from qlogicae_logis.v1.filesystem_manager import (
    FileEntityFileSystemTreeSetupOptions,
    FolderEntityFileSystemTreeSetupOptions,
)
from qlogicae_logis.v1.log_options import (
    LogOptions,
)
from qlogicae_logis.v1.target_cache_value import (
    TargetCacheValue,
)
from qlogicae_logis.v1.workspace_manager_configurations import (
    WorkspaceManagerConfigurations,
)


class WorkspaceManager(AbstractManager[WorkspaceManagerConfigurations]):
    def __init__(self) -> None:
        super().__init__(WorkspaceManagerConfigurations())

    @property
    def current_elapsed_console_execution_start(
        self,
    ) -> float:
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
        self.handle_workspace_configuration_file_data_extraction_setup()
        self.handle_workspace_selection_setup()
        self.handle_value_cache_macros_setup()
        self.handle_macros_parsing_setup()
        self.handle_logs_setup()

        return True

    def shutdown(self) -> bool:
        log_manager.singleton.shutdown()

        return True

    def debug_value_cache(self) -> bool:
        self.setup()

        self.handle_workspace_base_filesystem_replenishment_setup()
        self.handle_workspace_selection_filesystem_replenishment_setup()
        self.handle_toolset_configuration_file_data_extraction_setup()
        self.handle_toolset_configuration_data_setup()
        self.handle_clean_command_setup()
        self.handle_workspace_command_setup()

        value_cache_manager.singleton.display_all_items()

        return True

    def handle_workspace_command_setup(
        self,
    ) -> bool:
        command_export = (
            value_cache_manager.singleton.get_one_value(
                ["workspace", "data", "command", "export"],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        )
        command_export_default = (
            command_export["default"]
            if command_export
            and "default" in command_export else {}
        ) or {}
        command_export_default_filesystem_input = (
            command_export_default["filesystem-input"]
            if command_export_default
            and "filesystem-input" in command_export_default else {}
        ) or {}
        command_export_default_filesystem_input_is_enabled = (
            command_export_default_filesystem_input["is-enabled"]
            if command_export_default_filesystem_input
            and "is-enabled" in command_export_default_filesystem_input else {}
        ) or {}
        command_export_default_filesystem_input_is_enabled_value = (
            command_export_default_filesystem_input_is_enabled["value"]
            if command_export_default_filesystem_input_is_enabled
            and "value" in command_export_default_filesystem_input_is_enabled else True
        )

        command_export_default_group = (
            command_export_default["group"]
            if command_export_default
            and "group" in command_export_default else {}
        ) or {}
        command_export_default_group_is_enabled = (
            command_export_default_group["is-enabled"]
            if command_export_default_group
            and "is-enabled" in command_export_default_group else {}
        ) or {}

        command_export_default_group_is_enabled_value = (
            command_export_default_group_is_enabled["value"]
            if command_export_default_group_is_enabled
            and "value" in command_export_default_group_is_enabled else True
        )

        command_export_default_selection = (
            command_export_default["selection"]
            if command_export_default
            and "selection" in command_export_default else {}
        ) or {}
        command_export_default_selection_is_enabled = (
            command_export_default_selection["is-enabled"]
            if command_export_default_selection
            and "is-enabled" in command_export_default_selection else {}
        ) or {}
        command_export_default_selection_is_enabled_value = (
            command_export_default_selection_is_enabled["value"]
            if command_export_default_selection_is_enabled
            and "value" in command_export_default_selection_is_enabled else True
        )


        command_export_default_filesystem_input_targets = []
        if command_export_default_filesystem_input_is_enabled_value:
            command_export_default_filesystem_input_targets = (
                [
                    {"relative-path": Path("workspace/.gitignore")},
                    {"relative-path": Path("workspace/private/.gitignore")},
                    {"relative-path": Path("workspace/private/configuration")},
                    {"relative-path": Path("workspace/private/template")},
                    {"relative-path": Path("workspace/public/configuration")},
                    {"relative-path": Path("workspace/public/template")},
                ]
            )

        command_export_default_group_targets = set()
        if command_export_default_group_is_enabled_value:
            command_export_default_group_targets = {
                "all"
            }

        command_export_default_selection_targets = set()
        if command_export_default_selection_is_enabled_value:
            command_export_default_selection_targets = {
                workspace_export_manager.singleton.default_export_selection
            }

        command_export_groups = (
            command_export["group"]
            if command_export and "group" in command_export else {}
        ) or {}

        command_export_selections = (
            command_export["selection"]
            if command_export and "selection" in command_export else {}
        ) or {}

        command_export_groups = set(
            key for key, _value in command_export_groups.items()

        ) | command_export_default_group_targets

        command_export_selections = set(
            key for key, _value in command_export_selections.items()
        ) | command_export_default_selection_targets


        value_cache_manager.singleton.set_one_value(
            ["workspace-export-default-filesystem-input"],
            command_export_default_filesystem_input_targets
        )

        value_cache_manager.singleton.set_one_value(
            ["workspace-export-groups"],
            command_export_groups
        )

        value_cache_manager.singleton.set_one_value(
            ["workspace-export-selections"],
            command_export_selections
        )

        return True

    def handle_timestamp_console_execution_start_setup(
        self,
    ) -> bool:
        value_cache_manager.singleton.set_one_value(
            ["timestamp-console-execution-start"],
            time_manager.singleton.current_nanosecond,
        )

        return True

    def handle_timestamp_console_execution_end_setup(
        self,
    ) -> bool:
        value_cache_manager.singleton.set_one_value(
            ["timestamp-console-execution-end"],
            time_manager.singleton.current_nanosecond,
        )

        return True

    def handle_current_root_filesystem_paths_setup(
        self,
    ) -> bool:
        value_cache_manager.singleton.set_one_value(
            ["current-root-full-path"],
            system_manager.singleton.current_executing_console_filesystem_path,
            output_type=TargetCacheValue.FOLDER_PATH,
        )

        return True

    def handle_executing_console_filesystem_paths_setup(
        self,
    ) -> bool:
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

    def handle_current_root_filesystem_navigation_setup(
        self,
    ) -> bool:
        workspace_system_manager.singleton.navigate_to_root()

        return True

    def handle_workspace_base_filesystem_replenishment_setup(
        self,
    ) -> bool:
        current_root_full_path = value_cache_manager.singleton.get_one_value(
            ["current-root-full-path"],
            output_type=TargetCacheValue.FOLDER_PATH,
        )

        workspace_gitignore_file = FileEntityFileSystemTreeSetupOptions(
            name=".gitignore",
            content="private/**/*",
        )

        workspace_private_gitignore_file = FileEntityFileSystemTreeSetupOptions(
            name=".gitignore", content="*"
        )

        configuration_workspace_root_file = FileEntityFileSystemTreeSetupOptions(
            name="root.yaml",
            content="data:\n\nmetadata:\n",
        )

        configuration_workspace_group_file = FileEntityFileSystemTreeSetupOptions(
            name="group.yaml",
            content="data:\n\nmetadata:\n",
        )

        configuration_workspace_project_file = FileEntityFileSystemTreeSetupOptions(
            name="project.yaml",
            content="data:\n\nmetadata:\n",
        )

        selection_sub_tree = FolderEntityFileSystemTreeSetupOptions(
            name="selection",
            entities=[],
        )
        filesystem_sub_tree = FolderEntityFileSystemTreeSetupOptions(
            name="filesystem",
            entities=[],
        )
        specific_sub_tree = FolderEntityFileSystemTreeSetupOptions(
            name="specific",
            entities=[],
        )
        fragment_sub_tree = FolderEntityFileSystemTreeSetupOptions(
            name="fragment",
            entities=[specific_sub_tree],
        )
        target_sub_tree = FolderEntityFileSystemTreeSetupOptions(
            name="target",
            entities=[],
        )
        log_sub_tree = FolderEntityFileSystemTreeSetupOptions(
            name="log",
            entities=[],
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
                                selection_sub_tree,
                                configuration_workspace_group_file,
                            ],
                        ),
                        FolderEntityFileSystemTreeSetupOptions(
                            name="project",
                            entities=[
                                selection_sub_tree,
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
                        filesystem_sub_tree,
                        fragment_sub_tree,
                    ],
                ),
                FolderEntityFileSystemTreeSetupOptions(
                    name="group",
                    entities=[
                        selection_sub_tree,
                        filesystem_sub_tree,
                        fragment_sub_tree,
                    ],
                ),
                FolderEntityFileSystemTreeSetupOptions(
                    name="project",
                    entities=[
                        selection_sub_tree,
                        filesystem_sub_tree,
                        fragment_sub_tree,
                    ],
                ),
                FolderEntityFileSystemTreeSetupOptions(
                    name="root",
                    entities=[
                        filesystem_sub_tree,
                        fragment_sub_tree,
                    ],
                ),
            ],
        )

        temporary_workspace_sub_tree = FolderEntityFileSystemTreeSetupOptions(
            name="temporary",
            entities=[
                FolderEntityFileSystemTreeSetupOptions(
                    name="export",
                    entities=[
                        target_sub_tree,
                    ],
                ),
                FolderEntityFileSystemTreeSetupOptions(
                    name="template",
                    entities=[
                        filesystem_sub_tree,
                        fragment_sub_tree,
                    ],
                ),
                log_sub_tree,
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
                                workspace_private_gitignore_file,
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
                selection_sub_tree,
            ]
        )

        filesystem_manager.singleton.setup_filesystem_tree(
            current_root_full_path,
            root_filesystem_tree,
        )

    def handle_workspace_selection_filesystem_replenishment_setup(
        self,
    ) -> bool:
        current_root_full_path = value_cache_manager.singleton.get_one_value(
            ["current-root-full-path"],
            output_type=TargetCacheValue.FOLDER_PATH,
        )
        project_workspace_selections = (
            value_cache_manager.singleton.get_one_value(
                ["project-workspace-selections"],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        )
        group_workspace_selections = (
            value_cache_manager.singleton.get_one_value(
                ["group-workspace-selections"],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        )

        filesystem_sub_tree = FolderEntityFileSystemTreeSetupOptions(
            name="filesystem",
            entities=[],
        )
        specific_sub_tree = FolderEntityFileSystemTreeSetupOptions(
            name="specific",
            entities=[],
        )
        fragment_sub_tree = FolderEntityFileSystemTreeSetupOptions(
            name="fragment",
            entities=[specific_sub_tree],
        )

        for current_scope in [
            "private",
            "public",
        ]:
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
                                                                        filesystem_sub_tree,
                                                                        fragment_sub_tree,
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
                    current_root_full_path,
                    target_filesystem_sub_tree,
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
                                                                        filesystem_sub_tree,
                                                                        fragment_sub_tree,
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
                    current_root_full_path,
                    target_filesystem_sub_tree,
                )

        return True

    def handle_workspace_configuration_file_data_extraction_setup(
        self,
    ) -> bool:
        current_root_full_path = value_cache_manager.singleton.get_one_value(
            ["current-root-full-path"],
            output_type=TargetCacheValue.FOLDER_PATH,
        )

        def handle_path_1(root: str, scope: str) -> str:
            return f"{root}/workspace/{scope}/configuration/workspace"

        workspace_data = {}
        workspace_filesystem_paths: list[Path] = []

        scope_selections = ["private", "public"]

        for current_scope_selection in scope_selections:
            configuration_workspace_filesystem_path = handle_path_1(
                current_root_full_path,
                current_scope_selection,
            )

            for path in (
                Path(
                    f"{configuration_workspace_filesystem_path}/root.yaml"
                ),
                Path(
                    f"{configuration_workspace_filesystem_path}/project/project.yaml"
                ),
                Path(
                    f"{configuration_workspace_filesystem_path}/group/group.yaml"
                ),
            ):
                if path.is_file():
                    workspace_filesystem_paths.append(path)

            for directory in (
                Path(
                    f"{configuration_workspace_filesystem_path}/group/selection"
                ),
                Path(
                    f"{configuration_workspace_filesystem_path}/project/selection"
                ),
            ):
                if not directory.is_dir():
                    continue

                workspace_filesystem_paths.extend(
                    path
                    for path in directory.iterdir()
                    if path.is_file()
                )

        def read_workspace_file(path: Path) -> dict:
            return (
                workspace_filesystem_manager.singleton.read_file(path)
                or {}
            )

        max_workers = min(32, len(workspace_filesystem_paths) or 1)

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            raw_data_list = list(
                executor.map(
                    read_workspace_file,
                    workspace_filesystem_paths,
                )
            )

        for raw_data in raw_data_list:
            workspace_data = (
                object_merge_manager.singleton.handle_deep_merging(
                    workspace_data,
                    raw_data,
                )
                or {}
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

        return True

    def handle_value_cache_macros_setup(
        self,
    ) -> bool:
        current_root_full_path = value_cache_manager.singleton.get_one_value(
            ["current-root-full-path"],
            output_type=TargetCacheValue.FOLDER_PATH,
        )

        value_cache_manager.singleton.set_one_value(
            ["current-root-selection-full-path"],
            Path(f"{current_root_full_path}/selection"),
            output_type=TargetCacheValue.FOLDER_PATH,
        )

        time_zone = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "time",
                    "zone",
                    "value",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or time_manager.singleton.current_time_zone
        ) or time_manager.singleton.current_time_zone

        time_manager.singleton.current_time_zone = time_zone

        value_cache_manager.singleton.set_one_value(
            ["current-timestamp"],
            timestamp_manager.singleton.current_standard_timestamp,
        )

        value_cache_manager.singleton.set_one_value(
            ["current-date"],
            time_manager.singleton.current_iso8601_date,
        )

        value_cache_manager.singleton.set_one_value(
            ["current-date"],
            time_manager.singleton.current_iso8601_date,
        )

        value_cache_manager.singleton.set_one_value(
            ["current-year"],
            time_manager.singleton.current_year,
        )

        value_cache_manager.singleton.set_one_value(
            ["os-name"],
            system_manager.singleton.operating_system_name,
        )

        value_cache_manager.singleton.set_one_value(
            ["os-architecture"],
            system_manager.singleton.operating_system_architecture,
        )

        return True

    def handle_macros_parsing_setup(self) -> bool:
        workspace_data = value_cache_manager.singleton.get_one_value(
            ["workspace"],
            output_type=TargetCacheValue.ANY,
        )

        workspace_data_macros = (
            value_cache_manager.singleton.get_one_value(
                ["workspace", "data", "macros"],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        ) or {}
        workspace_data_macros_value_cache = (
            workspace_data_macros["value-cache"]
            if "value-cache" in workspace_data_macros
            else {}
        ) or {}
        workspace_data_macros_value_cache_targets = (
            workspace_data_macros_value_cache["targets"]
            if "targets" in workspace_data_macros_value_cache
            else {}
        ) or {}

        workspace_data_macros_default = (
            workspace_data_macros_value_cache["default"]
            if "default" in workspace_data_macros_value_cache
            else {}
        ) or {}
        workspace_data_macros_default_value_cache = (
            workspace_data_macros_default["value-cache"]
            if "value-cache" in workspace_data_macros_default
            else {}
        ) or {}
        workspace_data_macros_default_value_cache_is_enabled = (
            workspace_data_macros_default_value_cache["is-enabled"]
            if "is-enabled" in workspace_data_macros_default_value_cache
            else {}
        ) or {}
        workspace_data_macros_default_value_cache_is_enabled_value = (
            workspace_data_macros_default_value_cache_is_enabled["value"]
            if "value" in workspace_data_macros_default_value_cache_is_enabled
            else True
        )


        value_cache_macros = set()
        if workspace_data_macros_default_value_cache_is_enabled_value:
            value_cache_macros = {
                "current-date",
                "current-year",
                "current-timestamp",
                "current-root-full-path",
                "current-root-selection-full-path",
            }
        workspace_data_macros_value_cache_targets = value_cache_macros | {
            key for key, _value in workspace_data_macros_value_cache_targets.items()
        }

        workspace_data_macros_file = (
            workspace_data_macros["file"] if "file" in workspace_data_macros else {}
        ) or {}
        workspace_data_macros_file_targets = (
            workspace_data_macros_file["targets"]
            if "targets" in workspace_data_macros_file
            else {}
        ) or {}

        resolved_macros = {
            key: f"{
                value_cache_manager.singleton.get_one_value(
                    [key],
                    output_type=TargetCacheValue.ANY,
                )
            }"
            for key in workspace_data_macros_value_cache_targets
        } | {
            key: f"{item['value']}"
            for key, item in workspace_data_macros_file_targets.items()
        } or {}

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
        workspace_data_log = (
            value_cache_manager.singleton.get_one_value(
                ["workspace", "data", "log"],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        )

        workspace_data_log_is_enabled = (
            workspace_data_log["is-enabled"]
            if workspace_data_log and "is-enabled" in workspace_data_log
            else {}
        ) or {}
        workspace_data_log_is_enabled_value = (
            workspace_data_log_is_enabled["value"]
            if workspace_data_log_is_enabled
            and "value" in workspace_data_log_is_enabled
            else True
        )
        workspace_data_log_is_enabled_is_override = (
            workspace_data_log_is_enabled["override"]
            if workspace_data_log_is_enabled
            and "override" in workspace_data_log_is_enabled
            else False
        )

        workspace_data_log_is_verbose = (
            workspace_data_log["is-verbose"]
            if workspace_data_log and "is-verbose" in workspace_data_log
            else {}
        ) or {}
        workspace_data_log_is_verbose_value = (
            workspace_data_log_is_verbose["value"]
            if workspace_data_log_is_verbose
            and "value" in workspace_data_log_is_verbose
            else True
        )
        workspace_data_log_is_verbose_is_override = (
            workspace_data_log_is_verbose["override"]
            if workspace_data_log_is_verbose
            and "override" in workspace_data_log_is_verbose
            else False
        )

        workspace_data_log_file = (
            workspace_data_log["file"] if "file" in workspace_data_log else {}
        ) or {}
        workspace_data_log_file_is_default_included = (
            workspace_data_log_file["is-default-included"]
            if workspace_data_log_file
            and "is-default-included"in workspace_data_log_file
            else {}
        ) or {}
        workspace_data_log_file_is_default_included_value = (
            workspace_data_log_file_is_default_included["value"]
            if workspace_data_log_file_is_default_included
            and "value" in workspace_data_log_file_is_default_included
            else True
        )
        workspace_data_log_file_is_enabled = (
            workspace_data_log_file["is-enabled"]
            if workspace_data_log_file
            and "is-enabled" in workspace_data_log_file
            else {}
        ) or {}
        workspace_data_log_file_is_enabled_value = (
            workspace_data_log_file_is_enabled["value"]
            if workspace_data_log_file_is_enabled
            and "value" in workspace_data_log_file_is_enabled
            else True
        )
        workspace_data_log_file_is_verbose = (
            workspace_data_log_file["is-verbose"]
            if workspace_data_log_file
            and "is-verbose" in workspace_data_log_file
            else {}
        ) or {}
        workspace_data_log_file_is_verbose_value = (
            workspace_data_log_file_is_verbose["value"]
            if workspace_data_log_file_is_verbose
            and "value" in workspace_data_log_file_is_verbose
            else True
        )
        workspace_data_log_file_targets = (
            workspace_data_log_file["targets"]
            if workspace_data_log_file
            and "targets" in workspace_data_log_file
            else []
        ) or []
        if workspace_data_log_file_is_default_included_value:
            temporary_log_file_targets = []
            for item in workspace_data_log_file_targets:
                if item and "full-path" in item:
                    temporary_log_file_targets.append(item["full-path"])

            workspace_data_log_file_targets = [
                *temporary_log_file_targets,
                f"{current_root_full_path}/workspace/private/temporary/log/{current_date}.log",
            ]

        workspace_data_log_console = (
            workspace_data_log["console"]
            if workspace_data_log
            and "console" in workspace_data_log else {}
        ) or {}
        workspace_data_log_console_is_enabled = (
            workspace_data_log_console["is-enabled"]
            if workspace_data_log_console
            and "is-enabled" in workspace_data_log_console
            else {}
        ) or {}
        workspace_data_log_console_is_enabled_value = (
            workspace_data_log_console_is_enabled["value"]
            if workspace_data_log_console_is_enabled
            and "value" in workspace_data_log_console_is_enabled
            else True
        )
        workspace_data_log_console_is_verbose = (
            workspace_data_log_console["is-verbose"]
            if workspace_data_log_console
            and "is-verbose" in workspace_data_log_console
            else {}
        ) or {}
        workspace_data_log_console_is_verbose_value = (
            workspace_data_log_console_is_verbose["value"]
            if workspace_data_log_console_is_verbose
            and "value" in workspace_data_log_console_is_verbose
            else False
        )

        file_log_manager.singleton.options = LogOptions(
            is_enabled=workspace_data_log_is_enabled_value
            if workspace_data_log_is_enabled_is_override
            else workspace_data_log_file_is_enabled_value,
            is_verbose_enabled=workspace_data_log_is_verbose_value
            if workspace_data_log_is_verbose_is_override
            else (workspace_data_log_file_is_verbose_value),
        )
        console_log_manager.singleton.options = LogOptions(
            is_enabled=workspace_data_log_is_enabled_value
            if workspace_data_log_is_enabled_is_override
            else (workspace_data_log_console_is_enabled_value),
            is_verbose_enabled=workspace_data_log_is_verbose_value
            if workspace_data_log_is_verbose_is_override
            else (workspace_data_log_console_is_verbose_value),
        )

        if (
            workspace_data_log_is_enabled_value
            if workspace_data_log_is_enabled_is_override
            else workspace_data_log_file_is_enabled_value
        ):
            for current_log_file_target in workspace_data_log_file_targets:
                file_log_manager.singleton.add_file_output(current_log_file_target)

        return True

    def handle_toolset_configuration_file_data_extraction_setup(
        self,
    ) -> bool:
        original_executing_console_full_path = (
            value_cache_manager.singleton.get_one_value(
                ["original-executing-console-full-path"],
                output_type=TargetCacheValue.FOLDER_PATH,
            )
        )

        configuration_directory = Path(
            f"{original_executing_console_full_path}/project/configuration"
        )

        configuration_files = [
            path
            for path in configuration_directory.iterdir()
            if path.is_file()
        ]

        def read_configuration_file(
            path: Path,
        ) -> tuple[Path, dict]:
            return (
                path,
                (
                    workspace_filesystem_manager.singleton.read_file(path)
                    or {}
                ),
            )

        max_workers = min(32, len(configuration_files) or 1)

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(
                executor.map(
                    read_configuration_file,
                    configuration_files,
                )
            )

        for current_configuration_file, raw_data in results:
            value_cache_manager.singleton.set_one_value(
                [
                    (
                        "qlogicae-logis/project/configuration/"
                        f"{current_configuration_file.name}-raw"
                    )
                ],
                raw_data,
                output_type=TargetCacheValue.DEFINED,
            )

            value_cache_manager.singleton.set_one_value(
                [
                    (
                        "qlogicae-logis/project/configuration/"
                        f"{current_configuration_file.name}-full-path"
                    )
                ],
                current_configuration_file.resolve(),
                output_type=TargetCacheValue.FILE_PATH,
            )

        return True

    def handle_toolset_configuration_data_setup(
        self,
    ) -> bool:
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
        for (
            key,
            item,
        ) in toolset_about_raw_data.items():
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

    def handle_workspace_selection_setup(
        self,
    ) -> bool:
        workspace_selection = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "selection",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        )
        workspace_selection_default = (
            workspace_selection["default"] if "default" in workspace_selection else {}
        ) or {}
        workspace_selection_default_is_default_included = (
            workspace_selection_default["is-default-included"]
            if "is-default-included" in workspace_selection_default
            else {}
        ) or {}
        workspace_selection_default_is_default_included_value = (
            workspace_selection_default_is_default_included["value"]
            if "value" in workspace_selection_default_is_default_included
            else True
        )

        workspace_selection_default_targets = (
            {"all", "root", "group", "project"}
            if workspace_selection_default_is_default_included_value
            else set()
        ) or set()

        workspace_selection_project = (
            workspace_selection["project"] if "project" in workspace_selection else {}
        ) or {}
        workspace_selection_project_targets = (
            workspace_selection_project["targets"].items()
            if "targets" in workspace_selection_project
            else {}
        ) or {}
        workspace_selection_project_targets = set(
            key for key, _value in workspace_selection_project_targets
        )

        workspace_selection_group = (
            workspace_selection["group"] if "group" in workspace_selection else {}
        ) or {}
        workspace_selection_group_targets = (
            workspace_selection_group["targets"].items()
            if "targets" in workspace_selection_group
            else {}
        ) or {}
        workspace_selection_group_targets = set(
            key for key, _value in workspace_selection_group_targets
        )

        value_cache_manager.singleton.set_one_value(
            ["default-workspace-selections"],
            workspace_selection_default_targets,
        )
        value_cache_manager.singleton.set_one_value(
            ["project-workspace-selections"],
            workspace_selection_project_targets,
        )
        value_cache_manager.singleton.set_one_value(
            ["group-workspace-selections"],
            workspace_selection_group_targets,
        )
        value_cache_manager.singleton.set_one_value(
            ["workspace-selections"],
            (
                workspace_selection_default_targets
                | workspace_selection_project_targets
                | workspace_selection_group_targets
            )
            or {},
        )

        return True

    def handle_clean_command_setup(self) -> bool:
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
        workspace_data_command_clean = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "command",
                    "clean",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        )

        workspace_data_command_clean_default = (
            workspace_data_command_clean["default"]
            if "default" in workspace_data_command_clean
            else {}
        ) or {}
        workspace_data_command_clean_default_exclude = (
            workspace_data_command_clean_default["exclude"]
            if "exclude" in workspace_data_command_clean_default
            else {}
        ) or {}
        workspace_data_command_clean_default_exclude_is_enabled = (
            workspace_data_command_clean_default_exclude["is-enabled"]
            if "is-enabled" in workspace_data_command_clean_default_exclude
            else {}
        ) or {}
        workspace_data_command_clean_default_exclude_is_enabled_value = (
            workspace_data_command_clean_default_exclude_is_enabled["value"]
            if "value" in workspace_data_command_clean_default_exclude_is_enabled
            else {}
        )

        workspace_data_command_clean_include = (
            workspace_data_command_clean["include"]
            if "include" in workspace_data_command_clean
            else {}
        ) or {}

        workspace_data_command_clean_excluded = (
            workspace_data_command_clean["excluded"]
            if "excluded" in workspace_data_command_clean
            else {}
        ) or {}

        workspace_data_command_clean_include_targets = (
            workspace_data_command_clean_include["targets"]
            if "targets" in workspace_data_command_clean_include
            else {}
        ) or {}

        workspace_data_command_clean_exclude_targets = (
            workspace_data_command_clean_excluded["targets"]
            if "targets" in workspace_data_command_clean_excluded
            else []
        ) or []

        workspace_data_command_clean_exclude_targets = {
            item["full-path"] if "full-path" in item else ""
            for item in workspace_data_command_clean_exclude_targets
        }
        if workspace_data_command_clean_default_exclude_is_enabled_value:
            workspace_data_command_clean_exclude_targets = (
                workspace_data_command_clean_exclude_targets
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
            ["clean-include-selections"],
            workspace_data_command_clean_include_targets,
        )

        value_cache_manager.singleton.set_one_value(
            ["clean-exclude-selections"],
            workspace_data_command_clean_exclude_targets,
        )

        return True

    def handle_cli_argument_set_invalid(self, cli_arguments: Any) -> bool:
        log_manager.singleton.log_info(
            f"'{cli_arguments}' is not an existing cli option set"
        )

        return True


singleton = WorkspaceManager()


