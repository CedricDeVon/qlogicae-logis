from __future__ import annotations

from typing import Any

_Path: Any = None
_TimeManager: Any = None
_MacrosManager: Any = None
_SystemManager: Any = None
_TimeZoneManager: Any = None
_DatabaseManager: Any = None
_SingletonManager: Any = None
_TimestampManager: Any = None
_DataFileIoManager: Any = None
_ThreadPoolExecutor: Any = None
_ObjectMergeManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _Path
    global _TimeManager
    global _MacrosManager
    global _SystemManager
    global _TimeZoneManager
    global _DatabaseManager
    global _SingletonManager
    global _TimestampManager
    global _DataFileIoManager
    global _ThreadPoolExecutor
    global _ObjectMergeManager

    from concurrent.futures import ThreadPoolExecutor
    from pathlib import Path

    from qlogicae_cor.v1.library import (
        data_file_io_manager,
        macros_manager,
        object_merge_manager,
        singleton_manager,
        system_manager,
        time_manager,
        time_zone_manager,
        timestamp_manager,
    )

    from qlogicae_logis.v2.library import database_manager


    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _DatabaseManager = (
        database_manager.DatabaseManager
    )
    _Path = Path
    _ObjectMergeManager = (
        object_merge_manager.ObjectMergeManager
    )
    _MacrosManager = (
        macros_manager.MacrosManager
    )
    _DataFileIoManager = (
        data_file_io_manager.DataFileIoManager
    )
    _SystemManager = (
        system_manager.SystemManager
    )
    _ThreadPoolExecutor = (
        ThreadPoolExecutor
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

    _handle_dynamic_imports = lambda: None

class CommandUtilityManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()

    @property
    def default_value_cache_macros(self) -> set[str]:
        return {
            "current-date",
            "current-year",
            "current-timestamp",
            "root-filesystem-path",
            "selection-filesystem-path",
        }

    @property
    def default_template_types(self) -> tuple[str, str]:
        return ( "filesystem", "fragment", )

    @property
    def default_filesystem_accessibility_types(self) -> tuple[str, str]:
        return ( "private", "public", )

    @property
    def default_configuration_workspace_data_file_extensions(self) -> set[str]:
        return {".yaml", ".yml", ".json"}

    @property
    def default_base_selection_targets(self) -> set[str]:
        return {
            "all", "root", "group", "project"
        }

    def setup_root_workspace_filesystem_path(
        self,
    ) -> str:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        return (
            f"{database_manager.root_filesystem_path}/"
            f".{
            database_manager.setup_company_project_major_version(
            "/"
            )}"
        )

    def setup_root_workspace_plugin_filesystem_path(
        self,
        scope_selection: str,
    ) -> str:
        return (
            f"{self.setup_root_workspace_filesystem_path()}/{scope_selection}/plugin"
        )

    def setup_default_log_output_filesystem_path(
        self,
    ) -> str:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )
        time_manager = _SingletonManager.get_singleton(
            _TimeManager
        )

        return (
            f"{database_manager.root_filesystem_path}/.{
                database_manager.setup_company_project_major_version(
                        "/"
                    )
                }/private"
                f"/temporary/log/{time_manager.current_iso8601_date}.log"
        )

    def setup_export_temporary_output_filesystem_path(
        self,
    ) -> str:
        base_path = (
            self.setup_root_workspace_filesystem_path()
        )

        return (
            f"{base_path}/private/temporary/export"
        )

    def setup_temporary_template_output_filesystem_path(
        self,
    ) -> str:
        base_path = (
            self.setup_root_workspace_filesystem_path()
        )

        return (
            f"{base_path}/private/temporary/template"
        )

    def setup_export_temporary_targets_source_filesystem_path(
        self,
        target: str,
    ) -> str:
        base_path = (
            self.setup_root_workspace_filesystem_path()
        )

        return (
            f"{base_path}/private/temporary/export/targets/{target}"
        )

    def setup_export_temporary_targets_output_filesystem_path(
        self,
        target: str,
        relative_path: str,
    ) -> str:
        base_path = (
            self.setup_root_workspace_filesystem_path()
        )

        return (
            f"{base_path}/private/temporary/export/targets/{target}/{relative_path}"
        )

    def run_command_timestamp_execution_start_setup(
        self,
    ) -> bool:
        _SingletonManager.get_singleton(
            _DatabaseManager
        ).setup_timestamp_setup_execution_start()

        return True

    def run_command_timestamp_execution_end_setup(
        self,
    ) -> bool:
        _SingletonManager.get_singleton(
            _DatabaseManager
        ).setup_timestamp_setup_execution_complete()

        return True


    def run_command_root_filesystem_paths_setup(
        self,
    ) -> bool:
        _SingletonManager.get_singleton(
            _DatabaseManager
        ).setup_root_filesystem_path()

        return True

    def run_command_selection_filesystem_paths_setup(
        self,
    ) -> bool:
        _SingletonManager.get_singleton(
            _DatabaseManager
        ).setup_selection_filesystem_path()

        return True

    def run_command_executing_console_filesystem_paths_setup(
        self,
    ) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        database_manager.current_executing_script_filesystem_path = (
            self.current_executing_script_filesystem_path
        )
        database_manager.initial_executing_console_filesystem_path = (
            database_manager.root_filesystem_path
        )
        database_manager.previous_executing_console_filesystem_path = (
            database_manager.initial_executing_console_filesystem_path
        )
        database_manager.current_executing_console_filesystem_path = (
            database_manager.initial_executing_console_filesystem_path
        )

        return True

    def run_command_navigate_to_root(
        self,
    ) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        self.run_command_navigate_to_filesystem_path(
            database_manager.root_filesystem_path
        )

        return True

    def run_command_navigate_to_filesystem_path(
        self,
        filesystem_path: str
    ) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        database_manager.previous_executing_console_filesystem_path = (
            database_manager.current_executing_console_filesystem_path
        )
        database_manager.current_executing_console_filesystem_path = (
            filesystem_path
        )
        self.navigate_to_filesystem_path(
            filesystem_path
        )

        return True

    def run_command_configuration_workspace_filesystem_path_extraction_setup(
        self,
    ) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        database_manager.configuration_workspace_filesystem_paths = (
            self.setup_configuration_workspace_filesystem_paths(
                database_manager.root_filesystem_path
            )
        )

        return True

    def run_command_configuration_workspace_data_extraction_setup(
        self,
    ) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        database_manager.workspace_data = (
            self.setup_workspace_data(
                self.setup_raw_workspace_data(
                    database_manager
                        .configuration_workspace_filesystem_paths
                )
            )
        )

        # print(
        #     database_manager.workspace_data
        # )

        return True

    def run_command_value_cache_macros_setup(
        self,
    ) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )
        system_manager = _SingletonManager.get_singleton(
            _SystemManager
        )
        time_manager = _SingletonManager.get_singleton(
            _TimeManager
        )
        timestamp_manager = _SingletonManager.get_singleton(
            _TimestampManager
        )
        timezone_manager = _SingletonManager.get_singleton(
            _TimeZoneManager
        )

        timezone_value = database_manager.workspace_data_time_zone_value
        timezone_manager.selected_time_zone_type = timezone_value
        database_manager.current_timezone = timezone_value

        database_manager.current_timestamp = (
            timestamp_manager.generate_current_timestamp()
        )
        database_manager.current_date = (
            time_manager.current_iso8601_date
        )
        database_manager.current_year = (
            time_manager.current_year
        )
        database_manager.os_name = (
            system_manager.operating_system_name
        )
        database_manager.os_architecture = (
            system_manager.operating_system_architecture
        )

        return True

    def run_command_file_macros_setup(
        self,
    ) -> bool:

        return True

    def run_command_workspace_macros_setup(
        self,
    ) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )
        macros_manager = _SingletonManager.get_singleton(
            _MacrosManager
        )


        workspace_data_macros_default_value_cache_is_enabled_value = (
            database_manager
                .workspace_data_macros_default_value_cache_is_enabled_value
        )

        value_cache_macros = (
            self.setup_value_cache_macros(
                database_manager
                    .workspace_data_macros_value_cache_targets
            )
        )
        if workspace_data_macros_default_value_cache_is_enabled_value:
            value_cache_macros = (
                value_cache_macros |
                self.default_value_cache_macros
            )

        file_macros = (
            self.setup_file_macros(
                database_manager
                    .workspace_data_macros_file_targets,
            )
        )

        database_manager.workspace_macros = (
            self.setup_macros(
                database_manager.read_value_cache,
                value_cache_macros,
                file_macros
            )
        )

        if database_manager.workspace_data_macros_default_pre_parse_is_enabled_value:
            database_manager.workspace_data = (
                {
                    'data': (
                        macros_manager.parse_many(
                            database_manager.workspace_data,
                            database_manager.workspace_macros
                        )
                    )
                }
            )


        return True

    def run_command_workspace_selection_setup(
        self,
    ) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )


        workspace_data_selection_default_is_included_value = (
            database_manager
                    .workspace_data_selection_default_is_included_value
        )
        workspace_selection_base = set()
        if workspace_data_selection_default_is_included_value:
            workspace_selection_base = (
                self.setup_workspace_selection_base()
            )

        workspace_selection_project = (
            self.setup_workspace_selection_project(
                database_manager
                    .workspace_data_selection_project_targets
            )
        )
        workspace_selection_group = (
            self.setup_workspace_selection_group(
                database_manager
                    .workspace_data_selection_group_targets
            )
        )

        database_manager.workspace_selection_base = (
            workspace_selection_base
        )
        database_manager.workspace_selection_project = (
            workspace_selection_project
        )
        database_manager.workspace_selection_group = (
            workspace_selection_group
        )
        database_manager.workspace_selection_all = (
            self.setup_workspace_selection_all(
                workspace_selection_base,
                workspace_selection_project,
                workspace_selection_group
            )
        )

        return True

    def run_command_workspace_setup(
        self,
    ) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )


        workspace_data_command_export_default_filesystem_include_is_enabled_value = (
            database_manager
                .workspace_data_command_export_default_filesystem_include_is_enabled_value
        )
        workspace_data_command_export_default_filesystem_exclude_is_enabled_value = (
            database_manager
                .workspace_data_command_export_default_filesystem_exclude_is_enabled_value
        )
        workspace_data_command_export_default_group_is_enabled_value = (
            database_manager
                .workspace_data_command_export_default_group_is_enabled_value
        )
        workspace_data_command_export_default_selection_is_enabled_value = (
            database_manager
                .workspace_data_command_export_default_selection_is_enabled_value
        )
        workspace_data_command_export_group = (
            database_manager
                .workspace_data_command_export_group
        )
        workspace_data_command_export_selection = (
            database_manager
                .workspace_data_command_export_selection
        )


        database_manager.workspace_export_default_filesystem_includes = (
            self.setup_default_export_filesystem_include_paths()
            if workspace_data_command_export_default_filesystem_include_is_enabled_value
            else tuple()

        )
        database_manager.workspace_export_default_filesystem_excludes = (
            self.setup_default_export_filesystem_exclude_paths()
            if workspace_data_command_export_default_filesystem_exclude_is_enabled_value
            else tuple()
        )

        workspace_data_command_export_group = (
            self.setup_workspace_export_groups(
                workspace_data_command_export_group
            )
        )

        if workspace_data_command_export_default_group_is_enabled_value:
            workspace_data_command_export_group = (
                self.setup_default_workspace_export_groups() |
                workspace_data_command_export_group
            )

        workspace_data_command_export_selection = (
            self.setup_workspace_export_selections(
                workspace_data_command_export_selection
            )
        )
        if workspace_data_command_export_default_selection_is_enabled_value:
            workspace_data_command_export_selection = (
                self.setup_default_workspace_export_selections() |
                workspace_data_command_export_selection
            )

        database_manager.workspace_export_groups = (
            workspace_data_command_export_group
        )
        database_manager.workspace_export_selections = (
            workspace_data_command_export_selection
        )

        return True


    def navigate_to_filesystem_path(
        self,
        filesystem_path: str
    ) -> bool:
        system_manager = _SingletonManager.get_singleton(
            _SystemManager
        )

        system_manager.current_executing_console_filesystem_path = (
            filesystem_path
        )

        return True



    def setup_configuration_workspace_filesystem_path(
        self,
        root_filesystem_path: str,
        accessibility_type: str
    ) -> str:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        return (
            f"{root_filesystem_path}/.{
                database_manager.setup_company_project_major_version(
                        "/"
                    )
            }/"
            f"{accessibility_type}/configuration/workspace"
        )

    def setup_configuration_workspace_base_filee_filesystem_paths(
        self,
        root_filesystem_path: str,
        accessibility_type: str
    ) -> Any:
        configuration_workspace_filesystem_path = (
            self.setup_configuration_workspace_filesystem_path(
                root_filesystem_path,
                accessibility_type
            )
        )

        return (
            f"{configuration_workspace_filesystem_path}/root",
            f"{configuration_workspace_filesystem_path}/project/project",
            f"{configuration_workspace_filesystem_path}/group/group",
        )

    def setup_configuration_workspace_base_directory_filesystem_paths(
        self,
        root_filesystem_path: str,
        accessibility_type: str
    ) -> Any:
        configuration_workspace_filesystem_path = (
            self.setup_configuration_workspace_filesystem_path(
                root_filesystem_path,
                accessibility_type
            )
        )

        return (
            f"{configuration_workspace_filesystem_path}/group/selection",
            f"{configuration_workspace_filesystem_path}/project/selection",
        )

    def setup_configuration_workspace_filesystem_paths(
        self,
        root_filesystem_path: str,
    ) -> Any:
        filesystem_paths: Any = []
        configuration_workspace_data_file_extensions = (
            self.default_configuration_workspace_data_file_extensions
        )
        filesystem_accessibility_types = (
            self.default_filesystem_accessibility_types
        )

        for accessibility_type in (
            filesystem_accessibility_types
        ):
            configuration_workspace_base_filesystem_paths = (
                self.setup_configuration_workspace_base_filee_filesystem_paths(
                    root_filesystem_path,
                    accessibility_type
                )
            )
            for string_path in (
                configuration_workspace_base_filesystem_paths
            ):
                for data_file_type in (
                    configuration_workspace_data_file_extensions
                ):
                    path = _Path(
                        f"{string_path}{data_file_type}"
                    )

                    if path.is_file():
                        filesystem_paths.append(
                            str(path)
                        )

            configuration_workspace_base_directory_filesystem_paths = (
                self.setup_configuration_workspace_base_directory_filesystem_paths(
                    root_filesystem_path,
                    accessibility_type
                )
            )
            for string_path in (
                configuration_workspace_base_directory_filesystem_paths
            ):
                path = _Path(string_path)

                if not path.is_dir():
                    continue

                filesystem_paths.extend(
                    str(path)
                    for path in path.iterdir()
                    if path.is_file()
                    and path.suffix in configuration_workspace_data_file_extensions
                )

        return tuple(
            filesystem_paths
        )

    def setup_default_export_filesystem_include_paths(
        self,
    ) -> Any:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        project_company_major_version_filesystem_path = (
            database_manager.setup_company_project_major_version(
                    "/"
                )
        )

        outputs: Any = tuple()
        outputs = (
            {
                "filesystem-path": {
                    "value":
                        f".{project_company_major_version_filesystem_path}/"
                        ".gitignore"
                }
            },
            {
                "filesystem-path": {
                    "value":
                        f".{project_company_major_version_filesystem_path}/"
                        "public/configuration"
                }
            },
            {
                "filesystem-path": {
                    "value":
                        f".{project_company_major_version_filesystem_path}/"
                        "public/template"
                }
            },
        )

        return outputs

    def setup_default_export_filesystem_exclude_paths(
        self,
    ) -> Any:
        outputs: Any = tuple(

        )

        return outputs

    def setup_value_cache_targets(
        self,
        targets: Any
    ) -> Any:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        if not targets or not len(targets):
            targets = (
                database_manager.default_value_cache_targets
            )

        return targets


    def setup_raw_workspace_data(
        self,
        filesystem_paths: Any,
    ) -> Any:
        data_file_io_manager = _SingletonManager.get_singleton(
            _DataFileIoManager
        )

        max_workers = min(32, len(filesystem_paths) or 1)

        with _ThreadPoolExecutor(max_workers=max_workers) as executor:
            raw_workspace_data = tuple(
                executor.map(
                    data_file_io_manager.read_file,
                    filesystem_paths,
                )
            )

        return raw_workspace_data

    def setup_value_cache_macros(
        self,
        value_cache_macros: Any,
    ) -> Any:
        return {
            key for key, _value in value_cache_macros.items()
        }

    def setup_file_macros(
        self,
        file_macros: Any
    ) -> Any:
        return file_macros

    def setup_macros(
        self,
        callback: Any,
        value_cache_macros: Any,
        file_macros: Any,
    ) -> Any:
        macros_manager = _SingletonManager.get_singleton(
            _MacrosManager
        )

        return macros_manager.resolve_many(
            {
                key: f"{
                    callback(
                        key
                    )
                }"
                for key in value_cache_macros
            } | {
                key: f"{item['value']}"
                for key, item in file_macros.items()
            } or {}
        ) or {}

    def parse_value(
        self,
        value: object,
        resolved_macros: Any,
    ) -> Any:
        macros_manager = _SingletonManager.get_singleton(
            _MacrosManager
        )

        return (
            macros_manager.parse_many(
                value,
                resolved_macros
            )
        )

    def setup_workspace_data(
        self,
        raw_workspace_data: Any,
    ) -> Any:
        object_merge_manager = _SingletonManager.get_singleton(
            _ObjectMergeManager
        )

        workspace_data: Any = {}
        for raw_data in raw_workspace_data:
            workspace_data = (
                object_merge_manager.deep_merge(
                    workspace_data,
                    raw_data,
                )
                or {}
            )

        return workspace_data

    @property
    def current_executing_script_filesystem_path(self) -> str:
        return f"{_Path(__file__).resolve()}"

    def setup_workspace_export_groups(
        self,
        targets: Any,
    ) -> set[str]:
        return (
            set(
                key
                for key, _value
                in targets.items()
            )
        )

    def setup_workspace_export_selections(
        self,
        targets: Any,
    ) -> set[str]:
        return (
            set(
                key
                for key, _value
                in targets.items()
            )
        )

    def setup_default_workspace_export_groups(
        self,
    ) -> set[str]:
        outputs: set[str] = set()

        outputs = {
            "all"
        }

        return outputs

    def setup_default_workspace_export_selections(
        self,
    ) -> set[str]:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        outputs: set[str] = set()

        outputs = {
            database_manager.setup_company_project_major_version(
                "-"
            )
        }

        return outputs


    def setup_workspace_selection_base(self) -> set[str]:
        outputs: set[str] = (
            self.default_base_selection_targets
        )

        return outputs

    def setup_workspace_selection_project(self, inputs: Any) -> set[str]:
        return {
            key
            for key, _value
            in inputs.items()
        }

    def setup_workspace_selection_group(self, inputs: Any) -> set[str]:
        return {
            key
            for key, _value
            in inputs.items()
        }

    def setup_workspace_selection_all(
        self,
        base_selections: set[str],
        project_selections: set[str],
        group_selections: set[str],
    ) -> set[str]:
        return base_selections | project_selections | group_selections

