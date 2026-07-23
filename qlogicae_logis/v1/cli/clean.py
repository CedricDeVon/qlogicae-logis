import typer

from qlogicae_logis.v1 import cli_manager

app_clean = typer.Typer()
app_clean_list = typer.Typer()

app_clean.add_typer(
    app_clean_list,
    name="list",
    help="Show list information.",
)


@app_clean.command(
    name="selection",
    help="Clean filesystem paths based on a selection.",
)
def selection(
    targets: list[str] = typer.Argument(
        ...,
        help="List of cleaning targets.",
    ),
) -> bool:
    cli_manager.singleton.handle_clean_selection(targets)

    return True


@app_clean_list.command(
    name="included",
    help="Show selections and whitelisted filesystem paths.",
)
def included() -> bool:
    cli_manager.singleton.handle_clean_list_included()

    return True


@app_clean_list.command(
    name="excluded",
    help="Show blacklisted filesystem paths.",
)
def excluded() -> bool:
    cli_manager.singleton.handle_clean_list_excluded()

    return True
