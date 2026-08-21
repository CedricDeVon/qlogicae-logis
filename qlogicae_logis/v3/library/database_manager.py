from __future__ import annotations

from typing import Any

__all__ = (
    "DatabaseManager"
)

_utility_data: Any = None
_ImportManager: Any = None
_utility_metadata: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _ImportManager

    from ..library import (
        import_manager,
    )

    _ImportManager = (
        import_manager.ImportManager
    )

    _handle_dynamic_imports = lambda: None


def _handle_utility_dynamic_imports() -> None:
    global _utility_data
    global _utility_metadata
    global _handle_utility_dynamic_imports

    from ..project.configuration import utility

    _utility_data = utility.DATA
    _utility_metadata = utility.METADATA

    _handle_utility_dynamic_imports = lambda: None


class DatabaseManager:
    __slots__ = (
        "_import_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()
        _handle_utility_dynamic_imports()

        self._import_manager = (
            _ImportManager.get_singleton(
                _ImportManager
            )
        )

    # Constants
    def read_default_static_value_cache_macros(self) -> set[str]:
        return {
            "current-date",
            "current-year",
            "time-zone",
            "operating-system-name",
            "operating-system-architecture",
            "current-timestamp",
            "root-filesystem-path",
            "selection-filesystem-path",
        }

    def read_default_dynamic_value_cache_macros(self) -> dict[str, Any]:
        return {}

    def read_default_template_types(self) -> tuple[str, str]:
        return ( "filesystem", "fragment", )

    def read_default_filesystem_accessibility_types(self) -> tuple[str, str]:
        return ( "private", "public", )

    def read_default_data_file_extensions(self) -> set[str]:
        return (
            self.read_default_yaml_data_file_extensions() |
            self.read_default_json_data_file_extensions() |
            self.read_default_python_data_file_extensions()
        )

    def read_default_yaml_data_file_extensions(self) -> set[str]:
        return {".yaml", ".yml"}

    def read_default_json_data_file_extensions(self) -> set[str]:
        return {".json"}

    def read_default_python_data_file_extensions(self) -> set[str]:
        return {".py"}

    def read_default_plugin_file_extensions(self) -> set[str]:
        return {".py"}

    def read_default_selection_targets(self) -> Any:
        return {
            "all": "all",
            "root": "root",
            "group": "group",
            "project": "project",
        }

    def read_none(self) -> str:
        return "none"

    def read_not_a_number(self) -> str:
        return "nan"

    def read_redacted(self) -> str:
        return "redacted"

    def read_expunged(self) -> str:
        return "expunged"

    def read_debug(self) -> bool:
        data: bool = (
            _utility_data.get(
                "debug",
                {}
            ).get(
                "value",
                False
            )
        )

        return data

    def read_company_name(self) -> str:
        data: str = (
            _utility_data.get(
                "company-name",
                {}
            ).get(
                "value",
                "company"
            )
        )

        return data

    def read_project_name(self) -> str:
        data: str = (
            _utility_data.get(
                "project-name",
                {}
            ).get(
                "value",
                "project"
            )
        )

        return data

    def read_active_major_version_label(self) -> str:
        data: str = (
            _utility_data.get(
                "active-major-version-label",
                {}
            ).get(
                "value",
                "v0"
            )
        )

        return data

    def read_root_workspace_filesystem_path(
        self,
    ) -> str:
        return (
            f"{self._import_manager.read_current_executing_console_filesystem_path()}/"
            f".{
            self.read_company_project_major_version(
            "/"
            )}"
        )

    def read_root_plugin_filesystem_path(
        self,
        scope_selection: str,
    ) -> str:
        return (
            f"{self.read_root_workspace_filesystem_path()}/{scope_selection}/plugin"
        )

    def read_default_log_output_filesystem_paths(
        self,
    ) -> set[str]:
        return {
            f"{self.read_root_workspace_filesystem_path()}/private"
            f"/temporary/log/{self._import_manager.read_current_iso8601_date()}.log",
        }

    def read_default_disk_cache_output_file_path(
        self,
    ) -> str:
        return (
            f"{self.read_root_workspace_filesystem_path()}/private"
            f"/temporary/cache/disk/{self._import_manager.read_current_iso8601_date()}.db"
        )

    def read_default_cache_disk_output_folder_path(
        self,
    ) -> str:
        return (
            f"{self.read_root_workspace_filesystem_path()}/private"
            f"/temporary/cache/disk"
        )

    def read_temporary_template_output_filesystem_path(
        self,
    ) -> str:
        base_path = (
            self.read_root_workspace_filesystem_path()
        )

        return (
            f"{base_path}/private/temporary/template"
        )

    def read_temporary_export_output_filesystem_path(
        self,
    ) -> str:
        base_path = (
            self.read_root_workspace_filesystem_path()
        )

        return (
            f"{base_path}/private/temporary/export"
        )

    def read_temporary_export_targets_source_filesystem_path(
        self,
        target: str,
    ) -> str:
        base_path = (
            self.read_root_workspace_filesystem_path()
        )

        return (
            f"{base_path}/private/temporary/export/targets/{target}"
        )

    def read_temporary_export_targets_output_filesystem_path(
        self,
        target: str,
        relative_path: str,
    ) -> str:
        base_path = (
            self.read_root_workspace_filesystem_path()
        )

        return (
            f"{base_path}/private/temporary/export/targets/{target}/{relative_path}"
        )

    def read_configuration_workspace_filesystem_path(
        self,
        accessibility_type: str
    ) -> str:
        base_path = (
            self.read_root_workspace_filesystem_path()
        )

        return (
            f"{base_path}/{accessibility_type}/configuration/workspace"
        )

    def read_configuration_workspace_base_file_paths(
        self,
        accessibility_type: str
    ) -> Any:
        base_path = (
            self.read_configuration_workspace_filesystem_path(
                accessibility_type
            )
        )

        return (
            f"{base_path}/root",
            f"{base_path}/project/project",
            f"{base_path}/group/group",
        )

    def read_configuration_workspace_base_folder_paths(
        self,
        accessibility_type: str
    ) -> Any:
        base_path = (
            self.read_configuration_workspace_filesystem_path(
                accessibility_type
            )
        )

        return (
            f"{base_path}/group/selection",
            f"{base_path}/project/selection",
        )

    def read_file_metadata(
        self,
        filesystem_path: str
    ) -> Any:
        return {
            "timestamp_modified": {
                "value": (
                    self._import_manager
                        .read_filesystem_modification_timestamp(
                            value=filesystem_path
                        )
                )
            }
        }

    def read_company_project_major_version(
        self,
        delimeter: str,
    ) -> str:
        return (
            f"{self.read_company_name()}{delimeter}"
            f"{self.read_project_name()}{delimeter}"
            f"{self.read_active_major_version_label()}"
        )

    def read_root_key_path(
        self,
    ) -> tuple[str, str, str]:
        return (
            f"{self.read_company_name()}",
            f"{self.read_project_name()}",
            f"{self.read_active_major_version_label()}",
        )

    # Object
    def read_object_property_timestamp_modified_value(
        self,
        data: Any,
    ) -> int:
        value: int = data.get(
            "timestamp_modified",
            {},
        ).get(
            "value",
            None
        )

        return value

    def read_plugin_data(
        self,
        module: Any,
    ) -> Any:
        module = {
            "command": (
                module.command if hasattr(module, "command") else None
            ),
            "macros": (
                module.macros if hasattr(module, "macros") else None
            ),
        }

        return module

    def read_configuration_workspace_data_file(
        self,
        file_path: Any,
    ) -> Any:
        data: Any = {}
        file_path_suffix = (
            self._import_manager.read_file_suffix(
                value=file_path
            )
        )

        if file_path_suffix in self.read_default_yaml_data_file_extensions():
            data = self._import_manager.read_yaml_file(
                file_path=file_path
            ) or {}

        elif file_path_suffix in self.read_default_json_data_file_extensions():
            data = self._import_manager.read_json_file(
                file_path=file_path
            ) or {}

        elif file_path_suffix in self.read_default_python_data_file_extensions():
            data = self._import_manager.read_python_file(
                file_path=file_path
            ) or {}

        return data
