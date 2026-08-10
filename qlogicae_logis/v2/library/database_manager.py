from __future__ import annotations

from typing import Any

_about_data: Any = None
_utility_data: Any = None
_about_metadata: Any = None
_utility_metadata: Any = None

_Path: Any = None
_TimeManager: Any = None
_SystemManager: Any = None
_TimeZoneManager: Any = None
_TargetCacheValue: Any = None
_TimestampManager: Any = None
_SingletonManager: Any = None
_ValueCacheManager: Any = None
_PlaceholderValueManager: Any = None


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _Path
    global _TimeManager
    global _SystemManager
    global _TimeZoneManager
    global _TimestampManager
    global _TargetCacheValue
    global _SingletonManager
    global _ValueCacheManager
    global _PlaceholderValueManager

    from pathlib import Path

    from qlogicae_cor.v1.library import (
        placeholder_value_manager,
        singleton_manager,
        system_manager,
        target_cache_value,
        time_manager,
        time_zone_manager,
        timestamp_manager,
        value_cache_manager,
    )

    _Path = Path
    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _ValueCacheManager = (
        value_cache_manager.ValueCacheManager
    )
    _TimeManager = (
        time_manager.TimeManager
    )
    _TimeZoneManager = (
        time_zone_manager.TimeZoneManager
    )
    _TimestampManager = (
        timestamp_manager.TimestampManager
    )
    _SystemManager = (
        system_manager.SystemManager
    )
    _TargetCacheValue = (
        target_cache_value.TargetCacheValue
    )
    _PlaceholderValueManager = (
        placeholder_value_manager.PlaceholderValueManager
    )

    _handle_dynamic_imports = lambda: None


def _handle_about_dynamic_imports() -> None:
    global _about_data
    global _about_metadata
    global _handle_about_dynamic_imports

    from qlogicae_logis.v2.project.configuration import about

    _about_data = about.DATA
    _about_metadata = about.METADATA

    _handle_about_dynamic_imports = lambda: None


def _handle_utility_dynamic_imports() -> None:
    global _utility_data
    global _utility_metadata
    global _handle_utility_dynamic_imports

    from qlogicae_logis.v2.project.configuration import utility

    _utility_data = utility.DATA
    _utility_metadata = utility.METADATA

    _handle_utility_dynamic_imports = lambda: None


class DatabaseManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()
        _handle_utility_dynamic_imports()

    @property
    def registered_plugins(self) -> Any:
        result: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "registered-plugins",
            )),
            output_type=_TargetCacheValue.DEFINED,
        )

        return result

    @registered_plugins.setter
    def registered_plugins(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "registered-plugins",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    def setup_about_data_project_version_value(
        self
    ) -> Any:
        placeholder_value_manager = _SingletonManager.get_singleton(
            _PlaceholderValueManager
        )

        about_data = (
            self.about_data
        )

        project_version = (
            about_data["project-version"]
            if about_data
            and "project-version" in about_data
            else {}
        ) or {}

        return (
            project_version["value"]
            if project_version
            and "value" in project_version
            else placeholder_value_manager.none
        ) or placeholder_value_manager.none

    def setup_about_data_project_brand_name_value(self) -> Any:
        placeholder_value_manager = _SingletonManager.get_singleton(
            _PlaceholderValueManager
        )

        about_data = (
            self.about_data
        )

        brand_name = (
            about_data["brand-name"]
            if about_data
            and "brand-name" in about_data
            else {}
        ) or {}

        return (
            brand_name["value"]
            if brand_name
            and "value" in brand_name
            else placeholder_value_manager.none
        ) or placeholder_value_manager.none

    def setup_about_data_project_description_value(self) -> Any:
        placeholder_value_manager = _SingletonManager.get_singleton(
            _PlaceholderValueManager
        )

        about_data = (
            self.about_data
        )

        project_description = (
            about_data["project-description"]
            if about_data
            and "project-description" in about_data
            else {}
        ) or {}

        return (
            project_description["value"]
            if project_description
            and "value" in project_description
            else placeholder_value_manager.none
        ) or placeholder_value_manager.none

    def setup_about_data_project_table(self) -> Any:
        placeholder_value_manager = _SingletonManager.get_singleton(
            _PlaceholderValueManager
        )

        about_data = (
            self.about_data
        )

        about_table = {
            key: value
            for key, value in about_data.items()
            if value and
            "is-tabular" in value and
            value["is-tabular"]
        }

        return {
            "headers": ("key", "value",),
            "rows": (
                (
                    item["name"],
                    str(item["value"]),
                )
                if (
                    item
                    and "name" in item
                    and "value" in item
                )
                else (
                    placeholder_value_manager.none,
                    placeholder_value_manager.none,
                )
                for _key, item in about_table.items()
            ),
        }

    def display_all_values(self) -> bool:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).display_all_items()

        return True

    # About Database
    @property
    def about_data(self) -> Any:
        _handle_about_dynamic_imports()

        return _about_data

    @property
    def about_metadata(self) -> Any:
        _handle_about_dynamic_imports()

        return _about_metadata


    # Utility Database
    @property
    def company_name(self) -> str:
        data: str = _utility_data["company-name"]["value"]

        return data

    @property
    def project_name(self) -> str:
        data: str = _utility_data["project-name"]["value"]

        return data

    @property
    def active_major_version_label(self) -> str:
        data: str = _utility_data["active-major-version-label"]["value"]

        return data

    # Value Cache Database
    @property
    def root_value_cache_key_path(
        self,
    ) -> tuple[str, str, str]:
        return (
            f"{self.company_name}",
            f"{self.project_name}",
            f"{self.active_major_version_label}",
        )

    @property
    def default_value_cache_targets(self) -> tuple[str]:
        return (
            f"{self.company_name}."
            f"{self.project_name}."
            f"{self.active_major_version_label}",
        )

    def setup_company_project_major_version(
        self,
        delimeter: str,
    ) -> str:
        return (
            f"{self.company_name}{delimeter}"
            f"{self.project_name}{delimeter}"
            f"{self.active_major_version_label}"
        )

    def value_cache_key_path(self, key_path: Any) -> Any:
        return (
            *self.root_value_cache_key_path,
            *key_path,
        )

    def read_value_cache(self, key_path: Any) -> Any:
        result: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                key_path,
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return result

    def read_data(
        self,
        key_path: Any
    ) -> Any:
        result: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            key_path,
            output_type=_TargetCacheValue.ANY,
        )

        return result


    # Others
    @property
    def configuration_workspace_filesystem_paths(self) -> Any:
        result: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "configuration-workspace-filesystem-paths",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return result

    @configuration_workspace_filesystem_paths.setter
    def configuration_workspace_filesystem_paths(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "configuration-workspace-filesystem-paths",
            )),
            value,
            output_type=_TargetCacheValue.ANY,
        )

    @property
    def timestamp_setup_execution_start(self) -> int:
        result: int = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "timestamp-setup-execution-start",
            )),
            output_type=_TargetCacheValue.DEFINED,
        )

        return result

    def setup_timestamp_setup_execution_start(self) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "timestamp-setup-execution-start",
            )),
            _SingletonManager.get_singleton(
                _TimeManager
            ).current_nanosecond,
            output_type=_TargetCacheValue.DEFINED,
        )


    @property
    def timestamp_setup_execution_complete(self) -> int:
        result: int = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "timestamp-setup-execution-complete",
            )),
            output_type=_TargetCacheValue.DEFINED,
        )

        return result

    def setup_timestamp_setup_execution_complete(self) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "timestamp-setup-execution-complete",
            )),
            _SingletonManager.get_singleton(
                _TimeManager
            ).current_nanosecond,
            output_type=_TargetCacheValue.DEFINED,
        )


    @property
    def root_filesystem_path(self) -> str:
        result: str = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "root-filesystem-path",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return result

    def setup_root_filesystem_path(self) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "root-filesystem-path",
            )),
            _SingletonManager.get_singleton(
                _SystemManager
            ).current_executing_console_filesystem_path,
            output_type=_TargetCacheValue.ANY,
        )



    @property
    def selection_filesystem_path(self) -> str:
        result: str = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "selection-filesystem-path",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return result

    def setup_selection_filesystem_path(self) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "selection-filesystem-path",
            )),
            f"{_SingletonManager.get_singleton(
                _SystemManager
            ).current_executing_console_filesystem_path}/selection",
            output_type=_TargetCacheValue.ANY,
        )



    @property
    def current_executing_script_filesystem_path(self) -> str:
        result: str = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "current-executing-script-filesystem-path",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return result

    @current_executing_script_filesystem_path.setter
    def current_executing_script_filesystem_path(self, value: str) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "current-executing-script-filesystem-path",
            )),
            value,
            output_type=_TargetCacheValue.ANY,
        )


    @property
    def initial_executing_console_filesystem_path(self) -> str:
        result: str = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "initial-executing-console-filesystem-path",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return result

    @initial_executing_console_filesystem_path.setter
    def initial_executing_console_filesystem_path(self, value: str) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "initial-executing-console-filesystem-path",
            )),
            value,
            output_type=_TargetCacheValue.ANY,
        )


    @property
    def previous_executing_console_filesystem_path(self) -> str:
        result: str = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "previous-executing-console-filesystem-path",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return result

    @previous_executing_console_filesystem_path.setter
    def previous_executing_console_filesystem_path(self, value: str) -> None:
        value_cache_manager = _SingletonManager.get_singleton(
            _ValueCacheManager
        )

        value_cache_manager.set_one_value(
            self.value_cache_key_path((
                "previous-executing-console-filesystem-path",
            )),
            value,
            output_type=_TargetCacheValue.ANY,
        )

    @property
    def current_executing_console_filesystem_path(self) -> str:
        result: str = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "current-executing-console-filesystem-path",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return result

    @current_executing_console_filesystem_path.setter
    def current_executing_console_filesystem_path(self, value: str) -> None:
        value_cache_manager = _SingletonManager.get_singleton(
            _ValueCacheManager
        )

        value_cache_manager.set_one_value(
            self.value_cache_key_path((
                "current-executing-console-filesystem-path",
            )),
            value,
            output_type=_TargetCacheValue.ANY,
        )

    @property
    def workspace_data(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @workspace_data.setter
    def workspace_data(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
            )),
            value,
            output_type=_TargetCacheValue.ANY,
        )

    @property
    def workspace_metadata(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "metadata",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @workspace_metadata.setter
    def workspace_metadata(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
            )),
            value,
            output_type=_TargetCacheValue.ANY,
        )


    @property
    def workspace_data_time_zone_value(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "time",
                "zone",
                "value",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or _SingletonManager.get_singleton(
            _TimeZoneManager
        ).selected_time_zone_type


    @property
    def current_timestamp(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "current-timestamp",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or _SingletonManager.get_singleton(
            _TimestampManager
        ).generate_current_timestamp()

    @current_timestamp.setter
    def current_timestamp(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "current-timestamp",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )



    @property
    def current_timezone(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "current-timezone",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or _SingletonManager.get_singleton(
            _TimeZoneManager
        ).current_timezone

    @current_timezone.setter
    def current_timezone(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "current-timezone",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def current_date(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "current-date",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or _SingletonManager.get_singleton(
            _TimeManager
        ).current_iso8601_date

    @current_date.setter
    def current_date(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "current-date",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def current_year(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "current-year",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or _SingletonManager.get_singleton(
            _TimeManager
        ).current_year

    @current_year.setter
    def current_year(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "current-year",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def os_name(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "os-name",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or _SingletonManager.get_singleton(
            _TimeZoneManager
        ).operating_system_name

    @os_name.setter
    def os_name(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "os-name",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def os_architecture(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "os-architecture",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or _SingletonManager.get_singleton(
            _TimeZoneManager
        ).operating_system_architecture

    @os_architecture.setter
    def os_architecture(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "os-architecture",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )


    @property
    def workspace_macros(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "macros-static",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @workspace_macros.setter
    def workspace_macros(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "macros-static",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_macros_dynamic(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "macros-dynamic",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @workspace_macros_dynamic.setter
    def workspace_macros_dynamic(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "macros-dynamic",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_macros_value_cache_targets(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "macros",
                "value-cache",
                "targets",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @workspace_data_macros_value_cache_targets.setter
    def workspace_data_macros_value_cache_targets(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "macros",
                "value-cache",
                "targets",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_macros_file_targets(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "macros",
                "file",
                "targets",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @workspace_data_macros_file_targets.setter
    def workspace_data_macros_file_targets(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "macros",
                "file",
                "targets",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_macros_default_value_cache_is_enabled_value(self) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "macros",
                "default",
                "value-cache",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_macros_default_value_cache_is_enabled_value.setter
    def workspace_data_macros_default_value_cache_is_enabled_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "macros",
                "default",
                "value-cache",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_macros_default_pre_parse_is_enabled_value(self) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "macros",
                "default",
                "pre-parse",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_macros_default_pre_parse_is_enabled_value.setter
    def workspace_data_macros_default_pre_parse_is_enabled_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "macros",
                "default",
                "pre-parse",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_macros_default_on_parse_is_enabled_value(self) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "macros",
                "default",
                "on-parse",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else False

    @workspace_data_macros_default_on_parse_is_enabled_value.setter
    def workspace_data_macros_default_on_parse_is_enabled_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "macros",
                "default",
                "on-parse",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )




    @property
    def workspace_data_log_is_enabled_value(self) -> bool:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True


    @workspace_data_log_is_enabled_value.setter
    def workspace_data_log_is_enabled_value(
        self,
        value: bool,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_log_is_enabled_override(self) -> bool:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["override"] if data and "override" in data else False

    @workspace_data_log_is_enabled_override.setter
    def workspace_data_log_is_enabled_override(
        self,
        value: bool,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "is-enabled",
                "override",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_log_is_verbose_value(self) -> bool:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "is-verbose",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_log_is_verbose_value.setter
    def workspace_data_log_is_verbose_value(
        self,
        value: bool,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "is-verbose",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_log_is_verbose_override(self) -> bool:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "is-verbose",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["override"] if data and "override" in data else False

    @workspace_data_log_is_verbose_override.setter
    def workspace_data_log_is_verbose_override(
        self,
        value: bool,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "is-verbose",
                "override",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )





    @property
    def workspace_data_log_console_is_enabled_value(self) -> bool:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "console",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_log_console_is_enabled_value.setter
    def workspace_data_log_console_is_enabled_value(
        self,
        value: bool,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "console",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_log_console_is_verbose_value(self) -> bool:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "console",
                "is-verbose",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else False

    @workspace_data_log_console_is_verbose_value.setter
    def workspace_data_log_console_is_verbose_value(
        self,
        value: bool,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "console",
                "is-verbose",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )



    @property
    def workspace_data_log_file_is_enabled_value(self) -> bool:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "file",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_log_file_is_enabled_value.setter
    def workspace_data_log_file_is_enabled_value(
        self,
        value: bool,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "file",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_log_file_is_verbose_value(self) -> bool:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "file",
                "is-verbose",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else False

    @workspace_data_log_file_is_verbose_value.setter
    def workspace_data_log_file_is_verbose_value(
        self,
        value: bool,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "file",
                "is-verbose",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )


    @property
    def workspace_data_log_default_file_output_is_enabled_value(self) -> bool:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "default",
                "file",
                "output",
                "is-enabld",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_log_default_file_output_is_enabled_value.setter
    def workspace_data_log_default_file_output_is_enabled_value(
        self,
        value: bool,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "default",
                "file",
                "output",
                "is-enabld",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )



    @property
    def workspace_data_log_file_targets(self) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "file",
                "targets",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or tuple()

        return data

    @workspace_data_log_file_targets.setter
    def workspace_data_log_file_targets(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "log",
                "file",
                "targets",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )



    @property
    def workspace_data_selection_default_is_included_value(self) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "workspace",
                "default",
                "is-included",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_selection_default_is_included_value.setter
    def workspace_data_selection_default_is_included_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "workspace",
                "default",
                "is-included",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )


    @property
    def workspace_data_selection_project_targets(self) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "workspace",
                "project",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["selection"] if data and "selection" in data else {}

    @workspace_data_selection_project_targets.setter
    def workspace_data_selection_project_targets(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "workspace",
                "project",
                "selection",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_selection_group_targets(self) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "workspace",
                "group",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["selection"] if data and "selection" in data else {}

    @workspace_data_selection_group_targets.setter
    def workspace_data_selection_group_targets(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "workspace",
                "group",
                "selection",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_selection_base(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace-selection-base",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @workspace_selection_base.setter
    def workspace_selection_base(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace-selection-base",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_selection_project(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace-selection-project",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @workspace_selection_project.setter
    def workspace_selection_project(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace-selection-project",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_selection_group(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace-selection-group",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @workspace_selection_group.setter
    def workspace_selection_group(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace-selection-group",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_selection_all(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace-selection-all",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @workspace_selection_all.setter
    def workspace_selection_all(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace-selection-all",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )


    @property
    def workspace_data_command_filesystem_clean_is_enabled_value(self) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "filesystem",
                "clean",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_command_filesystem_clean_is_enabled_value.setter
    def workspace_data_command_filesystem_clean_is_enabled_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "filesystem",
                "clean",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_command_filesystem_clean_default_exclude_is_enabled_value(
        self
    ) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "filesystem",
                "clean",
                "default",
                "exclude",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_command_filesystem_clean_default_exclude_is_enabled_value.setter
    def workspace_data_command_filesystem_clean_default_exclude_is_enabled_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "filesystem",
                "clean",
                "default",
                "exclude",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_command_filesystem_clean_default_include_is_enabled_value(
        self
    ) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "filesystem",
                "clean",
                "default",
                "include",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_command_filesystem_clean_default_include_is_enabled_value.setter
    def workspace_data_command_filesystem_clean_default_include_is_enabled_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "filesystem",
                "clean",
                "default",
                "include",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_command_filesystem_clean_include_targets(self) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "filesystem",
                "clean",
                "include",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["targets"] if data and "targets" in data else {}

    @workspace_data_command_filesystem_clean_include_targets.setter
    def workspace_data_command_filesystem_clean_include_targets(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "filesystem",
                "clean",
                "include",
                "targets",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_command_filesystem_clean_exclude_targets(self) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "filesystem",
                "clean",
                "exclude",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["targets"] if data and "targets" in data else {}

    @workspace_data_command_filesystem_clean_exclude_targets.setter
    def workspace_data_command_filesystem_clean_exclude_targets(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "filesystem",
                "clean",
                "exclude",
                "targets",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def filesystem_clean_selection_include(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "filesystem-clean-selection-include",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @filesystem_clean_selection_include.setter
    def filesystem_clean_selection_include(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "filesystem-clean-selection-include",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def filesystem_clean_selection_exclude(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "filesystem-clean-selection-exclude",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @filesystem_clean_selection_exclude.setter
    def filesystem_clean_selection_exclude(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "filesystem-clean-selection-exclude",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_export_default_filesystem_includes(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace-export-default-filesystem-includes",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @workspace_export_default_filesystem_includes.setter
    def workspace_export_default_filesystem_includes(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace-export-default-filesystem-includes",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_export_default_filesystem_excludes(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace-export-default-filesystem-excludes",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @workspace_export_default_filesystem_excludes.setter
    def workspace_export_default_filesystem_excludes(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace-export-default-filesystem-excludes",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_export_groups(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace-export-groups",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @workspace_export_groups.setter
    def workspace_export_groups(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace-export-groups",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_export_selections(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace-export-selections",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @workspace_export_selections.setter
    def workspace_export_selections(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace-export-selections",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )


    @property
    def workspace_data_command_export(
        self
    ) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["export"] if data and "export" in data else {}

    @workspace_data_command_export.setter
    def workspace_data_command_export(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )


    @property
    def workspace_data_command_export_is_enabled_value(
        self
    ) -> bool:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_command_export_is_enabled_value.setter
    def workspace_data_command_export_is_enabled_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )




    @property
    def workspace_data_command_export_default_filesystem_include_is_enabled_value(
        self
    ) -> bool:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
                "default",
                "filesystem",
                "include",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_command_export_default_filesystem_include_is_enabled_value.setter
    def workspace_data_command_export_default_filesystem_include_is_enabled_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
                "default",
                "filesystem",
                "include",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_command_export_default_filesystem_exclude_is_enabled_value(
        self
    ) -> bool:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
                "default",
                "filesystem",
                "exclude",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_command_export_default_filesystem_exclude_is_enabled_value.setter
    def workspace_data_command_export_default_filesystem_exclude_is_enabled_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
                "default",
                "filesystem",
                "exclude",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )



    @property
    def workspace_data_command_export_default_group_is_enabled_value(self) -> bool:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
                "default",
                "group",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_command_export_default_group_is_enabled_value.setter
    def workspace_data_command_export_default_group_is_enabled_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
                "default",
                "group",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )



    @property
    def workspace_data_command_export_default_selection_is_enabled_value(self) -> bool:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
                "default",
                "selection",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_command_export_default_selection_is_enabled_value.setter
    def workspace_data_command_export_default_selection_is_enabled_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
                "default",
                "selection",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_command_export_cleanup_is_enabled_value(self) -> bool:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
                "cleanup",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_command_export_cleanup_is_enabled_value.setter
    def workspace_data_command_export_cleanup_is_enabled_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
                "cleanup",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )


    @property
    def workspace_data_command_export_group(self) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["group"] if data and "group" in data else {}

    @workspace_data_command_export_group.setter
    def workspace_data_command_export_group(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
                "group",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_command_export_selection(self) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["selection"] if data and "selection" in data else {}

    @workspace_data_command_export_selection.setter
    def workspace_data_command_export_selection(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "export",
                "selection",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workflow_selections(self) -> Any:
        return _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workflow-selections",
            )),
            output_type=_TargetCacheValue.ANY,
        ) or {}

    @workflow_selections.setter
    def workflow_selections(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workflow-selections",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_workflow_selection(self) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "workflow",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["selection"] if data and "selection" in data else {}

    @workspace_data_workflow_selection.setter
    def workspace_data_workflow_selection(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "workflow",
                "selection",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )



    @property
    def workspace_data_command_template(
        self
    ) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["template"] if data and "template" in data else {}

    @workspace_data_command_template.setter
    def workspace_data_command_template(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "template",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_command_template_is_enabled_value(
        self
    ) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "template",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_command_template_is_enabled_value.setter
    def workspace_data_command_template_is_enabled_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "template",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_command_template_cleanup_is_enabled_value(
        self
    ) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "template",
                "cleanup",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_command_template_cleanup_is_enabled_value.setter
    def workspace_data_command_template_cleanup_is_enabled_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "command",
                "template",
                "cleanup",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    def setup_workspace_data_selection_group_targets_name(
        self,
        group_name: Any,
    ) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "workspace",
                "group",
                "selection",
                group_name,
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["targets"] if data and "targets" in data else {}

    def setup_workspace_data_selection_project_targets_name_filesystem_path_value(
        self,
        project_name: Any,
    ) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "workspace",
                "project",
                "selection",
                project_name,
                "filesystem-path",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else (
            f"{self.selection_filesystem_path}/{project_name}"
        )

    @property
    def workspace_data_workflow(
        self
    ) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["workflow"] if data and "workflow" in data else {}

    @workspace_data_workflow.setter
    def workspace_data_workflow(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "workflow",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_data_workflow_is_enabled_value(
        self
    ) -> Any:
        data: Any = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "workflow",
                "is-enabled",
            )),
            output_type=_TargetCacheValue.ANY,
        )

        return data["value"] if data and "value" in data else True

    @workspace_data_workflow_is_enabled_value.setter
    def workspace_data_workflow_is_enabled_value(
        self,
        value: Any,
    ) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            self.value_cache_key_path((
                "workspace",
                "data",
                "workflow",
                "is-enabled",
                "value",
            )),
            value,
            output_type=_TargetCacheValue.DEFINED,
        )
