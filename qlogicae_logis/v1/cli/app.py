import typer

from qlogicae_logis.v1 import (
    cli_manager,
    workspace_manager,
)
from qlogicae_logis.v1.cli import (
    about,
    clean,
    script,
    template,
)

cli_application = typer.Typer()

cli_application.add_typer(about.app_about, name="about", help="Show build information.")
cli_application.add_typer(clean.app_clean, name="clean", help="Clean filesystem.")
cli_application.add_typer(script.app_script, name="script", help="Run scripts.")
cli_application.add_typer(
    template.app_template, name="template", help="Apply templates."
)


if __name__ == "__main__":
    cli_manager.singleton.render_progress_bar(
        {
            "items": [
                {
                    "callback": workspace_manager.singleton.handle_timestamp_console_execution_start_setup
                },
                {
                    "callback": workspace_manager.singleton.handle_current_root_filesystem_paths_setup
                },
                {
                    "callback": workspace_manager.singleton.handle_executing_console_filesystem_paths_setup
                },
                {
                    "callback": workspace_manager.singleton.handle_current_root_filesystem_navigation_setup
                },
                {
                    "callback": workspace_manager.singleton.handle_workspace_base_filesystem_replenishment_setup
                },
                {
                    "callback": workspace_manager.singleton.handle_workspace_configuration_file_data_extraction_setup
                },
                {
                    "callback": workspace_manager.singleton.handle_workspace_selection_setup
                },
                {
                    "callback": workspace_manager.singleton.handle_workspace_selection_filesystem_replenishment_setup
                },
                {
                    "callback": workspace_manager.singleton.handle_value_cache_macros_setup
                },
                {"callback": workspace_manager.singleton.handle_macros_parsing_setup},
                {"callback": workspace_manager.singleton.handle_logs_setup},
            ]
        }
    )

    cli_application()
