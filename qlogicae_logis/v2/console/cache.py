import typer

app_cache = typer.Typer()
app_cache_view = typer.Typer()

app_cache.add_typer(
    app_cache_view,
    name="view",
    help="View cache information.",
)


@app_cache_view.command(
    name="runtime",
    help="View runtime cache.",
)
def runtime(
    key_path: str = typer.Option(
        ...,
        "--target",
        "-t",
        exists=True,
        file_okay=True,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        help="Key path.",
    ),
) -> bool:

    return True
