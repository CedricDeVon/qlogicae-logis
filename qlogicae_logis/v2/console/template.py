from __future__ import annotations

from typing import Any

import typer

app_template = typer.Typer()
app_template_list = typer.Typer()
app_template.add_typer(
    app_template_list,
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


@app_template_list.command(
    name="selections",
    help="Show a list of template selections.",
)
def selections() -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _CommandManager
    ).run_command_template_list_selections()

    return True


@app_template.command(
    name="apply",
    help="Apply filesystem templates.",
)
def apply(
    targets: list[str] = typer.Argument(
        ["all"],
        help="List of workspace targets.",
    ),
) -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _CommandManager
    ).run_command_template_apply(
        targets=targets
    )

    return True
