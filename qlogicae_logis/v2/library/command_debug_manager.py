from __future__ import annotations

from typing import Any

_DatabaseManager: Any = None
_SingletonManager: Any = None
_ConsoleDisplayManager: Any = None
_CommandUtilityManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _DatabaseManager
    global _SingletonManager
    global _ConsoleDisplayManager
    global _CommandUtilityManager

    from qlogicae_cor.v1.library import (
        console_display_manager,
        singleton_manager,
    )

    from qlogicae_logis.v2.library import (
        command_utility_manager,
        database_manager,
    )

    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _DatabaseManager = (
        database_manager.DatabaseManager
    )
    _CommandUtilityManager = (
        command_utility_manager.CommandUtilityManager
    )
    _ConsoleDisplayManager = console_display_manager.ConsoleDisplayManager

    _handle_dynamic_imports = lambda: None

class CommandDebugManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()

    def run_command_debug_view_value_cache(
        self,
        **kwargs: Any,
    ) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )
        command_utility_manager = _SingletonManager.get_singleton(
            _CommandUtilityManager
        )


        targets = kwargs.get("target", [])
        targets = (
            command_utility_manager
                .setup_value_cache_targets(
                    tuple(targets)
                )
        )

        for target in targets:
            if not target:
                continue

            data = (
                database_manager.read_data(
                    tuple(
                        target.split(".")
                    )
                )
            )
            workspace_data_macros_default_on_parse_is_enabled_value = (
                database_manager
                    .workspace_data_macros_default_on_parse_is_enabled_value
            )
            if workspace_data_macros_default_on_parse_is_enabled_value:
                data = (
                    command_utility_manager.parse_many(
                        data,
                    )
                )

            _SingletonManager.get_singleton(
                _ConsoleDisplayManager
            ).render_one_component(
                data
            )

        return True
