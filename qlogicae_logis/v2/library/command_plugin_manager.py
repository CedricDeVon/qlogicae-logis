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

        registered_plugins: set[str] = set()
        module_data_macros_static_values = {}
        module_data_macros_dynamic_values = {}

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

                if not hasattr(module, "DATA"):
                    log_manager.full_log_warning(
                        f"'{file}' must contain a 'DATA' object "
                        "for each plugin module"
                    )
                    continue

                module_data = module.DATA

                if module_data is None:
                    log_manager.full_log_warning(
                        f"'{file}' must contain a 'DATA' object "
                        "for each plugin module"
                    )
                    continue

                module_data_commands = (
                    module_data["commands"]
                    if module_data
                    and "commands" in module_data
                    else {}
                ) or {}

                for command_name, command_item in (
                    module_data_commands.items()
                ):
                    if not command_name or not command_item:
                        log_manager.full_log_warning(
                            "invalid arguments"
                        )
                        continue

                    if "value" not in command_item:
                        log_manager.full_log_warning(
                            "invalid arguments"
                        )
                        continue

                    command_storage_manager.add_command(
                        f"run_command_{command_name}",
                        command_item["value"],
                    )

                module_data_macros = (
                    module_data["macros"]
                    if module_data
                    and "macros" in module_data
                    else {}
                ) or {}

                module_data_macros_static = (
                    module_data_macros["static"]
                    if module_data_macros
                    and "static" in module_data_macros
                    else {}
                ) or {}

                module_data_macros_dynamic = (
                    module_data_macros["dynamic"]
                    if module_data_macros
                    and "dynamic" in module_data_macros
                    else {}
                ) or {}


                for macros_static_name, macros_static_item in (
                    module_data_macros_static.items()
                ):
                    if not macros_static_name or not macros_static_item:
                        log_manager.full_log_warning(
                            "invalid arguments"
                        )
                        continue

                    if "value" not in macros_static_item:
                        log_manager.full_log_warning(
                            "invalid arguments"
                        )
                        continue

                    module_data_macros_static_values[macros_static_name] = (
                        macros_static_item["value"]
                    )

                for macros_dynamic_name, macros_dynamic_item in (
                    module_data_macros_dynamic.items()
                ):
                    if not macros_dynamic_name or not macros_dynamic_item:
                        log_manager.full_log_warning(
                            "invalid arguments"
                        )
                        continue

                    if "value" not in macros_dynamic_item:
                        log_manager.full_log_warning(
                            "invalid arguments"
                        )
                        continue

                    module_data_macros_dynamic_values[macros_dynamic_name] = (
                        macros_dynamic_item["value"]
                    )

            registered_plugins.add(
                f"{scope_selection}-{module_name}"
            )

        database_manager.workspace_macros = (
            database_manager.workspace_macros |
            module_data_macros_static_values
        )
        database_manager.workspace_macros_dynamic = (
            database_manager.workspace_macros_dynamic |
            module_data_macros_dynamic_values
        )
        database_manager.registered_plugins = (
            registered_plugins
        )

        return True


