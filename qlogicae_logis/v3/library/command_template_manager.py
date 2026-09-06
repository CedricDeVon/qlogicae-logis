from __future__ import annotations

from typing import Any

from ..library.decorator_manager import DecoratorManager

__all__ = (
    "CommandTemplateManager"
)

_LogManager: Any = None
_TaskManager: Any = None
_ImportManager: Any = None
_DisplayManager: Any = None
_DatabaseManager: Any = None
_DecoratorManager = DecoratorManager
_CommandStorageManager: Any = None
_ValueCacheDatabaseManager: Any = None
_PersistentCacheDatabasManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _LogManager
    global _TaskManager
    global _ImportManager
    global _DisplayManager
    global _DatabaseManager
    global _CommandStorageManager
    global _ValueCacheDatabaseManager
    global _PersistentCacheDatabasManager

    from ..library import (
        command_storage_manager,
        database_manager,
        display_manager,
        import_manager,
        log_manager,
        persistent_cache_database_manager,
        task_manager,
        value_cache_database_manager,
    )

    _TaskManager = (
        task_manager
            .TaskManager
    )
    _LogManager = (
        log_manager
            .LogManager
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

    _handle_dynamic_imports = lambda: None

class CommandTemplateManager:
    __slots__ = (
        "_log_manager",
        "_task_manager",
        "_import_manager",
        "_display_manager",
        "_database_manager",
        "_command_storage_manager",
        "_value_cache_database_manager",
        "_persistent_cache_database_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._command_storage_manager = (
            _ImportManager.read_singleton(
                _CommandStorageManager
            )
        )
        self._log_manager = (
            _ImportManager.read_singleton(
                _LogManager
            )
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
                    .read_command_name("template_apply"),
                self.run_command_template_apply,
            ),
            (
                self._command_storage_manager
                    .read_command_name("template_list_selections"),
                self.run_command_template_list_selections,
            ),
        ))

    def run_command_template_apply(
        self,
        **kwargs: Any
    ) -> bool:
        def handle_target_root() -> bool:
            result: bool = True
            destination_temporary_target_filesystem_path = (
                f"{temporary_template_output_filesystem_path}/root/filesystem"
            )
            for accessibility_type in default_filesystem_accessibility_types:
                if not accessibility_type:
                    self._log_manager.log_display_warning(
                        reference=handle_target_root,
                        message="one or more accessibility types are null",
                    )
                    result = False
                    continue

                source_all_filesystem_path = (
                    f"{root_workspace_filesystem_path}/{accessibility_type}/template/all/filesystem"
                )
                source_root_filesystem_path = (
                    f"{root_workspace_filesystem_path}/{accessibility_type}/template/root/filesystem"
                )

                self._import_manager.setup_filesystem_tree_paths(
                    target_paths=(
                        source_all_filesystem_path,
                        source_root_filesystem_path,
                        destination_temporary_target_filesystem_path,
                    ),
                )
                self._import_manager.copy_filesystem_path(
                    source_path=source_all_filesystem_path,
                    target_path=destination_temporary_target_filesystem_path,
                )
                self._import_manager.copy_filesystem_path(
                    source_path=source_root_filesystem_path,
                    target_path=destination_temporary_target_filesystem_path,
                )

            self._import_manager.macros_parse_filesystem(
                filesystem_path=destination_temporary_target_filesystem_path,
                workspace_macros=macros_data,
            )
            self._import_manager.copy_filesystem_path(
                source_path=destination_temporary_target_filesystem_path,
                target_path=root_filesystem_path,
            )

            return result

        def handle_target_group() -> bool:
            result: bool = True
            for selection_group in selection_groups:
                if not selection_group:
                    result = False
                    continue

                result = handle_target_group_selection(
                    selection_group
                ) and result

            return result

        def handle_target_project() -> bool:
            result: bool = True
            for selection_project in selection_projects:
                if not selection_project:
                    result = False
                    continue

                result = handle_target_project_selection(
                    selection_project
                ) and result

            return result

        def handle_target_group_selection(group_target: str) -> bool:
            if not group_target:
                self._log_manager.log_display_warning(
                    reference=handle_target_group_selection,
                    message="target is null",
                )
                return False

            selection_group = (
                data_selection_groups.get(group_target, {}) or {}
            )
            if not selection_group:
                self._log_manager.log_display_warning(
                    reference=handle_target_group_selection,
                    message=f"template group '{group_target}' does not exist",
                )
                return False

            result: bool = True
            selection_group_targets = (
                set(selection_group.get("targets", {})) or set()
            )
            destination_temporary_target_filesystem_path = (
                f"{temporary_template_output_filesystem_path}/group/selection/{group_target}/filesystem"
            )
            for accessibility_type in default_filesystem_accessibility_types:
                if not accessibility_type:
                    self._log_manager.log_display_warning(
                        reference=handle_target_group_selection,
                        message="one or more accessibility types are null",
                    )
                    result = False
                    continue

                source_all_filesystem_path = (
                    f"{root_workspace_filesystem_path}/{accessibility_type}/template/all/filesystem"
                )
                source_group_filesystem_path = (
                    f"{root_workspace_filesystem_path}/{accessibility_type}/template/group/filesystem"
                )
                source_target_filesystem_path = (
                    f"{root_workspace_filesystem_path}/{accessibility_type}/template/group/selection/{group_target}/filesystem"
                )

                self._import_manager.setup_filesystem_tree_paths(
                    target_paths=(
                        source_all_filesystem_path,
                        source_group_filesystem_path,
                        source_target_filesystem_path,
                        destination_temporary_target_filesystem_path,
                    ),
                )
                self._import_manager.copy_filesystem_path(
                    source_path=source_all_filesystem_path,
                    target_path=destination_temporary_target_filesystem_path,
                )
                self._import_manager.copy_filesystem_path(
                    source_path=source_group_filesystem_path,
                    target_path=destination_temporary_target_filesystem_path,
                )
                self._import_manager.copy_filesystem_path(
                    source_path=source_target_filesystem_path,
                    target_path=destination_temporary_target_filesystem_path,
                )

            self._import_manager.macros_parse_filesystem(
                filesystem_path=destination_temporary_target_filesystem_path,
                workspace_macros=macros_data,
            )

            for selection_group_target in selection_group_targets:
                if not selection_group_target:
                    self._log_manager.log_display_warning(
                        reference=handle_target_group_selection,
                        message="one or more targets are null",
                    )
                    result = False
                    continue

                if selection_group_target == "root":
                    source_temporary_target_filesystem_path = (
                        f"{temporary_template_output_filesystem_path}/root/filesystem"
                    )
                    self._import_manager.copy_filesystem_path(
                        source_path=destination_temporary_target_filesystem_path,
                        target_path=source_temporary_target_filesystem_path,
                    )
                    result = handle_target_root() and result

                elif selection_group_target in selection_projects:
                    source_temporary_target_filesystem_path = (
                        f"{temporary_template_output_filesystem_path}/project/selection/{selection_group_target}/filesystem"
                    )
                    self._import_manager.copy_filesystem_path(
                        source_path=destination_temporary_target_filesystem_path,
                        target_path=source_temporary_target_filesystem_path,
                    )
                    result = handle_target_project_selection(
                        selection_group_target
                    ) and result

                elif selection_group_target in selection_groups:
                    source_temporary_target_filesystem_path = (
                        f"{temporary_template_output_filesystem_path}/group/selection/{selection_group_target}/filesystem"
                    )
                    self._import_manager.copy_filesystem_path(
                        source_path=destination_temporary_target_filesystem_path,
                        target_path=source_temporary_target_filesystem_path,
                    )
                    result = handle_target_group_selection(
                        selection_group_target
                    ) and result

            return result

        def handle_target_project_selection(project_target: str) -> bool:
            if not project_target:
                self._log_manager.log_display_warning(
                    reference=handle_target_project_selection,
                    message="target is null",
                )
                return False

            selection_project = (
                data_selection_projects
                    .get(project_target, {}) or {}
            )
            if not selection_project:
                self._log_manager.log_display_warning(
                    reference=handle_target_project_selection,
                    message=f"template project '{project_target}' does not exist",
                )
                return False

            selection_project_filesystem_path_value = (
                (selection_project
                    .get("filesystem-path", {}) or {})
                    .get("value", "")
            )

            if not selection_project_filesystem_path_value:
                self._log_manager.log_display_warning(
                    reference=handle_target_project_selection,
                    message=f"template project '{project_target}' "
                    "filesystem path does not exist",
                )
                return False

            destination_target_filesystem_path = (
                f"{temporary_template_output_filesystem_path}/project/selection/{project_target}/filesystem"
            )
            method_result: bool = True
            for accessibility_type in default_filesystem_accessibility_types:
                if not accessibility_type:
                    self._log_manager.log_display_warning(
                        reference=handle_target_project_selection,
                        message="one or more accessibility types are null",
                    )
                    method_result = False
                    continue

                source_all_filesystem_path = (
                    f"{root_workspace_filesystem_path}/{accessibility_type}/template/all/filesystem"
                )
                source_project_filesystem_path = (
                    f"{root_workspace_filesystem_path}/{accessibility_type}/template/project/filesystem"
                )
                source_target_filesystem_path = (
                    f"{root_workspace_filesystem_path}/{accessibility_type}/template/project/selection/{project_target}/filesystem"
                )

                self._import_manager.setup_filesystem_tree_paths(
                    target_paths=(
                        source_all_filesystem_path,
                        source_project_filesystem_path,
                        source_target_filesystem_path,
                        destination_target_filesystem_path,
                    ),
                )
                self._import_manager.copy_filesystem_path(
                    source_path=source_all_filesystem_path,
                    target_path=destination_target_filesystem_path,
                )
                self._import_manager.copy_filesystem_path(
                    source_path=source_project_filesystem_path,
                    target_path=destination_target_filesystem_path,
                )
                self._import_manager.copy_filesystem_path(
                    source_path=source_target_filesystem_path,
                    target_path=destination_target_filesystem_path,
                )

            self._import_manager.macros_parse_filesystem(
                filesystem_path=destination_target_filesystem_path,
                workspace_macros=macros_data,
            )
            self._import_manager.copy_filesystem_path(
                source_path=destination_target_filesystem_path,
                target_path=selection_project_filesystem_path_value,
            )
            return method_result

        self._task_manager.run_task_common_setup()
        self._task_manager.run_task_workspace_default_setup()
        self._task_manager.run_task_workspace_group_setup()
        self._task_manager.run_task_workspace_project_setup()
        self._task_manager.run_task_filesystem_clean_exclude_setup()
        self._task_manager.run_task_filesystem_clean_include_setup()

        if not kwargs:
            self._log_manager.log_display_warning(
                reference=self.run_command_template_apply,
                message="kwargs is null or an empty object",
            )
            return False

        targets = (kwargs.get("targets", ["all"]) or ["all"])
        if not targets or len(targets) < 1:
            targets = ["all"]

        macros_data = (
            self._value_cache_database_manager
                .read_macros()
        )
        default_filesystem_accessibility_types = (
            self._database_manager
                .read_default_filesystem_accessibility_types()
        )
        data_selection_projects = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_workspace_project_selection()
        )
        selection_projects = (
            self._value_cache_database_manager
                .read_workspace_project()
        )
        selection_projects = (
            self._database_manager
                .read_object_selection_origins(
                    selection_projects
                )
        )
        data_selection_groups = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_workspace_group_selection()
        )
        selection_groups = (
            self._value_cache_database_manager
                .read_workspace_group()
        )
        selection_groups = (
            self._database_manager
                .read_object_selection_origins(
                    selection_groups
                )
        )
        root_filesystem_path = (
            self._value_cache_database_manager
                .read_root_filesystem_path()
        )
        root_workspace_filesystem_path = (
            self._database_manager
                .read_root_workspace_filesystem_path()
        )
        temporary_template_output_filesystem_path = (
            self._database_manager
                .read_temporary_template_output_filesystem_path()
        )
        cleanup_before_is_enabled = (
            self._value_cache_database_manager
                .read_con_wor_data_template_cleanup_before_is_enabled_value()
        )
        cleanup_after_is_enabled = (
            self._value_cache_database_manager
                .read_con_wor_data_template_cleanup_after_is_enabled_value()
        )
        result: bool = True
        if cleanup_before_is_enabled:
            self._task_manager.run_task_safe_clean_filesystem_path(
                target_path=temporary_template_output_filesystem_path
            )

        for target in targets:
            if not target:
                self._log_manager.log_display_warning(
                    reference=self.run_command_template_apply,
                    message="one or more targets are null",
                )
                result = False
                continue

            if target == "all":
                result = handle_target_root() and result
                result = handle_target_group() and result
                result = handle_target_project() and result

            elif target == "root":
                result = handle_target_root() and result

            elif target == "group":
                result = handle_target_group() and result

            elif target == "project":
                result = handle_target_project() and result

            elif target in selection_groups:
                result = handle_target_group_selection(
                    target
                ) and result

            elif target in selection_projects:
                result = handle_target_project_selection(
                    target
                ) and result

            else:
                self._log_manager.log_display_warning(
                    reference=self.run_command_template_apply,
                    message=f"template '{target}' does not exist",
                )
                result = False

        if cleanup_after_is_enabled:
            self._task_manager.run_task_safe_clean_filesystem_path(
                target_path=temporary_template_output_filesystem_path
            )

        return result

    def run_command_template_list_selections(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()
        self._task_manager.run_task_workspace_default_setup()
        self._task_manager.run_task_workspace_group_setup()
        self._task_manager.run_task_workspace_project_setup()

        value = {}
        value_default = (
            self._value_cache_database_manager.read_workspace_default()
        ) or {}
        if value_default:
            value["defaults"] = value_default

        value_project = (
            self._value_cache_database_manager.read_workspace_project()
        ) or {}
        if value_project:
            value["projects"] = value_project

        value_group = (
            self._value_cache_database_manager.read_workspace_group()
        ) or {}
        if value_group:
            value["groups"] = value_group

        value_all = (
            self._value_cache_database_manager.read_workspace_all()
        ) or {}
        if value_all:
            value["all"] = value_all

        if not value:
            return True

        self._display_manager.display_tree_object(
            value=value,
        )

        return True
