from __future__ import annotations

from typing import Any

_about_data: Any = None
_about_metadata: Any = None

_SingletonManager: Any = None
_ConsoleDisplayManager: Any = None
_ConsoleComponentManager: Any = None
_PlaceholderValueManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _about_data
    global _ConsoleDisplayManager
    global _ConsoleComponentManager
    global _SingletonManager
    global _PlaceholderValueManager

    from qlogicae_cor.v1.library import placeholder_value_manager, singleton_manager

    from qlogicae_logis.v2.project.configuration import about
    from qlogicae_logis.v2.library import (
        console_component_manager,
        console_display_manager,
    )

    _about_data = about.DATA
    _about_metadata = about.METADATA
    _ConsoleDisplayManager = console_display_manager.ConsoleDisplayManager
    _ConsoleComponentManager = console_component_manager.ConsoleComponentManager
    _SingletonManager = singleton_manager.SingletonManager
    _PlaceholderValueManager = placeholder_value_manager.PlaceholderValueManager

    _handle_dynamic_imports = lambda: None


class ConsoleAboutManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()

    def render_version(self) -> bool:
        project_version = (
            _about_data["project-version"]
            if _about_data
            and "project-version" in _about_data
            else {}
        ) or {}

        project_version_value = (
            project_version["value"]
            if project_version
            and "value" in project_version
            else "None"
        ) or "None"

        _SingletonManager.get_singleton(
            _ConsoleDisplayManager
        ).render_one_component(
            project_version_value
        )

        return True

    def render_me(self) -> bool:
        placeholder_value_manager = _SingletonManager.get_singleton(
            _PlaceholderValueManager
        )
        console_display_manager = _SingletonManager.get_singleton(
            _ConsoleDisplayManager
        )
        console_component_manager = _SingletonManager.get_singleton(
            _ConsoleComponentManager
        )

        toolset_about_table = {
            key: value
            for key, value in _about_data.items()
            if value and
            "is-tabular" in value and
            value["is-tabular"]
        }

        toolset_about_table_rows = []
        for _key, item in toolset_about_table.items():
            item_name = (
                item["name"]
                if "name" in item
                else placeholder_value_manager.none
            )
            item_value = (
                str(item["value"])
                if "value" in item
                else placeholder_value_manager.none
            )
            toolset_about_table_rows.append([item_name, item_value])

        toolset_about_table_data = {
            "headers": ["key", "value"],
            "rows": toolset_about_table_rows,
        }
        toolset_about_brand_name = (
            _about_data["brand-name"]["value"]
            if _about_data
            and "brand-name" in _about_data
            and "value" in _about_data["brand-name"]
            else placeholder_value_manager.none
        ) or placeholder_value_manager.none
        toolset_about_project_description = (
            _about_data["project-description"]["value"]
            if _about_data
            and "project-description" in _about_data
            and "value" in _about_data["project-description"]
            else placeholder_value_manager.none
        ) or placeholder_value_manager.none

        console_display_manager.render_many_components(
            [
                console_component_manager.setup_branding(
                    toolset_about_brand_name, toolset_about_project_description
                ),
                console_component_manager.setup_horizontal_rule(),
                console_component_manager.setup_table(
                    toolset_about_table_data
                ),
                console_component_manager.setup_end_padding(),
            ]
        )

        return True
