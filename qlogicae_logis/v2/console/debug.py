from __future__ import annotations

from typing import Any

import typer

app_debug = typer.Typer()
app_debug_view = typer.Typer()

app_debug.add_typer(
    app_debug_view,
    name="view",
    help="View debug.",
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

@app_debug_view.command(
    name="value-cache",
    help="View value cache.",
)
def value_cache(
    targets: list[str] = typer.Option(
        [],
        "--key-path",
        "-kp",
        exists=True,
        file_okay=True,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        help="Value cache key path.",
    ),
) -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _CommandManager
    ).run_command_debug_view_value_cache(
        targets=targets
    )

    return True
