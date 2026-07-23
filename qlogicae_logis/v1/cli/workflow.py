import typer

from qlogicae_logis.v1 import cli_manager

app_workflow = typer.Typer()
app_workflow_list = typer.Typer()
app_workflow.add_typer(
    app_workflow_list,
    name="list",
    help="Show list information.",
)


@app_workflow_list.command(
    name="selections",
    help="Show a list of defined workflows.",
)
def selections() -> bool:
    cli_manager.singleton.handle_workflow_list_selections()

    return True


@app_workflow.command(name="run", help="Run workflow selections.")
def run(
    targets: list[str] = typer.Argument(
        ...,
        help="List of workflows.",
    ),
) -> bool:
    cli_manager.singleton.handle_workflow_run(targets)

    return True
