from __future__ import annotations

from typing import Any

_DatabaseManager: Any = None
_SingletonManager: Any = None
_ConsoleDisplayManager: Any = None
_ConsoleComponentManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _DatabaseManager
    global _SingletonManager
    global _ConsoleDisplayManager
    global _ConsoleComponentManager

    from qlogicae_cor.v1.library import (
        console_component_manager,
        console_display_manager,
        singleton_manager,
    )

    from qlogicae_logis.v2.library import database_manager

    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _DatabaseManager = (
        database_manager.DatabaseManager
    )
    _ConsoleDisplayManager = console_display_manager.ConsoleDisplayManager
    _ConsoleComponentManager = console_component_manager.ConsoleComponentManager

    _handle_dynamic_imports = lambda: None

class CommandAboutManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()

    def run_command_about_version(
        self,
    ) -> bool:
        _SingletonManager.get_singleton(
            _ConsoleDisplayManager
        ).render_one_component(
            _SingletonManager.get_singleton(
                _DatabaseManager
            ).setup_about_data_project_version_value()
        )

        return True

    def run_command_about_me(
        self,
    ) -> bool:
        console_component_manager = _SingletonManager.get_singleton(
            _ConsoleComponentManager
        )
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        _SingletonManager.get_singleton(
            _ConsoleDisplayManager
        ).render_many_components(
            (
                console_component_manager.setup_branding(
                    database_manager
                        .setup_about_data_project_brand_name_value(),
                    database_manager
                        .setup_about_data_project_description_value()
                ),
                console_component_manager.setup_horizontal_rule(),
                console_component_manager.setup_table(
                    database_manager
                        .setup_about_data_project_table()
                ),
                console_component_manager.setup_end_padding(),
            )
        )

        return True

