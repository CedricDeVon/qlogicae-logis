from __future__ import annotations

from typing import Any

__all__ = (
    "ConsoleManager"
)

_argparse: Any = None
_TaskManager: Any = None
_ImportManager: Any = None
_DatabaseManager: Any = None
_CommandAboutManager: Any = None
_CommandCacheManager: Any = None
_CommandDebugManager: Any = None
_CommandWorkflowManager: Any = None
_CommandTemplateManager: Any = None
_CommandWorkspaceManager: Any = None
_CommandFilesystemManager: Any = None


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _argparse
    global _TaskManager
    global _ImportManager
    global _DatabaseManager
    global _CommandAboutManager
    global _CommandCacheManager
    global _CommandDebugManager
    global _CommandWorkflowManager
    global _CommandTemplateManager
    global _CommandWorkspaceManager
    global _CommandFilesystemManager

    import argparse

    from ..library import (
        command_about_manager,
        command_cache_manager,
        command_debug_manager,
        command_filesystem_manager,
        command_template_manager,
        command_workflow_manager,
        command_workspace_manager,
        database_manager,
        import_manager,
        task_manager,
    )

    _argparse = argparse
    _TaskManager = task_manager.TaskManager
    _ImportManager = import_manager.ImportManager
    _DatabaseManager = database_manager.DatabaseManager
    _CommandAboutManager = command_about_manager.CommandAboutManager
    _CommandCacheManager = command_cache_manager.CommandCacheManager
    _CommandDebugManager = command_debug_manager.CommandDebugManager
    _CommandWorkflowManager = command_workflow_manager.CommandWorkflowManager
    _CommandTemplateManager = command_template_manager.CommandTemplateManager
    _CommandWorkspaceManager = command_workspace_manager.CommandWorkspaceManager
    _CommandFilesystemManager = command_filesystem_manager.CommandFilesystemManager

    _handle_dynamic_imports = lambda: None


