import typer

from qlogicae_logis.v1.cli import (
    about,
    clean,
    template,
    workflow,
    workspace,
)

cli_application = typer.Typer()

cli_application.add_typer(
    about.app_about,
    name="about",
    help="Show build information.",
)
cli_application.add_typer(
    workflow.app_workflow,
    name="workflow",
    help="Run workflows.",
)
cli_application.add_typer(
    template.app_template,
    name="template",
    help="Apply templates.",
)
cli_application.add_typer(
    workspace.app_workspace,
    name="workspace",
    help="Manage workspaces.",
)
cli_application.add_typer(
    clean.app_clean,
    name="clean",
    help="Clean filesystem.",
)


def main() -> None:
    cli_application()


if __name__ == "__main__":
    main()
