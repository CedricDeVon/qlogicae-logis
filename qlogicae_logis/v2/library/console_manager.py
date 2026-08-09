from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import typer

_Path: Any = None
_typer: Any = None
_CommandManager: Any = None
_SingletonManager: Any = None


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _Path
    global _typer
    global _SingletonManager
    global _CommandManager

    from pathlib import Path

    import typer
    from qlogicae_cor.v1.library import (
        singleton_manager,
    )

    from qlogicae_logis.v2.library import (
        command_manager,
    )

    _Path = Path
    _typer = typer
    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _CommandManager = (
        command_manager.CommandManager
    )

    _handle_dynamic_imports = lambda: None

class ConsoleManager:
    __slots__ = (
        "_application",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._application: typer.Typer = _typer.Typer()

    def run(self) -> bool:
        self.setup_about_command()
        self.setup_workflow_command()
        self.setup_workspace_command()
        self.setup_filesystem_command()
        self.setup_template_command()
        self.setup_debug_command()

        command_manager = _SingletonManager.get_singleton(
            _CommandManager
        )

        try:
            self._application()

        finally:
            command_manager.run_command_shutdown()

        return True


    def setup_about_command(self) -> bool:
        application_about: typer.Typer = _typer.Typer()

        @application_about.command(name="version", help="Current version.")
        def version() -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_about_version()

            return True

        @application_about.command(name="me", help="All information.")
        def me() -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_about_me()

            return True


        self._application.add_typer(
            application_about,
            name="about",
            help="Show build information.",
        )

        return True


    def setup_debug_command(self) -> bool:
        application_debug: typer.Typer = _typer.Typer()
        application_debug_view: typer.Typer = _typer.Typer()


        @application_debug_view.command(
            name="value-cache",
            help="View value cache.",
        )
        def value_cache(
            targets: list[str] = _typer.Option(
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
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_debug_view_value_cache(
                targets=targets
            )

            return True


        self._application.add_typer(
            application_debug,
            name="debug",
            help="Manage debug.",
        )
        application_debug.add_typer(
            application_debug_view,
            name="view",
            help="View debug.",
        )

        return True


    def setup_filesystem_command(self) -> bool:
        application_filesystem: typer.Typer = _typer.Typer()
        application_filesystem_tree: typer.Typer = _typer.Typer()
        application_filesystem_clean: typer.Typer = _typer.Typer()
        application_filesystem_clean_list: typer.Typer = _typer.Typer()


        @application_filesystem.command(
            name="copy",
            help="Copy filesystem entities.",
        )
        def copy(
            source_path: _Path = _typer.Option(
                ...,
                "--source-path",
                "-sp",
                exists=True,
                file_okay=True,
                dir_okay=True,
                readable=True,
                resolve_path=True,
                help="Filesystem source path.",
            ),
            target_paths: list[_Path] = _typer.Option(
                ...,
                "--target-paths",
                "-tp",
                exists=False,
                file_okay=True,
                dir_okay=True,
                writable=True,
                resolve_path=True,
                help="Filesystem target paths",
            ),
            overwrite: bool = _typer.Option(
                False,
                "--overwrite/--no-overwrite",
                "-o/-no",
                help="",
            ),
        ) -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_filesystem_copy(
                source_path=source_path,
                target_paths=target_paths,
                overwrite=overwrite,
            )

            return True

        @application_filesystem.command(
            name="move",
            help="Move filesystem entities.",
        )
        def move(
            source_path: _Path = _typer.Option(
                ...,
                "--source-path",
                "-sp",
                exists=True,
                file_okay=True,
                dir_okay=True,
                readable=True,
                resolve_path=True,
                help="Filesystem source path.",
            ),
            target_path: _Path = _typer.Option(
                ...,
                "--target-paths",
                "-tp",
                exists=False,
                file_okay=True,
                dir_okay=True,
                writable=True,
                resolve_path=True,
                help="Filesystem target path.",
            ),
            overwrite: bool = _typer.Option(
                False,
                "--overwrite/--no-overwrite",
                "-o/-no",
                help="",
            ),
        ) -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_filesystem_move(
                source_path=source_path,
                target_path=target_path,
                overwrite=overwrite,
            )

            return True

        @application_filesystem.command(
            name="rename",
            help="Rename filesystem entities.",
        )
        def rename(
            old_path: _Path = _typer.Option(
                ...,
                "--old-path",
                "-op",
                exists=True,
                file_okay=True,
                dir_okay=True,
                readable=True,
                resolve_path=True,
                help="Old file or folder name.",
            ),
            new_path: _Path = _typer.Option(
                ...,
                "--new-path",
                "-np",
                exists=False,
                file_okay=True,
                dir_okay=True,
                writable=True,
                resolve_path=True,
                help="New file or folder name.",
            ),
        ) -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_filesystem_rename(
                old_path=old_path,
                new_path=new_path,
            )

            return True

        @application_filesystem_tree.command(
            name="setup",
            help="Setup filesystem tree.",
        )
        def setup(
            target_paths: list[_Path] = _typer.Option(
                ...,
                "--target-paths",
                "-tp",
                exists=False,
                file_okay=False,
                dir_okay=True,
                writable=True,
                resolve_path=True,
                help="Multiple folder paths",
            ),
        ) -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_filesystem_tree_setup(
                target_paths=target_paths
            )

            return True

        @application_filesystem_clean.command(
            name="path",
            help="Filesystem path cleaning.",
        )
        def path(
            target_paths: list[_Path] = _typer.Option(
                ...,
                "--target-paths",
                "-tp",
                exists=True,
                file_okay=True,
                dir_okay=True,
                writable=True,
                resolve_path=True,
                help="List of cleaning filesystem paths.",
            ),
        ) -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_filesystem_clean_path(
                target_paths=target_paths
            )

            return True

        @application_filesystem_clean.command(
            name="selection",
            help="Filesystem paths based on a selection.",
        )
        def selection(
            targets: list[str] = _typer.Argument(
                ...,
                help="List of cleaning targets.",
            ),
        ) -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_filesystem_clean_selection(
                targets=targets
            )

            return True

        @application_filesystem_clean_list.command(
            name="included",
            help="Show selections and whitelisted filesystem paths.",
        )
        def included() -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_filesystem_clean_list_included()

            return True

        @application_filesystem_clean_list.command(
            name="excluded",
            help="Show blacklisted filesystem paths.",
        )
        def excluded() -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_filesystem_clean_list_excluded()

            return True


        self._application.add_typer(
            application_filesystem,
            name="filesystem",
            help="Filesystem management.",
        )
        application_filesystem.add_typer(
            application_filesystem_tree,
            name="tree",
            help="Filesystem tree management.",
        )
        application_filesystem.add_typer(
            application_filesystem_clean,
            name="clean",
            help="Safe filesystem cleaning.",
        )
        application_filesystem_clean.add_typer(
            application_filesystem_clean_list,
            name="list",
            help="Show list information.",
        )

        return True


    def setup_workspace_command(self) -> bool:
        application_workspace: typer.Typer = _typer.Typer()
        application_workspace_list: typer.Typer = _typer.Typer()


        @application_workspace.command(
            name="export",
            help="Create workspaces archive file.",
        )
        def export(
            targets: list[str] = _typer.Argument(
                [],
                help="List of export targets.",
            ),
        ) -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_workspace_export(
                targets=targets
            )

            return True

        @application_workspace_list.command(
            name="exports",
            help="List of exportable workspaces.",
        )
        def exports() -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_workspace_list_exports()

            return True

        @application_workspace.command(
            name="import",
            help="Extract workspace archive file.",
        )
        def import_(
            input_path: str = _typer.Option(
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
            output_path: str = _typer.Option(
                "",
                "--output",
                "-o",
                file_okay=False,
                writable=True,
                resolve_path=True,
                help="Output filesystem path from exported workspace archive content.",
            ),
        ) -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_workspace_import(
                input_path=input_path,
                output_path=output_path
            )

            return True

        @application_workspace.command(
            name="setup",
            help="Initial or filesystem replenishment.",
        )
        def setup() -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_workspace_setup()

            return True


        self._application.add_typer(
            application_workspace,
            name="workspace",
            help="Manage workspaces.",
        )
        application_workspace.add_typer(
            application_workspace_list,
            name="list",
            help="Show list information.",
        )

        return True


    def setup_template_command(self) -> bool:
        application_template: typer.Typer = _typer.Typer()
        application_template_list: typer.Typer = _typer.Typer()


        @application_template_list.command(
            name="selections",
            help="Show a list of template selections.",
        )
        def selections() -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_template_list_selections()

            return True

        @application_template.command(
            name="apply",
            help="Apply filesystem templates.",
        )
        def apply(
            targets: list[str] = _typer.Argument(
                ["all"],
                help="List of workspace targets.",
            ),
        ) -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_template_apply(
                targets=targets
            )

            return True


        self._application.add_typer(
            application_template,
            name="template",
            help="Apply templates.",
        )
        application_template.add_typer(
            application_template_list,
            name="list",
            help="Show list information.",
        )

        return True


    def setup_workflow_command(self) -> bool:
        application_workflow: typer.Typer = _typer.Typer()
        application_workflow_list: typer.Typer = _typer.Typer()


        @application_workflow_list.command(
            name="selections",
            help="Show a list of defined workflows.",
        )
        def selections() -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_workflow_list_selections()

            return True

        @application_workflow.command(name="run", help="Run workflow selections.")
        def run(
            targets: list[str] = _typer.Argument(
                ...,
                help="List of workflows.",
            ),
        ) -> bool:
            command_manager = _SingletonManager.get_singleton(
                _CommandManager
            )
            command_manager.run_command_base_setup()
            command_manager.run_command_workflow_run(
                targets=targets
            )

            return True


        self._application.add_typer(
            application_workflow,
            name="workflow",
            help="Run workflows.",
        )
        application_workflow.add_typer(
            application_workflow_list,
            name="list",
            help="Show list information.",
        )

        return True
