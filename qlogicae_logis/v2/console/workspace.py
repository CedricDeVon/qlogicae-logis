from __future__ import annotations

from typing import Any

import typer

app_workspace = typer.Typer()
app_workspace_list = typer.Typer()
app_workspace.add_typer(
    app_workspace_list,
    name="list",
    help="Show list information.",
)


_SingletonManager: Any = None
_CommandManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _SingletonManager
    global _CommandManager

    from qlogicae_cor.v1.library import (
        singleton_manager,
    )

    from qlogicae_logis.v2.library import (
        command_manager,
    )

    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _CommandManager = (
        command_manager.CommandManager
    )

    _handle_dynamic_imports = lambda: None

@app_workspace.command(
    name="export",
    help="Create workspaces archive file.",
)
def export(
    targets: list[str] = typer.Argument(
        [],
        help="List of export targets.",
    ),
) -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _CommandManager
    ).run_command_workspace_export(
        targets=targets
    )

    return True


@app_workspace_list.command(
    name="exports",
    help="List of exportable workspaces.",
)
def exports() -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _CommandManager
    ).run_command_workspace_list_exports()

    return True


@app_workspace.command(
    name="import",
    help="Extract workspace archive file.",
)
def import_(
    input_path: str = typer.Option(
        "",
        "--input",
        "-i",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        help="Input filesystem path of exported workspace archive.",
    ),
    output_path: str = typer.Option(
        "",
        "--output",
        "-o",
        file_okay=False,
        writable=True,
        resolve_path=True,
        help="Output filesystem path from exported workspace archive content.",
    ),
) -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _CommandManager
    ).run_command_workspace_import(
        input_path=input_path,
        output_path=output_path
    )

    return True


@app_workspace.command(
    name="setup",
    help="Initial or filesystem replenishment.",
)
def setup() -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _CommandManager
    ).run_command_workspace_setup()

    return True
