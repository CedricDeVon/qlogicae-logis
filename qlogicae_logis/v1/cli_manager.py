
from qlogicae_cor.v1.abstract_manager import AbstractManager

from qlogicae_logis.v1 import (
    cli_command_manager,
    cli_display_manager,
    workspace_manager,
)
from qlogicae_logis.v1.cli_manager_configurations import (
    CliManagerConfigurations,
)


class CliManager(AbstractManager[CliManagerConfigurations]):
    def __init__(self) -> None:
        super().__init__(CliManagerConfigurations())

    def handle_about_version(self) -> bool:
        def handle_command_generation():
            return [
                {"callback": (
                    cli_command_manager.singleton.handle_about_version_command
                )},
            ]

        self.handle_tasks(
            [*self.handle_pre_about_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_about_me(self) -> bool:
        def handle_command_generation():
            return [
                {"callback": (
                    cli_command_manager.singleton.handle_about_me_command
                )},
            ]

        self.handle_tasks(
            [*self.handle_pre_about_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_filesystem_copy(self, **kwargs) -> bool:
        def handle_command_generation():
            return [
                {
                    "callback": (
                        cli_command_manager.singleton.handle_filesystem_copy_command
                    ),
                    "arguments": kwargs
                },
            ]

        self.handle_tasks(
            [*self.handle_pre_filesystem_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_filesystem_move(self, **kwargs) -> bool:
        def handle_command_generation():
            return [
                {
                    "callback": (
                        cli_command_manager.singleton.handle_filesystem_move_command
                    ),
                    "arguments": kwargs
                },
            ]

        self.handle_tasks(
            [*self.handle_pre_filesystem_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_filesystem_rename(self, **kwargs) -> bool:
        def handle_command_generation():
            return [
                {
                    "callback": (
                        cli_command_manager.singleton.handle_filesystem_rename_command
                    ),
                    "arguments": kwargs
                },
            ]

        self.handle_tasks(
            [*self.handle_pre_filesystem_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_filesystem_tree_setup(self, **kwargs) -> bool:
        def handle_command_generation():
            return [
                {
                    "callback": (
                        cli_command_manager.singleton.handle_filesystem_tree_setup_command
                    ),
                    "arguments": kwargs
                },
            ]

        self.handle_tasks(
            [*self.handle_pre_filesystem_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_filesystem_clean_path(self, **kwargs) -> bool:
        def handle_command_generation():
            return [
                {
                    "callback": (
                        cli_command_manager.singleton.handle_filesystem_clean_path_command
                    ),
                    "arguments": kwargs
                },
            ]

        self.handle_tasks(
            [*self.handle_pre_filesystem_clean_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_filesystem_clean_selection(self, targets) -> bool:
        def handle_command_generation():
            sub_tasks = []
            callback = (
                cli_command_manager.singleton.handle_filesystem_clean_selection_command
            )
            for current_target in targets:
                sub_tasks.append(
                    {
                        "callback": (
                            callback
                        ),
                        "arguments": {
                            "targets": [current_target]
                        }
                    }
                )

            return sub_tasks

        self.handle_tasks(
            [*self.handle_pre_filesystem_clean_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_filesystem_clean_list_included(self) -> bool:
        def handle_command_generation():
            callback = (
                cli_command_manager
                    .singleton
                    .handle_filesystem_clean_list_included_command
            )
            return [{"callback": callback}]

        self.handle_tasks(
            [*self.handle_pre_filesystem_clean_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_filesystem_clean_list_excluded(self) -> bool:
        def handle_command_generation():
            callback = (
                cli_command_manager
                    .singleton
                    .handle_filesystem_clean_list_excluded_command
            )
            return [{"callback": callback}]

        self.handle_tasks(
            [*self.handle_pre_filesystem_clean_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_workspace_export(self, targets) -> bool:
        def handle_command_generation():
            sub_tasks = []
            callback = (
                cli_command_manager
                    .singleton
                    .handle_workspace_export_command
            )
            for current_target in targets:
                sub_tasks.append(
                    {
                        "callback": callback,
                        "arguments": {
                            "targets": [current_target]
                        }
                    }
                )

            return sub_tasks

        self.handle_tasks(
            [*self.handle_pre_workspace_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_workspace_import(self, input_path, output_path) -> bool:
        def handle_command_generation():
            callback = cli_command_manager.singleton.handle_workspace_import_command
            return [
                {
                    "callback": callback,
                    "arguments": {
                        "input_path": input_path,
                        "output_path": output_path,
                    }
                }
            ]

        self.handle_tasks(
            [*self.handle_pre_workspace_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_workspace_list_exports(self) -> bool:
        def handle_command_generation():
            callback = (
                cli_command_manager.singleton.handle_workspace_list_exports_command
            )
            return [{"callback": callback}]

        self.handle_tasks(
            [*self.handle_pre_workspace_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_workspace_setup(self) -> bool:
        def handle_command_generation():
            callback = cli_command_manager.singleton.handle_workspace_setup_command
            return [{"callback": callback}]

        self.handle_tasks(
            [*self.handle_pre_workspace_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_workflow_run(self, targets) -> bool:
        def handle_command_generation():
            sub_tasks = []
            callback = cli_command_manager.singleton.handle_workflow_run_command
            for current_target in targets:
                sub_tasks.append(
                    {
                        "callback": callback,
                        "arguments": {
                            "targets": [current_target]
                        }
                    }
                )

            return sub_tasks

        self.handle_tasks(
            [*self.handle_pre_template_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_workflow_list_selections(self) -> bool:
        def handle_command_generation():
            callback = (
                cli_command_manager.singleton.handle_workflow_list_selections_command
            )
            return [{"callback": callback}]

        self.handle_tasks(
            [*self.handle_pre_workflow_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_template_list_selections(self) -> bool:
        def handle_command_generation():
            callback = (
                cli_command_manager.singleton.handle_template_list_selections_command
            )
            return [{"callback": callback}]

        self.handle_tasks(
            [*self.handle_pre_workflow_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_template_apply(self, targets) -> bool:
        def handle_command_generation():
            sub_tasks = []
            callback = (
                cli_command_manager.singleton.handle_template_apply_command
            )
            for current_target in targets:
                sub_tasks.append(
                    {
                        "callback": callback,
                        "arguments": {
                            "targets": [current_target]
                        }
                    }
                )

            return sub_tasks

        self.handle_tasks(
            [*self.handle_pre_template_command_generation()],
            [*handle_command_generation()],
            [*self.handle_post_command_generation()],
        )

        return True

    def handle_pre_about_command_generation(self):
        return [
            {
                "callback": workspace_manager.
                    singleton.
                    handle_timestamp_console_execution_start_setup,
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_current_root_filesystem_paths_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_executing_console_filesystem_paths_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_current_root_filesystem_navigation_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_toolset_configuration_file_data_extraction_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_toolset_configuration_data_setup
            },
        ]

    def handle_pre_filesystem_command_generation(self):
        return [
            {
                "callback": workspace_manager.
                    singleton.
                    handle_timestamp_console_execution_start_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_current_root_filesystem_paths_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_executing_console_filesystem_paths_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_current_root_filesystem_navigation_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_workspace_configuration_file_data_extraction_setup
            },
            {"callback": workspace_manager.
                singleton.
                handle_workspace_selection_setup},
            {"callback": workspace_manager.
                singleton.
                handle_value_cache_macros_setup},
            {"callback": workspace_manager.
                singleton.
                handle_macros_parsing_setup},
            {"callback": workspace_manager.
                singleton.
                handle_logs_setup},
        ]

    def handle_pre_filesystem_clean_command_generation(self):
        return [
            {
                "callback": workspace_manager.
                    singleton.
                    handle_timestamp_console_execution_start_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_current_root_filesystem_paths_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_executing_console_filesystem_paths_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_current_root_filesystem_navigation_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_workspace_configuration_file_data_extraction_setup
            },
            {"callback": workspace_manager.
                singleton.
                handle_workspace_selection_setup},
            {"callback": workspace_manager.
                singleton.
                handle_value_cache_macros_setup},
            {"callback": workspace_manager.
                singleton.
                handle_macros_parsing_setup},
            {"callback": workspace_manager.
                singleton.
                handle_logs_setup},
            {
                "callback": (workspace_manager.
                    singleton.
                    handle_filesystem_clean_command_setup),
            },
        ]

    def handle_pre_workspace_command_generation(self):
        return [
            {
                "callback": workspace_manager.
                    singleton.
                    handle_timestamp_console_execution_start_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_current_root_filesystem_paths_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_executing_console_filesystem_paths_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_current_root_filesystem_navigation_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_workspace_configuration_file_data_extraction_setup
            },
            {"callback": workspace_manager.
                singleton.
                handle_workspace_selection_setup},
            {"callback": workspace_manager.
                singleton.
                handle_value_cache_macros_setup},
            {"callback": workspace_manager.
                singleton.
                handle_macros_parsing_setup},
            {"callback": workspace_manager.
                singleton.
                handle_logs_setup},
            {"callback": workspace_manager.
                singleton.
                handle_workspace_command_setup},
        ]

    def handle_pre_workflow_command_generation(self):
        return [
            {
                "callback": workspace_manager.
                    singleton.
                    handle_timestamp_console_execution_start_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_current_root_filesystem_paths_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_executing_console_filesystem_paths_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_current_root_filesystem_navigation_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_workspace_configuration_file_data_extraction_setup
            },
            {"callback": workspace_manager.
                singleton.
                handle_workspace_selection_setup},
            {"callback": workspace_manager.
                singleton.
                handle_value_cache_macros_setup},
            {"callback": workspace_manager.
                singleton.
                handle_macros_parsing_setup},
            {"callback": workspace_manager.
                singleton.
                handle_logs_setup},
        ]

    def handle_pre_template_command_generation(self):
        return [
            {
                "callback": workspace_manager.
                    singleton.
                    handle_timestamp_console_execution_start_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_current_root_filesystem_paths_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_executing_console_filesystem_paths_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_current_root_filesystem_navigation_setup
            },
            {
                "callback": workspace_manager.
                    singleton.
                    handle_workspace_configuration_file_data_extraction_setup
            },
            {"callback": workspace_manager.
                singleton.
                handle_workspace_selection_setup},
            {"callback": workspace_manager.
                singleton.
                handle_value_cache_macros_setup},
            {"callback": workspace_manager.
                singleton.
                handle_macros_parsing_setup},
            {"callback": workspace_manager.
                singleton.
                handle_logs_setup},
        ]

    def handle_tasks(self, pre_tasks, on_tasks, post_tasks) -> bool:
        cli_display_manager.singleton.render_progress_bar({"items": pre_tasks})

        cli_display_manager.singleton.render_directly({"items": on_tasks})

        cli_display_manager.singleton.render_progress_bar({"items": post_tasks})

        return True

    def handle_post_command_generation(self) -> bool:
        return [{"callback": workspace_manager.singleton.shutdown}]


singleton = CliManager()