class ConsoleManager:
    __slots__ = (
        "_application",
        "_commands",
        "_command_about_manager",
        "_command_cache_manager",
        "_command_debug_manager",
        "_command_filesystem_manager",
        "_command_template_manager",
        "_command_workflow_manager",
        "_command_workspace_manager",
        "_task_manager",
        "_database_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._application: _argparse.ArgumentParser = (
            _argparse.ArgumentParser()
        )
        self._commands = self._application.add_subparsers(
            dest="command",
            metavar="",
        )
        self._command_about_manager = _ImportManager.read_singleton(
            _CommandAboutManager
        )
        self._command_cache_manager = _ImportManager.read_singleton(
            _CommandCacheManager
        )
        self._command_debug_manager = _ImportManager.read_singleton(
            _CommandDebugManager
        )
        self._command_filesystem_manager = _ImportManager.read_singleton(
            _CommandFilesystemManager
        )
        self._command_template_manager = _ImportManager.read_singleton(
            _CommandTemplateManager
        )
        self._command_workflow_manager = _ImportManager.read_singleton(
            _CommandWorkflowManager
        )
        self._command_workspace_manager = _ImportManager.read_singleton(
            _CommandWorkspaceManager
        )
        self._task_manager = _ImportManager.read_singleton(
            _TaskManager
        )
        self._database_manager = (
            _ImportManager.read_singleton(
                _DatabaseManager
            )
        )

    def run(self) -> bool:
        self.setup()

        try:
            arguments = self.read_arguments()

            command_handler = getattr(
                arguments,
                "command_handler",
                None,
            )

            if command_handler is not None:
                command_handler(
                    arguments
                )

            else:
                self._application.print_help()

        finally:
            self.shutdown()

        return True

    def setup_about_command(self) -> bool:
        def about_version(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_about_manager.run_command_about_version()
            return True

        application_about = self._commands.add_parser(
            "about",
            help="Build information.",
        )

        application_about_commands = (
            application_about.add_subparsers(
                dest="about_command",
            )
        )

        application_about_version = (
            application_about_commands.add_parser(
                "version",
                help="Current version on pip.",
            )
        )
        application_about_version.set_defaults(
            command_handler=about_version,
        )

        return True

    def setup_cache_command(self) -> bool:
        def cache_view_disk(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_cache_manager.run_command_cache_view_disk(
                key_paths=(arguments.key_paths or [])
            )
            return True

        def cache_view_value(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_cache_manager.run_command_cache_view_value(
                key_paths=(arguments.key_paths or [])
            )
            return True

        def cache_clear_disk(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_cache_manager.run_command_cache_clear_disk()
            return True

        def cache_clear_value(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_cache_manager.run_command_cache_clear_value()
            return True


        application_cache = self._commands.add_parser(
            "cache",
            help="Manage cache.",
        )

        cache_commands = application_cache.add_subparsers(
            dest="cache_command",
        )

        application_cache_view = cache_commands.add_parser(
            "view",
            help="View cache.",
        )

        cache_view_commands = application_cache_view.add_subparsers(
            dest="cache_view_command",
        )

        cache_view_disk_parser = cache_view_commands.add_parser(
            "disk",
            help="View disk cache.",
        )
        cache_view_disk_parser.add_argument(
            "--key-path",
            "-kp",
            dest="key_paths",
            action="append",
            default=[],
            type=str,
        )
        cache_view_disk_parser.set_defaults(
            command_handler=cache_view_disk,
        )

        cache_view_value_parser = cache_view_commands.add_parser(
            "value",
            help="View value cache.",
        )
        cache_view_value_parser.add_argument(
            "--key-path",
            "-kp",
            dest="key_paths",
            action="append",
            default=[],
            type=str,
        )
        cache_view_value_parser.set_defaults(
            command_handler=cache_view_value,
        )

        application_cache_clear = cache_commands.add_parser(
            "clear",
            help="Clear cache.",
        )

        cache_clear_commands = application_cache_clear.add_subparsers(
            dest="cache_clear_command",
        )

        cache_clear_disk_parser = cache_clear_commands.add_parser(
            "disk",
            help="Clear disk cache.",
        )
        cache_clear_disk_parser.set_defaults(
            command_handler=cache_clear_disk,
        )

        cache_clear_value_parser = cache_clear_commands.add_parser(
            "value",
            help="Clear value cache.",
        )
        cache_clear_value_parser.set_defaults(
            command_handler=cache_clear_value,
        )

        return True

    def setup_debug_command(self) -> bool:
        if not self._database_manager.read_debug_is_enabled():
            return False

        def debug_view_value_cache(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_debug_manager.run_command_debug_view_value_cache(
                key_paths=(arguments.key_paths or [])
            )
            return True

        def debug_view_disk_cache(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_debug_manager.run_command_debug_view_disk_cache(
                key_paths=(arguments.key_paths or [])
            )
            return True

        application_debug = self._commands.add_parser(
            "debug",
            help="Manage debug.",
        )

        application_debug_commands = (
            application_debug.add_subparsers(
                dest="debug_command",
            )
        )

        application_debug_view = (
            application_debug_commands.add_parser(
                "view",
                help="View debug.",
            )
        )

        application_debug_view_commands = (
            application_debug_view.add_subparsers(
                dest="debug_view_command",
            )
        )

        application_debug_view_value_cache = (
            application_debug_view_commands.add_parser(
                "value-cache",
                help="View value cache.",
            )
        )
        application_debug_view_value_cache.add_argument(
            "--key-path",
            "-kp",
            dest="key_paths",
            action="append",
            default=[],
            type=str,
        )

        application_debug_view_value_cache.set_defaults(
            command_handler=debug_view_value_cache,
        )

        application_debug_view_disk_cache = (
            application_debug_view_commands.add_parser(
                "disk-cache",
                help="View disk cache.",
            )
        )

        application_debug_view_disk_cache.add_argument(
            "--key-path",
            "-kp",
            dest="key_paths",
            action="append",
            default=[],
            type=str,
        )

        application_debug_view_disk_cache.set_defaults(
            command_handler=debug_view_disk_cache,
        )

        return True

    def setup_filesystem_command(self) -> bool:
        def filesystem_copy(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_filesystem_manager.run_command_filesystem_copy(
                source_path=arguments.source_path,
                target_paths=(arguments.target_paths or []),
            )
            return True

        def filesystem_move(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_filesystem_manager.run_command_filesystem_move(
                source_path=arguments.source_path,
                target_path=arguments.target_path,
            )
            return True

        def filesystem_rename(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_filesystem_manager.run_command_filesystem_rename(
                old_path=arguments.old_path,
                new_path=arguments.new_path,
            )
            return True

        def filesystem_tree_setup(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_filesystem_manager.run_command_filesystem_tree_setup(
                target_paths=(arguments.target_paths or [])
            )
            return True

        def filesystem_clean_path(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_filesystem_manager.run_command_filesystem_clean_path(
                target_paths=(arguments.target_paths or [])
            )
            return True

        def filesystem_clean_selection(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_filesystem_manager.run_command_filesystem_clean_selection(
                targets=(arguments.targets or [])
            )
            return True

        def filesystem_clean_list_included(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_filesystem_manager.run_command_filesystem_clean_list_included()
            return True

        def filesystem_clean_list_excluded(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_filesystem_manager.run_command_filesystem_clean_list_excluded()
            return True


        application_filesystem = self._commands.add_parser(
            "filesystem",
            help="Filesystem management.",
        )

        application_filesystem_commands = (
            application_filesystem.add_subparsers(
                dest="filesystem_command",
            )
        )

        application_filesystem_copy = (
            application_filesystem_commands.add_parser(
                "copy",
                help="Copy filesystem entities.",
            )
        )

        application_filesystem_copy.add_argument(
            "--source-path",
            "-sp",
            dest="source_path",
            required=True,
            type=str,
        )

        application_filesystem_copy.add_argument(
            "--target-path",
            "-tp",
            dest="target_paths",
            required=True,
            nargs="+",
            type=str,
        )

        application_filesystem_copy.set_defaults(
            command_handler=filesystem_copy,
        )

        application_filesystem_move = (
            application_filesystem_commands.add_parser(
                "move",
                help="Move filesystem entities.",
            )
        )

        application_filesystem_move.add_argument(
            "--source-path",
            "-sp",
            dest="source_path",
            required=True,
            type=str,
        )

        application_filesystem_move.add_argument(
            "--target-path",
            "-tp",
            dest="target_path",
            required=True,
            type=str,
        )

        application_filesystem_move.set_defaults(
            command_handler=filesystem_move,
        )

        application_filesystem_rename = (
            application_filesystem_commands.add_parser(
                "rename",
                help="Rename filesystem entities.",
            )
        )

        application_filesystem_rename.add_argument(
            "--old-path",
            "-op",
            dest="old_path",
            required=True,
            type=str,
        )

        application_filesystem_rename.add_argument(
            "--new-path",
            "-np",
            dest="new_path",
            required=True,
            type=str,
        )

        application_filesystem_rename.set_defaults(
            command_handler=filesystem_rename,
        )

        application_filesystem_tree = (
            application_filesystem_commands.add_parser(
                "tree",
                help="Filesystem tree management.",
            )
        )

        application_filesystem_tree_commands = (
            application_filesystem_tree.add_subparsers(
                dest="filesystem_tree_command",
            )
        )

        application_filesystem_tree_setup = (
            application_filesystem_tree_commands.add_parser(
                "setup",
                help="Setup filesystem tree.",
            )
        )

        application_filesystem_tree_setup.add_argument(
            "--target-path",
            "-tp",
            dest="target_paths",
            required=True,
            nargs="+",
            type=str,
        )

        application_filesystem_tree_setup.set_defaults(
            command_handler=filesystem_tree_setup,
        )

        application_filesystem_clean = (
            application_filesystem_commands.add_parser(
                "clean",
                help="Safe filesystem cleaning.",
            )
        )

        application_filesystem_clean_commands = (
            application_filesystem_clean.add_subparsers(
                dest="filesystem_clean_command",
            )
        )

        application_filesystem_clean_path = (
            application_filesystem_clean_commands.add_parser(
                "path",
                help="Filesystem path cleaning.",
            )
        )

        application_filesystem_clean_path.add_argument(
            "--target-path",
            "-tp",
            dest="target_paths",
            required=True,
            nargs="+",
            type=str,
        )

        application_filesystem_clean_path.set_defaults(
            command_handler=filesystem_clean_path,
        )

        application_filesystem_clean_selection = (
            application_filesystem_clean_commands.add_parser(
                "selection",
                help="Filesystem paths based on a selection.",
            )
        )

        application_filesystem_clean_selection.add_argument(
            "--target",
            "-t",
            dest="targets",
            nargs="+",
        )

        application_filesystem_clean_selection.set_defaults(
            command_handler=filesystem_clean_selection,
        )

        application_filesystem_clean_list = (
            application_filesystem_clean_commands.add_parser(
                "list",
                help="Show list information.",
            )
        )

        application_filesystem_clean_list_commands = (
            application_filesystem_clean_list.add_subparsers(
                dest="filesystem_clean_list_command",
            )
        )

        application_filesystem_clean_list_included = (
            application_filesystem_clean_list_commands.add_parser(
                "included",
                help=(
                    "Show selections and whitelisted "
                    "filesystem paths."
                ),
            )
        )

        application_filesystem_clean_list_included.set_defaults(
            command_handler=filesystem_clean_list_included,
        )

        application_filesystem_clean_list_excluded = (
            application_filesystem_clean_list_commands.add_parser(
                "excluded",
                help="Show blacklisted filesystem paths.",
            )
        )

        application_filesystem_clean_list_excluded.set_defaults(
            command_handler=filesystem_clean_list_excluded,
        )

        return True

    def setup_workspace_command(self) -> bool:
        def workspace_export(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_workspace_manager.run_command_workspace_export(
                targets=(arguments.targets or [])
            )
            return True

        def workspace_import(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_workspace_manager.run_command_workspace_import(
                input_path=(arguments.input_path or []),
                output_path=(arguments.output_path or []),
            )
            return True

        def workspace_replenish(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_workspace_manager.run_command_workspace_replenish()
            return True

        def workspace_list_exports(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_workspace_manager.run_command_workspace_list_exports()
            return True

        def workspace_setup(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_workspace_manager.run_command_workspace_setup()
            return True

        def workspace_install(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_workspace_manager.run_command_workspace_install(
                targets=(arguments.targets or [])
            )
            return True


        application_workspace = self._commands.add_parser(
            "workspace",
            help="Manage workspaces.",
        )

        application_workspace_commands = (
            application_workspace.add_subparsers(
                dest="workspace_command",
            )
        )

        application_workspace_export = (
            application_workspace_commands.add_parser(
                "export",
                help="Create workspaces archive file.",
            )
        )

        application_workspace_export.add_argument(
            "--target",
            "-t",
            dest="targets",
            nargs="*",
            type=str,
            default=[],
        )

        application_workspace_export.set_defaults(
            command_handler=workspace_export,
        )

        application_workspace_import = (
            application_workspace_commands.add_parser(
                "import",
                help="Extract workspace archive file.",
            )
        )

        application_workspace_import.add_argument(
            "--input-path",
            "-ip",
            dest="input_path",
            default="",
            type=str,
        )

        application_workspace_import.add_argument(
            "--output-path",
            "-op",
            dest="output_path",
            default="",
            type=str,
        )

        application_workspace_import.set_defaults(
            command_handler=workspace_import,
        )

        application_workspace_setup = (
            application_workspace_commands.add_parser(
                "setup",
                help="Complete workspace setup.",
            )
        )

        application_workspace_setup.set_defaults(
            command_handler=workspace_setup,
        )

        application_workspace_replenish = (
            application_workspace_commands.add_parser(
                "replenish",
                help="Filesystem replenishment.",
            )
        )

        application_workspace_replenish.set_defaults(
            command_handler=workspace_replenish,
        )

        application_workspace_install = (
            application_workspace_commands.add_parser(
                "install",
                help="Initial or filesystem replenishment.",
            )
        )

        application_workspace_install.add_argument(
            "--target",
            "-t",
            dest="targets",
            nargs="*",
            type=str,
            default=[],
        )

        application_workspace_install.set_defaults(
            command_handler=workspace_install,
        )

        application_workspace_list = (
            application_workspace_commands.add_parser(
                "list",
                help="Show list information.",
            )
        )

        application_workspace_list_commands = (
            application_workspace_list.add_subparsers(
                dest="workspace_list_command",
            )
        )

        application_workspace_list_exports = (
            application_workspace_list_commands.add_parser(
                "exports",
                help="List of exportable workspaces.",
            )
        )

        application_workspace_list_exports.set_defaults(
            command_handler=workspace_list_exports,
        )

        return True

    def setup_template_command(self) -> bool:
        def template_apply(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_template_manager.run_command_template_apply(
                targets=(arguments.targets or [])
            )
            return True

        def template_list_selections(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_template_manager.run_command_template_list_selections()
            return True


        application_template = self._commands.add_parser(
            "template",
            help="Apply templates.",
        )

        application_template_commands = (
            application_template.add_subparsers(
                dest="template_command",
            )
        )

        application_template_apply = (
            application_template_commands.add_parser(
                "apply",
                help="Apply filesystem templates.",
            )
        )

        application_template_apply.add_argument(
            "--target",
            "-t",
            dest="targets",
            nargs="*",
            type=str,
            default=[],
        )

        application_template_apply.set_defaults(
            command_handler=template_apply,
        )

        application_template_list = (
            application_template_commands.add_parser(
                "list",
                help="Show list information.",
            )
        )

        application_template_list_commands = (
            application_template_list.add_subparsers(
                dest="template_list_command",
            )
        )

        application_template_list_selections = (
            application_template_list_commands.add_parser(
                "selections",
                help="Show a list of template selections.",
            )
        )

        application_template_list_selections.set_defaults(
            command_handler=template_list_selections,
        )

        return True

    def setup_workflow_command(self) -> bool:
        def workflow_run(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_workflow_manager.run_command_workflow_run(
                targets=(arguments.targets or [])
            )
            return True

        def workflow_list_selections(
            arguments: _argparse.Namespace,
        ) -> bool:
            self._command_workflow_manager.run_command_workflow_list_selections()
            return True


        application_workflow = self._commands.add_parser(
            "workflow",
            help="Run workflows.",
        )

        application_workflow_commands = (
            application_workflow.add_subparsers(
                dest="workflow_command",
            )
        )

        application_workflow_run = (
            application_workflow_commands.add_parser(
                "run",
                help="Run workflow selections.",
            )
        )

        application_workflow_run.add_argument(
            "--target",
            "-t",
            dest="targets",
            nargs="+",
            type=str,
            default=[],
        )

        application_workflow_run.set_defaults(
            command_handler=workflow_run,
        )

        application_workflow_list = (
            application_workflow_commands.add_parser(
                "list",
                help="Show list information.",
            )
        )

        application_workflow_list_commands = (
            application_workflow_list.add_subparsers(
                dest="workflow_list_command",
            )
        )

        application_workflow_list_selections = (
            application_workflow_list_commands.add_parser(
                "selections",
                help="Show a list of defined workflows.",
            )
        )

        application_workflow_list_selections.set_defaults(
            command_handler=workflow_list_selections,
        )

        return True

    def read_arguments(self) -> Any:
        arguments = self._application.parse_args()

        return arguments

    def setup(self) -> bool:
        self.setup_about_command()
        self.setup_workflow_command()
        self.setup_workspace_command()
        self.setup_filesystem_command()
        self.setup_template_command()
        self.setup_cache_command()
        self.setup_debug_command()

        return True

    def shutdown(self) -> bool:
        self._task_manager.run_task_full_shutdown()

        return True
