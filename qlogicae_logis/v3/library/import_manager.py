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
_ZipFile: Any = None
_metadata: Any = None
_resource: Any = None
_Timestamp: Any = None
_LogOptions: Any = None
_LogManager: Any = None
_TimeManager: Any = None
_tracemalloc: Any = None
_MacrosManager: Any = None
_SystemManager: Any = None
_ScriptProcess: Any = None
_FileIoManager: Any = None
_TimeZoneManager: Any = None
_module_from_spec: Any = None
_SingletonManager: Any = None
_TimestampManager: Any = None
_TargetCacheValue: Any = None
_ConsoleLogManager: Any = None
_ValueCacheManager: Any = None
_CorFileLogManager: Any = None
_ObjectMergeManager: Any = None
_TextEncodingManager: Any = None
_ScriptProcessManager: Any = None
# _GroupSelectionManager: Any = None
_spec_from_file_location: Any = None
_DiskCacheStorageManager: Any = None
_ScriptProcessEnumManager: Any = None
_FilesystemCompressionManager: Any = None
_FileEntityFileSystemTreeSetupOptions: Any = None
_FolderEntityFileSystemTreeSetupOptions: Any = None


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _gc
    global _sys
    global _time
    global _uuid
    global _yaml
    global _Path
    global _shutil
    global _logging
    global _ZipFile
    global _metadata
    global _resource
    global _Timestamp
    global _LogOptions
    global _LogManager
    global _tracemalloc
    global _TimeManager
    global _MacrosManager
    global _SystemManager
    global _ScriptProcess
    global _FileIoManager
    global _module_from_spec
    global _TimeZoneManager
    global _SingletonManager
    global _TimestampManager
    global _TargetCacheValue
    global _ConsoleLogManager
    global _ValueCacheManager
    global _CorFileLogManager
    global _ObjectMergeManager
    global _TextEncodingManager
    global _ScriptProcessManager
    global _spec_from_file_location
    global _DiskCacheStorageManager
    global _ScriptProcessEnumManager
    global _FilesystemCompressionManager
    global _FileEntityFileSystemTreeSetupOptions
    global _FolderEntityFileSystemTreeSetupOptions

    import gc
    import logging
    import resource
    import shutil
    import sys
    import time
    import tracemalloc
    import uuid
    from importlib import metadata
    from importlib.util import module_from_spec, spec_from_file_location
    from pathlib import Path
    from zipfile import ZipFile

    from .._vendor.pyyaml import yaml
    from .._vendor.qlogicae_cor.v2.library import (
        console_log_manager,
        disk_cache_storage_manager,
        file_entity_filesystem_tree_setup_options,
        file_io_manager,
        file_log_manager,
        filesystem_compression_manager,
        folder_entity_filesystem_tree_setup_options,
        log_manager,
        log_options,
        macros_manager,
        object_merge_manager,
        script_process,
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
    _sys = sys
    _uuid = uuid
    _yaml = yaml
    _Path = Path
    _time = time
    _shutil = shutil
    _ZipFile = ZipFile
    _logging = logging
    _metadata = metadata
    _resource = resource
    _tracemalloc = tracemalloc
    _Timestamp = timestamp.Timestamp
    _LogOptions = log_options.LogOptions
    _LogManager = log_manager.LogManager
    _module_from_spec = module_from_spec
    _TimeManager = time_manager.TimeManager
    _MacrosManager = macros_manager.MacrosManager
    _SystemManager = system_manager.SystemManager
    _spec_from_file_location = spec_from_file_location
    _TimeZoneManager = time_zone_manager.TimeZoneManager
    _CorFileLogManager = file_log_manager.FileLogManager
    _SingletonManager = singleton_manager.SingletonManager
    _TimestampManager = timestamp_manager.TimestampManager
    _TargetCacheValue = target_cache_value.TargetCacheValue
    _ValueCacheManager = value_cache_manager.ValueCacheManager
    _ObjectMergeManager = object_merge_manager.ObjectMergeManager
    _ScriptProcessManager = script_process_manager.ScriptProcessManager
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
    _ConsoleLogManager = console_log_manager.ConsoleLogManager
    _DiskCacheStorageManager = (
        disk_cache_storage_manager.DiskCacheStorageManager
    )
    _ScriptProcess = script_process.ScriptProcess
    _FileIoManager = file_io_manager.FileIoManager
    _TextEncodingManager = (
        text_encoding_manager
            .TextEncodingManager
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
        # "_timestamp_manager",
        "_text_encoding_manager",
        "_script_process_manager",
        "_macros_manager",
        "_object_merge_manager",
        # "_group_selection_manager",
        "_filesystem_compression_manager",
        "_system_manager",
        "_file_io_manager",
        "_file_log_manager",
        "_console_log_manager",
        "_log_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._time_manager = self.read_singleton(
            _TimeManager
        )
        self._disk_cache_storage_manager = self.read_singleton(
            _DiskCacheStorageManager
        )
        self._value_cache_manager = self.read_singleton(
            _ValueCacheManager
        )
        self._time_zone_manager = self.read_singleton(
            _TimeZoneManager
        )
        # self._timestamp_manager = self.read_singleton(
        #     _TimestampManager
        # )
        self._text_encoding_manager = self.read_singleton(
            _TextEncodingManager
        )
        self._script_process_manager = self.read_singleton(
            _ScriptProcessManager
        )
        self._macros_manager = self.read_singleton(
            _MacrosManager
        )
        self._object_merge_manager = self.read_singleton(
            _ObjectMergeManager
        )
        # self._group_selection_manager = self.read_singleton(
        #     _GroupSelectionManager
        # )
        self._filesystem_compression_manager = self.read_singleton(
            _FilesystemCompressionManager
        )
        self._system_manager = self.read_singleton(
            _SystemManager
        )
        self._file_io_manager = self.read_singleton(
            _FileIoManager
        )
        self._file_log_manager = self.read_singleton(
            _CorFileLogManager
        )
        self._console_log_manager = self.read_singleton(
            _ConsoleLogManager
        )
        self._log_manager = self.read_singleton(
            _LogManager
        )

    @classmethod
    def read_singleton(self, value: Any) -> Any:
        if not value:
            return {}

        _handle_singleton_manager_imports()

        return (
            _SingletonManager.get_singleton(
                value
            )
        )

    # def convert_to_os_specific_path_value(
    #     self,
    #     **kwargs: Any,
    # ) -> str:
    #     filesystem_path = kwargs.get(
    #         "filesystem_path",
    #         ""
    #     )

    #     return f"{_Path(
    #         filesystem_path
    #     )}"

    def compress(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        source = (
            kwargs.get("source", "")
        )
        destination = (
            kwargs.get("destination", "")
        )
        mode = (
            kwargs.get("mode", "")
        )
        if not destination or not mode:
            return False

        source = _Path(source)
        compression = (
            kwargs.get("compression", "deflated")
        )
        compression = (
            self.read_zip_format_compression(
                value=compression
            )
        )
        compresslevel = (
            kwargs.get("compresslevel", 6)
        )
        allowZip64 = (
            kwargs.get("allowZip64", True)
        )
        strict_timestamps = (
            kwargs.get("strict_timestamps", True)
        )

        with _ZipFile(
            destination,
            mode=mode,
            compression=compression,
            compresslevel=compresslevel,
            allowZip64=allowZip64,
            strict_timestamps=strict_timestamps,
        ) as archive:
            for path in source.rglob("*"):
                archive.write(
                    path,
                    arcname=path.relative_to(source),
                )


        return True

    def read_metadata_version(self, target: str) -> str:
        if not target:
            return "v0.0.0"

        return (
            _metadata.version(target) or "v0.0.0"
        )

    # def snapshot_memory_usage(self) -> Any:
    #     current_bytes, peak_bytes = (
    #         _tracemalloc.get_traced_memory()
    #         if _tracemalloc.is_tracing()
    #         else (0, 0)
    #     )

    #     peak_rss = _resource.getrusage(
    #         _resource.RUSAGE_SELF,
    #     ).ru_maxrss

    #     if _sys.platform != "darwin":
    #         peak_rss *= 1024

    #     return {
    #         "tracemalloc-current": { "value": current_bytes },
    #         "tracemalloc-peak": { "value": peak_bytes },
    #         "process-peak-rss": { "value": peak_rss },
    #         "gc-tracked-objects": { "value": len(_gc.get_objects(),) },
    #     }

    # TimeManager
    def time_delay(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        value = (
            kwargs.get(
                "value",
                0
            )
        )
        if not value:
            return False

        _time.sleep(
            value
        )

        return True

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

    # def read_current_day(
    #     self,
    # ) -> int:
    #     value: int = (
    #         self._time_manager.current_day
    #     )

    #     return value

    # def read_current_month(
    #     self,
    # ) -> int:
    #     value: int = (
    #         self._time_manager.current_month
    #     )

    #     return value

    def read_current_year(
        self,
    ) -> int:
        value: int = (
            self._time_manager.current_year
        )

        return value

    # DiskCacheStorageManager
    # def is_key_found_via_disk_cache(
    #     self,
    #     **kwargs: Any,
    # ) -> bool:
    #     if not kwargs:
    #         return False

    #     value: bool = (
    #         self._disk_cache_storage_manager.is_keys_found(
    #             key_path=kwargs.get(
    #                 "key_path",
    #                 ""
    #             ),
    #         )
    #     )

    #     return value

    # def is_item_expired_via_disk_cache(
    #     self,
    #     **kwargs: Any,
    # ) -> bool:
    #     if not kwargs:
    #         return False

    #     value: bool = (
    #         self._disk_cache_storage_manager.is_item_expired(
    #             key_path=kwargs.get(
    #                 "key_path",
    #                 ""
    #             ),
    #         )
    #     )

    #     return value

    def read_all_values_via_disk_cache(
        self,
    ) -> dict[str, Any]:
        value: dict[str, Any] = (
            self._disk_cache_storage_manager.get_all_values()
        )

        return value

    def read_many_values_via_disk_cache(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        if not kwargs:
            return {}

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
        if not kwargs:
            return False

        self._disk_cache_storage_manager.set_many_values(
            values=kwargs.get(
                "values",
                {}
            ) or {},
        )

        return True

    # def remove_many_values_via_disk_cache(
    #     self,
    #     **kwargs: Any,
    # ) -> dict[str, bool]:
    #     if not kwargs:
    #         return {}

    #     value: dict[str, Any] = (
    #         self._disk_cache_storage_manager.remove_many_values(
    #             key_paths=kwargs.get(
    #                 "key_paths",
    #                 tuple()
    #             ),
    #         )
    #     )

    #     return value

    def open_via_disk_cache(
        self,
    ) -> bool:
        self._disk_cache_storage_manager.open()

        return True

    def close_via_disk_cache(
        self,
    ) -> bool:
        self._disk_cache_storage_manager.close()

        return True

    def clear_all_values_via_disk_cache(
        self,
    ) -> bool:
        self._disk_cache_storage_manager.clear_all_values()

        return True

    # def remove_expired_values_via_disk_cache(self) -> int:
    #     value: int = (
    #         self._disk_cache_storage_manager.remove_expired_values()
    #     )

    #     return value

    # def sync_via_disk_cache(self) -> bool:
    #     self._disk_cache_storage_manager.sync()

    #     return True

    # def reorganize_via_disk_cache(self) -> bool:
    #     self._disk_cache_storage_manager.reorganize()

    #     return True

    # def display_all_items_via_disk_cache(self) -> bool:
    #     self._disk_cache_storage_manager.display_all_items()

    #     return True

    def write_database_path_via_disk_cache(
        self,
        value: str
    ) -> bool:
        if not value:
            return False

        self._disk_cache_storage_manager.database_path = (
            value
        )

        return True

    # ValueCacheManager
    def read_any_value_via_value_cache(
        self,
        **kwargs: Any,
    ) -> Any:
        if not kwargs:
            return {}

        value: Any = (
            self._value_cache_manager.get_one_value(
                key_path=kwargs.get(
                    "key_path",
                    tuple()
                ),
                output_type=(
                    _TargetCacheValue.ANY
                )
            )
        )

        return value

    # def read_defined_value_via_value_cache(
    #     self,
    #     **kwargs: Any,
    # ) -> Any:
    #     if not kwargs:
    #         return {}

    #     value: Any = (
    #         self._value_cache_manager.get_one_value(
    #             key_path=kwargs.get(
    #                 "key_path",
    #                 tuple()
    #             ),
    #             output_type=(
    #                 _TargetCacheValue.DEFINED
    #             )
    #         )
    #     )

    #     return value

    def write_any_value_via_value_cache(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        self._value_cache_manager.set_one_value(
            key_path=kwargs.get(
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

    # def write_defined_value_via_value_cache(
    #     self,
    #     **kwargs: Any,
    # ) -> bool:
    #     if not kwargs:
    #         return False

    #     self._value_cache_manager.set_one_value(
    #         key_path=kwargs.get(
    #             "key_path",
    #             tuple()
    #         ),
    #         value=kwargs.get(
    #             "value",
    #             {}
    #         ),
    #         output_type=(
    #             _TargetCacheValue.DEFINED
    #         )
    #     )

    #     return True

    # def write_file_path_value_via_value_cache(
    #     self,
    #     **kwargs: Any,
    # ) -> bool:
    #     if not kwargs:
    #         return False

    #     self._value_cache_manager.set_one_value(
    #         key_path=kwargs.get(
    #             "key_path",
    #             tuple()
    #         ),
    #         value=kwargs.get(
    #             "value",
    #             {}
    #         ),
    #         output_type=(
    #             _TargetCacheValue.FILE_PATH
    #         )
    #     )

    #     return True

    # def write_folder_path_value_via_value_cache(
    #     self,
    #     **kwargs: Any,
    # ) -> bool:
    #     if not kwargs:
    #         return False

    #     self._value_cache_manager.set_one_value(
    #         key_path=kwargs.get(
    #             "key_path",
    #             tuple()
    #         ),
    #         value=kwargs.get(
    #             "value",
    #             {}
    #         ),
    #         output_type=(
    #             _TargetCacheValue.FOLDER_PATH
    #         )
    #     )

    #     return True

    # def write_filesystem_path_value_via_value_cache(
    #     self,
    #     **kwargs: Any,
    # ) -> bool:
    #     if not kwargs:
    #         return False

    #     self._value_cache_manager.set_one_value(
    #         key_path=kwargs.get(
    #             "key_path",
    #             tuple()
    #         ),
    #         value=kwargs.get(
    #             "value",
    #             {}
    #         ),
    #         output_type=(
    #             _TargetCacheValue.FILESYSTEM_PATH
    #         )
    #     )

    #     return True

    # def display_all_items_via_value_cache(
    #     self,
    # ) -> bool:
    #     self._value_cache_manager.display_all_items()

    #     return True

    def remove_one_value_via_value_cache(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        self._value_cache_manager.remove_one_value(
            key_path=kwargs.get(
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
    # def read_selected_time_zone(
    #     self,
    # ) -> str:
    #     value: str = (
    #         self._time_zone_manager.selected_time_zone_type
    #     )

    #     return value

    # def write_selected_time_zone(
    #     self,
    #     **kwargs: Any,
    # ) -> bool:
    #     if not kwargs:
    #         return False

    #     self._time_zone_manager.selected_time_zone_type = (
    #         kwargs.get(
    #             "value",
    #             "local"
    #         ),
    #     )

    #     return True

    # # TimestampManager
    # def generate_current_date_timestamp(
    #     self,
    # ) -> str:
    #     value: str = (
    #         self._timestamp_manager.generate_current_timestamp(
    #             _Timestamp.ISO_DATE_STRING
    #         )
    #     )

    #     return value

    # def generate_current_filesystem_timestamp(
    #     self,
    # ) -> str:
    #     value: str = (
    #         self._timestamp_manager.generate_current_timestamp(
    #             _Timestamp.ISO_FILESYSTEM_STRING
    #         )
    #     )

    #     return value

    # # TextEncodingManager
    # def read_selected_encoding(
    #     self,
    # ) -> str:
    #     value: str = (
    #         self._text_encoding_manager.selected_encoding
    #     )

    #     return value

    # def write_selected_encoding(
    #     self,
    #     **kwargs: Any,
    # ) -> bool:
    #     if not kwargs:
    #         return False

    #     self._text_encoding_manager.selected_encoding = (
    #         kwargs.get(
    #             "value",
    #             "utf-8"
    #         ),
    #     )

    #     return True


    # ScriptProcess
    def run_shell_command(
        self,
        **kwargs: Any,
    ) -> Any:
        if not kwargs:
            return False

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
        if not kwargs:
            return False

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

    def run_command(
        self,
        **kwargs: Any,
    ) -> Any:
        if not kwargs:
            return {}

        script_process = (
            kwargs.get(
                "script_process",
                "shell"
            )
        )
        command = (
            kwargs.get(
                "command",
                ""
            )
        )
        if not command:
            return {}

        cli_output = {}
        if script_process == "shell":
            cli_output = self.run_shell_command(
                command=command
            )

        elif script_process == "subprocess":
            cli_output = self.run_subprocess_command(
                command=command
            )

        return cli_output

    # MacrosManager
    def macros_resolve_many(
        self,
        **kwargs: Any,
    ) -> Any:
        if not kwargs:
            return False

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
        if not kwargs:
            return False

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
        if not kwargs:
            return False

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
        if not kwargs:
            return False

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

    # def object_deep_merge_fragments(
    #     self,
    #     **kwargs: Any,
    # ) -> object:
    #     if not kwargs:
    #         return False

    #     value: object = (
    #         self._object_merge_manager.deep_merge_fragments(
    #             left=kwargs.get(
    #                 "left",
    #                 {}
    #             ),
    #             right=kwargs.get(
    #                 "right",
    #                 {}
    #             ),
    #         )
    #     )

    #     return value

    # group_selection_manager
    # def object_flatten_group(
    #     self,
    #     **kwargs: Any,
    # ) -> Any:
    #     if not kwargs:
    #         return False

    #     return (
    #         self._group_selection_manager
    #             .flatten_group(
    #                 kwargs.get(
    #                     "target",
    #                     ""
    #                 ),
    #                 kwargs.get(
    #                     "data",
    #                     {}
    #                 ),
    #             )
    #     ) or {}

    # # yaml
    # def convert_yaml_string_to_object(
    #     self,
    #     **kwargs: Any,
    # ) -> object:
    #     if not kwargs:
    #         return {}

    #     return _yaml.safe_load(
    #         kwargs.get(
    #             "value",
    #             ""
    #         )
    #     ) or {}

    # def convert_yaml_object_to_string(
    #     self,
    #     **kwargs: Any,
    # ) -> str:
    #     if not kwargs:
    #         return ""

    #     return _yaml.safe_dump(
    #         kwargs.get(
    #             "value",
    #             ""
    #         ),
    #         sort_keys=kwargs.get(
    #             "sort_keys",
    #             False,
    #         ),
    #         default_flow_style=kwargs.get(
    #             "default_flow_style",
    #             False,
    #         ),
    #         allow_unicode=kwargs.get(
    #             "allow_unicode",
    #             True,
    #         ),
    #         indent=kwargs.get(
    #             "indent",
    #             4,
    #         )
    #     ) or ""

    # def format_yaml_to_string(
    #     self,
    #     **kwargs: Any,
    # ) -> object:
    #     if not kwargs:
    #         return False

    #     return (
    #         _yaml.dump(
    #             kwargs.get(
    #                 "value",
    #                 ""
    #             ),
    #             sort_keys=kwargs.get(
    #                 "sort_keys",
    #                 False,
    #             ),
    #             default_flow_style=kwargs.get(
    #                 "default_flow_style",
    #                 False,
    #             ),
    #             allow_unicode=kwargs.get(
    #                 "allow_unicode",
    #                 True,
    #             ),
    #             indent=kwargs.get(
    #                 "indent",
    #                 4,
    #             )
    #         )
    #     )

    def read_yaml_file(
        self,
        **kwargs: Any,
    ) -> object:
        if not kwargs:
            return False

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

    # def write_yaml_file(
    #     self,
    #     **kwargs: Any,
    # ) -> bool:
    #     if not kwargs:
    #         return False

    #     path = _Path(
    #         kwargs.get(
    #             "file_path",
    #             ""
    #         ),
    #     )

    #     with path.open(
    #         mode="w",
    #         encoding=kwargs.get(
    #             "encoding",
    #             "utf-8"
    #         ),
    #     ) as file:
    #         _yaml.safe_dump(
    #             kwargs.get(
    #                 "value",
    #                 ""
    #             ),
    #             file,
    #             sort_keys=kwargs.get(
    #                 "sort_keys",
    #                 False,
    #             ),
    #             default_flow_style=kwargs.get(
    #                 "default_flow_style",
    #                 False,
    #             ),
    #             allow_unicode=kwargs.get(
    #                 "allow_unicode",
    #                 True,
    #             ),
    #             indent=kwargs.get(
    #                 "indent",
    #                 4,
    #             )
    #         )

    #     return True

    # Python
    def read_python_file(
        self,
        **kwargs: Any,
    ) -> object:
        if not kwargs:
            return False

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

    # FilesystemManager
    def read_child_folder_paths(
        self,
        **kwargs: Any,
    ) -> Any:
        if not kwargs:
            return False

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
        if not kwargs:
            return False

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
        if not kwargs:
            return False

        value: float = (
            _Path(
                kwargs.get(
                    "value",
                    "",
                ),
            ).stat().st_mtime
        )

        return value

    # def read_filesystem_status_change_timestamp(
    #     self,
    #     **kwargs: Any,
    # ) -> float:
    #     if not kwargs:
    #         return False

    #     value: float = (
    #         _Path(
    #             kwargs.get(
    #                 "value",
    #                 "",
    #             ),
    #         ).stat().st_ctime
    #     )

    #     return value

    # def read_filesystem_access_timestamp(
    #     self,
    #     **kwargs: Any,
    # ) -> float:
    #     if not kwargs:
    #         return False

    #     value: float = (
    #         _Path(
    #             kwargs.get(
    #                 "value",
    #                 "",
    #             ),
    #         ).stat().st_atime
    #     )

    #     return value

    def read_filesystem_via_pattern(
        self,
        **kwargs: Any,
    ) -> Any:
        if not kwargs:
            return False

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
        if not kwargs:
            return False

        archive_path = kwargs.get("archive_path", "")
        destination_path = kwargs.get("destination_path", "")
        if not archive_path or not destination_path:
            return False

        overwrite = kwargs.get("overwrite", False)
        value: bool = self._filesystem_compression_manager.zip_extract(
            archive_path=archive_path,
            destination_path=destination_path,
            overwrite=overwrite,
        )

        return value

    def read_zip_format_compression(
        self,
        **kwargs: Any,
    ) -> Any:
        if not kwargs:
            return False

        value = kwargs.get("value", "")
        if not value:
            return False

        value = (
            self._filesystem_compression_manager.get_zip_format_compression(
                value,
            )
        )

        return value

    # def is_filesystem_path_valid(
    #     self,
    #     **kwargs: Any,
    # ) -> bool:
    #     if not kwargs:
    #         return False

    #     value: bool = _Path(
    #         kwargs.get(
    #             "value",
    #             "",
    #         )
    #     ).exists()

    #     return value

    def is_file_path_valid(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

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
        if not kwargs:
            return False

        value: bool = _Path(
            kwargs.get(
                "value",
                "",
            )
        ).is_dir()

        return value

    def setup_filesystem_tree_paths(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        target_paths = kwargs.get("target_paths", [])
        if not target_paths or len(target_paths) < 1:
            return False

        for target_path in target_paths:
            if not target_path:
                continue

            _Path(target_path).mkdir(
                parents=True,
                exist_ok=True,
            )

        return True

    def setup_filesystem_tree_path(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        target_path = kwargs.get("target_path", "")
        if not target_path or not target_path:
            return False

        target_path = _Path(target_path)
        if target_path.exists():
            return False

        target_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        return True

    def setup_filesystem_tree(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        root_path = kwargs.get("root_path", "")
        tree = kwargs.get("tree", None)
        if not root_path or not tree:
            return False

        path = _Path(root_path)

        if not path.exists():
            raise ValueError(
                f"filesystem path '{path}' is invalid"
            )

        path.mkdir(
            parents=True,
            exist_ok=True,
        )

        for entity in tree.entities or []:
            entity_path = path / entity.name

            if isinstance(
                entity,
                _FolderEntityFileSystemTreeSetupOptions,
            ):
                entity_path.mkdir(
                    parents=True,
                    exist_ok=True,
                )

                self.setup_filesystem_tree(
                    root_path=entity_path,
                    tree=entity,
                )

            elif isinstance(
                entity,
                _FileEntityFileSystemTreeSetupOptions,
            ):
                if not entity_path.exists():
                    entity_path.write_text(
                        entity.content,
                        encoding=entity.encoding,
                    )

        return True

    def move_filesystem_path(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        source_path = kwargs.get("source_path", "")
        target_path = kwargs.get("target_path", "")

        if not source_path or not target_path:
            return False

        source_path = _Path(source_path)
        target_path = _Path(target_path)

        target_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        _shutil.move(
            str(source_path),
            str(target_path),
        )

        return True

    def copy_filesystem_paths(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        source_path = kwargs.get("source_path", "")
        target_paths = kwargs.get("target_paths", [])

        if not source_path or len(target_paths) < 1:
            return False

        source_path = _Path(source_path).resolve()

        for target_path in target_paths:
            if not target_path:
                continue

            target_path = _Path(target_path).resolve()

            if source_path == target_path:
                return False

            if source_path.is_dir():
                _shutil.copytree(
                    source_path,
                    target_path,
                    dirs_exist_ok=True,
                )

            elif source_path.is_file():
                target_path.parent.mkdir(
                    parents=True,
                    exist_ok=True,
                )

                _shutil.copy2(
                    source_path,
                    target_path,
                )

        return True

    def copy_filesystem_path(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        source_path = kwargs.get("source_path", "")
        target_path = kwargs.get("target_path", "")

        if not source_path or not target_path:
            return False

        source_path = _Path(source_path).resolve()

        if not target_path:
            return False

        target_path = _Path(target_path).resolve()

        if source_path == target_path:
            return False

        if source_path.is_dir():
            _shutil.copytree(
                source_path,
                target_path,
                dirs_exist_ok=True,
            )

        elif source_path.is_file():
            target_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            _shutil.copy2(
                source_path,
                target_path,
            )

        return True

    def clean_filesystem_paths(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        target_paths = kwargs.get("target_paths", [])
        if not target_paths or len(target_paths) < 1:
            return False

        for target_path in target_paths:
            if not target_path:
                continue

            target_path = _Path(
                target_path
            ).resolve()

            protected_paths = {
                _Path(""),
                _Path("/"),
                _Path.home(),
            }

            if target_path in protected_paths:
                continue

            if not target_path.exists():
                continue

            if target_path.is_file() or target_path.is_symlink():
                target_path.unlink()
                continue

            if target_path.is_dir():
                for item in target_path.iterdir():
                    if item.is_file() or item.is_symlink():
                        item.unlink()
                    elif item.is_dir():
                        _shutil.rmtree(item)

        return True

    def clean_filesystem_path(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        target_path = kwargs.get("target_path", "")
        if not target_path:
            return False

        target_path = _Path(
            target_path
        ).resolve()

        protected_paths = {
            _Path(""),
            _Path("/"),
            _Path.home(),
        }

        if target_path in protected_paths:
            return False

        if not target_path.exists():
            return False

        if target_path.is_file() or target_path.is_symlink():
            target_path.unlink()
            return False

        if target_path.is_dir():
            for item in target_path.iterdir():
                if item.is_file() or item.is_symlink():
                    item.unlink()
                elif item.is_dir():
                    _shutil.rmtree(item)

        return True

    def read_filesystem_entity_parents(
        self,
        **kwargs: Any,
    ) -> set[str]:
        if not kwargs:
            return set()

        data: set[str] = set()
        target_path = kwargs.get("target_path", "")
        if not target_path:
            return data

        parents = _Path(target_path).parents
        if not parents:
            return data

        for parent in parents:
            if not parent:
                continue

            data.add(f"{parent}")

        return data

    def rename_filesystem_entity(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        old_path = kwargs.get("old_path", "")
        new_path = kwargs.get("new_path", "")
        if not old_path or not new_path:
            return False

        _Path(old_path).rename(
            kwargs.get(new_path)
        )

        return True

    def read_python_filesystem_paths(
        self,
        **kwargs: Any,
    ) -> Any:
        if not kwargs:
            return False

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
    # def generate_uuidv4(
    #     self
    # ) -> str:
    #     value: str = _uuid.uuid4()
    #     return value

    # def generate_uuidv5(
    #     self,
    #     **kwargs: Any,
    # ) -> str:
    #     if not kwargs:
    #         return ""

    #     value: str = _uuid.uuid5(
    #         _uuid.NAMESPACE_DNS,
    #         kwargs.get(
    #             "key",
    #             "key",
    #         )
    #     )
    #     return value

    # def generate_uuidv7(
    #     self,
    # ) -> str:
    #     value: str = _uuid.uuid7()
    #     return value

    # SystemManager
    # def read_method_name(
    #     self,
    #     level: int = 2,
    # ) -> str:
    #     value: str = f"{_sys._getframe(level).f_code.co_name}"
    #     return value

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

    # def read_current_executing_script_filesystem_path(
    #     self,
    # ) -> str:
    #     value: str = (
    #         self._system_manager
    #             .current_executing_script_filesystem_path
    #     )
    #     return value

    # def read_current_executing_console_filesystem_path(
    #     self,
    # ) -> str:
    #     value: str = (
    #         self._system_manager
    #             .current_executing_console_filesystem_path
    #     )
    #     return value

    def write_current_executing_console_filesystem_path(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        self._system_manager.current_executing_console_filesystem_path = (
            kwargs.get(
                "filesystem_path",
                "",
            )
        )

        return True

    def read_original_executing_console_filesystem_path(
        self,
    ) -> str:
        value: str = (
            self._system_manager
                .original_executing_console_filesystem_path
        )
        return value

    # FileIoManager
    def read_file(
        self,
        **kwargs: Any,
    ) -> str:
        if not kwargs:
            return ""

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
        if not kwargs:
            return False

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
        if not kwargs:
            return False

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
        if not kwargs:
            return False

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

    # def log_info_to_file(
    #     self,
    #     **kwargs: Any,
    # ) -> bool:
    #     if not kwargs:
    #         return False

    #     self._file_log_manager.log_info(
    #         message=kwargs.get(
    #             "message",
    #             "",
    #         ),
    #     )

    #     return True

    # def log_warning_to_file(
    #     self,
    #     **kwargs: Any,
    # ) -> bool:
    #     if not kwargs:
    #         return False

    #     self._file_log_manager.log_warning(
    #         message=kwargs.get(
    #             "message",
    #             "",
    #         ),
    #     )

    #     return True

    # def log_debug_to_file(
    #     self,
    #     **kwargs: Any,
    # ) -> bool:
    #     if not kwargs:
    #         return False

    #     self._file_log_manager.log_info(
    #         message=kwargs.get(
    #             "message",
    #             "",
    #         ),
    #     )

    #     return True

    # def log_info_to_all(
    #     self,
    #     **kwargs: Any,
    # ) -> bool:
    #     if not kwargs:
    #         return False

    #     self._log_manager.log_info(
    #         message=kwargs.get(
    #             "message",
    #             "",
    #         ),
    #     )

    #     return True

    def log_cache_info_to_file(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        self._file_log_manager.cache_log(
            message=kwargs.get(
                "message",
                "",
            ),
            log_level=_logging.INFO
        )

        return True

    def log_cache_debug_to_file(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        self._file_log_manager.cache_log(
            message=kwargs.get(
                "message",
                "",
            ),
            log_level=_logging.DEBUG
        )

        return True

    def log_cache_warning_to_file(
        self,
        **kwargs: Any,
    ) -> bool:
        if not kwargs:
            return False

        self._file_log_manager.cache_log(
            message=kwargs.get(
                "message",
                "",
            ),
            log_level=_logging.WARNING
        )

        return True

    def read_system_console_argument_string(
        self
    ) -> str:
        return "-".join(
            _sys.argv[1:]
        )

    def log_shutdown(
        self,
    ) -> bool:
        self._log_manager.shutdown()

        return True
