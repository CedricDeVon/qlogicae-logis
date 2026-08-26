from __future__ import annotations

from typing import Any

from ..library.decorator_manager import DecoratorManager

__all__ = (
    "CommandTemplateManager"
)

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

    _handle_dynamic_imports = lambda: None

class CommandTemplateManager:
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
                self._task_manager.setup_command_name("template_apply"),
                self.run_command_template_apply,
            ),
            (
                self._task_manager.setup_command_name("template_list_selections"),
                self.run_command_template_list_selections,
            ),
        ))

    @_DecoratorManager.command_decorator
    def run_command_template_apply(
        self,
        **kwargs: Any
    ) -> bool:
        # def handle_target_root() -> bool:
        #     return True

        # def handle_target_group() -> bool:
        #     return True

        # def handle_target_project() -> bool:
        #     return True

        # def handle_target_group_selection(target: str) -> bool:
        #     return True

        # def handle_target_project_selection(target: str) -> bool:
        #     return True

        # self._task_manager.run_task_common_setup()
        # self._task_manager.run_task_workspace_default_setup()
        # self._task_manager.run_task_workspace_group_setup()
        # self._task_manager.run_task_workspace_project_setup()
        # self._task_manager.run_task_filesystem_clean_exclude_setup()
        # self._task_manager.run_task_filesystem_clean_include_setup()

        # targets = kwargs.get("targets", ["all"])
        # if len(targets) < 1:
        #     return False

        # default_filesystem_accessibility_types = (
        #     self._database_manager
        #         .read_default_filesystem_accessibility_types()
        # )
        # selection_projects = (
        #     self._value_cache_database_manager
        #         .read_workspace_project()
        # )
        # selection_groups = (
        #     self._value_cache_database_manager
        #         .read_workspace_group()
        # )
        # default_template_types = (
        #     self._database_manager
        #         .read_default_template_types()
        # )
        # root_filesystem_path = (
        #     self._value_cache_database_manager
        #         .read_root_filesystem_path()
        # )
        # workspace_filesystem_path = (
        #     self._value_cache_database_manager
        #         .read_root_filesystem_path()
        # )
        # temporary_template_output_filesystem_path = (
        #     self._database_manager
        #         .read_temporary_template_output_filesystem_path()
        # )
        # cleanup_before_is_enabled = (
        #     self._value_cache_database_manager
        #         .read_con_wor_data_template_cleanup_before_is_enabled_value()
        # )
        # cleanup_after_is_enabled = (
        #     self._value_cache_database_manager
        #         .read_con_wor_data_template_cleanup_after_is_enabled_value()
        # )

        # if cleanup_before_is_enabled:
        #     self._task_manager.run_task_safe_clean_filesystem_path(
        #         target_path=temporary_template_output_filesystem_path
        #     )

        # for target in targets:
        #     if not target:
        #         continue

        #     if target == "all":
        #         handle_target_root()
        #         handle_target_group()
        #         handle_target_project()

        #     elif target == "root":
        #         handle_target_root()

        #     elif target == "group":
        #         handle_target_group()

        #     elif target == "project":
        #         handle_target_project()

        #     elif target in selection_groups:
        #         handle_target_group_selection(
        #             selection_groups[target]
        #         )

        #     elif target in selection_projects:
        #         handle_target_project_selection(
        #             selection_projects[target]
        #         )

        # if cleanup_after_is_enabled:
        #     self._task_manager.run_task_safe_clean_filesystem_path(
        #         target_path=temporary_template_output_filesystem_path
        #     )

        return True

    @_DecoratorManager.command_decorator
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
            return False

        self._display_manager.display_tree_object(
            value=value,
        )

        return True
