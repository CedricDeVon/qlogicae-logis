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
                self._task_manager.setup_command_name("workspace_export"),
                self.run_command_workspace_export,
            ),
            (
                self._task_manager.setup_command_name("workspace_import"),
                self.run_command_workspace_import,
            ),
            (
                self._task_manager.setup_command_name("workspace_setup"),
                self.run_command_workspace_setup,
            ),
            (
                self._task_manager.setup_command_name("workspace_replenish"),
                self.run_command_workspace_replenish,
            ),
            (
                self._task_manager.setup_command_name("workspace_install"),
                self.run_command_workspace_install,
            ),
            (
                self._task_manager.setup_command_name("workspace_list_exports"),
                self.run_command_workspace_list_exports,
            ),
        ))

    @_DecoratorManager.command_decorator
    def run_command_workspace_export(
        self,
        **kwargs: Any
    ) -> bool:
        def handle_workspace_export_group(target: str) -> bool:


            return True

        def handle_workspace_export_selection(target: str) -> bool:


            return True

        self._task_manager.run_task_common_setup()
        self._task_manager.run_task_export_group_setup()
        self._task_manager.run_task_export_selection_setup()
        self._task_manager.run_task_filesystem_clean_exclude_setup()
        self._task_manager.run_task_filesystem_clean_include_setup()

        targets = kwargs.get("targets", [])
        if len(targets) < 1:
            return False

        root_filesystem_path = (
            self._value_cache_database_manager
                .read_root_filesystem_path()
        )
        workspace_data_command_export_group = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_export_group()
        )
        workspace_data_command_export_selection = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_export_selection()
        )
        workspace_data_command_export_cleanup_before_is_enabled = (
            self._value_cache_database_manager
                .read_con_wor_data_export_cleanup_before_is_enabled_value()
        )
        workspace_data_command_export_cleanup_after_is_enabled = (
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

        if workspace_data_command_export_cleanup_before_is_enabled:
            self._task_manager.run_task_safe_clean_filesystem_path(
                target_path=export_temporary_output_filesystem_path
            )

        for target in targets:
            if not target:
                continue

            if target == "all":
                for export_selection in export_selection_values:
                    handle_workspace_export_selection(
                        export_selection
                    )

            elif target in export_groups:
                handle_workspace_export_group(
                    export_groups[target]
                )

            elif target in export_selections:
                handle_workspace_export_selection(
                    export_selections[target]
                )

        if workspace_data_command_export_cleanup_after_is_enabled:
            self._task_manager.run_task_safe_clean_filesystem_path(
                target_path=export_temporary_output_filesystem_path
            )

        return True

    @_DecoratorManager.command_decorator
    def run_command_workspace_import(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()

        input_path = kwargs.get("input_path", "")
        output_path = kwargs.get("output_path", "")
        if not input_path or not output_path:
            return False

        self._import_manager.uncompress_zip(
            archive_path=input_path,
            destination_path=output_path,
        )

        return True

    @_DecoratorManager.command_decorator
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

    @_DecoratorManager.command_decorator
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

    @_DecoratorManager.command_decorator
    def run_command_workspace_setup(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()

        return True

    @_DecoratorManager.command_decorator
    def run_command_workspace_install(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()

        # targets = kwargs.get("targets", [])

        return True
