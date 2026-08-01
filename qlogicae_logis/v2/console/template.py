import typer

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
    return True
