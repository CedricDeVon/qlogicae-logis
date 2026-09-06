from __future__ import annotations

from typing import Any

from ..library.decorator_manager import DecoratorManager

__all__ = (
    "CommandFilesystemManager"
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
    global _CommandStorageManager
    global _DatabaseManager
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

class CommandFilesystemManager:
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
        self._log_manager = (
            _ImportManager.read_singleton(
                _LogManager
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
                    .read_command_name("filesystem_copy"),
                self.run_command_filesystem_copy,
            ),
            (
                self._command_storage_manager
                    .read_command_name("filesystem_move"),
                self.run_command_filesystem_move,
            ),
            (
                self._command_storage_manager
                    .read_command_name("filesystem_rename"),
                self.run_command_filesystem_rename,
            ),
            (
                self._command_storage_manager
                    .read_command_name("filesystem_tree_setup"),
                self.run_command_filesystem_tree_setup,
            ),
            (
                self._command_storage_manager
                    .read_command_name("filesystem_clean_path"),
                self.run_command_filesystem_clean_path,
            ),
            (
                self._command_storage_manager
                    .read_command_name("filesystem_clean_selection"),
                self.run_command_filesystem_clean_selection,
            ),
            (
                self._command_storage_manager
                    .read_command_name("filesystem_clean_list_included"),
                self.run_command_filesystem_clean_list_included,
            ),
            (
                self._command_storage_manager
                    .read_command_name("filesystem_clean_list_excluded"),
                self.run_command_filesystem_clean_list_excluded,
            ),
        ))

    def run_command_filesystem_copy(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()

        if not kwargs:
            self._log_manager.log_display_warning(
                reference=self.run_command_filesystem_copy,
                message="kwargs is null or an empty object",
            )
            return False

        source_paths = kwargs.get("source_paths", tuple()) or tuple()
        if len(source_paths) < 1:
            self._log_manager.log_display_warning(
                reference=self.run_command_filesystem_copy,
                message="no source paths found",
            )
            return False

        target_paths = kwargs.get("target_paths", tuple()) or tuple()
        if len(target_paths) < 1:
            self._log_manager.log_display_warning(
                reference=self.run_command_filesystem_copy,
                message="no target paths found",
            )
            return False

        for source_path in source_paths:
            if not source_path:
                self._log_manager.log_display_warning(
                reference=self.run_command_filesystem_copy,
                    message="one or more source paths are null",
                )
                continue

            self._import_manager.copy_filesystem_paths(
                source_path=source_path,
                target_paths=target_paths,
            )

        return True

    def run_command_filesystem_move(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()

        if not kwargs:
            self._log_manager.log_display_warning(
                reference=self.run_command_filesystem_move,
                message="kwargs is null or an empty object",
            )
            return False

        self._import_manager.move_filesystem_path(
            **kwargs,
        )

        return True

    def run_command_filesystem_rename(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()

        if not kwargs:
            self._log_manager.log_display_warning(
                reference=self.run_command_filesystem_rename,
                message="kwargs is null or an empty object",
            )
            return False

        self._import_manager.rename_filesystem_entity(
            **kwargs,
        )

        return True

    def run_command_filesystem_tree_setup(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()

        if not kwargs:
            self._log_manager.log_display_warning(
                reference=self.run_command_filesystem_tree_setup,
                message="kwargs is null or an empty object",
            )
            return False

        self._import_manager.setup_filesystem_tree_paths(
            **kwargs,
        )

        return True

    def run_command_filesystem_clean_path(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()
        self._task_manager.run_task_filesystem_clean_exclude_setup()

        if not kwargs:
            self._log_manager.log_display_warning(
                reference=self.run_command_filesystem_clean_path,
                message="kwargs is null or an empty object",
            )
            return False

        target_paths = kwargs.get("target_paths", tuple()) or tuple()
        if len(target_paths) < 1:
            self._log_manager.log_display_warning(
                reference=self.run_command_filesystem_clean_path,
                message="no target paths found",
            )
            return False

        excluded = (
            self._value_cache_database_manager
                .read_filesystem_clean_excluded()
        ) or {}

        result: bool = True
        for target_path in target_paths:
            if not target_path:
                self._log_manager.log_display_warning(
                    reference=self.run_command_filesystem_clean_path,
                    message="one or more target paths are null",
                )
                result = False
                continue

            if target_path in excluded:
                continue

            self._import_manager.clean_filesystem_paths(
                target_paths=(target_path,)
            )

        return result

    def run_command_filesystem_clean_selection(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()
        self._task_manager.run_task_filesystem_clean_include_setup()
        self._task_manager.run_task_filesystem_clean_exclude_setup()

        if not kwargs:
            self._log_manager.log_display_warning(
                reference=self.run_command_filesystem_clean_selection,
                message="kwargs is null or an empty object",
            )
            return False

        targets = kwargs.get("targets", tuple()) or tuple()
        selections = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_command_filesystem_clean_include_selection()
        ) or {}
        included = (
            self._value_cache_database_manager.read_filesystem_clean_included()
        ) or {}
        excluded = (
            self._value_cache_database_manager.read_filesystem_clean_excluded()
        ) or {}

        result: bool = True
        for target in targets:
            if not target:
                self._log_manager.log_display_warning(
                    reference=self.run_command_filesystem_clean_selection,
                    message="one or more targets are null",
                )
                result = False
                continue

            if target not in included:
                self._log_manager.log_display_warning(
                    reference=self.run_command_filesystem_clean_selection,
                    message=f"clean selection '{target}' does not exist",
                )
                result = False
                continue

            selection = (
                selections
                    .get(
                        included
                            .get(
                                target,
                                ""
                            ),
                        ""
                    )
            )
            if not selection:
                self._log_manager.log_display_warning(
                    reference=self.run_command_filesystem_clean_selection,
                    message="selection is null",
                )
                result = False
                continue

            paths = (
                self._value_cache_database_manager
                    .read_object_filesystem_pattern_values(
                        selection.get("targets", {}) or {}
                    )
            )
            for path in paths:
                if not path:
                    self._log_manager.log_display_warning(
                        reference=self.run_command_filesystem_clean_selection,
                        message="one or more paths are null",
                    )
                    result = False
                    continue

                if path in excluded:
                    continue

                self._import_manager.clean_filesystem_paths(
                    target_paths=(path,)
                )

        return result

    def run_command_filesystem_clean_list_included(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()
        self._task_manager.run_task_filesystem_clean_include_setup()

        value = {}
        filesystem_clean_included = (
            self._value_cache_database_manager.read_filesystem_clean_included()
        ) or {}
        if filesystem_clean_included:
            value["included"] = filesystem_clean_included

        self._display_manager.display_tree_object(
            value=value,
        )

        return True

    def run_command_filesystem_clean_list_excluded(
        self,
        **kwargs: Any
    ) -> bool:
        self._task_manager.run_task_common_setup()
        self._task_manager.run_task_filesystem_clean_exclude_setup()

        value = {}
        filesystem_clean_excluded = (
            self._value_cache_database_manager.read_filesystem_clean_excluded()
        ) or {}
        if filesystem_clean_excluded:
            value["excluded"] = filesystem_clean_excluded

        self._display_manager.display_tree_object(
            value=value,
        )

        return True
