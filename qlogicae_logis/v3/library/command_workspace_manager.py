from __future__ import annotations

from typing import Any

from ..library.decorator_manager import DecoratorManager

__all__ = (
    "CommandWorkspaceManager"
)

_TaskManager: Any = None
_ImportManager: Any = None
_DisplayManager: Any = None
_DatabaseManager: Any = None
_DecoratorManager = DecoratorManager
_CommandStorageManager: Any = None
_ValueCacheDatabaseManager: Any = None
_PersistentCacheDatabasManager: Any = None
_FileEntityFileSystemTreeSetupOptions: Any = None
_FolderEntityFileSystemTreeSetupOptions: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _TaskManager
    global _ImportManager
    global _DisplayManager
    global _CommandStorageManager
    global _DatabaseManager
    global _ValueCacheDatabaseManager
    global _PersistentCacheDatabasManager
    global _FileEntityFileSystemTreeSetupOptions
    global _FolderEntityFileSystemTreeSetupOptions

    from .._vendor.qlogicae_cor.v2.library import (
        file_entity_filesystem_tree_setup_options,
        folder_entity_filesystem_tree_setup_options,
    )
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
                    .read_command_name("workspace_export"),
                self.run_command_workspace_export,
            ),
            (
                self._command_storage_manager
                    .read_command_name("workspace_import"),
                self.run_command_workspace_import,
            ),
            (
                self._command_storage_manager
                    .read_command_name("workspace_setup"),
                self.run_command_workspace_setup,
            ),
            (
                self._command_storage_manager
                    .read_command_name("workspace_replenish"),
                self.run_command_workspace_replenish,
            ),
            (
                self._command_storage_manager
                    .read_command_name("workspace_install"),
                self.run_command_workspace_install,
            ),
            (
                self._command_storage_manager
                    .read_command_name("workspace_list_exports"),
                self.run_command_workspace_list_exports,
            ),
        ))

    def run_command_workspace_export(
        self,
        **kwargs: Any
    ) -> bool:
        if not kwargs:
            return False

        def handle_workspace_export_group(target: str) -> bool:
            if not target or target not in command_export_group:
                return False

            export_group = (
                command_export_group[target]
            )
            is_enabled_value = (
                self._value_cache_database_manager
                    .read_object_is_enabled_value(
                        export_group
                    )
            )
            if not is_enabled_value:
                return False

            export_group_selections = (
                self._value_cache_database_manager
                    .read_object_is_enabled_value(
                        export_group
                    )
            )

            for key in export_group_selections:
                if not key:
                    continue

                if key in command_export_group:
                    handle_workspace_export_group(
                        key
                    )

                elif key in command_export_selection:
                    handle_workspace_export_selection(
                        key
                    )

            return True

        def handle_workspace_export_selection(target: str) -> bool:
            export_selection = (
                command_export_selection
                    .get(target, {}) or {}
            )
            if target in default_export_selection_data:
                if not export_selection:
                    export_selection = (
                        default_export_selection_data
                            .get(target, {}) or {}
                    )

            export_selection_is_enabled_value = (
                self._value_cache_database_manager
                    .read_object_is_enabled_value(
                        export_selection
                    )
            )
            if not export_selection_is_enabled_value:
                return False

            export_selection_input_exclude_targets = (
                self._value_cache_database_manager
                    .read_object_input_exclude_targets(
                        export_selection
                    )
            )
            export_selection_input_exclude_targets = (
                self._value_cache_database_manager
                    .read_object_pattern_values(
                        export_selection_input_exclude_targets
                    )
            )
            export_selection_input_include_targets = (
                self._value_cache_database_manager
                    .read_object_input_include_targets(
                        export_selection
                    )
            )
            export_selection_input_include_targets = (
                self._value_cache_database_manager
                    .read_object_filesystem_pattern_values(
                        export_selection_input_include_targets
                    )
            )
            export_selection_input_include_targets = (
                self._database_manager
                    .read_object_filtered_export_included(
                        export_selection_input_include_targets,
                        export_selection_input_exclude_targets
                    )
            )

            export_selection_output_targets = (
                self._value_cache_database_manager
                    .read_object_output_targets(
                        export_selection
                    )
            )
            export_selection_output_targets = (
                self._value_cache_database_manager
                    .read_object_filesystem_values(
                        export_selection_output_targets
                    )
            )
            export_selection_compression_format_value = (
                self._value_cache_database_manager
                    .read_object_compression_format_value(
                        export_selection
                    )
            )
            export_selection_compression_type_value = (
                self._value_cache_database_manager
                    .read_object_compression_type_value(
                        export_selection
                    )
            )
            export_selection_compression_level_value = (
                self._value_cache_database_manager
                    .read_object_compression_level_value(
                        export_selection
                    )
            )
            export_selection_compression_is_zip_64_allowed_value = (
                self._value_cache_database_manager
                    .read_object_compression_is_zip_64_allowed_value(
                        export_selection
                    )
            )
            export_selection_compression_is_timestamp_strict_value = (
                self._value_cache_database_manager
                    .read_object_compression_is_timestamp_strict_value(
                        export_selection
                    )
            )

            temporary_copy_items = []
            temporary_output_path = (
                f"{export_temporary_output_filesystem_path}/{target}"
            )
            for include_target in export_selection_input_include_targets:
                if not include_target:
                    continue

                temporary_input_path = (
                    f"{root_filesystem_path}/{include_target}"
                )
                temporary_output_target_path = (
                    f"{temporary_output_path}/{include_target}"
                )

                temporary_copy_items.append(
                    {
                        "input": temporary_input_path,
                        "output": temporary_output_target_path
                    }
                )

            for item in temporary_copy_items:
                if not item or "input" not in item or "output" not in item:
                    continue

                input_path = (item.get("input", "") or "")
                output_path = (item.get("output", "") or "")
                if not input_path or not output_path:
                    continue

                self._import_manager.copy_filesystem_paths(
                    source_path=input_path,
                    target_paths=(output_path,),
                )

            for export_selection_output_target in export_selection_output_targets:
                destination = (
                    f"{export_selection_output_target}.{export_selection_compression_format_value}"
                )

                self._import_manager.compress(
                    source=temporary_output_path,
                    destination=destination,
                    mode="w",
                    compression=export_selection_compression_type_value,
                    compresslevel=export_selection_compression_level_value,
                    allowZip64=export_selection_compression_is_zip_64_allowed_value,
                    strict_timestamps=export_selection_compression_is_timestamp_strict_value,
                )

            return True

        self._task_manager.run_task_common_setup()
        self._task_manager.run_task_export_group_setup()
        self._task_manager.run_task_export_selection_setup()
        self._task_manager.run_task_filesystem_clean_exclude_setup()
        self._task_manager.run_task_filesystem_clean_include_setup()

        targets = (kwargs.get("targets", []) or [])
        if len(targets) < 1:
            return False

        root_filesystem_path = (
            self._value_cache_database_manager
                .read_root_filesystem_path()
        )
        command_export_group = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_export_group()
        )
        command_export_selection = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_export_selection()
        )
        command_export_cleanup_before_is_enabled = (
            self._value_cache_database_manager
                .read_con_wor_data_export_cleanup_before_is_enabled_value()
        )
        command_export_cleanup_after_is_enabled = (
            self._value_cache_database_manager
                .read_con_wor_data_export_cleanup_after_is_enabled_value()
        )
        export_groups = (
            self._value_cache_database_manager
                .read_export_group()
        )
        export_selections = (
            self._value_cache_database_manager
                .read_export_selection()
        )
        export_selection_values = (
            self._database_manager
                .read_object_selection_origins(
                    export_selections
                )
        )
        default_export_selection_data = (
            self._database_manager
                .read_default_export_selection_data()
        )
        export_temporary_output_filesystem_path = (
            self._database_manager
                .read_temporary_export_output_filesystem_path()
        )

        if command_export_cleanup_before_is_enabled:
            self._task_manager.run_task_safe_clean_filesystem_path(
                target_path=export_temporary_output_filesystem_path
            )

        for target in targets:
            if not target:
                continue

            if target == "all":
                for selection in export_selection_values:
                    handle_workspace_export_selection(
                        selection
                    )

            elif target in export_groups:
                handle_workspace_export_group(
                    export_groups[target]
                )

            elif target in export_selections:
                handle_workspace_export_selection(
                    export_selections[target]
                )

        if command_export_cleanup_after_is_enabled:
            self._task_manager.run_task_safe_clean_filesystem_path(
                target_path=export_temporary_output_filesystem_path
            )

        return True

    def run_command_workspace_import(
        self,
        **kwargs: Any
    ) -> bool:
        if not kwargs:
            return False

        self._task_manager.run_task_common_setup()

        input_path = (kwargs.get("input_path", "") or "")
        output_path = (kwargs.get("output_path", "") or "")
        if not input_path or not output_path:
            return False

        if not self._import_manager.is_filesystem_path_valid(
            value=input_path
        ):
            return False

        self._import_manager.uncompress_zip(
            archive_path=input_path,
            destination_path=output_path,
        )

        return True

    def run_command_workspace_replenish(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()
        self._task_manager.run_task_workspace_group_setup()
        self._task_manager.run_task_workspace_project_setup()

        root_filesystem_path = (
            self._value_cache_database_manager
                .read_root_filesystem_path()
        )
        workspace_selection_project = {
            value
            for _key, value
            in self._value_cache_database_manager
                .read_workspace_project().items()
        }
        workspace_selection_group = {
            value
            for _key, value
            in self._value_cache_database_manager
                .read_workspace_group().items()
        }
        default_filesystem_accessibility_types = (
            self._database_manager
                .read_default_filesystem_accessibility_types()
        )
        company_name = (
            self._database_manager
                .read_company_name()
        )
        project_name = (
            self._database_manager
                .read_project_name()
        )
        active_major_version_label = (
            self._database_manager
                .read_active_major_version_label()
        )

        default_content = ""

        filesystem_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="filesystem",
            entities=[],
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

        target_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="target",
            entities=[],
        )

        log_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="log",
            entities=[],
        )

        cache_disk_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
            name="cache",
            entities=[
                _FolderEntityFileSystemTreeSetupOptions(
                    name="disk",
                    entities=[

                    ],
                )
            ],
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
                    ],
                ),
                _FolderEntityFileSystemTreeSetupOptions(
                    name="group",
                    entities=[
                        selection_sub_tree,
                        filesystem_sub_tree,
                    ],
                ),
                _FolderEntityFileSystemTreeSetupOptions(
                    name="project",
                    entities=[
                        selection_sub_tree,
                        filesystem_sub_tree,
                    ],
                ),
                _FolderEntityFileSystemTreeSetupOptions(
                    name="root",
                    entities=[
                        filesystem_sub_tree,
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
                    ],
                ),
                log_sub_tree,
                cache_disk_sub_tree,
            ],
        )

        root_filesystem_tree = _FolderEntityFileSystemTreeSetupOptions(
            entities=[
                _FolderEntityFileSystemTreeSetupOptions(
                    name=f".{company_name}",
                    entities=[
                        _FolderEntityFileSystemTreeSetupOptions(
                            name=project_name,
                            entities=[
                                _FolderEntityFileSystemTreeSetupOptions(
                                    name=active_major_version_label,
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

        self._import_manager.setup_filesystem_tree(
            root_path=root_filesystem_path,
            tree=root_filesystem_tree,
        )

        for current_scope in default_filesystem_accessibility_types:
            for current_workspace_selection in workspace_selection_project:
                target_filesystem_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
                    entities=[
                        _FolderEntityFileSystemTreeSetupOptions(
                            name=f".{company_name}",
                            entities=[
                                _FolderEntityFileSystemTreeSetupOptions(
                                    name=project_name,
                                    entities=[
                                        _FolderEntityFileSystemTreeSetupOptions(
                                            name=active_major_version_label,
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
                self._import_manager.setup_filesystem_tree(
                    root_path=root_filesystem_path,
                    tree=target_filesystem_sub_tree,
                )

            for current_workspace_selection in workspace_selection_group:
                target_filesystem_sub_tree = _FolderEntityFileSystemTreeSetupOptions(
                    entities=[
                        _FolderEntityFileSystemTreeSetupOptions(
                            name=f".{company_name}",
                            entities=[
                                _FolderEntityFileSystemTreeSetupOptions(
                                    name=project_name,
                                    entities=[
                                        _FolderEntityFileSystemTreeSetupOptions(
                                            name=active_major_version_label,
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

                self._import_manager.setup_filesystem_tree(
                    root_path=root_filesystem_path,
                    tree=target_filesystem_sub_tree,
                )

        return True

    def run_command_workspace_list_exports(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()
        self._task_manager.run_task_export_group_setup()
        self._task_manager.run_task_export_selection_setup()

        value = {}
        export_groups = (
            self._value_cache_database_manager.read_export_group()
        ) or {}
        if export_groups:
            value["groups"] = export_groups

        export_selections = (
            self._value_cache_database_manager.read_export_selection()
        ) or {}
        if export_selections:
            value["selections"] = export_selections

        if not value:
            return False

        self._display_manager.display_tree_object(
            value=value,
        )

        return True

    def run_command_workspace_setup(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()

        return True

    def run_command_workspace_install(
        self,
        **kwargs: Any
    ) -> bool:
        def handle_workspace_install(target: str) -> bool:
            if not target or target not in selection_projects:
                return False

            selection_project_installation = (
                (data_selection_projects
                    .get(target, {}) or {})
                    .get("installation", {}) or {}
            )
            if not selection_project_installation:
                return False

            selection_project_installation_is_enabled_value = (
                self._value_cache_database_manager
                    .read_object_is_enabled_value(
                        selection_project_installation
                    )
            )
            if not selection_project_installation_is_enabled_value:
                return False

            selection_project_installation_is_operating_system_included = (
                self._value_cache_database_manager
                    .read_is_object_operating_system_included(
                        selection_project_installation
                    )
            )
            if not selection_project_installation_is_operating_system_included:
                return False

            selection_project_installation_filesystem_path_value = (
                self._value_cache_database_manager
                    .read_object_filesystem_path_value(
                        selection_project_installation
                    )
            )
            if not selection_project_installation_filesystem_path_value:
                return False

            selection_project_installation_scripts = (
                self._value_cache_database_manager
                    .read_object_scripts(
                        selection_project_installation
                    )
            )
            selection_project_installation_delay_value = (
                self._value_cache_database_manager.read_object_delay_value(
                    selection_project_installation
                )
            )
            self._import_manager.time_delay(
                value=selection_project_installation_delay_value
            )

            self._task_manager.navigate_via_filesystem_path(
                selection_project_installation_filesystem_path_value
            )

            for installation_script in selection_project_installation_scripts:
                if not installation_script:
                    continue

                installation_script_is_enabled_value = (
                    self._value_cache_database_manager
                        .read_object_is_enabled_value(
                            installation_script
                        )
                )
                if not installation_script_is_enabled_value:
                    continue

                installation_script_is_operating_system_included = (
                    self._value_cache_database_manager
                        .read_is_object_operating_system_included(
                            installation_script
                        )
                )
                if not installation_script_is_operating_system_included:
                    continue

                installation_script_run_value = (
                    self._value_cache_database_manager
                        .read_object_run_value(
                            installation_script
                        )
                )
                if not installation_script_run_value:
                    continue

                installation_script_process_value = (
                    self._value_cache_database_manager
                        .read_object_process_value(
                            installation_script
                        )
                )

                installation_script_delay_value = (
                    self._value_cache_database_manager.read_object_delay_value(
                        installation_script
                    )
                )

                self._import_manager.time_delay(
                    value=installation_script_delay_value
                )

                cli_output = (
                    self._import_manager.run_command(
                        script_process=installation_script_process_value,
                        command=installation_script_run_value,
                    )
                )

                self._import_manager.log_cache_info_to_file(
                    message=f"{cli_output}"
                )

            self._task_manager.navigate_via_filesystem_path(
                root_filesystem_path
            )

            return True

        self._task_manager.run_task_common_setup()
        self._task_manager.run_task_workspace_default_setup()
        self._task_manager.run_task_workspace_group_setup()
        self._task_manager.run_task_workspace_project_setup()
        self._task_manager.run_task_filesystem_clean_exclude_setup()
        self._task_manager.run_task_filesystem_clean_include_setup()

        if not kwargs:
            self._import_manager.log_cache_warning_to_file(
                message="invalid arguments"
            )
            return False

        targets = (kwargs.get("targets", []) or [])
        if not targets or len(targets) < 1:
            self._import_manager.log_cache_warning_to_file(
                message="no targets selected"
            )
            return False

        root_filesystem_path = (
            self._value_cache_database_manager
                .read_root_filesystem_path()
        )
        data_selection_projects = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_workspace_project_selection()
        )
        selection_projects = (
            self._value_cache_database_manager
                .read_workspace_project()
        )

        for target in targets:
            if not target or target not in selection_projects:
                self._import_manager.log_cache_warning_to_file(
                    message=f"'{target}' is not a valid workspace"
                )
                continue

            handle_workspace_install(
                selection_projects.get(
                    target,
                    ""
                ) or ""
            )

        return True
