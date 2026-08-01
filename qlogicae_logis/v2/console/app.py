import typer

from qlogicae_logis.v2.console import (
    about,
    cache,
    filesystem,
    template,
    workflow,
    workspace,
)

console_application = typer.Typer()

console_application.add_typer(
    about.app_about,
    name="about",
    help="Show build information.",
)
console_application.add_typer(
    workspace.app_workspace,
    name="workspace",
    help="Manage workspaces.",
)
console_application.add_typer(
    workflow.app_workflow,
    name="workflow",
    help="Run workflows.",
)
console_application.add_typer(
    template.app_template,
    name="template",
    help="Apply templates.",
)
console_application.add_typer(
    filesystem.app_filesystem,
    name="filesystem",
    help="Filesystem management.",
)
console_application.add_typer(
    cache.app_cache,
    name="cache",
    help="Manage cache.",
)

def main() -> None:
    console_application()


if __name__ == "__main__":
    main()


