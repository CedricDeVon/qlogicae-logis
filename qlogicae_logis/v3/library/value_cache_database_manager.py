from __future__ import annotations

from typing import Any

__all__ = (
    "ValueCacheDatabaseManager"
)

_TaskManager: Any = None
_ImportManager: Any = None
_DatabaseManager: Any = None
_CommandStorageManager: Any = None


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _TaskManager
    global _ImportManager
    global _DatabaseManager
    global _CommandStorageManager

    from ..library import (
        database_manager,
        import_manager,
        task_manager,
    )

    _TaskManager = (
        task_manager
            .TaskManager
    )
    _ImportManager = (
        import_manager
            .ImportManager
    )
    _DatabaseManager = (
        database_manager.DatabaseManager
    )

    _handle_dynamic_imports = lambda: None

class ValueCacheDatabaseManager:
    __slots__ = (
        "_import_manager",
        "_database_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._import_manager = (
            _ImportManager.get_singleton(
                _ImportManager
            )
        )
        self._database_manager = (
            _ImportManager.get_singleton(
                _DatabaseManager
            )
        )

    def read_key_path(self, key_path: Any) -> Any:
        return (
            *self._database_manager.read_root_key_path(),
            *key_path,
        )

    def read_any_value(
        self,
        key_path: Any
    ) -> Any:
        result: Any = (
            self._import_manager.read_any_value_via_value_cache(
                key_path=(
                    self.read_key_path(
                        key_path
                    )
                ),
            )
        ) or {}

        return result

    def write_any_value(
        self,
        key_path: Any,
        value: Any
    ) -> bool:
        result: bool = (
            self._import_manager.write_any_value_via_value_cache(
                key_path=(
                    self.read_key_path(
                        key_path
                    )
                ),
                value=value,
            )
        )

        return result

    def remove_any_value(
        self,
        key_path: Any,
    ) -> bool:
        result: bool = (
            self._import_manager.remove_one_value_via_value_cache(
                key_path=(
                    self.read_key_path(
                        key_path
                    )
                ),
            )
        )

        return result

    def read_debug_snapshot_execution_timestamp_start(
        self,
        label: str = "",
    ) -> int:
        if not self._database_manager.read_debug():
            return 0

        result: int = self.read_any_value(
            (
                "debug",
                "snapshot",
                f"{label}",
                "timestamp",
                "start",
                "value",
            ),
        )

        return result

    def write_debug_snapshot_execution_timestamp_start(
        self,
        label: str = "",
    ) -> bool:
        if not self._database_manager.read_debug():
            return True

        self.write_any_value(
            (
                "debug",
                "snapshot",
                f"{label}",
                "timestamp",
                "start",
                "value",
            ),
            self._import_manager.read_current_nanosecond()
        )

        return True

    def read_debug_snapshot_execution_timestamp_complete(
        self,
        label: str = "",
    ) -> int:
        if not self._database_manager.read_debug():
            return 0

        result: int = self.read_any_value(
            (
                "debug",
                "snapshot",
                f"{label}",
                "timestamp",
                "complete",
                "value",
            ),
        )

        return result

    def write_debug_snapshot_execution_timestamp_complete(
        self,
        label: str = "",
    ) -> bool:
        if not self._database_manager.read_debug():
            return True

        self.write_any_value(
            (
                "debug",
                "snapshot",
                f"{label}",
                "timestamp",
                "complete",
                "value",
            ),
            self._import_manager.read_current_nanosecond()
        )

        self.write_debug_snapshot_execution_timestamp_duration(label=label)

        return True

    def read_debug_snapshot_execution_timestamp_duration(
        self,
        label: str = "",
    ) -> float:
        if not self._database_manager.read_debug():
            return 0.0

        result: float = self.read_any_value(
            (
                "debug",
                "snapshot",
                f"{label}",
                "timestamp",
                "duration",
                "value",
            ),
        )

        return result

    def write_debug_snapshot_execution_timestamp_duration(
        self,
        label: str = "",
    ) -> bool:
        if not self._database_manager.read_debug():
            return True

        duration = (
            (self.read_debug_snapshot_execution_timestamp_complete(label=label) -
            self.read_debug_snapshot_execution_timestamp_start(
                label=label
            )) / 1000000
        )

        self.write_any_value(
            (
                "debug",
                "snapshot",
                f"{label}",
                "timestamp",
                "duration",
                "value",
            ),
            duration
        )

        return True


    def read_current_timestamp(self) -> int:
        result: int = self.read_any_value(
            (
                "current-timestamp",
                "value",
            ),
        ) or 0

        return result

    def write_current_timestamp(self) -> bool:
        self.write_any_value(
            (
                "current-timestamp",
                "value",
            ),
            self._import_manager.read_current_nanosecond()
        )

        return True

    def read_time_zone_name(self) -> str:
        result: str = self.read_any_value(
            (
                "time-zone",
                "value",
            ),
        ) or ""

        return result

    def write_time_zone_name(self, value: Any) -> bool:
        self.write_any_value(
            (
                "time-zone",
                "value",
            ),
            value
        )

        return True

    def write_default_time_zone_name(self) -> bool:
        self.write_any_value(
            (
                "time-zone",
                "value",
            ),
            "local"
        )

        return True

    def read_operating_system_name(self) -> str:
        result: str = self.read_any_value(
            (
                "operating-system-name",
                "value",
            ),
        ) or ""

        return result

    def write_operating_system_name(self, value: Any) -> bool:
        self.write_any_value(
            (
                "operating-system-name",
                "value",
            ),
            value
        )

        return True

    def write_default_operating_system_name(self) -> bool:
        self.write_any_value(
            (
                "operating-system-name",
                "value",
            ),
            self._import_manager.read_operating_system_name()
        )

        return True

    def read_operating_system_architecture(self) -> str:
        result: str = self.read_any_value(
            (
                "operating-system-architecture",
                "value",
            ),
        ) or ""

        return result

    def write_operating_system_architecture(self, value: Any) -> bool:
        self.write_any_value(
            (
                "operating-system-architecture",
                "value",
            ),
            value
        )

        return True

    def write_default_operating_system_architecture(self) -> bool:
        self.write_any_value(
            (
                "operating-system-architecture",
                "value",
            ),
            self._import_manager.read_operating_system_architecture()
        )

        return True

    def read_current_date(self) -> str:
        result: str = self.read_any_value(
            (
                "current-date",
                "value",
            ),
        ) or "1970"

        return result

    def write_current_date(self) -> bool:
        self.write_any_value(
            (
                "current-date",
                "value",
            ),
            self._import_manager.read_current_iso8601_date()
        )

        return True

    def read_current_year(self) -> int:
        result: int = self.read_any_value(
            (
                "current-year",
                "value",
            ),
        ) or 0

        return result

    def write_current_year(self) -> bool:
        self.write_any_value(
            (
                "current-year",
                "value",
            ),
            self._import_manager.read_current_year()
        )

        return True

    def read_root_filesystem_path(self) -> str:
        result: str = self.read_any_value(
            (
                "root-filesystem-path",
                "value",
            ),
        )

        return result

    def write_root_filesystem_path(self) -> bool:
        self.write_any_value(
            (
                "root-filesystem-path",
                "value",
            ),
            self._import_manager.read_current_executing_console_filesystem_path()
        )

        return True

    def read_selection_filesystem_path(self) -> str:
        result: str = self.read_any_value(
            (
                "selection-filesystem-path",
                "value",
            ),
        )

        return result

    def write_selection_filesystem_path(self) -> bool:
        self.write_any_value(
            (
                "selection-filesystem-path",
                "value",
            ),
            f"{
                self._import_manager.read_current_executing_console_filesystem_path()
            }/selection",
        )

        return True

    def read_current_executing_script_filesystem_path(self) -> str:
        result: str = self.read_any_value(
            (
                "current-executing-script-filesystem-path",
                "value",
            ),
        )

        return result

    def write_current_executing_script_filesystem_path(
        self,
        value: str
    ) -> bool:
        self.write_any_value(
            (
                "current-executing-script-filesystem-path",
                "value",
            ),
            value,
        )

        return True

    def read_initial_executing_console_filesystem_path(
        self
    ) -> str:
        result: str = self.read_any_value(
            (
                "initial-executing-console-filesystem-path",
                "value",
            ),
        )

        return result

    def write_initial_executing_console_filesystem_path(
        self,
        value: str
    ) -> bool:
        self.write_any_value(
            (
                "initial-executing-console-filesystem-path",
                "value",
            ),
            value,
        )

        return True

    def read_previous_executing_console_filesystem_path(
        self
    ) -> str:
        result: str = self.read_any_value(
            (
                "previous-executing-console-filesystem-path",
                "value",
            ),
        )

        return result

    def write_previous_executing_console_filesystem_path(
        self,
        value: str
    ) -> bool:
        self.write_any_value(
            (
                "previous-executing-console-filesystem-path",
                "value",
            ),
            value,
        )

        return True

    def read_current_executing_console_filesystem_path(
        self
    ) -> str:
        result: str = self.read_any_value(
            (
                "current-executing-console-filesystem-path",
                "value",
            ),
        )

        return result

    def write_current_executing_console_filesystem_path(
        self,
        value: str
    ) -> bool:
        self.write_any_value(
            (
                "current-executing-console-filesystem-path",
                "value",
            ),
            value,
        )

        return True

    def read_macros(
        self,
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "macros",
            ),
        ) or {}

        return result

    def write_macros(
        self,
        value: Any
    ) -> bool:
        self.write_any_value(
            (
                "macros",
            ),
            value,
        )

        return True

    def read_public_configuration_workspace(
        self
    ) -> Any:
        result: Any = self.read_configuration_workspace(
            "public",
        ) or {}

        return result

    def write_public_configuration_workspace(
        self,
        value: Any
    ) -> bool:
        self.write_configuration_workspace(
            "public",
            value,
        )

        return True

    def read_private_configuration_workspace(
        self
    ) -> Any:
        result: Any = self.read_configuration_workspace(
            "private",
        ) or {}

        return result

    def write_private_configuration_workspace(
        self,
        value: Any
    ) -> bool:
        self.write_configuration_workspace(
            "private",
            value,
        )

        return True

    def read_configuration_workspace(
        self,
        accessibility_type: str
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "raw",
                accessibility_type,
            ),
        ) or {}

        return result

    def write_configuration_workspace(
        self,
        accessibility_type: str,
        value: Any
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "raw",
                accessibility_type,
            ),
            value,
        )

        return True

    def remove_configuration_workspace(
        self,
    ) -> bool:
        self.remove_any_value(
            (
                "configuration",
                "workspace",
                "raw",
            ),
        )

        return True

    def read_configuration_workspace_data(
        self,
        accessibility_type: str,
        key_path: str,
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "raw",
                accessibility_type,
                key_path,
                "data",
                "value",
            ),
        ) or {}

        return result

    def write_configuration_workspace_rdata(
        self,
        accessibility_type: str,
        key_path: str,
        value: Any
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "raw",
                accessibility_type,
                key_path,
                "data",
                "value",
            ),
            value,
        )

        return True

    def read_is_configuration_workspace_modified(
        self
    ) -> bool:
        result: bool = self.read_any_value(
            (
                "configuration",
                "workspace",
                "raw",
                "is-modified",
                "value"
            ),
        )

        return result

    def write_is_configuration_workspace_modified(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "raw",
                "is-modified",
                "value"
            ),
            value,
        )

        return True

    def read_configuration_workspace_file_count(
        self,
        accessibility_type: str,
    ) -> bool:
        result: bool = self.read_any_value(
            (
                "configuration",
                "workspace",
                "raw",
                "count",
                accessibility_type,
                "value"
            ),
        )

        return result

    def write_configuration_workspace_file_count(
        self,
        accessibility_type: str,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "raw",
                "count",
                accessibility_type,
                "value"
            ),
            value,
        )

        return True

    def read_merged_configuration_workspace_data(
        self,
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
            ),
        ) or {}

        return result

    def write_merged_configuration_workspace_data(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_macros_static_value_cache_targets(
        self
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "macros",
                "static",
                "value-cache",
                "targets",
            ),
        ) or {}

        return result

    def write_configuration_workspace_data_macros_static_value_cache_targets(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "macros",
                "static",
                "value-cache",
                "targets",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_macros_static_file_targets(
        self
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "macros",
                "static",
                "file",
                "targets",
            ),
        ) or {}

        return result

    def write_configuration_workspace_data_macros_static_file_targets(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "macros",
                "static",
                "file",
                "targets",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_plugin_import_is_enabled_value(
        self
    ) -> bool:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "plugin",
                "import",
                "is-enabled",
            ),
        ) or {}

        return bool(result.get("value", True))

    def write_configuration_workspace_data_plugin_import_is_enabled_value(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "plugin",
                "import",
                "is-enabled",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_display_console_is_enabled_value(
        self
    ) -> bool:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "is-enabled",
            ),
        ) or {}

        return bool(result.get("value", True))

    def write_configuration_workspace_data_display_console_is_enabled_value(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "is-enabled",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_display_console_style(
        self
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
            ),
        )

        return result

    def write_configuration_workspace_data_display_console_style(
        self,
        value: Any
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_display_console_style_reset_value(
        self
    ) -> str:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "reset",
            ),
        ) or {}

        return str(result.get("value", "reset"))

    def write_configuration_workspace_data_display_console_style_reset_value(
        self,
        value: str
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "reset",
                "value",
            ),
            value,
        )

        return True


    def read_configuration_workspace_data_display_console_style_base_1_value(
        self
    ) -> str:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "base-1",
            ),
        ) or {}

        return str(result.get("value", ""))

    def write_configuration_workspace_data_display_console_style_base_1_value(
        self,
        value: str
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "base-1",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_display_console_style_base_2_value(
        self
    ) -> str:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "base-2",
            ),
        ) or {}

        return str(result.get("value", "grey"))

    def write_configuration_workspace_data_display_console_style_base_2_value(
        self,
        value: str
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "base-2",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_display_console_style_highlight_1_value(
        self
    ) -> str:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "highlight-1",
            ),
        ) or {}

        return str(result.get("value", "green"))

    def write_configuration_workspace_data_display_console_style_highlight_1_value(
        self,
        value: str
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "highlight-1",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_display_console_style_highlight_2_value(
        self
    ) -> str:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "highlight-2",
            ),
        ) or {}

        return str(result.get("value", "green"))

    def write_configuration_workspace_data_display_console_style_highlight_2_value(
        self,
        value: str
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "highlight-2",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_display_console_style_maximum_depth_value(
        self
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "maximum-depth",
            ),
        ) or {}

        return result.get("value", None)

    def write_configuration_workspace_data_display_console_style_maximum_depth_value(
        self,
        value: Any
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "maximum-depth",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_display_console_style_indent_count_value(
        self
    ) -> int:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "indent-count",
            ),
        ) or {}

        return int(result.get("value", 4))

    def write_configuration_workspace_data_display_console_style_indent_count_value(
        self,
        value: int
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "indent-count",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_display_console_style_is_skipped_value(
        self
    ) -> bool:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "is-skipped",
            ),
        ) or {}

        return bool(result.get("value", True))

    def write_configuration_workspace_data_display_console_style_is_skipped_value(
        self,
        value: int
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "is-skipped",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_display_console_style_vertical_count_value(
        self
    ) -> int:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "vertical-count",
            ),
        ) or {}

        return int(result.get("value", 1))

    def write_configuration_workspace_data_display_console_style_vertical_count_value(
        self,
        value: int
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "display",
                "console",
                "style",
                "vertical-count",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_time_zone_value(
        self
    ) -> str:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "time",
                "zone",
            ),
        ) or {}

        return str(result.get("value", "local"))

    def write_configuration_workspace_data_time_zone_value(
        self,
        value: str
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "time",
                "zone",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_operating_system_name_value(
        self
    ) -> str:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "operating-system",
                "name",
            ),
        ) or {}

        return str(
            result.get(
                "value",
                self._import_manager
                    .read_operating_system_name()
            )
        )

    def write_configuration_workspace_data_operating_system_name_value(
        self,
        value: str
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "operating-system",
                "name",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_operating_system_value(
        self
    ) -> str:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "operating-system",
            ),
        ) or {}

        return str(
            result.get(
                "value",
                f"{
                    self._import_manager
                        .read_operating_system_name()
                }-{
                    self._import_manager
                        .read_operating_system_architecture()
                }"
            )
        )

    def write_configuration_workspace_data_operating_system_value(
        self,
        value: str
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "operating-system",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_operating_system_architecture_value(
        self
    ) -> str:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "operating-system",
                "architecture",
            ),
        ) or {}

        return str(
            result.get(
                "value",
                self._import_manager
                    .read_operating_system_architecture()
            )
        )

    def write_configuration_workspace_data_operating_system_architecture_value(
        self,
        value: str
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "operating-system",
                "architecture",
                "value",
            ),
            value,
        )

        return True




    def read_configuration_workspace_data_log_is_enabled_value(
        self
    ) -> bool:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "is-enabled",
            ),
        ) or {}

        return bool(result.get("value", True))

    def write_configuration_workspace_data_log_is_enabled_value(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "is-enabled",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_log_is_enabled_override(
        self
    ) -> bool:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "is-enabled",
            ),
        ) or {}

        return bool(result.get("override", False))

    def write_configuration_workspace_data_log_is_enabled_override(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "is-enabled",
                "override",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_log_is_verbose_value(
        self
    ) -> bool:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "is-verbose",
            ),
        ) or {}

        return bool(result.get("value", True))

    def write_configuration_workspace_data_log_is_verbose_value(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "is-verbose",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_log_is_verbose_override(
        self
    ) -> bool:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "is-verbose",
            ),
        ) or {}

        return bool(result.get("override", False))

    def write_configuration_workspace_data_log_is_verbose_override(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "is-verbose",
                "override",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_log_file_is_enabled_value(
        self
    ) -> bool:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "file",
                "is-enabled",
            ),
        ) or {}

        return bool(result.get("value", True))

    def write_configuration_workspace_data_log_file_is_enabled_value(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "file",
                "is-enabled",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_log_file_is_verbose_value(
        self
    ) -> bool:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "file",
                "is-verbose",
            ),
        ) or {}

        return bool(result.get("value", True))

    def write_configuration_workspace_data_log_file_is_verbose_value(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "file",
                "is-verbose",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_log_file_targets(
        self
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "file",
            ),
        ) or {}

        return result.get("targets", {})

    def write_configuration_workspace_data_log_file_targets(
        self,
        value: Any
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "file",
                "targets",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_log_console_is_enabled_value(
        self
    ) -> bool:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "console",
                "is-enabled",
            ),
        ) or {}

        return bool(result.get("value", True))

    def write_configuration_workspace_data_log_console_is_enabled_value(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "console",
                "is-enabled",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_log_console_is_verbose_value(
        self
    ) -> bool:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "console",
                "is-verbose",
            ),
        ) or {}

        return bool(result.get("value", False))

    def write_configuration_workspace_data_log_console_is_verbose_value(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "console",
                "is-verbose",
                "value",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_log_default_file_output_is_enabled_value(
        self
    ) -> bool:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "default",
                "file",
                "output"
                "is-enabled",
            ),
        ) or {}

        return bool(result.get("value", True))

    def write_configuration_workspace_data_log_default_file_output_is_enabled_value(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "log",
                "default",
                "file",
                "output"
                "is-enabled",
                "value",
            ),
            value,
        )

        return True

    def read_plugin_raw(
        self,
        accessibility_type: str
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "plugin",
                "raw",
                accessibility_type,
            ),
        ) or {}

        return result

    def write_plugin_raw(
        self,
        accessibility_type: str,
        value: Any
    ) -> bool:
        self.write_any_value(
            (
                "plugin",
                "raw",
                accessibility_type,
            ),
            value,
        )

        return True

    def remove_plugin_raw(
        self,
    ) -> bool:
        self.remove_any_value(
            (
                "plugin",
                "raw",
            ),
        )

        return True

    def read_plugin_raw_data(
        self,
        accessibility_type: str,
        key_path: str,
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "plugin",
                "raw",
                accessibility_type,
                key_path,
                "data",
                "value",
            ),
        ) or {}

        return result

    def write_plugin_raw_data(
        self,
        accessibility_type: str,
        key_path: str,
        value: Any
    ) -> bool:
        self.write_any_value(
            (
                "plugin",
                "raw",
                accessibility_type,
                key_path,
                "data",
                "value",
            ),
            value,
        )

        return True

    def read_plugin_public_raw(
        self
    ) -> Any:
        result: Any = self.read_plugin_raw(
            "public",
        ) or {}

        return result

    def write_plugin_public_raw(
        self,
        value: Any
    ) -> bool:
        self.write_plugin_raw(
            "public",
            value,
        )

        return True

    def read_plugin_private_raw(
        self
    ) -> Any:
        result: Any = self.read_plugin_raw(
            "private",
        ) or {}

        return result

    def write_plugin_private_raw(
        self,
        value: Any
    ) -> bool:
        self.write_plugin_raw(
            "private",
            value,
        )

        return True

    def read_plugin_raw_file_count(
        self,
        accessibility_type: str,
    ) -> bool:
        result: bool = self.read_any_value(
            (
                "plugin",
                "raw",
                "count",
                accessibility_type,
                "value"
            ),
        )

        return result

    def write_plugin_raw_file_count(
        self,
        accessibility_type: str,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "plugin",
                "raw",
                "count",
                accessibility_type,
                "value"
            ),
            value,
        )

        return True

    def read_plugin_data_macros_static_targets(
        self
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "plugin",
                "data",
                "macros",
                "static",
                "targets",
            ),
        ) or {}

        return result

    def write_plugin_data_macros_static_targets(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "plugin",
                "data",
                "macros",
                "static",
                "targets",
            ),
            value,
        )

        return True

    def read_plugin_data_macros_dynamic_targets(
        self
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "plugin",
                "data",
                "macros",
                "dynamic",
                "targets",
            ),
        ) or {}

        return result

    def write_plugin_data_macros_dynamic_targets(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "plugin",
                "data",
                "macros",
                "dynamic",
                "targets",
            ),
            value,
        )

        return True

    def read_plugin_data(
        self
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "plugin",
                "data",
            ),
        ) or {}

        return result

    def write_plugin_data(
        self,
        value: bool
    ) -> bool:
        self.write_any_value(
            (
                "plugin",
                "data",
            ),
            value,
        )

        return True

    def read_default_object_macros_values(
        self,
        data: Any,
    ) -> Any:
        outputs: Any = {}
        if not data:
            return outputs

        for value in data:
            outputs[value] = {
                "value": (
                    self.read_any_value((
                        value,
                        "value",
                    ))
                )
            }

        return outputs

    def read_configuration_workspace_data_command_filesystem_clean_exclude_targets(
        self
    ) -> tuple[str, ...]:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "command",
                "filesystem",
                "clean",
                "exclude",
            ),
        ) or {}

        return tuple(result.get("targets", tuple()))

    def write_configuration_workspace_data_command_filesystem_clean_exclude_targets(
        self,
        value: tuple[str, ...]
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "command",
                "filesystem",
                "clean",
                "exclude",
                "targets",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_command_filesystem_clean_include_selection(
        self
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "command",
                "filesystem",
                "clean",
                "include",
            ),
        ) or {}

        return result.get("selection", {})

    def write_configuration_workspace_data_command_filesystem_clean_include_selection(
        self,
        value: Any
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "command",
                "filesystem",
                "clean",
                "include",
                "selection",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_workspace_project_selection(
        self
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "workspace",
                "project",
            ),
        ) or {}

        return result.get("selection", {})

    def write_configuration_workspace_data_workspace_project_selection(
        self,
        value: Any
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "workspace",
                "project",
                "selection",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_workspace_group_selection(
        self
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "workspace",
                "group",
            ),
        ) or {}

        return result.get("selection", {})

    def write_configuration_workspace_data_workspace_group_selection(
        self,
        value: Any
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "workspace",
                "group",
                "selection",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_export_group(
        self
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "export",
            ),
        ) or {}

        return result.get("group", {})

    def write_configuration_export_data_export_group(
        self,
        value: Any
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "export",
                "group",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_export_selection(
        self
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "export",
            ),
        ) or {}

        return result.get("selection", {})

    def write_configuration_workspace_data_export_selection(
        self,
        value: Any
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "export",
                "selection",
            ),
            value,
        )

        return True

    def read_configuration_workspace_data_workflow_selection(
        self
    ) -> Any:
        result: Any = self.read_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "workflow",
            ),
        ) or {}

        return result.get("selection", {})

    def write_configuration_workspace_data_workflow_selection(
        self,
        value: Any
    ) -> bool:
        self.write_any_value(
            (
                "configuration",
                "workspace",
                "data",
                "workflow",
                "selection",
            ),
            value,
        )

        return True

    def read_filesystem_clean_excluded(
        self
    ) -> set[str]:
        result: Any = self.read_any_value(
            (
                "filesystem",
                "clean",
            ),
        ) or {}

        return set(result.get("excluded", set()))

    def write_filesystem_clean_excluded(
        self,
        value: set[str]
    ) -> bool:
        self.write_any_value(
            (
                "filesystem",
                "clean",
                "excluded",
            ),
            value,
        )

        return True

    def read_filesystem_clean_included(
        self
    ) -> set[str]:
        result: Any = self.read_any_value(
            (
                "filesystem",
                "clean",
            ),
        ) or {}

        return set(result.get("included", set()))

    def write_filesystem_clean_included(
        self,
        value: set[str]
    ) -> bool:
        self.write_any_value(
            (
                "filesystem",
                "clean",
                "included",
            ),
            value,
        )

        return True

    def read_workspace_group(
        self
    ) -> set[str]:
        result: Any = self.read_any_value(
            (
                "workspace",
            ),
        ) or {}

        return set(result.get("group", set()))

    def write_workspace_group(
        self,
        value: set[str]
    ) -> bool:
        self.write_any_value(
            (
                "workspace",
                "group",
            ),
            value,
        )

        return True

    def read_workspace_project(
        self
    ) -> set[str]:
        result: Any = self.read_any_value(
            (
                "workspace",
            ),
        ) or {}

        return set(result.get("project", set()))

    def write_workspace_project(
        self,
        value: set[str]
    ) -> bool:
        self.write_any_value(
            (
                "workspace",
                "project",
            ),
            value,
        )

        return True

    def read_workspace_default(
        self
    ) -> set[str]:
        result: Any = self.read_any_value(
            (
                "workspace",
            ),
        ) or {}

        return set(result.get("default", set()))

    def write_workspace_default(
        self,
        value: set[str]
    ) -> bool:
        self.write_any_value(
            (
                "workspace",
                "default",
            ),
            value,
        )

        return True

    def read_workspace_all(
        self
    ) -> set[str]:
        result: Any = self.read_any_value(
            (
                "workspace",
            ),
        ) or {}

        return set(result.get("all", set()))

    def write_workspace_all(
        self,
        value: set[str]
    ) -> bool:
        self.write_any_value(
            (
                "workspace",
                "all",
            ),
            value,
        )

        return True

    def read_export_selection(
        self
    ) -> set[str]:
        result: Any = self.read_any_value(
            (
                "export",
            ),
        ) or {}

        return set(result.get("selection", set()))

    def write_export_selection(
        self,
        value: set[str]
    ) -> bool:
        self.write_any_value(
            (
                "export",
                "selection",
            ),
            value,
        )

        return True

    def read_export_group(
        self
    ) -> set[str]:
        result: Any = self.read_any_value(
            (
                "export",
            ),
        ) or {}

        return set(result.get("group", set()))

    def write_export_group(
        self,
        value: set[str]
    ) -> bool:
        self.write_any_value(
            (
                "export",
                "group",
            ),
            value,
        )

        return True

    def read_workflow_selection(
        self
    ) -> set[str]:
        result: Any = self.read_any_value(
            (
                "workflow",
            ),
        ) or {}

        return set(result.get("selection", set()))

    def write_workflow_selection(
        self,
        value: set[str]
    ) -> bool:
        self.write_any_value(
            (
                "workflow",
                "selection",
            ),
            value,
        )

        return True

