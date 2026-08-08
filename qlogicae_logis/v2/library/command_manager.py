from __future__ import annotations

from typing import Any

_LogManager: Any = None
_SingletonManager: Any = None
_CommandAboutManager: Any = None
_CommandDebugManager: Any = None
_CommandPluginManager: Any = None
_CommandStorageManager: Any = None
_CommandUtilityManager: Any = None
_CommandTemplateManager: Any = None
_CommandWorkflowManager: Any = None
_CommandWorkspaceManager: Any = None
_CommandFilesystemManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _LogManager
    global _SingletonManager
    global _CommandAboutManager
    global _CommandDebugManager
    global _CommandPluginManager
    global _CommandStorageManager
    global _CommandUtilityManager
    global _CommandTemplateManager
    global _CommandWorkflowManager
    global _CommandWorkspaceManager
    global _CommandFilesystemManager

    from qlogicae_cor.v1.library import (
        singleton_manager,
    )

    from qlogicae_logis.v2.library import (
        command_about_manager,
        command_debug_manager,
        command_filesystem_manager,
        command_plugin_manager,
        command_storage_manager,
        command_template_manager,
        command_utility_manager,
        command_workflow_manager,
        command_workspace_manager,
        log_manager,
    )

    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _CommandStorageManager = (
        command_storage_manager.CommandStorageManager
    )
    _CommandAboutManager = (
        command_about_manager.CommandAboutManager
    )
    _CommandDebugManager = (
        command_debug_manager.CommandDebugManager
    )
    _CommandFilesystemManager = (
        command_filesystem_manager.CommandFilesystemManager
    )
    _CommandTemplateManager = (
        command_template_manager.CommandTemplateManager
    )
    _CommandUtilityManager = (
        command_utility_manager.CommandUtilityManager
    )
    _CommandWorkflowManager = (
        command_workflow_manager.CommandWorkflowManager
    )
    _CommandWorkspaceManager = (
        command_workspace_manager.CommandWorkspaceManager
    )
    _CommandPluginManager = (
        command_plugin_manager.CommandPluginManager
    )
    _LogManager = (
        log_manager.LogManager
    )

    _handle_dynamic_imports = lambda: None

class CommandManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()

        command_storage_manager = _SingletonManager.get_singleton(
            _CommandStorageManager
        )

        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_about_version"
            ),
            self.run_command_about_version
        )
        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_about_me"
            ),
            self.run_command_about_me
        )

        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_debug_view_value_cache"
            ),
            self.run_command_debug_view_value_cache
        )
        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_base_setup"
            ),
            self.run_command_base_setup
        )

        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_filesystem_copy"
            ),
            self.run_command_filesystem_copy
        )
        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_filesystem_move"
            ),
            self.run_command_filesystem_move
        )
        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_filesystem_tree_setup"
            ),
            self.run_command_filesystem_tree_setup
        )
        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_filesystem_rename"
            ),
            self.run_command_filesystem_rename
        )
        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_filesystem_clean_selection"
            ),
            self.run_command_filesystem_clean_selection
        )
        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_filesystem_clean_path"
            ),
            self.run_command_filesystem_clean_path
        )
        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_filesystem_clean_list_included"
            ),
            self.run_command_filesystem_clean_list_included
        )
        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_filesystem_clean_list_excluded"
            ),
            self.run_command_filesystem_clean_list_excluded
        )


        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_template_list_selections"
            ),
            self.run_command_template_list_selections
        )
        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_template_apply"
            ),
            self.run_command_template_apply
        )


        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_workspace_list_exports"
            ),
            self.run_command_workspace_list_exports
        )
        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_workspace_setup"
            ),
            self.run_command_workspace_setup
        )
        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_workspace_import"
            ),
            self.run_command_workspace_import
        )
        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_workspace_export"
            ),
            self.run_command_workspace_export
        )


        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_workflow_list_selections"
            ),
            self.run_command_workflow_list_selections
        )
        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_workflow_run"
            ),
            self.run_command_workflow_run
        )


        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command"
            ),
            self.run_command
        )
        command_storage_manager.add_command(
            self.setup_command_name(
                "run_command_shutdown"
            ),
            self.run_command_shutdown
        )


    def setup_command_name(
        self,
        *args: Any,
    ) -> str:
        return (
            "-".join(args)
        )

    def run_command(
        self,
        callback: Any,
        kwargs: Any = None,
    ) -> bool:
        log_manager = _SingletonManager.get_singleton(
            _LogManager
        )

        log_manager.log_execution_start()

        if kwargs:
            callback(
                **kwargs
            )
        else:
            callback()


        log_manager.log_execution_complete()

        return True

    def run_command_about_version(self) -> bool:
        command_about_manager = _SingletonManager.get_singleton(
            _CommandAboutManager
        )

        self.run_command(
            command_about_manager.run_command_about_version
        )

        return True

    def run_command_about_me(self) -> bool:
        command_about_manager = _SingletonManager.get_singleton(
            _CommandAboutManager
        )

        self.run_command(
            command_about_manager.run_command_about_me
        )

        return True

    def run_command_debug_view_value_cache(self, **kwargs: Any) -> bool:
        command_debug_manager = _SingletonManager.get_singleton(
            _CommandDebugManager
        )

        self.run_command(
            command_debug_manager.run_command_debug_view_value_cache,
            kwargs
        )

        return True

    def run_command_filesystem_copy(self, **kwargs: Any) -> bool:
        command_filesystem_manager = _SingletonManager.get_singleton(
            _CommandFilesystemManager
        )

        self.run_command(
            command_filesystem_manager.run_command_filesystem_copy,
            kwargs
        )

        return True

    def run_command_filesystem_move(self, **kwargs: Any) -> bool:
        command_filesystem_manager = _SingletonManager.get_singleton(
            _CommandFilesystemManager
        )

        self.run_command(
            command_filesystem_manager.run_command_filesystem_move,
            kwargs
        )

        return True

    def run_command_filesystem_tree_setup(self, **kwargs: Any) -> bool:
        command_filesystem_manager = _SingletonManager.get_singleton(
            _CommandFilesystemManager
        )

        self.run_command(
            command_filesystem_manager.run_command_filesystem_tree_setup,
            kwargs
        )

        return True

    def run_command_filesystem_rename(self, **kwargs: Any) -> bool:
        command_filesystem_manager = _SingletonManager.get_singleton(
            _CommandFilesystemManager
        )

        self.run_command(
            command_filesystem_manager.run_command_filesystem_rename,
            kwargs
        )

        return True

    def run_command_filesystem_clean_path(self, **kwargs: Any) -> bool:
        command_filesystem_manager = _SingletonManager.get_singleton(
            _CommandFilesystemManager
        )

        self.run_command(
            command_filesystem_manager.run_command_filesystem_clean_path,
            kwargs
        )

        return True

    def run_command_filesystem_clean_selection(self, **kwargs: Any) -> bool:
        command_filesystem_manager = _SingletonManager.get_singleton(
            _CommandFilesystemManager
        )

        self.run_command(
            command_filesystem_manager.run_command_filesystem_clean_selection,
            kwargs
        )

        return True

    def run_command_filesystem_clean_list_included(self) -> bool:
        command_filesystem_manager = _SingletonManager.get_singleton(
            _CommandFilesystemManager
        )

        self.run_command(
            command_filesystem_manager
                .run_command_filesystem_clean_list_included
        )

        return True

    def run_command_filesystem_clean_list_excluded(self) -> bool:
        command_filesystem_manager = _SingletonManager.get_singleton(
            _CommandFilesystemManager
        )

        self.run_command(
            command_filesystem_manager
                .run_command_filesystem_clean_list_excluded
        )

        return True

    def run_command_template_list_selections(self) -> bool:
        command_template_manager = _SingletonManager.get_singleton(
            _CommandTemplateManager
        )

        self.run_command(
            command_template_manager
                .run_command_template_list_selections
        )

        return True

    def run_command_template_apply(self, **kwargs: Any) -> bool:
        command_template_manager = _SingletonManager.get_singleton(
            _CommandTemplateManager
        )

        self.run_command(
            command_template_manager
                .run_command_template_apply,
            kwargs
        )

        return True

    def run_command_workflow_run(self, **kwargs: Any) -> bool:
        command_workflow_manager = _SingletonManager.get_singleton(
            _CommandWorkflowManager
        )

        self.run_command(
            command_workflow_manager
                .run_command_workflow_run,
            kwargs
        )

        return True

    def run_command_workflow_list_selections(self) -> bool:
        command_workflow_manager = _SingletonManager.get_singleton(
            _CommandWorkflowManager
        )

        self.run_command(
            command_workflow_manager
                .run_command_workflow_list_selections
        )

        return True

    def run_command_workspace_list_exports(self) -> bool:
        command_workspace_manager = _SingletonManager.get_singleton(
            _CommandWorkspaceManager
        )

        self.run_command(
            command_workspace_manager
                .run_command_workspace_list_exports
        )

        return True


    def run_command_workspace_setup(self) -> bool:
        command_workspace_manager = _SingletonManager.get_singleton(
            _CommandWorkspaceManager
        )

        self.run_command(
            command_workspace_manager
                .run_command_workspace_setup
        )

        return True

    def run_command_workspace_import(self, **kwargs: Any) -> bool:
        command_workspace_manager = _SingletonManager.get_singleton(
            _CommandWorkspaceManager
        )

        self.run_command(
            command_workspace_manager
                .run_command_workspace_import,
            kwargs
        )

        return True

    def run_command_workspace_export(self, **kwargs: Any) -> bool:
        command_workspace_manager = _SingletonManager.get_singleton(
            _CommandWorkspaceManager
        )

        self.run_command(
            command_workspace_manager
                .run_command_workspace_export,
            kwargs
        )

        return True

    def run_command_base_setup(self) -> bool:
        command_utility_manager = _SingletonManager.get_singleton(
            _CommandUtilityManager
        )
        command_filesystem_manager = _SingletonManager.get_singleton(
            _CommandFilesystemManager
        )
        command_workflow_manager = _SingletonManager.get_singleton(
            _CommandWorkflowManager
        )
        command_plugin_manager = _SingletonManager.get_singleton(
            _CommandPluginManager
        )
        log_manager = _SingletonManager.get_singleton(
            _LogManager
        )

        command_utility_manager.run_command_timestamp_execution_start_setup()
        command_utility_manager.run_command_timestamp_execution_end_setup()
        command_utility_manager.run_command_root_filesystem_paths_setup()
        command_utility_manager.run_command_selection_filesystem_paths_setup()
        command_utility_manager.run_command_executing_console_filesystem_paths_setup()
        command_utility_manager.run_command_navigate_to_root()

        command_utility_manager.run_command_configuration_workspace_filesystem_path_extraction_setup()
        command_utility_manager.run_command_configuration_workspace_data_extraction_setup()
        command_utility_manager.run_command_value_cache_macros_setup()
        command_utility_manager.run_command_file_macros_setup()
        command_utility_manager.run_command_workspace_macros_setup()
        command_utility_manager.run_command_workspace_selection_setup()
        command_utility_manager.run_command_workspace_setup()

        command_filesystem_manager.run_command_filesystem_setup()
        command_workflow_manager.run_command_workflow_setup()

        log_manager.run_command_log_setup()

        command_plugin_manager.run_command_plugin_setup()

        return True

    def run_command_shutdown(self) -> bool:
        log_manager = _SingletonManager.get_singleton(
            _LogManager
        )

        log_manager.shutdown()

        return True

