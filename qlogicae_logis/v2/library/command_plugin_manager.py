from __future__ import annotations

from typing import Any

_Path: Any = None
_LogManager: Any = None
_DatabaseManager: Any = None
_SingletonManager: Any = None
_module_from_spec: Any = None
_CommandUtilityManager: Any = None
_CommandStorageManager: Any = None
_spec_from_file_location: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _Path
    global _LogManager
    global _DatabaseManager
    global _SingletonManager
    global _module_from_spec
    global _CommandUtilityManager
    global _CommandStorageManager
    global _spec_from_file_location


    from importlib.util import module_from_spec, spec_from_file_location
    from pathlib import Path

    from qlogicae_cor.v1.library import (
        singleton_manager,
    )

    from qlogicae_logis.v2.library import (
        command_storage_manager,
        command_utility_manager,
        database_manager,
        log_manager,
    )

    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _DatabaseManager = (
        database_manager.DatabaseManager
    )
    _CommandStorageManager = (
        command_storage_manager.CommandStorageManager
    )
    _CommandUtilityManager = (
        command_utility_manager.CommandUtilityManager
    )
    _LogManager = (
        log_manager.LogManager
    )
    _Path = (
        Path
    )
    _module_from_spec = (
        module_from_spec
    )
    _spec_from_file_location = (
        spec_from_file_location
    )

    _handle_dynamic_imports = lambda: None

class CommandPluginManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()

    def run_command_plugin_setup(self) -> bool:
        log_manager = _SingletonManager.get_singleton(
            _LogManager
        )
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )
        command_storage_manager = _SingletonManager.get_singleton(
            _CommandStorageManager
        )
        command_utility_manager = _SingletonManager.get_singleton(
            _CommandUtilityManager
        )

        workspace_scope_selections = (
            command_utility_manager
                .default_filesystem_accessibility_types
        )

        command_plugins: set[str] = set()
        for scope_selection in workspace_scope_selections:
            if not scope_selection:
                log_manager.full_log_warning(
                    "invalid arguments"
                )
                continue

            target_path = _Path(
                f"{
                    command_utility_manager.setup_root_workspace_plugin_filesystem_path(
                        scope_selection
                    )
                }"
            )

            files = sorted(
                path
                for path in target_path.rglob("*.py")
                if "__pycache__" not in path.parts
            )
            for file in files:
                if not file:
                    log_manager.full_log_warning(
                        "invalid arguments"
                    )
                    continue

                module_name = file.stem

                spec = _spec_from_file_location(module_name, file)
                if spec is None or spec.loader is None:
                    log_manager.full_log_warning(
                        f"cannot load module from '{file}'"
                    )
                    continue

                module = _module_from_spec(spec)
                spec.loader.exec_module(module)

                if not module.run_command:
                    log_manager.full_log_warning(
                        f"'{file}' must contain a 'run_command'"
                        "function for each plugin module"
                    )
                    continue

                command_storage_manager.add_command(
                    f"run_command_{module_name}",
                    module.run_command,
                )

                command_plugins.add(
                    module_name
                )

        database_manager.command_plugins = (
            command_plugins
        )

        return True


