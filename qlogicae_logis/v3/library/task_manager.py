from __future__ import annotations

from typing import Any, ParamSpec, TypeVar

from ..library.decorator_manager import DecoratorManager

P = ParamSpec("P")
R = TypeVar("R")


__all__ = (
    "TaskManager"
)

_ImportManager: Any = None
_DatabaseManager: Any = None
_TaskStorageManager: Any = None
_DecoratorManager = DecoratorManager
_ValueCacheDatabaseManager: Any = None
_PersistentCacheDatabasManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _ImportManager
    global _DatabaseManager
    global _TaskStorageManager
    global _ValueCacheDatabaseManager
    global _PersistentCacheDatabasManager

    from ..library import (
        database_manager,
        import_manager,
        persistent_cache_database_manager,
        task_storage_manager,
        value_cache_database_manager,
    )

    _ImportManager = (
        import_manager.ImportManager
    )
    _DatabaseManager = (
        database_manager.DatabaseManager
    )
    _ValueCacheDatabaseManager = (
        value_cache_database_manager.ValueCacheDatabaseManager
    )
    _TaskStorageManager = (
        task_storage_manager.TaskStorageManager
    )
    _PersistentCacheDatabasManager = (
        persistent_cache_database_manager.PersistentCacheDatabasManager
    )

    _handle_dynamic_imports = lambda: None


