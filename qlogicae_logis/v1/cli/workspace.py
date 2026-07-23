from pathlib import Path

import typer

from qlogicae_logis.v1 import cli_manager

app_workspace = typer.Typer()
app_workspace_list = typer.Typer()
app_workspace.add_typer(
    app_workspace_list,
    name="list",
    help="Show list information.",
)


@app_workspace.command(
    name="export",
    help="Create workspaces archive file.",
)
def export(
    targets: list[str] = typer.Argument(
        ...,
        help="List of export targets.",
    ),
) -> bool:
    cli_manager.singleton.handle_workspace_export(
        targets
    )

    return True


@app_workspace_list.command(
    name="exports",
    help="List of exportable workspaces.",
)
def exports() -> bool:
    cli_manager.singleton.handle_workspace_list_exports()

    return True


@app_workspace.command(
    name="import",
    help="Extract workspace archive file.",
)
def import_(
    input_path: Path = typer.Option(
        Path("qlogicae-workspace"),
        "--input",
        "-i",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        help="Input filesystem path of exported workspace archive.",
    ),
    output_path: Path = typer.Option(
        Path(),
        "--output",
        "-o",
        file_okay=False,
        writable=True,
        resolve_path=True,
        help="Output filesystem path from exported workspace archive content.",
    ),
) -> bool:
    cli_manager.singleton.handle_workspace_import(
        input_path,
        output_path,
    )

    return True


@app_workspace.command(
    name="setup",
    help="Initial or filesystem replenishment.",
)
def setup() -> bool:
    cli_manager.singleton.handle_workspace_setup()

    return True
