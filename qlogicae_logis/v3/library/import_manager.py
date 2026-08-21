from __future__ import annotations

from typing import Any

__all__ = (
    "ImportManager"
)

_gc: Any = None
_sys: Any = None
_time: Any = None
_uuid: Any = None
_yaml: Any = None
_Path: Any = None
_shutil: Any = None
_logging: Any = None
_Mapping: Any = None
_Sequence: Any = None
_argparse: Any = None
_resource: Any = None
_Timestamp: Any = None
_LogOptions: Any = None
_LogManager: Any = None
_JsonManager: Any = None
_TimeManager: Any = None
_tracemalloc: Any = None
_MacrosManager: Any = None
_SystemManager: Any = None
_ScriptProcess: Any = None
_FileIoManager: Any = None
_JsonTextManager: Any = None
_CompletedProcess: Any = None
_module_from_spec: Any = None
_TimeZoneManager: Any = None
_SingletonManager: Any = None
_TimestampManager: Any = None
_TargetCacheValue: Any = None
_JsonFileIoManager: Any = None
_ConsoleLogManager: Any = None
_ValueCacheManager: Any = None
_CorFileLogManager: Any = None
_FilesystemManager: Any = None
_ObjectMergeManager: Any = None
_ThreadPoolExecutor: Any = None
_AsynchronousManager: Any = None
_TextEncodingManager: Any = None
_EnumConversionValue: Any = None
_ScriptProcessManager: Any = None
_CorConsoleLogManager: Any = None
_GroupSelectionManager: Any = None
_spec_from_file_location: Any = None
_DiskCacheStorageManager: Any = None
_PlaceholderValueManager: Any = None
_ScriptProcessEnumManager: Any = None
_FilesystemCompressionManager: Any = None
_EnumConversionValueEnumManager: Any = None
_FileEntityFileSystemTreeSetupOptions: Any = None
_FolderEntityFileSystemTreeSetupOptions: Any = None


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _gc
    global _resource
    global _tracemalloc
    global _sys
    global _time
    global _uuid
    global _yaml
    global _Path
    global _shutil
    global _logging
    global _argparse
    global _Timestamp
    global _LogOptions
    global _LogManager
    global _JsonManager
    global _TimeManager
    global _MacrosManager
    global _SystemManager
    global _ScriptProcess
    global _FileIoManager
    global _JsonTextManager
    global _CompletedProcess
    global _module_from_spec
    global _TimeZoneManager
    global _SingletonManager
    global _TimestampManager
    global _TargetCacheValue
    global _JsonFileIoManager
    global _ConsoleLogManager
    global _ValueCacheManager
    global _CorFileLogManager
    global _FilesystemManager
    global _ObjectMergeManager
    global _ThreadPoolExecutor
    global _AsynchronousManager
    global _TextEncodingManager
    global _EnumConversionValue
    global _ScriptProcessManager
    global _CorConsoleLogManager
    global _GroupSelectionManager
    global _spec_from_file_location
    global _DiskCacheStorageManager
    global _PlaceholderValueManager
    global _ScriptProcessEnumManager
    global _FilesystemCompressionManager
    global _EnumConversionValueEnumManager
    global _FileEntityFileSystemTreeSetupOptions
    global _FolderEntityFileSystemTreeSetupOptions
    global _Mapping
    global _Sequence

    import argparse
    import gc
    import logging
    import resource
    import shutil
    import sys
    import time
    import tracemalloc
    import uuid
    from collections.abc import Mapping, Sequence
    from concurrent.futures import ThreadPoolExecutor
    from importlib.util import module_from_spec, spec_from_file_location
    from pathlib import Path
    from subprocess import CompletedProcess

    from .._vendor.pyyaml import yaml
    from .._vendor.qlogicae_cor.v2.library import (
        asynchronous_manager,
        console_log_manager,
        disk_cache_storage_manager,
        enum_conversion_value,
        enum_conversion_value_enum_manager,
        file_entity_filesystem_tree_setup_options,
        file_io_manager,
        file_log_manager,
        filesystem_compression_manager,
        filesystem_manager,
        folder_entity_filesystem_tree_setup_options,
        group_selection_manager,
        json_file_io_manager,
        json_manager,
        json_text_manager,
        log_manager,
        log_options,
        macros_manager,
        object_merge_manager,
        placeholder_value_manager,
        script_process,
        script_process_enum_manager,
        script_process_manager,
        singleton_manager,
        system_manager,
        target_cache_value,
        text_encoding_manager,
        time_manager,
        time_zone_manager,
        timestamp,
        timestamp_manager,
        value_cache_manager,
    )

    _gc = gc
    _logging = logging
    _resource = resource
    _tracemalloc = tracemalloc
    _sys = sys
    _Mapping = Mapping
    _Sequence = Sequence
    _uuid = uuid
    _yaml = yaml
    _Path = Path
    _time = time
    _shutil = shutil
    _argparse = argparse
    _ThreadPoolExecutor = ThreadPoolExecutor
    _CompletedProcess = CompletedProcess
    _Timestamp = timestamp.Timestamp
    _LogOptions = log_options.LogOptions
    _LogManager = log_manager.LogManager
    _TimeManager = time_manager.TimeManager
    _MacrosManager = macros_manager.MacrosManager
    _SystemManager = system_manager.SystemManager
    _TimeZoneManager = time_zone_manager.TimeZoneManager
    _CorFileLogManager = file_log_manager.FileLogManager
    _SingletonManager = singleton_manager.SingletonManager
    _TimestampManager = timestamp_manager.TimestampManager
    _TargetCacheValue = target_cache_value.TargetCacheValue
    _ValueCacheManager = value_cache_manager.ValueCacheManager
    _FilesystemManager = filesystem_manager.FilesystemManager
    _ObjectMergeManager = object_merge_manager.ObjectMergeManager
    _CorConsoleLogManager = console_log_manager.ConsoleLogManager
    _EnumConversionValue = enum_conversion_value.EnumConversionValue
    _ScriptProcessManager = script_process_manager.ScriptProcessManager
    _PlaceholderValueManager = (
        placeholder_value_manager.PlaceholderValueManager
    )
    _ScriptProcessEnumManager = (
        script_process_enum_manager.ScriptProcessEnumManager
    )
    _FilesystemCompressionManager = (
        filesystem_compression_manager.FilesystemCompressionManager
    )
    _FileEntityFileSystemTreeSetupOptions = (
        file_entity_filesystem_tree_setup_options
        .FileEntityFileSystemTreeSetupOptions
    )
    _FolderEntityFileSystemTreeSetupOptions = (
        folder_entity_filesystem_tree_setup_options
        .FolderEntityFileSystemTreeSetupOptions
    )
    _AsynchronousManager = asynchronous_manager.AsynchronousManager
    _EnumConversionValueEnumManager = (
        enum_conversion_value_enum_manager.EnumConversionValueEnumManager
    )
    _ConsoleLogManager = console_log_manager.ConsoleLogManager
    _DiskCacheStorageManager = (
        disk_cache_storage_manager.DiskCacheStorageManager
    )
    _JsonFileIoManager = json_file_io_manager.JsonFileIoManager
    _JsonTextManager = json_text_manager.JsonTextManager
    _JsonManager = json_manager.JsonManager
    _ScriptProcess = script_process.ScriptProcess
    _FileIoManager = file_io_manager.FileIoManager
    _GroupSelectionManager = group_selection_manager.GroupSelectionManager
    _TextEncodingManager = (
        text_encoding_manager
            .TextEncodingManager
    )
    _module_from_spec = (
        module_from_spec
    )
    _spec_from_file_location = (
        spec_from_file_location
    )

    _handle_dynamic_imports = lambda: None


