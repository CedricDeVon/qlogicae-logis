from __future__ import annotations

from typing import Any

_typer: Any = None
_CommandManager: Any = None
_SingletonManager: Any = None


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _typer
    global _SingletonManager
    global _CommandManager

    import typer
    from qlogicae_cor.v1.library import (
        singleton_manager,
    )

    from qlogicae_logis.v2.library import (
        command_manager,
    )

    _typer =  typer
    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _CommandManager = (
        command_manager.CommandManager
    )

    _handle_dynamic_imports = lambda: None

class ConsoleManager:
    def __init__(self) -> None:
        pass

    @classmethod
    def run(self) -> bool:
        _handle_dynamic_imports()

        from qlogicae_logis.v2.console import (
            about,
            debug,
            filesystem,
            template,
            workflow,
            workspace,
        )

        application = _typer.Typer()
        application.add_typer(
            about.app_about,
            name="about",
            help="Show build information.",
        )
        application.add_typer(
            workspace.app_workspace,
            name="workspace",
            help="Manage workspaces.",
        )
        application.add_typer(
            workflow.app_workflow,
            name="workflow",
            help="Run workflows.",
        )
        application.add_typer(
            template.app_template,
            name="template",
            help="Apply templates.",
        )
        application.add_typer(
            filesystem.app_filesystem,
            name="filesystem",
            help="Filesystem management.",
        )
        application.add_typer(
            debug.app_debug,
            name="debug",
            help="Manage debug.",
        )


        command_manager = _SingletonManager.get_singleton(
            _CommandManager
        )

        try:
            command_manager.run_command_base_setup()

            application()

        finally:
            command_manager.run_command_shutdown()

        return True
