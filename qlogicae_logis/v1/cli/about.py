import typer

from qlogicae_logis.v1 import cli_manager

app_about = typer.Typer()


@app_about.command(name="version", help="Current version.")
def version() -> bool:
    cli_manager.singleton.handle_about_version()

    return True


@app_about.command(name="me", help="All information.")
def me() -> bool:
    cli_manager.singleton.handle_about_me()

    return True
