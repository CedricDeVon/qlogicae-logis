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
    global _utility_data
    global _ImportManager
    global _utility_metadata

    from ..library import (
        import_manager,
    )
    from ..project.configuration import (
        utility,
    )

    _utility_data = (
        utility.DATA
    )
    _utility_metadata = (
        utility.METADATA
    )
    _ImportManager = (
        import_manager.ImportManager
    )

    _handle_dynamic_imports = lambda: None


class DatabaseManager:
    __slots__ = (
        "_import_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._import_manager = (
            _ImportManager.read_singleton(
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

    # def read_default_template_types(self) -> tuple[str, ...]:
    #     return ( "filesystem", )

    def read_default_filesystem_accessibility_types(self) -> tuple[str, ...]:
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

    # def read_default_plugin_file_extensions(self) -> set[str]:
    #     return {".py"}

    def read_default_groups(self) -> Any:
        return { "all": "all" }

    def read_default_selection_targets(self) -> Any:
        return {
            "root": "root",
            "group": "group",
            "project": "project",
        }

    # def read_none(self) -> str:
    #     return "none"

    # def read_not_a_number(self) -> str:
    #     return "nan"

    # def read_redacted(self) -> str:
    #     return "redacted"

    # def read_expunged(self) -> str:
    #     return "expunged"

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

    def read_debug_is_enabled(self) -> bool:
        data: bool = (
            ((_utility_data.get(
                "debug",
                {}
            ) or {}).get(
                "is-enabled",
                {}
            ) or {}).get(
                "value",
                False
            )
        )

        return data

    def read_company_name(self) -> str:
        data: str = (
            (_utility_data.get(
                "company-name",
                {}
            ) or {}).get(
                "value",
                "company"
            ) or "company"
        )

        return data

    def read_project_name(self) -> str:
        data: str = (
            (_utility_data.get(
                "project-name",
                {}
            ) or {}).get(
                "value",
                "project"
            ) or "project"
        )

        return data

    def read_company_project_name(self) -> str:
        data: str = (
            f"{self.read_company_name()}-"
            f"{self.read_project_name()}"
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
            ) or "v0"
        )

        return data

    def read_root_workspace_filesystem_path(
        self,
    ) -> str:
        return (
            f"{self._import_manager.read_original_executing_console_filesystem_path()}/"
            f".{
                self.read_company_project_major_version(
                    "/"
                )
            }"
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

    def read_default_export_groups(
        self,
    ) -> Any:
        data = {
            "all"
        }

        return { key: key for key in data }

    def read_object_filtered_export_included(
        self,
        targets: Any,
        patterns: Any
    ) -> Any:
        if not targets or not patterns:
            return targets

        data = set()
        for pattern in patterns:
            if not pattern:
                continue

            for target in targets:
                if pattern in target:
                    continue

                data.add(target)

        return data

    def read_default_disk_cache_output_file_path(
        self,
    ) -> str:
        base_path = (
            self.read_root_workspace_filesystem_path()
        )
        iso8601_date = (
            self._import_manager.read_current_iso8601_date()
        )

        return (
            f"{base_path}/private/temporary/cache/disk/{iso8601_date}.db"
        )

    def read_default_cache_disk_output_folder_path(
        self,
    ) -> str:
        base_path = (
            self.read_root_workspace_filesystem_path()
        )

        return (
            f"{base_path}/private/temporary/cache/disk"
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

    # def read_temporary_export_targets_source_filesystem_path(
    #     self,
    #     target: str,
    # ) -> str:
    #     if not target:
    #         raise ValueError("arguments must not be null")

    #     base_path = (
    #         self.read_root_workspace_filesystem_path()
    #     )

    #     return (
    #         f"{base_path}/private/temporary/export/targets/{target}"
    #     )

    # def read_temporary_export_targets_output_filesystem_path(
    #     self,
    #     target: str,
    #     relative_path: str,
    # ) -> str:
    #     if not target or not relative_path:
    #         raise ValueError("arguments must not be null")

    #     base_path = (
    #         self.read_root_workspace_filesystem_path()
    #     )

    #     return (
    #         f"{base_path}/private/temporary/export/targets/{target}/{relative_path}"
    #     )

    def read_configuration_workspace_filesystem_path(
        self,
        accessibility_type: str
    ) -> str:
        if not accessibility_type:
            raise ValueError("arguments must not be null")

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
        if not accessibility_type:
            raise ValueError("arguments must not be null")

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
        if not accessibility_type:
            raise ValueError("arguments must not be null")

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
        if not filesystem_path:
            raise ValueError("arguments must not be null")

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

    def read_object_property_timestamp_modified_value(
        self,
        data: Any,
    ) -> int:
        value: int = (data.get(
            "timestamp_modified",
            {},
        ) or {}).get(
            "value",
            0
        )

        return value

    def read_object_selection_origins(
        self,
        data: Any
    ) -> Any:
        if not data:
            raise ValueError("arguments must not be null")

        return { value for _key, value in data.items() }

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

    def read_default_export_selections(
        self,
    ) -> Any:
        company_project_major_version = (
            self.read_company_project_major_version("-")
        )
        data: Any = {
            f"{company_project_major_version}",
            f"{company_project_major_version}-public",
            f"{company_project_major_version}-private",
        }

        return { key: key for key in data }

    def read_default_export_selection_data(
        self,
    ) -> Any:
        root_path = (
            self._import_manager
                .read_original_executing_console_filesystem_path()
        )
        workspace_path = (
            f".{self.read_company_project_major_version("/")}"
        )
        export_name = (
            self
                .read_company_project_major_version("-")
        )
        input_target_public_export = {
            "filesystem-path": {
                "value": f"{workspace_path}/public"
            }
        }
        input_target_private_export = [
            {
                "filesystem-path": {
                    "value": f"{workspace_path}/.gitignore"
                }
            },
            {
                "filesystem-path": {
                    "value": f"{workspace_path}/private/.gitignore"
                }
            },
            {
                "filesystem-path": {
                    "value": f"{workspace_path}/private/configuration"
                }
            },
            {
                "filesystem-path": {
                    "value": f"{workspace_path}/private/plugin"
                }
            },
            {
                "filesystem-path": {
                    "value": f"{workspace_path}/private/template"
                }
            },
        ]

        def handle_read_output_targets(tag: str = "") -> Any:
            if tag:
                tag = f"-{tag}"

            return {
                "targets": [
                    {
                        "filesystem-path": {
                            "value": f"{root_path}/{export_name}{tag}"
                        }

                    }
                ]
            }

        data: Any = {
            f"{export_name}": {
                "input": {
                    "include": {
                        "targets": [
                            input_target_public_export,
                            *input_target_private_export
                        ]
                    }
                },
                "output": handle_read_output_targets()
            },
            f"{export_name}-public": {
                "input": {
                    "include": {
                        "targets": [
                            input_target_public_export
                        ]
                    },
                },
                "output": handle_read_output_targets("public")
            },
            f"{export_name}-private": {
                "input": {
                    "include": {
                        "targets": [
                            *input_target_private_export
                        ]
                    }
                },
                "output": handle_read_output_targets("private")
            },
        }

        return data

    def read_configuration_workspace_data_file(
        self,
        file_path: Any,
    ) -> Any:
        if not file_path:
            return {}

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