def _handle_singleton_manager_imports() -> None:
    global _handle_singleton_manager_imports

    global _SingletonManager

    from .._vendor.qlogicae_cor.v2.library import (
        singleton_manager,
    )

    _SingletonManager = singleton_manager.SingletonManager

    _handle_singleton_manager_imports = lambda: None


class ImportManager:
    __slots__ = (
        "_time_manager",
        "_disk_cache_storage_manager",
        "_value_cache_manager",
        "_time_zone_manager",
        "_timestamp_manager",
        "_text_encoding_manager",
        "_script_process_manager",
        "_macros_manager",
        "_object_merge_manager",
        "_group_selection_manager",
        "_json_file_io_manager",
        "_json_text_manager",
        "_filesystem_compression_manager",
        "_filesystem_manager",
        "_system_manager",
        "_file_io_manager",
        "_file_log_manager",
        "_console_log_manager",
        "_log_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._time_manager = self.get_singleton(
            _TimeManager
        )
        self._disk_cache_storage_manager = self.get_singleton(
            _DiskCacheStorageManager
        )
        self._value_cache_manager = self.get_singleton(
            _ValueCacheManager
        )
        self._time_zone_manager = self.get_singleton(
            _TimeZoneManager
        )
        self._timestamp_manager = self.get_singleton(
            _TimestampManager
        )
        self._text_encoding_manager = self.get_singleton(
            _TextEncodingManager
        )
        self._script_process_manager = self.get_singleton(
            _ScriptProcessManager
        )
        self._macros_manager = self.get_singleton(
            _MacrosManager
        )
        self._object_merge_manager = self.get_singleton(
            _ObjectMergeManager
        )
        self._group_selection_manager = self.get_singleton(
            _GroupSelectionManager
        )
        self._json_file_io_manager = self.get_singleton(
            _JsonFileIoManager
        )
        self._json_text_manager = self.get_singleton(
            _JsonTextManager
        )
        self._filesystem_compression_manager = self.get_singleton(
            _FilesystemCompressionManager
        )
        self._filesystem_manager = self.get_singleton(
            _FilesystemManager
        )
        self._system_manager = self.get_singleton(
            _SystemManager
        )
        self._file_io_manager = self.get_singleton(
            _FileIoManager
        )
        self._file_log_manager = self.get_singleton(
            _CorFileLogManager
        )
        self._console_log_manager = self.get_singleton(
            _ConsoleLogManager
        )
        self._log_manager = self.get_singleton(
            _LogManager
        )

    @classmethod
    def get_singleton(self, value: Any) -> Any:
        _handle_singleton_manager_imports()

        return (
            _SingletonManager.get_singleton(
                value
            )
        )

    def snapshot_memory_usage(self) -> Any:
        current_bytes, peak_bytes = (
            _tracemalloc.get_traced_memory()
            if _tracemalloc.is_tracing()
            else (0, 0)
        )

        peak_rss = _resource.getrusage(
            _resource.RUSAGE_SELF,
        ).ru_maxrss

        if _sys.platform != "darwin":
            peak_rss *= 1024

        return {
            "tracemalloc-current": { "value": current_bytes },
            "tracemalloc-peak": { "value": peak_bytes },
            "process-peak-rss": { "value": peak_rss },
            "gc-tracked-objects": { "value": len(_gc.get_objects(),) },
        }

    # TimeManager
    def read_current_iso8601_date(
        self,
    ) -> str:
        value: str = (
            self._time_manager.current_iso8601_date
        )

        return value

    def read_current_nanosecond(
        self,
    ) -> int:
        value: int = (
            self._time_manager.current_nanosecond
        )

        return value

    def read_current_day(
        self,
    ) -> int:
        value: int = (
            self._time_manager.current_day
        )

        return value

    def read_current_month(
        self,
    ) -> int:
        value: int = (
            self._time_manager.current_month
        )

        return value

    def read_current_year(
        self,
    ) -> int:
        value: int = (
            self._time_manager.current_year
        )

        return value

    # DiskCacheStorageManager
    def is_key_found_via_disk_cache(
        self,
        **kwargs: Any,
    ) -> bool:
        value: bool = (
            self._disk_cache_storage_manager.is_keys_found(
                key_path=kwargs.get(
                    "key_path",
                    ""
                ),
            )
        )

        return value

    def is_item_expired_via_disk_cache(
        self,
        **kwargs: Any,
    ) -> bool:
        value: bool = (
            self._disk_cache_storage_manager.is_item_expired(
                key_path=kwargs.get(
                    "key_path",
                    ""
                ),
            )
        )

        return value

    def read_all_values_via_disk_cache(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        value: dict[str, Any] = (
            self._disk_cache_storage_manager.read_all_values()
        )

        return value

    def read_many_values_via_disk_cache(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        value: dict[str, Any] = (
            self._disk_cache_storage_manager.get_many_values(
                key_paths=kwargs.get(
                    "key_paths",
                    tuple()
                ),
            )
        )

        return value

    def write_many_values_via_disk_cache(
        self,
        **kwargs: Any,
    ) -> bool:
        self._disk_cache_storage_manager.set_many_values(
            values=kwargs.get(
                "values",
                {}
            ),
        )

        return True

    def remove_many_values_via_disk_cache(
        self,
        **kwargs: Any,
    ) -> dict[str, bool]:
        value: dict[str, Any] = (
            self._disk_cache_storage_manager.remove_many_values(
                key_paths=kwargs.get(
                    "key_paths",
                    tuple()
                ),
            )
        )

        return value

    def open_via_disk_cache(
        self,
        **kwargs: Any,
    ) -> bool:
        self._disk_cache_storage_manager.open()

        return True

    def close_via_disk_cache(
        self,
        **kwargs: Any,
    ) -> bool:
        self._disk_cache_storage_manager.close()

        return True

    def clear_all_values_via_disk_cache(
        self,
    ) -> bool:
        self._disk_cache_storage_manager.clear_all_values()

        return True

    def remove_expired_values_via_disk_cache(self) -> int:
        value: int = (
            self._disk_cache_storage_manager.remove_expired_values()
        )

        return value

    def sync_via_disk_cache(self) -> bool:
        self._disk_cache_storage_manager.sync()

        return True

    def reorganize_via_disk_cache(self) -> bool:
        self._disk_cache_storage_manager.reorganize()

        return True

    def display_all_items_via_disk_cache(self) -> bool:
        self._disk_cache_storage_manager.display_all_items()

        return True

    def write_database_path_via_disk_cache(
        self,
        value: str
    ) -> bool:
        self._disk_cache_storage_manager.database_path = (
            value
        )

        return True

    # ValueCacheManager
    def read_any_value_via_value_cache(
        self,
        **kwargs: Any,
    ) -> Any:
        value: Any = (
            self._value_cache_manager.get_one_value(
                keys=kwargs.get(
                    "key_path",
                    tuple()
                ),
                output_type=(
                    _TargetCacheValue.ANY
                )
            )
        )

        return value

    def read_defined_value_via_value_cache(
        self,
        **kwargs: Any,
    ) -> Any:
        value: Any = (
            self._value_cache_manager.get_one_value(
                keys=kwargs.get(
                    "key_path",
                    tuple()
                ),
                output_type=(
                    _TargetCacheValue.DEFINED
                )
            )
        )

        return value

    def write_any_value_via_value_cache(
        self,
        **kwargs: Any,
    ) -> bool:
        self._value_cache_manager.set_one_value(
            keys=kwargs.get(
                "key_path",
                tuple()
            ),
            value=kwargs.get(
                "value",
                {}
            ),
            output_type=(
                _TargetCacheValue.ANY
            )
        )

        return True

    def write_defined_value_via_value_cache(
        self,
        **kwargs: Any,
    ) -> bool:
        self._value_cache_manager.set_one_value(
            keys=kwargs.get(
                "key_path",
                tuple()
            ),
            value=kwargs.get(
                "value",
                {}
            ),
            output_type=(
                _TargetCacheValue.DEFINED
            )
        )

        return True

    def write_file_path_value_via_value_cache(
        self,
        **kwargs: Any,
    ) -> bool:
        self._value_cache_manager.set_one_value(
            keys=kwargs.get(
                "key_path",
                tuple()
            ),
            value=kwargs.get(
                "value",
                {}
            ),
            output_type=(
                _TargetCacheValue.FILE_PATH
            )
        )

        return True

    def write_folder_path_value_via_value_cache(
        self,
        **kwargs: Any,
    ) -> bool:
        self._value_cache_manager.set_one_value(
            keys=kwargs.get(
                "key_path",
                tuple()
            ),
            value=kwargs.get(
                "value",
                {}
            ),
            output_type=(
                _TargetCacheValue.FOLDER_PATH
            )
        )

        return True

    def write_filesystem_path_value_via_value_cache(
        self,
        **kwargs: Any,
    ) -> bool:
        self._value_cache_manager.set_one_value(
            keys=kwargs.get(
                "key_path",
                tuple()
            ),
            value=kwargs.get(
                "value",
                {}
            ),
            output_type=(
                _TargetCacheValue.FILESYSTEM_PATH
            )
        )

        return True

    def display_all_items_via_value_cache(
        self,
    ) -> bool:
        self._value_cache_manager.display_all_items()

        return True

    def remove_one_value_via_value_cache(
        self,
        **kwargs: Any,
    ) -> bool:
        self._value_cache_manager.remove_one_value(
            keys=kwargs.get(
                "key_path",
                tuple()
            ),
        )

        return True

    def clear_all_values_via_value_cache(
        self,
    ) -> bool:
        self._value_cache_manager.clear_all_values()

        return True


    # TimeManager
    def read_selected_time_zone(
        self,
    ) -> str:
        value: str = (
            self._time_zone_manager.selected_time_zone_type
        )

        return value

    def write_selected_time_zone(
        self,
        **kwargs: Any,
    ) -> bool:
        self._time_zone_manager.selected_time_zone_type = (
            kwargs.get(
                "value",
                "local"
            ),
        )

        return True

    # TimestampManager
    def generate_current_date_timestamp(
        self,
    ) -> str:
        value: str = (
            self._timestamp_manager.generate_current_timestamp(
                _Timestamp.ISO_DATE_STRING
            )
        )

        return value

    def generate_current_filesystem_timestamp(
        self,
    ) -> str:
        value: str = (
            self._timestamp_manager.generate_current_timestamp(
                _Timestamp.ISO_FILESYSTEM_STRING
            )
        )

        return value

    # TextEncodingManager
    def read_selected_encoding(
        self,
    ) -> str:
        value: str = (
            self._text_encoding_manager.selected_encoding
        )

        return value

    def write_selected_encoding(
        self,
        **kwargs: Any,
    ) -> bool:
        self._text_encoding_manager.selected_encoding = (
            kwargs.get(
                "value",
                "utf-8"
            ),
        )

        return True


    # ScriptProcess
    def run_shell_command(
        self,
        **kwargs: Any,
    ) -> Any:
        value: Any = (
            self._script_process_manager.execute_command(
                command=kwargs.get(
                    "command",
                    ""
                ),
                script_process_type=(
                    _ScriptProcess.SHELL
                )
            )
        )

        return value

    def run_subprocess_command(
        self,
        **kwargs: Any,
    ) -> Any:
        value: Any = (
            self._script_process_manager.execute_command(
                command=kwargs.get(
                    "command",
                    ""
                ),
                script_process_type=(
                    _ScriptProcess.SUBPROCESS
                )
            )
        )

        return value

    # MacrosManager
    def macros_resolve_many(
        self,
        **kwargs: Any,
    ) -> Any:
        value: Any = (
            self._macros_manager.resolve_many(
                kwargs.get(
                    "values",
                    {}
                ),
            )
        )

        return value

    def macros_parse_many(
        self,
        **kwargs: Any,
    ) -> object:
        value: object = (
            self._macros_manager.parse_many(
                values=kwargs.get(
                    "values",
                    ""
                ),
                resolved=kwargs.get(
                    "resolved",
                    {}
                ),
            )
        )

        return value


    def macros_parse_filesystem(
        self,
        **kwargs: Any,
    ) -> bool:
        value: bool = (
            self._macros_manager.parse_filesystem(
                filesystem_path=kwargs.get(
                    "filesystem_path",
                    ""
                ),
                workspace_macros=kwargs.get(
                    "workspace_macros",
                    {}
                ),
            )
        )

        return value

    # ObjectMergeManager
    def object_deep_merge(
        self,
        **kwargs: Any,
    ) -> object:
        value: object = (
            self._object_merge_manager.deep_merge(
                left=kwargs.get(
                    "left",
                    {}
                ),
                right=kwargs.get(
                    "right",
                    {}
                ),
            )
        )

        return value

    def object_deep_merge_fragments(
        self,
        **kwargs: Any,
    ) -> object:
        value: object = (
            self._object_merge_manager.deep_merge_fragments(
                left=kwargs.get(
                    "left",
                    {}
                ),
                right=kwargs.get(
                    "right",
                    {}
                ),
            )
        )

        return value

    # group_selection_manager
    def object_flatten_group(
        self,
        **kwargs: Any,
    ) -> Any:
        return (
            self._group_selection_manager
                .flatten_group(
                    kwargs.get(
                        "target",
                        ""
                    ),
                    kwargs.get(
                        "data",
                        {}
                    ),
                )
        ) or {}

    # yaml
    def convert_yaml_string_to_object(
        self,
        **kwargs: Any,
    ) -> object:
        return _yaml.safe_load(
            kwargs.get(
                "value",
                ""
            )
        ) or {}

    def convert_yaml_object_to_string(
        self,
        **kwargs: Any,
    ) -> str:
        return _yaml.safe_dump(
            kwargs.get(
                "value",
                ""
            ),
            sort_keys=kwargs.get(
                "sort_keys",
                False,
            ),
            default_flow_style=kwargs.get(
                "default_flow_style",
                False,
            ),
            allow_unicode=kwargs.get(
                "allow_unicode",
                True,
            ),
            indent=kwargs.get(
                "indent",
                4,
            )
        ) or ""

    def format_yaml_to_string(
        self,
        **kwargs: Any,
    ) -> object:
        return (
            _yaml.dump(
                kwargs.get(
                    "value",
                    ""
                ),
                sort_keys=kwargs.get(
                    "sort_keys",
                    False,
                ),
                default_flow_style=kwargs.get(
                    "default_flow_style",
                    False,
                ),
                allow_unicode=kwargs.get(
                    "allow_unicode",
                    True,
                ),
                indent=kwargs.get(
                    "indent",
                    4,
                )
            )
        )

    def read_yaml_file(
        self,
        **kwargs: Any,
    ) -> object:
        path = _Path(
            kwargs.get(
                "file_path",
                ""
            ),
        )

        with path.open(
            mode="r",
            encoding=kwargs.get(
                "encoding",
                "utf-8"
            ),
        ) as file:
            return _yaml.safe_load(file) or {}

    def write_yaml_file(
        self,
        **kwargs: Any,
    ) -> bool:
        path = _Path(
            kwargs.get(
                "file_path",
                ""
            ),
        )

        with path.open(
            mode="w",
            encoding=kwargs.get(
                "encoding",
                "utf-8"
            ),
        ) as file:
            _yaml.safe_dump(
                kwargs.get(
                    "value",
                    ""
                ),
                file,
                sort_keys=kwargs.get(
                    "sort_keys",
                    False,
                ),
                default_flow_style=kwargs.get(
                    "default_flow_style",
                    False,
                ),
                allow_unicode=kwargs.get(
                    "allow_unicode",
                    True,
                ),
                indent=kwargs.get(
                    "indent",
                    4,
                )
            )

        return True

    # JSON
    def read_json_file(
        self,
        **kwargs: Any,
    ) -> object:
        file_path = kwargs.get(
            "file_path",
            ""
        )

        return self._json_file_io_manager.read_file(
            file_path
        ) or {}


    def write_json_file(
        self,
        **kwargs: Any,
    ) -> bool:
        file_path = kwargs.get(
            "file_path",
            ""
        )
        data = kwargs.get(
            "data",
            {}
        )

        self._json_file_io_manager.write_file(
            file_path,
            data
        )

        return True

    # Python
    def read_python_file(
        self,
        **kwargs: Any,
    ) -> object:
        file_path = _Path(
            kwargs.get(
                "file_path",
                ""
            )
        )

        module_name = file_path.stem
        spec = _spec_from_file_location(module_name, file_path)
        module = _module_from_spec(spec)
        spec.loader.exec_module(module)

        return module or {}

    # JsonTextManager
    def convert_to_json_string(
        self,
        **kwargs: Any,
    ) -> str:
        value: str = (
            self._json_text_manager.convert_to_string(
                value=kwargs.get(
                    "value", ""
                )
            )
        )

        return value

    # FilesystemManager
    def read_child_folder_paths(
        self,
        **kwargs: Any,
    ) -> Any:
        return _Path(
            kwargs.get(
                "value",
                "",
            ),
        ).iterdir()

    def read_file_suffix(
        self,
        **kwargs: Any,
    ) -> Any:
        return _Path(
            kwargs.get(
                "value",
                "",
            ),
        ).suffix


    def read_filesystem_modification_timestamp(
        self,
        **kwargs: Any,
    ) -> float:
        value: float = (
            _Path(
                kwargs.get(
                    "value",
                    "",
                ),
            ).stat().st_mtime
        )

        return value

    def read_filesystem_status_change_timestamp(
        self,
        **kwargs: Any,
    ) -> float:
        value: float = (
            _Path(
                kwargs.get(
                    "value",
                    "",
                ),
            ).stat().st_ctime
        )

        return value

    def read_filesystem_access_timestamp(
        self,
        **kwargs: Any,
    ) -> float:
        value: float = (
            _Path(
                kwargs.get(
                    "value",
                    "",
                ),
            ).stat().st_atime
        )

        return value

    def read_filesystem_via_pattern(
        self,
        **kwargs: Any,
    ) -> Any:
        filesystem_path: str = kwargs.get(
            "filesystem_path",
            "",
        )
        pattern: str = kwargs.get(
            "pattern",
            "",
        )
        value: Any = tuple(
            _Path(
                filesystem_path
            ).glob(pattern)
        )

        return value

    def uncompress_zip(
        self,
        **kwargs: Any,
    ) -> bool:
        value: bool = self._filesystem_compression_manager.zip_extract(
            archive_path=kwargs.get(
                "archive_path",
                "",
            ),
            destination_path=kwargs.get(
                "destination_path",
                "",
            ),
            overwrite=kwargs.get(
                "overwrite",
                False,
            ),
        )

        return value


    def is_filesystem_path_valid(
        self,
        **kwargs: Any,
    ) -> bool:
        value: bool = _Path(
            kwargs.get(
                "value",
                "",
            )
        ).exists()

        return value

    def is_file_path_valid(
        self,
        **kwargs: Any,
    ) -> bool:
        value: bool = _Path(
            kwargs.get(
                "value",
                "",
            )
        ).is_file()

        return value

    def is_folder_path_valid(
        self,
        **kwargs: Any,
    ) -> bool:
        value: bool = _Path(
            kwargs.get(
                "value",
                "",
            )
        ).is_dir()

        return value

    def setup_filesystem_tree_path(
        self,
        **kwargs: Any,
    ) -> bool:
        _Path(kwargs.get(
            "directory",
            "",
        )).mkdir(
            parents=True,
            exist_ok=True,
        )

        return True

    def move_filesystem_path(
        self,
        **kwargs: Any,
    ) -> bool:
        source = _Path(kwargs.get(
            "first_path",
            "",
        ))
        destination = _Path(kwargs.get(
            "second_path",
            "",
        ))

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        _shutil.move(
            str(source),
            str(destination),
        )

        return True

    def copy_filesystem_path(
        self,
        **kwargs: Any,
    ) -> bool:
        fs_first_path = _Path(kwargs.get(
            "first_path",
            "",
        ))
        fs_second_path = _Path(kwargs.get(
            "second_path",
            "",
        ))

        if fs_first_path.is_dir():
            _shutil.copytree(
                fs_first_path,
                fs_second_path,
                dirs_exist_ok=True,
            )

        elif fs_first_path.is_file():
            fs_second_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            _shutil.copy2(
                fs_first_path,
                fs_second_path,
            )

        else:
            return True

        return True

    def clean_filesystem_path(
        self,
        **kwargs: Any,
    ) -> bool:
        directory = _Path(
            kwargs.get(
                "path",
                "",
            )
        ).resolve()

        protected_paths = {
            _Path(""),
            _Path("/"),
            _Path.home(),
        }

        if directory in protected_paths:
            raise ValueError(
                f"folder path '{directory}' is protected"
            )

        if not directory.exists():
            return True

        if not directory.is_dir():
            raise ValueError(
                f"file path '{directory}' is not a folder"
            )

        for item in directory.iterdir():
            if item.is_file() or item.is_symlink():
                item.unlink()

            elif item.is_dir():
                _shutil.rmtree(item)

        return True

    def rename_filesystem_entity(
        self,
        **kwargs: Any,
    ) -> bool:
        _Path(kwargs.get(
            "source",
            "",
        )).rename(
            kwargs.get(
                "destination",
                "",
            )
        )

        return True

    def read_python_filesystem_paths(
        self,
        **kwargs: Any,
    ) -> Any:
        target_path = _Path(
            kwargs.get(
                "path",
                "",
            )
        )

        value: Any = tuple(
            str(path)
            for path in target_path.rglob("*.py")
            if "__pycache__" not in path.parts
        )

        return value

    # uuid
    def generate_uuidv4(
        self
    ) -> str:
        value: str = _uuid.uuid4()
        return value

    def generate_uuidv5(
        self,
        **kwargs: Any,
    ) -> str:
        value: str = _uuid.uuid5(
            _uuid.NAMESPACE_DNS,
            kwargs.get(
                "key",
                "key",
            )
        )
        return value

    def generate_uuidv7(
        self,
    ) -> str:
        value: str = _uuid.uuid7()
        return value


    # SystemManager
    def read_method_name(
        self,
        level: int = 2,
    ) -> str:
        value: str = f"{_sys._getframe(level).f_code.co_name}"
        return value

    def read_operating_system_name(
        self,
    ) -> str:
        value: str = self._system_manager.operating_system_name
        return value

    def read_operating_system_architecture(
        self,
    ) -> str:
        value: str = self._system_manager.operating_system_architecture
        return value

    def read_current_executing_script_filesystem_path(
        self,
    ) -> str:
        value: str = (
            self._system_manager
                .current_executing_script_filesystem_path
        )
        return value

    def read_current_executing_console_filesystem_path(
        self,
    ) -> str:
        value: str = (
            self._system_manager
                .current_executing_console_filesystem_path
        )
        return value

    def write_current_executing_console_filesystem_path(
        self,
        **kwargs: Any,
    ) -> bool:
        self._system_manager.current_executing_console_filesystem_path = (
            kwargs.get(
                "filesystem_path",
                "",
            )
        )

        return True

    # FileIoManager
    def read_file(
        self,
        **kwargs: Any,
    ) -> str:
        value: str = (
            self._file_io_manager.read_file(
                file_path=kwargs.get(
                    "file_path",
                    "",
                )
            )
        )

        return value

    def write_file(
        self,
        **kwargs: Any,
    ) -> bool:
        self._file_io_manager.write_file(
            file_path=kwargs.get(
                "file_path",
                "",
            ),
            data=kwargs.get(
                "data",
                {},
            ),
        )

        return True

    # Logging
    def setup_file_log_settings(
        self,
        **kwargs: Any,
    ) -> bool:
        is_enabled = kwargs.get(
            "is_enabled",
            True,
        )
        is_verbose = kwargs.get(
            "is_verbose",
            True,
        )

        self._file_log_manager.options = _LogOptions(
            is_enabled=is_enabled,
            is_verbose_enabled=is_verbose
        )

        if is_enabled:
            file_outputs = kwargs.get(
                "file_outputs",
                tuple(),
            )

            for file_output in file_outputs:
                self._file_log_manager.add_file_output(
                    file_output
                )

        return True

    def setup_console_log_settings(
        self,
        **kwargs: Any,
    ) -> bool:
        is_enabled = kwargs.get(
            "is_enabled",
            True,
        )
        is_verbose = kwargs.get(
            "is_verbose",
            True,
        )

        self._console_log_manager.options = _LogOptions(
            is_enabled=is_enabled,
            is_verbose_enabled=is_verbose
        )

        return True

    def log_info_to_file(
        self,
        **kwargs: Any,
    ) -> bool:
        self._file_log_manager.log_info(
            message=kwargs.get(
                "message",
                "",
            ),
        )

        return True

    def log_warning_to_file(
        self,
        **kwargs: Any,
    ) -> bool:
        self._file_log_manager.log_warning(
            message=kwargs.get(
                "message",
                "",
            ),
        )

        return True

    def log_info_to_all(
        self,
        **kwargs: Any,
    ) -> bool:
        self._log_manager.log_info(
            message=kwargs.get(
                "message",
                "",
            ),
        )

        return True

    def log_cache_info_to_file(
        self,
        **kwargs: Any,
    ) -> bool:
        self._file_log_manager.cache_log(
            message=kwargs.get(
                "message",
                "",
            ),
            log_level=_logging.INFO
        )

        return True

    def log_cache_warning_to_file(
        self,
        **kwargs: Any,
    ) -> bool:
        self._file_log_manager.cache_log(
            message=kwargs.get(
                "message",
                "",
            ),
            log_level=_logging.WARNING
        )

        return True

    def log_shutdown(
        self,
        **kwargs: Any,
    ) -> bool:
        self._log_manager.shutdown()

        return True

    def run_async(
        self,
        **kwargs: Any,
    ) -> bool:
        tasks: Any = (
            kwargs.get("tasks", tuple())
        )

        with _ThreadPoolExecutor(
            max_workers=min(32, len(tasks) or 1),
        ) as executor:
            tuple(
                executor.map(
                    lambda task: task[0](task[1]),
                    tasks,
                )
            )

        return True
