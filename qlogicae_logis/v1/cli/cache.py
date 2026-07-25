
import typer

from qlogicae_logis.v1 import workspace_manager

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
def runtime() -> bool:
    workspace_manager.singleton.debug_value_cache()

    return True
