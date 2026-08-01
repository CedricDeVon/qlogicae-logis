import typer

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
    return True


@app_workflow.command(name="run", help="Run workflow selections.")
def run(
    targets: list[str] = typer.Argument(
        ...,
        help="List of workflows.",
    ),
) -> bool:
    return True