class TaskManager:
    __slots__ = (
        "_import_manager",
        "_database_manager",
        "_task_storage_manager",
        "_value_cache_database_manager",
        "_persistent_cache_database_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

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
        self._task_storage_manager = (
            _ImportManager.read_singleton(
                _TaskStorageManager
            )
        )

    def setup_command_name(
        self,
        value: str
    ) -> str:
        return (
            f"{value.replace("_", "-")}"
        )

    @_DecoratorManager.single_task_decorator
    def run_task_system_values(self) -> bool:
        self._value_cache_database_manager.write_current_timestamp()
        self._value_cache_database_manager.write_current_date()
        self._value_cache_database_manager.write_current_year()
        self._value_cache_database_manager.write_default_time_zone_name()
        self._value_cache_database_manager.write_default_operating_system_name()
        self._value_cache_database_manager.write_default_operating_system_architecture()

        return True


    @_DecoratorManager.single_task_decorator
    def run_task_root_filesystem_path(
        self,
    ) -> bool:
        self._value_cache_database_manager.write_root_filesystem_path()

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_selection_filesystem_path(
        self,
    ) -> bool:
        self._value_cache_database_manager.write_selection_filesystem_path()

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_executing_console_filesystem_paths(
        self,
    ) -> bool:
        self._value_cache_database_manager.write_initial_executing_console_filesystem_path(
            self._import_manager
                .read_original_executing_console_filesystem_path()
        )
        self._value_cache_database_manager.write_previous_executing_console_filesystem_path(
            self._value_cache_database_manager
                .read_initial_executing_console_filesystem_path()
        )
        self._value_cache_database_manager.write_current_executing_console_filesystem_path(
            self._value_cache_database_manager
                .read_initial_executing_console_filesystem_path()
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_disk_cache_output_folder_path(
        self,
    ) -> bool:
        self._import_manager.setup_filesystem_tree_path(
            target_path=(
                self._database_manager.read_default_cache_disk_output_folder_path()
            )
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_disk_cache_output_file_path(
        self,
    ) -> bool:
        self._import_manager.write_database_path_via_disk_cache(
            self._database_manager.read_default_disk_cache_output_file_path()
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_disk_cache_startup(
        self,
    ) -> bool:
        self._import_manager.open_via_disk_cache()

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_disk_cache_refresh(self) -> bool:
        for _index in range(5):
            self._persistent_cache_database_manager.write_refresh_data(
                {}
            )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_initial_console_filesystem_path(
        self,
    ) -> bool:
        self.navigate_via_root_filesystem_path()

        return True

    @_DecoratorManager.single_task_decorator
    def navigate_via_root_filesystem_path(
        self,
    ) -> bool:

        self.navigate_via_filesystem_path(
            self._value_cache_database_manager.read_root_filesystem_path()
        )

        return True

    def navigate_via_filesystem_path(
        self,
        filesystem_path: str
    ) -> bool:

        self._value_cache_database_manager.write_previous_executing_console_filesystem_path(
            self._value_cache_database_manager
                .read_original_executing_console_filesystem_path()
        )
        self._import_manager.write_current_executing_console_filesystem_path(
            filesystem_path=filesystem_path
        )
        self._value_cache_database_manager.write_current_executing_console_filesystem_path(
            filesystem_path
        )

        return True

    def run_task_configuration_workspace(
        self,
        accessibility_type: str
    ) -> bool:
        is_modified = (
            self._value_cache_database_manager
                .read_is_configuration_workspace_modified()
        ) or False

        file_extensions = (
            self._database_manager
                .read_default_data_file_extensions()
        )

        value_data: Any = {}
        configuration_workspace_data: Any = {}
        base_paths = (
            self._database_manager.read_configuration_workspace_base_file_paths(
                accessibility_type
            )
        )
        base_directory_filesystem_paths = (
            self._database_manager.read_configuration_workspace_base_folder_paths(
                accessibility_type
            )
        )

        for base_path in base_paths:
            for file_extension in (
                file_extensions
            ):
                file_path = (
                    f"{base_path}{file_extension}"
                )

                if not self._import_manager.is_file_path_valid(value=file_path):
                    continue

                value_metadata = (
                    self._database_manager
                        .read_file_metadata(
                            file_path
                        )
                )

                cached_metadata = (
                    self._persistent_cache_database_manager.read_configuration_workspace_metadata(
                        accessibility_type,
                        file_path,
                    )
                )

                value_data_timestamp_modified = (
                    self._database_manager
                        .read_object_property_timestamp_modified_value(
                            value_metadata
                        )
                ) or 1
                cached_timestamp_modified = (
                    self._database_manager
                        .read_object_property_timestamp_modified_value(
                            cached_metadata
                        )
                ) or 2

                if (
                    cached_timestamp_modified != value_data_timestamp_modified
                ):
                    value_data = (
                        self._database_manager
                            .read_configuration_workspace_data_file(
                                file_path
                            )
                    )

                    self._persistent_cache_database_manager.write_configuration_workspace_data(
                        accessibility_type,
                        file_path,
                        value_data,
                    )
                    self._persistent_cache_database_manager.write_configuration_workspace_metadata(
                        accessibility_type,
                        file_path,
                        value_metadata,
                    )

                    is_modified = True

                else:
                    value_data = (
                        self._persistent_cache_database_manager.read_configuration_workspace_data(
                            accessibility_type,
                            file_path,
                        )
                    )
                    value_metadata = cached_metadata

                configuration_workspace_data[file_path] = (
                    self._value_cache_database_manager
                        .read_file_data(
                            value_data,
                            value_metadata
                        )
                )

        for base_path in (
            base_directory_filesystem_paths
        ):
            if not self._import_manager.is_folder_path_valid(value=base_path):
                continue

            file_paths = (
                self._import_manager.
                    read_child_folder_paths(
                        value=base_path
                    )
            )

            for file_path in file_paths:
                file_path = f"{file_path}"
                if (
                    self._import_manager.is_file_path_valid(value=file_path)
                    and self._import_manager.read_file_suffix(value=file_path)
                    in file_extensions
                ):
                    value_metadata = (
                        self._database_manager
                            .read_file_metadata(
                                file_path
                            )
                    )

                    cached_metadata = (
                        self._persistent_cache_database_manager.read_configuration_workspace_metadata(
                            accessibility_type,
                            file_path,
                        )
                    )

                    value_data_timestamp_modified = (
                        self._database_manager
                            .read_object_property_timestamp_modified_value(
                                value_metadata
                            )
                    ) or 1
                    cached_timestamp_modified = (
                        self._database_manager
                            .read_object_property_timestamp_modified_value(
                                cached_metadata
                            )
                    ) or 2

                    if (
                        cached_timestamp_modified != value_data_timestamp_modified
                    ):
                        value_data = (
                            self._database_manager
                                .read_configuration_workspace_data_file(
                                    file_path
                                )
                        )

                        self._persistent_cache_database_manager.write_configuration_workspace_data(
                            accessibility_type,
                            file_path,
                            value_data,
                        )
                        self._persistent_cache_database_manager.write_configuration_workspace_metadata(
                            accessibility_type,
                            file_path,
                            value_metadata,
                        )

                        is_modified = True

                    else:
                        value_data = (
                            self._persistent_cache_database_manager.read_configuration_workspace_data(
                                accessibility_type,
                                file_path,
                            )
                        )
                        value_metadata = cached_metadata

                    configuration_workspace_data[file_path] = (
                        self._value_cache_database_manager
                            .read_file_data(
                                value_data,
                                value_metadata
                            )
                    )

        file_count = (
            len(configuration_workspace_data)
        )
        cached_file_count = (
            self._persistent_cache_database_manager
                .read_configuration_workspace_file_count(
                    accessibility_type
                )
        )

        if file_count != cached_file_count:
            self._persistent_cache_database_manager.write_configuration_workspace_file_count(
                accessibility_type,
                file_count
            )

            is_modified = True

        self._value_cache_database_manager.write_is_configuration_workspace_modified(
            is_modified
        )
        self._value_cache_database_manager.write_configuration_workspace_file_count(
            accessibility_type,
            file_count
        )
        self._value_cache_database_manager.write_configuration_workspace(
            accessibility_type,
            configuration_workspace_data
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_private_configuration_workspace_extraction(
        self,
    ) -> bool:
        self.run_task_configuration_workspace(
            "private",
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_public_configuration_workspace_extraction(
        self,
    ) -> bool:
        self.run_task_configuration_workspace(
            "public",
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_configuration_workspace_object_merging(
        self,
    ) -> bool:
        is_modified = (
            self._value_cache_database_manager
                .read_is_configuration_workspace_modified()
        ) or False
        if is_modified:
            merged_data: Any = {}
            configuration_workspace = (
                self._value_cache_database_manager
                    .read_private_configuration_workspace() |
                self._value_cache_database_manager
                    .read_public_configuration_workspace()
            )

            for _key, item in configuration_workspace.items():
                merged_data = (
                    self._import_manager.object_deep_merge(
                        left=merged_data,
                        right=item.get("data", {})
                    )
                )

            self._persistent_cache_database_manager.write_merged_configuration_workspace_data(
                merged_data
            )
            self._value_cache_database_manager.write_merged_configuration_workspace_data(
                merged_data
            )
        else:
            self._value_cache_database_manager.write_merged_configuration_workspace_data(

                    self._persistent_cache_database_manager
                        .read_merged_configuration_workspace_data()
            )

        self._value_cache_database_manager.remove_configuration_workspace()

        return True

    def run_task_plugins(
        self,
        accessibility_type: str
    ) -> bool:
        if (
            not self._value_cache_database_manager
                .read_configuration_workspace_data_plugin_import_is_enabled_value()
        ):
            self._value_cache_database_manager.write_plugin_raw(
                accessibility_type,
                {}
            )

            return True

        plugin_data: Any = {}
        filesystem_path = (
            f"{
                self._database_manager.read_root_plugin_filesystem_path(
                    accessibility_type
                )
            }"
        )
        file_paths = self._import_manager.read_python_filesystem_paths(
            path=f"{filesystem_path}"
        )

        if len(file_paths) < 1:
            self._value_cache_database_manager.write_plugin_raw(
                accessibility_type,
                plugin_data
            )

            return True

        for file_path in file_paths:
            if not file_path:
                continue

            file_path = f"{file_path}"

            plugin_data[file_path] = (
                self._database_manager.read_plugin_data(
                    self._import_manager.read_python_file(
                        file_path=file_path
                    )
                )
            )

        self._value_cache_database_manager.write_plugin_raw(
            accessibility_type,
            plugin_data
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_private_plugin_extraction(
        self,
    ) -> bool:
        self.run_task_plugins(
            "private",
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_public_plugin_extraction(
        self,
    ) -> bool:
        self.run_task_plugins(
            "public",
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_plugin_object_merging(
        self,
    ) -> bool:
        plugin_raw = (
            self._value_cache_database_manager
                .read_plugin_private_raw() |
            self._value_cache_database_manager
                .read_plugin_public_raw()
        )
        merged_data: Any = {}

        for _key, item in plugin_raw.items():
            merged_data = (
                self._import_manager.object_deep_merge(
                    left=merged_data,
                    right=item
                )
            )

        self._value_cache_database_manager.write_plugin_data(
            merged_data
        )

        self._value_cache_database_manager.remove_plugin_raw()

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_static_macros_extraction(
        self,
    ) -> bool:
        macros: Any = {}
        default_static_value_cache_macros_values: Any = (
            self._value_cache_database_manager
                .read_default_object_macros_values(
                    self._database_manager
                        .read_default_static_value_cache_macros()
                )
        )
        configuration_workspace_data_macros_static_value_cache_targets: Any = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_macros_static_value_cache_targets()
        )
        configuration_workspace_data_macros_static_file_targets: Any = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_macros_static_file_targets()
        )
        plugin_data_macros_static_targets: Any = (
            self._value_cache_database_manager
                .read_plugin_data_macros_static_targets()
        )

        macros = (
            default_static_value_cache_macros_values |
            configuration_workspace_data_macros_static_value_cache_targets |
            configuration_workspace_data_macros_static_file_targets |
            plugin_data_macros_static_targets
        )

        self._value_cache_database_manager.write_macros(
            macros
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_static_macros_object_merging(
        self,
    ) -> bool:
        macros: Any = (
            self._value_cache_database_manager.read_macros()
        )
        macros = (
            self._value_cache_database_manager
                .read_object_macros(
                    macros
            )
        )

        self._value_cache_database_manager.write_macros(
            macros
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_static_macros_resolution(
        self,
    ) -> bool:
        macros: Any = (
            self._value_cache_database_manager.read_macros()
        )
        macros = (
            self._import_manager
                .macros_resolve_many(
                    values=macros
                )
        )

        self._value_cache_database_manager.write_macros(
            macros
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_dynamic_macros_resolution(
        self,
    ) -> bool:
        macros: Any = (
            self._value_cache_database_manager.read_macros()
        )

        default_dynamic_value_cache_macros_values: Any = (
            self._value_cache_database_manager
                .read_default_object_macros_values(
                    self._database_manager
                        .read_default_dynamic_value_cache_macros()
                )
        )
        default_dynamic_value_cache_macros_values = (
            self._value_cache_database_manager
                .read_object_macros(
                    default_dynamic_value_cache_macros_values
            )
        )
        plugin_data_macros_dynamic_targets: Any = (
            self._value_cache_database_manager
                .read_plugin_data_macros_dynamic_targets()
        )
        plugin_data_macros_dynamic_targets = (
            self._value_cache_database_manager
                .read_object_macros(
                    plugin_data_macros_dynamic_targets
                )
        )

        self._value_cache_database_manager.write_macros(
            macros |
            default_dynamic_value_cache_macros_values |
            plugin_data_macros_dynamic_targets
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_configuration_workspace_macros_resolution(
        self,
    ) -> bool:
        resolved_macros: Any = (
            self._value_cache_database_manager
                .read_macros()
        )
        configuration_workspace_data: Any = (
            self._value_cache_database_manager
                .read_merged_configuration_workspace_data()
        )

        configuration_workspace_data = (
            self._import_manager
                .macros_parse_many(
                    values=configuration_workspace_data,
                    resolved=resolved_macros
                )
        )
        self._value_cache_database_manager.write_merged_configuration_workspace_data(
            configuration_workspace_data
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_console_logging_setup(
        self,
    ) -> bool:
        is_enabled_value = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_log_is_enabled_value()
        )
        is_enabled_override = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_log_is_enabled_override()
        )
        is_verbose_value = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_log_is_verbose_value()
        )
        is_verbose_override = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_log_is_verbose_override()
        )
        console_is_enabled_value = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_log_console_is_enabled_value()
        )
        console_is_verbose_value = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_log_console_is_verbose_value()
        )

        console_is_enabled_value = (
            is_enabled_value
            if is_enabled_override
            else console_is_enabled_value
        )
        console_is_verbose_value = (
            is_verbose_value
            if is_verbose_override
            else console_is_verbose_value
        )

        self._import_manager.setup_console_log_settings(
            is_enabled=console_is_enabled_value,
            is_verbose=console_is_verbose_value,
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_file_logging_setup(
        self,
    ) -> bool:
        is_enabled_value = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_log_is_enabled_value()
        )
        is_enabled_override = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_log_is_enabled_override()
        )
        is_verbose_value = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_log_is_verbose_value()
        )
        is_verbose_override = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_log_is_verbose_override()
        )
        file_is_enabled_value = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_log_file_is_enabled_value()
        )
        file_is_verbose_value = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_log_file_is_verbose_value()
        )
        file_targets = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_log_file_targets()
        )
        default_file_output_is_enabled_value = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_log_default_file_output_is_enabled_value()
        )
        default_file_outputs = (
            self._database_manager
                .read_default_log_output_filesystem_paths()
        )

        file_is_enabled_value = (
            is_enabled_value
            if is_enabled_override
            else file_is_enabled_value
        )
        file_is_verbose_value = (
            is_verbose_value
            if is_verbose_override
            else file_is_verbose_value
        )
        file_targets = (
            self._value_cache_database_manager
                .read_object_filesystem_values(
                    file_targets
                )
        )
        if default_file_output_is_enabled_value:
            file_targets = (
                default_file_outputs |
                file_targets
            )

        self._import_manager.setup_file_log_settings(
            is_enabled=file_is_enabled_value,
            is_verbose=file_is_verbose_value,
            file_outputs=file_targets,
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_file_logging_shutdown(
        self,
    ) -> bool:
        self._import_manager.log_shutdown()

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_filesystem_values(self) -> bool:
        self._value_cache_database_manager.write_time_zone_name(
            self._value_cache_database_manager
                .read_configuration_workspace_data_time_zone_value()
        )
        self._value_cache_database_manager.write_operating_system_name(
            self._value_cache_database_manager
                .read_configuration_workspace_data_operating_system_name_value()
        )
        self._value_cache_database_manager.write_operating_system_architecture(
            self._value_cache_database_manager
                .read_configuration_workspace_data_operating_system_architecture_value()
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_workflow_setup(self) -> bool:
        data = (
            self._value_cache_database_manager
                .read_object_selections(
                    self._value_cache_database_manager
                        .read_configuration_workspace_data_workflow_selection()
                )
        )

        self._value_cache_database_manager.write_workflow_selection(
            data
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_export_group_setup(self) -> bool:
        data = (
            self._value_cache_database_manager
                .read_object_selections(
                    self._value_cache_database_manager
                        .read_configuration_workspace_data_export_group()
                ) | self._database_manager
                        .read_default_export_groups()
        )
        self._value_cache_database_manager.write_export_group(
            data
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_export_selection_setup(self) -> bool:
        data = (
            self._value_cache_database_manager
                .read_object_selections(
                    self._value_cache_database_manager
                        .read_configuration_workspace_data_export_selection()
                ) | self._database_manager
                        .read_default_export_selections()
        )
        self._value_cache_database_manager.write_export_selection(
            data
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_workspace_group_setup(self) -> bool:
        data = (
            self._value_cache_database_manager
                .read_object_selections(
                    self._value_cache_database_manager
                        .read_configuration_workspace_data_workspace_group_selection()
                ) | self._database_manager
                        .read_default_groups()
        )

        self._value_cache_database_manager.write_workspace_group(
            data
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_workspace_project_setup(self) -> bool:
        data = (
            self._value_cache_database_manager
                .read_object_selections(
                    self._value_cache_database_manager
                        .read_configuration_workspace_data_workspace_project_selection()
                )
        )

        self._value_cache_database_manager.write_workspace_project(
            data
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_workspace_default_setup(self) -> bool:
        data = (
            self._database_manager
                .read_default_selection_targets()
        )

        self._value_cache_database_manager.write_workspace_default(
            data
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_filesystem_clean_exclude_setup(self) -> bool:
        defaults = (
            self._value_cache_database_manager
                        .read_default_clean_excluded()
        )

        data = (
            self._value_cache_database_manager
                .read_object_exclude_filesystem_path_values(
                    self._value_cache_database_manager
                        .read_configuration_workspace_data_command_filesystem_clean_exclude_targets()
                ) | defaults
        )

        self._value_cache_database_manager.write_filesystem_clean_excluded(
            data
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_filesystem_clean_include_setup(self) -> bool:
        defaults = (
            self._value_cache_database_manager
                .read_default_clean_included()
        )

        data = (
            self._value_cache_database_manager
                .read_object_command_filesystem_clean_included(
                    self._value_cache_database_manager
                        .read_configuration_workspace_data_command_filesystem_clean_include_selection()
                ) | defaults
        )

        self._value_cache_database_manager.write_filesystem_clean_included(
            data
        )

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_disk_cache_shutdown(self) -> bool:
        self._import_manager.close_via_disk_cache()

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_disk_cache_cleanup_before(self) -> bool:
        is_enabled = (
            self._value_cache_database_manager
                .read_con_wor_data_cache_cleanup_before_is_enabled_value()
        )
        if is_enabled:
            self._import_manager.clear_all_values_via_disk_cache()

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_disk_cache_cleanup_after(self) -> bool:
        is_enabled = (
            self._value_cache_database_manager
                .read_con_wor_data_cache_cleanup_after_is_enabled_value()
        )
        if is_enabled:
            self._import_manager.clear_all_values_via_disk_cache()

        return True

    @_DecoratorManager.multi_task_decorator
    def run_task_system_setup(self) -> bool:
        self.run_task_system_values()
        self.run_task_root_filesystem_path()
        self.run_task_selection_filesystem_path()
        self.run_task_executing_console_filesystem_paths()
        self.run_task_initial_console_filesystem_path()
        self.run_task_disk_cache_output_folder_path()
        self.run_task_disk_cache_output_file_path()
        self.run_task_disk_cache_startup()
        self.run_task_disk_cache_cleanup_before()
        self.run_task_disk_cache_refresh()

        return True

    @_DecoratorManager.multi_task_decorator
    def run_task_common_setup(self) -> bool:
        self.run_task_system_setup()
        self.run_task_private_configuration_workspace_extraction()
        self.run_task_public_configuration_workspace_extraction()
        self.run_task_private_plugin_extraction()
        self.run_task_public_plugin_extraction()
        self.run_task_configuration_workspace_object_merging()
        self.run_task_filesystem_values()
        self.run_task_plugin_object_merging()
        self.run_task_static_macros_extraction()
        self.run_task_static_macros_object_merging()
        self.run_task_static_macros_resolution()
        self.run_task_dynamic_macros_resolution()
        self.run_task_configuration_workspace_macros_resolution()
        self.run_task_console_logging_setup()

        return True

    @_DecoratorManager.multi_task_decorator
    def run_task_full_debug_value_cache_setup(self) -> bool:
        self.run_task_common_setup()
        self.run_task_filesystem_clean_exclude_setup()
        self.run_task_filesystem_clean_include_setup()
        self.run_task_workflow_setup()
        self.run_task_workspace_default_setup()
        self.run_task_workspace_project_setup()
        self.run_task_workspace_group_setup()
        self.run_task_export_selection_setup()
        self.run_task_export_group_setup()

        return True

    @_DecoratorManager.multi_task_decorator
    def run_task_full_debug_disk_cache_setup(self) -> bool:
        self.run_task_system_setup()

        return True

    @_DecoratorManager.single_task_decorator
    def run_task_full_shutdown(self) -> bool:
        self.run_task_disk_cache_cleanup_after()
        self.run_task_disk_cache_shutdown()
        self.run_task_file_logging_setup()
        self.run_task_file_logging_shutdown()

        return True

    @_DecoratorManager.multi_task_decorator
    def run_task_safe_clean_filesystem_path(
        self,
        target_path: str
    ) -> bool:
        self.run_task_filesystem_clean_exclude_setup()

        filesystem_clean_excluded = (
            self._value_cache_database_manager.read_filesystem_clean_excluded()
        ) or {}
        if target_path in filesystem_clean_excluded:
            return False

        self._import_manager.clean_filesystem_path(
            target_path=target_path
        )

        return True
