from __future__ import annotations

from typing import Any

_Path: Any = None
_chain: Any = None
_ZipFile: Any = None
_Callable: Any = None
_LogManager: Any = None
_MacrosManager: Any = None
_DatabaseManager: Any = None
_SingletonManager: Any = None
_FilesystemManager: Any = None
_ThreadPoolExecutor: Any = None
_EnumConversionValue: Any = None
_ConsoleDisplayManager: Any = None
_CommandUtilityManager: Any = None
_FilesystemCompressionManager: Any = None
_FileEntityFileSystemTreeSetupOptions: Any = None
_FolderEntityFileSystemTreeSetupOptions: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _Path
    global _chain
    global _ZipFile
    global _Callable
    global _LogManager
    global _MacrosManager
    global _DatabaseManager
    global _SingletonManager
    global _FilesystemManager
    global _ThreadPoolExecutor
    global _EnumConversionValue
    global _ConsoleDisplayManager
    global _CommandUtilityManager
    global _FilesystemCompressionManager
    global _FileEntityFileSystemTreeSetupOptions
    global _FolderEntityFileSystemTreeSetupOptions

    from collections.abc import Callable
    from concurrent.futures import ThreadPoolExecutor
    from itertools import chain
    from pathlib import Path
    from zipfile import ZipFile

    from qlogicae_cor.v1.library import (
        console_display_manager,
        enum_conversion_value,
        file_entity_filesystem_tree_setup_options,
        filesystem_compression_manager,
        filesystem_manager,
        folder_entity_filesystem_tree_setup_options,
        macros_manager,
        singleton_manager,
    )

    from qlogicae_logis.v2.library import (
        command_utility_manager,
        database_manager,
        log_manager,
    )

    _Path = Path
    _chain = chain
    _ZipFile = ZipFile
    _Callable = Callable
    _ThreadPoolExecutor = (
        ThreadPoolExecutor
    )
    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _DatabaseManager = (
        database_manager.DatabaseManager
    )
    _MacrosManager = (
        macros_manager.MacrosManager
    )
    _LogManager = (
        log_manager.LogManager
    )
    _FilesystemManager = (
        filesystem_manager.FilesystemManager
    )
    _FilesystemCompressionManager = (
        filesystem_compression_manager.FilesystemCompressionManager
    )
    _ConsoleDisplayManager = (
        console_display_manager.ConsoleDisplayManager
    )
    _EnumConversionValue = (
        enum_conversion_value.EnumConversionValue
    )
    _CommandUtilityManager = (
        command_utility_manager.CommandUtilityManager
    )
    _FileEntityFileSystemTreeSetupOptions = (
        file_entity_filesystem_tree_setup_options
            .FileEntityFileSystemTreeSetupOptions
    )
    _FolderEntityFileSystemTreeSetupOptions = (
        folder_entity_filesystem_tree_setup_options
            .FolderEntityFileSystemTreeSetupOptions
    )

    _handle_dynamic_imports = lambda: None

class CommandWorkspaceManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()

    @property
    def default_workspace_export_name(self) -> str:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        return (
            f"{database_manager.setup_company_project_major_version("-")}"
        )

    @property
    def default_workspace_export_file(self) -> str:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        return (
            f"{database_manager.setup_company_project_major_version("-")}.zip"
        )

    def run_command_workspace_list_exports(self) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )
        console_display_manager = _SingletonManager.get_singleton(
            _ConsoleDisplayManager
        )

        workspace_export_groups = list(
            database_manager.workspace_export_groups
        )
        workspace_export_selections = list(
            database_manager.workspace_export_selections
        )

        workspace_export_groups.sort()
        workspace_export_selections.sort()

        console_display_manager.render_one_component(
            "\n".join(
                _chain(
                    (
                        f"[red]group <- {item}[/]"
                        for item
                        in workspace_export_groups
                    ),
                    (
                        f"[green]selection <- {item}[/]"
                        for item
                        in workspace_export_selections
                    ),
                )
            )
        )

        return True

    def run_command_workspace_import(
        self,
        **kwargs: Any
    ) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        input_path = kwargs.get("input_path", "")
        output_path = kwargs.get("output_path", "")

        root_filesystem_path = (
            database_manager
                .root_filesystem_path
        )

        if not input_path:
            input_path = self.default_workspace_export_file

        if not output_path:
            output_path = root_filesystem_path

        _SingletonManager.get_singleton(
            _FilesystemCompressionManager
        ).zip_extract(
            input_path,
            output_path
        )

        return True

    def run_command_workspace_setup(
        self,
    ) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )
        filesystem_manager = _SingletonManager.get_singleton(
            _FilesystemManager
        )

        root_filesystem_path = (
            database_manager
                .root_filesystem_path
        )

        workspace_selection_project = (
            database_manager
                .workspace_selection_project
        )

        workspace_selection_group = (
            database_manager
                .workspace_selection_group
        )

        default_filesystem_accessibility_types = (
            database_manager
                .default_filesystem_accessibility_types
        )
        default_content = (
            "data:\n\nmetadata:\n"
        )

        filesystem_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="filesystem",
            entities=[],
        )

        specific_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="specific",
            entities=[],
        )

        fragment_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="fragment",
            entities=[specific_sub_tree],
        )

        workspace_gitignore_file = _FileEntityFileSystemTreeSetupOptions(
            name=".gitignore",
            content="private/**/*",
        )

        workspace_private_gitignore_file = _FileEntityFileSystemTreeSetupOptions(
            name=".gitignore", content="*"
        )

        configuration_workspace_root_file = _FileEntityFileSystemTreeSetupOptions(
            name="root.yaml",
            content=default_content,
        )

        configuration_workspace_group_file = _FileEntityFileSystemTreeSetupOptions(
            name="group.yaml",
            content=default_content,
        )

        configuration_workspace_project_file = _FileEntityFileSystemTreeSetupOptions(
            name="project.yaml",
            content=default_content,
        )

        selection_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="selection",
            entities=[],
        )

        filesystem_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="filesystem",
            entities=[],
        )

        specific_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="specific",
            entities=[],
        )

        fragment_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="fragment",
            entities=[specific_sub_tree],
        )

        target_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="target",
            entities=[],
        )

        log_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="log",
            entities=[],
        )

        configuration_workspace_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="configuration",
            entities=[
                _FolderEntityFileSystemTreeSetupOptions(
                    name="workspace",
                    entities=[
                        _FolderEntityFileSystemTreeSetupOptions(
                            name="group",
                            entities=[
                                selection_sub_tree,
                                configuration_workspace_group_file,
                            ],
                        ),
                        _FolderEntityFileSystemTreeSetupOptions(
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

        template_workspace_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="template",
            entities=[
                _FolderEntityFileSystemTreeSetupOptions(
                    name="all",
                    entities=[
                        filesystem_sub_tree,
                        fragment_sub_tree,
                    ],
                ),
                _FolderEntityFileSystemTreeSetupOptions(
                    name="group",
                    entities=[
                        selection_sub_tree,
                        filesystem_sub_tree,
                        fragment_sub_tree,
                    ],
                ),
                _FolderEntityFileSystemTreeSetupOptions(
                    name="project",
                    entities=[
                        selection_sub_tree,
                        filesystem_sub_tree,
                        fragment_sub_tree,
                    ],
                ),
                _FolderEntityFileSystemTreeSetupOptions(
                    name="root",
                    entities=[
                        filesystem_sub_tree,
                        fragment_sub_tree,
                    ],
                ),
            ],
        )

        temporary_workspace_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="temporary",
            entities=[
                _FolderEntityFileSystemTreeSetupOptions(
                    name="export",
                    entities=[
                        target_sub_tree,
                    ],
                ),
                _FolderEntityFileSystemTreeSetupOptions(
                    name="template",
                    entities=[
                        filesystem_sub_tree,
                        fragment_sub_tree,
                    ],
                ),
                log_sub_tree,
            ],
        )

        root_filesystem_tree = _FolderEntityFileSystemTreeSetupOptions(
            entities=[
                _FolderEntityFileSystemTreeSetupOptions(
                    name=f".{database_manager.company_name}",
                    entities=[
                        _FolderEntityFileSystemTreeSetupOptions(
                            name=database_manager.project_name,
                            entities=[
                                _FolderEntityFileSystemTreeSetupOptions(
                                    name=database_manager.active_major_version_label,
                                    entities=[
                                        _FolderEntityFileSystemTreeSetupOptions(
                                            name="private",
                                            entities=[
                                                configuration_workspace_sub_tree,
                                                template_workspace_sub_tree,
                                                temporary_workspace_sub_tree,
                                                workspace_private_gitignore_file,
                                            ],
                                        ),
                                        _FolderEntityFileSystemTreeSetupOptions(
                                            name="public",
                                            entities=[
                                                configuration_workspace_sub_tree,
                                                template_workspace_sub_tree,
                                            ],
                                        ),
                                        workspace_gitignore_file,
                                    ]
                                )
                            ]
                        )
                    ],
                ),
                selection_sub_tree,
            ]
        )

        filesystem_manager.setup_filesystem_tree(
            root_filesystem_path,
            root_filesystem_tree,
        )

        for current_scope in default_filesystem_accessibility_types:
            for current_workspace_selection in workspace_selection_project:
                target_filesystem_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
                    entities=[
                        _FolderEntityFileSystemTreeSetupOptions(
                            name=f".{database_manager.company_name}",
                            entities=[
                                _FolderEntityFileSystemTreeSetupOptions(
                                    name=database_manager.project_name,
                                    entities=[
                                        _FolderEntityFileSystemTreeSetupOptions(
                                            name=database_manager.active_major_version_label,
                                            entities=[
                                                _FolderEntityFileSystemTreeSetupOptions(
                                                    name=current_scope,
                                                    entities=[
                                                        _FolderEntityFileSystemTreeSetupOptions(
                                                            name="configuration",
                                                            entities=[
                                                                _FolderEntityFileSystemTreeSetupOptions(
                                                                    name="workspace",
                                                                    entities=[
                                                                        _FolderEntityFileSystemTreeSetupOptions(
                                                                            name="project",
                                                                            entities=[
                                                                                _FolderEntityFileSystemTreeSetupOptions(
                                                                                    name="selection",
                                                                                    entities=[
                                                                                        _FileEntityFileSystemTreeSetupOptions(
                                                                                            name=f"{current_workspace_selection}.yaml",
                                                                                            content=default_content,
                                                                                        )
                                                                                    ],
                                                                                )
                                                                            ],
                                                                        )
                                                                    ],
                                                                )
                                                            ],
                                                        ),
                                                        _FolderEntityFileSystemTreeSetupOptions(
                                                            name="template",
                                                            entities=[
                                                                _FolderEntityFileSystemTreeSetupOptions(
                                                                    name="project",
                                                                    entities=[
                                                                        _FolderEntityFileSystemTreeSetupOptions(
                                                                            name="selection",
                                                                            entities=[
                                                                                _FolderEntityFileSystemTreeSetupOptions(
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
                            ]
                        )
                    ]
                )
                filesystem_manager.setup_filesystem_tree(
                    root_filesystem_path,
                    target_filesystem_sub_tree,
                )

            for current_workspace_selection in workspace_selection_group:
                target_filesystem_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
                    entities=[
                        _FolderEntityFileSystemTreeSetupOptions(
                            name=f".{database_manager.company_name}",
                            entities=[
                                _FolderEntityFileSystemTreeSetupOptions(
                                    name=database_manager.project_name,
                                    entities=[
                                        _FolderEntityFileSystemTreeSetupOptions(
                                            name=database_manager.active_major_version_label,
                                            entities=[
                                                _FolderEntityFileSystemTreeSetupOptions(
                                                    name=current_scope,
                                                    entities=[
                                                        _FolderEntityFileSystemTreeSetupOptions(
                                                            name="configuration",
                                                            entities=[
                                                                _FolderEntityFileSystemTreeSetupOptions(
                                                                    name="workspace",
                                                                    entities=[
                                                                        _FolderEntityFileSystemTreeSetupOptions(
                                                                            name="group",
                                                                            entities=[
                                                                                _FolderEntityFileSystemTreeSetupOptions(
                                                                                    name="selection",
                                                                                    entities=[
                                                                                        _FileEntityFileSystemTreeSetupOptions(
                                                                                            name=f"{current_workspace_selection}.yaml",
                                                                                            content=default_content,
                                                                                        )
                                                                                    ],
                                                                                )
                                                                            ],
                                                                        )
                                                                    ],
                                                                )
                                                            ],
                                                        ),
                                                        _FolderEntityFileSystemTreeSetupOptions(
                                                            name="template",
                                                            entities=[
                                                                _FolderEntityFileSystemTreeSetupOptions(
                                                                    name="group",
                                                                    entities=[
                                                                        _FolderEntityFileSystemTreeSetupOptions(
                                                                            name="selection",
                                                                            entities=[
                                                                                _FolderEntityFileSystemTreeSetupOptions(
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

                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        selection_sub_tree
                    ]
                )

                filesystem_manager.setup_filesystem_tree(
                    root_filesystem_path,
                    target_filesystem_sub_tree,
                )

        return True

    def run_command_workspace_export(
        self,
        **kwargs: Any
    ) -> bool:
        def handle_workspace_export_selection(target: str) -> bool:
            if not target or target not in workspace_export_selections:
                log_manager.full_log_warning(
                    f"workspace property "
                    f"'data.export.selection.{target} "
                    "may not exist"
                )
                return False

            export_data_selection = {}
            if target != default_target:
                export_data_selection = workspace_data_command_export_selection[target]

            export_data_selection_is_enabled = (
                export_data_selection["is-enabled"]
                if export_data_selection and "is-enabled" in export_data_selection
                else {}
            ) or {}
            export_data_selection_is_enabled_value = (
                export_data_selection_is_enabled["value"]
                if export_data_selection_is_enabled
                and "value" in export_data_selection_is_enabled
                else True
            )
            if not export_data_selection_is_enabled_value:
                log_manager.full_log_warning(
                    f"workspace property "
                    f"'data.export.selection.{target}."
                    "is-enabled.value' may have been set to 'false'"
                )
                return False

            export_data_selection_output = (
                export_data_selection["output"]
                if export_data_selection
                and "output" in export_data_selection
                else {}
            ) or {}

            export_data_selection_output_full_path = (
                export_data_selection_output["filesystem-path"]
                if export_data_selection_output
                and "filesystem-path" in export_data_selection_output
                else {}
            ) or {}
            export_data_selection_output_full_path_value = (
                export_data_selection_output_full_path["value"]
                if export_data_selection_output_full_path
                and "value" in export_data_selection_output_full_path
                else root_filesystem_path
            ) or root_filesystem_path
            export_data_selection_output_full_path_value = (
                macros_manager.parse_many(
                    export_data_selection_output_full_path_value,
                    workspace_macros
                )
            )

            export_data_selection_input = (
                export_data_selection["input"]
                if export_data_selection and "input" in export_data_selection
                else {}
            ) or {}
            export_data_selection_input_root_path = (
                export_data_selection_input["root-path"]
                if export_data_selection_input
                and "root-path" in export_data_selection_input
                else {}
            ) or {}
            export_data_selection_input_root_path_value = (
                export_data_selection_input_root_path["value"]
                if export_data_selection_input_root_path
                and "value" in export_data_selection_input_root_path
                else root_filesystem_path
            ) or root_filesystem_path

            export_data_selection_input_targets = (
                export_data_selection_input["targets"]
                if export_data_selection_input
                and "targets" in export_data_selection_input
                else []
            ) or []


            if export_default_filesystem_include_is_enabled_value:
                export_data_selection_input_targets = [
                    *export_data_selection_input_targets,
                    *workspace_export_default_filesystem_input,
                ]

            export_data_selection_compression = (
                export_data_selection["compression"]
                if export_data_selection and "compression" in export_data_selection
                else {}
            ) or {}
            # export_data_selection_compression_format = (
            #     export_data_selection_compression["format"]
            #     if export_data_selection_compression
            #     and "format" in export_data_selection_compression
            #     else {}
            # ) or {}
            # export_data_selection_compression_format_value = (
            #     export_data_selection_compression_format["value"]
            #     if export_data_selection_compression_format
            #     and "value" in export_data_selection_compression_format
            #     else "zip"
            # ) or "zip"
            # export_data_selection_compression_format_value = (
            #     export_data_selection_compression_format_value
            #     if export_data_selection_compression_format_value
            #     and "zip" != export_data_selection_compression_format_value
            #     else "zip"
            # ) or "zip"

            export_data_selection_compression_type = (
                export_data_selection_compression["type"]
                if export_data_selection_compression
                and "type" in export_data_selection_compression
                else {}
            ) or {}
            export_data_selection_compression_type_value = (
                export_data_selection_compression_type["value"]
                if export_data_selection_compression_type
                and "value" in export_data_selection_compression_type
                else "deflated"
            ) or "deflated"

            export_data_selection_compression_type_value = (
                filesystem_compression_manager.get_zip_format_compression(
                    export_data_selection_compression_type_value
                )
            )

            export_data_selection_compression_level = (
                export_data_selection_compression["level"]
                if export_data_selection_compression
                and "level" in export_data_selection_compression
                else {}
            ) or {}
            export_data_selection_compression_level_value = (
                export_data_selection_compression_level["value"]
                if export_data_selection_compression_level
                and "value" in export_data_selection_compression_level
                else 6
            ) or 6

            export_data_selection_compression_is_zip_64_allowed = (
                export_data_selection_compression["is-zip-64-allowed"]
                if export_data_selection_compression
                and "is-zip-64-allowed" in export_data_selection_compression
                else {}
            )
            export_data_selection_compression_is_zip_64_allowed_value = (
                export_data_selection_compression_is_zip_64_allowed["value"]
                if export_data_selection_compression_is_zip_64_allowed
                and "value" in export_data_selection_compression_is_zip_64_allowed
                else True
            )

            export_data_selection_compression_is_timestamp_strict = (
                export_data_selection_compression["is-timestamp-strict"]
                if export_data_selection_compression
                and "is-timestamp-strict" in export_data_selection_compression
                else {}
            ) or {}
            export_data_selection_compression_is_timestamp_strict_value = (
                export_data_selection_compression_is_timestamp_strict["value"]
                if export_data_selection_compression_is_timestamp_strict
                and "value"
                in export_data_selection_compression_is_timestamp_strict
                else True
            )

            for (
                current_export_data_selection_input
            ) in export_data_selection_input_targets:
                if (
                    not current_export_data_selection_input
                    or "filesystem-path" not in current_export_data_selection_input
                ):
                    log_manager.full_log_warning(
                        "'workspace export' - workspace property "
                        f"'data.export.selection.{target}.input.targets' "
                        "items must require a "
                        "'filesystem-path' filesystem value"
                    )
                    continue

                current_export_data_selection_input_relative_path = (
                    current_export_data_selection_input["filesystem-path"]
                )
                current_export_data_selection_input_relative_path_value = (
                    current_export_data_selection_input_relative_path["value"]
                    if current_export_data_selection_input_relative_path
                    and "value" in current_export_data_selection_input_relative_path
                    else ""
                ) or ""

                if not current_export_data_selection_input_relative_path_value:
                    log_manager.full_log_warning(
                        "'workspace export' - workspace property "
                        f"'data.export.selection.{target}.input.targets' "
                        "items must require a "
                        "'filesystem-path' filesystem value"
                    )
                    continue

                tmp_input_path = (
                    macros_manager.parse_many(
                        f"{export_data_selection_input_root_path_value}/"
                        f"/{current_export_data_selection_input_relative_path_value}",
                        workspace_macros
                    )
                )

                filesystem_manager.copy_filesystem_path(
                    tmp_input_path,
                    command_utility_manager
                        .setup_export_temporary_targets_output_filesystem_path(
                            target,
                            current_export_data_selection_input_relative_path_value
                        ),
                )

            source = _Path(
                command_utility_manager
                    .setup_export_temporary_targets_source_filesystem_path(
                        target
                    )
            )
            destination = _Path(
                macros_manager.parse_many(
                    f"{export_data_selection_output_full_path_value}/{target}.zip",
                    workspace_macros
                )
            )

            with _ZipFile(
                destination,
                mode="w",
                compression=export_data_selection_compression_type_value,
                compresslevel=export_data_selection_compression_level_value,
                allowZip64=export_data_selection_compression_is_zip_64_allowed_value,
                strict_timestamps=export_data_selection_compression_is_timestamp_strict_value,
            ) as archive:
                for path in source.rglob("*"):
                    archive.write(
                        path,
                        arcname=path.relative_to(source),
                    )

            return True

        def handle_workspace_export_group(target: str) -> bool:
            if not target or target not in workspace_data_command_export_group:
                log_manager.full_log_warning(
                    f"workspace property "
                    f"'data.export.group.{target} "
                    "may not exist"
                )
                return False

            export_data_group = workspace_data_command_export_group[target]
            export_data_group_is_enabled = (
                export_data_group["is-enabled"]
                if export_data_group and "is-enabled" in export_data_group
                else {}
            ) or {}
            export_data_group_is_enabled_value = (
                export_data_group_is_enabled["value"]
                if export_data_group_is_enabled
                and "value" in export_data_group_is_enabled
                else True
            )
            if not export_data_group_is_enabled_value:
                log_manager.full_log_warning(
                    f"workspace property "
                    f"'data.export.group.{target}."
                    "is-enabled.value' may have been set to 'false'"
                )
                return False

            export_data_group_selections = (
                export_data_group["selection"]
                if "selection" in export_data_group else {}
            ) or {}

            with _ThreadPoolExecutor(
                max_workers=min(
                    32,
                    len(export_data_group_selections) or 1,
                ),
            ) as executor:
                futures = []

                for key in export_data_group_selections:
                    if key in workspace_data_command_export_group:
                        futures.append(
                            executor.submit(
                                handle_workspace_export_group,
                                key,
                            )
                        )

                    elif key in workspace_data_command_export_selection:
                        futures.append(
                            executor.submit(
                                handle_workspace_export_selection,
                                key,
                            )
                        )

                for future in futures:
                    future.result()

            return True


        targets = kwargs.get("targets", [])
        default_target = (
            self.default_workspace_export_name
        )
        if not len(targets):
            targets = [default_target]

        log_manager = _SingletonManager.get_singleton(
            _LogManager
        )
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )
        workspace_data_command_export_is_enabled_value = (
            database_manager
                .workspace_data_command_export_is_enabled_value
        )
        if not workspace_data_command_export_is_enabled_value:
            log_manager.full_log_warning(
                "workspace property "
                "'data.export.is-enabled.value' "
                "may have been set to 'false'"
            )
            return False

        command_utility_manager = _SingletonManager.get_singleton(
            _CommandUtilityManager
        )
        filesystem_manager = _SingletonManager.get_singleton(
            _FilesystemManager
        )
        filesystem_compression_manager = _SingletonManager.get_singleton(
            _FilesystemCompressionManager
        )
        macros_manager = _SingletonManager.get_singleton(
            _MacrosManager
        )
        root_filesystem_path = (
            database_manager
                .root_filesystem_path
        )
        workspace_macros = (
            database_manager
                .workspace_macros
        )
        export_default_filesystem_include_is_enabled_value = (
            database_manager
                .workspace_data_command_export_default_filesystem_include_is_enabled_value
        )
        workspace_data_command_export_group = (
            database_manager
                .workspace_data_command_export_group
        )
        workspace_data_command_export_selection = (
            database_manager
                .workspace_data_command_export_selection
        )
        workspace_export_selections = (
            database_manager
                .workspace_export_selections
        )
        workspace_export_groups = (
            database_manager
                .workspace_export_groups
        )
        workspace_export_default_filesystem_input = (
            database_manager
                .workspace_export_default_filesystem_includes
        )
        export_temporary_output_filesystem_path = (
            command_utility_manager
                .setup_export_temporary_output_filesystem_path()
        )
        workspace_data_command_export_cleanup_is_enabled_value = (
            database_manager
                .workspace_data_command_export_cleanup_is_enabled_value
        )

        tasks: list[tuple[_Callable[[str], bool], str]] = []

        if workspace_data_command_export_cleanup_is_enabled_value:
            filesystem_manager.clean_filesystem_path(
                export_temporary_output_filesystem_path
            )

        for target in targets:
            if target == "all":
                tasks.extend(
                    (
                        handle_workspace_export_selection,
                        selection,
                    )
                    for selection in workspace_export_selections
                )

            elif target in workspace_export_groups:
                tasks.append(
                    (
                        handle_workspace_export_group,
                        target,
                    )
                )

            elif target in workspace_export_selections:
                tasks.append(
                    (
                        handle_workspace_export_selection,
                        target,
                    )
                )

            else:
                log_manager.full_log_warning(
                    f"'{target}' does not exist"
                )

        with _ThreadPoolExecutor(
            max_workers=min(32, len(tasks) or 1),
        ) as executor:
            list(
                executor.map(
                    lambda task: task[0](task[1]),
                    tasks,
                )
            )

        if workspace_data_command_export_cleanup_is_enabled_value:
            filesystem_manager.clean_filesystem_path(
                export_temporary_output_filesystem_path
            )

        return True
