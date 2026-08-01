from __future__ import annotations

from typing import Any

import typer

app_about = typer.Typer()


_SingletonManager: Any = None
_ConsoleAboutManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _SingletonManager
    global _ConsoleAboutManager

    from qlogicae_cor.v1.library import singleton_manager

    from qlogicae_logis.v2.library.console_about_manager import ConsoleAboutManager

    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _ConsoleAboutManager = (
        ConsoleAboutManager
    )

    _handle_dynamic_imports = lambda: None


@app_about.command(name="version", help="Current version.")
def version() -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _ConsoleAboutManager
    ).render_version()

    return True


@app_about.command(name="me", help="All information.")
def me() -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _ConsoleAboutManager
    ).render_me()

    return True
