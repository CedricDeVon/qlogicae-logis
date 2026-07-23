import typer

from qlogicae_logis.v1 import cli_manager

app_template = typer.Typer()
app_template_list = typer.Typer()
app_template.add_typer(
    app_template_list,
    name="list",
    help="Show list information.",
)


@app_template_list.command(
    name="selections",
    help="Show a list of template selections.",
)
def selections() -> bool:
    cli_manager.singleton.handle_template_list_selections()

    return True


@app_template.command(
    name="apply",
    help="Apply filesystem templates.",
)
def apply(
    targets: list[str] = typer.Argument(
        ...,
        help="List of workspace targets.",
    ),
) -> bool:
    cli_manager.singleton.handle_template_apply(targets)

    return True
