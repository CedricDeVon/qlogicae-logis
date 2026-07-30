import sys
from pympler import asizeof

from qlogicae_logis.v1.cli_command_manager import CliCommandManager
from qlogicae_logis.v1.cli_command_manager_configurations import (
    CliCommandManagerConfigurations
)
from qlogicae_logis.v1.cli_display_manager import CliDisplayManager
from qlogicae_logis.v1.cli_display_manager_configurations import (
    CliDisplayManagerConfigurations,
)
from qlogicae_logis.v1.cli_manager import CliManager
from qlogicae_logis.v1.cli_manager_configurations import (
    CliManagerConfigurations,
)
from qlogicae_logis.v1.console_log_manager import ConsoleLogManager
from qlogicae_logis.v1.console_log_manager_configurations import (
    ConsoleLogManagerConfigurations,
)
from qlogicae_logis.v1.enum_conversion_output_enum_manager import (
    EnumConversionOutputEnumManager,
)
from qlogicae_logis.v1.enum_conversion_output_enum_manager_configurations import (
    EnumConversionOutputEnumManagerConfigurations,
)
from qlogicae_logis.v1.file_io_manager import FileIoManager
from qlogicae_logis.v1.file_io_manager_configurations import (
    FileIoManagerConfigurations,
)
from qlogicae_logis.v1.file_log_manager import FileLogManager
from qlogicae_logis.v1.file_log_manager_configurations import (
    FileLogManagerConfigurations,
)
from qlogicae_logis.v1.filesystem_compression_manager import (
    FilesystemCompressionManager,
)
from qlogicae_logis.v1.filesystem_compression_manager_configurations import (
    FilesystemCompressionManagerConfigurations,
)
from qlogicae_logis.v1.filesystem_manager import FileSystemManager
from qlogicae_logis.v1.filesystem_manager_configurations import (
    FileSystemManagerConfigurations,
)
from qlogicae_logis.v1.json_file_io_manager import JsonFileIoManager
from qlogicae_logis.v1.json_file_io_manager_configurations import (
    JsonFileIoManagerConfigurations,
)
from qlogicae_logis.v1.json_manager import JsonManager
from qlogicae_logis.v1.json_manager_configurations import (
    JsonManagerConfigurations,
)
from qlogicae_logis.v1.json_text_manager import JsonTextManager
from qlogicae_logis.v1.json_text_manager_configurations import (
    JsonTextManagerConfigurations,
)
from qlogicae_logis.v1.log_manager import LogManager
from qlogicae_logis.v1.log_manager_configurations import (
    LogManagerConfigurations,
)
from qlogicae_logis.v1.log_options_manager import LogOptionsManager
from qlogicae_logis.v1.log_options_manager_configurations import (
    LogOptionsManagerConfigurations,
)
from qlogicae_logis.v1.macros_manager import MacrosManager
from qlogicae_logis.v1.macros_manager_configurations import (
    MacrosManagerConfigurations,
)
from qlogicae_logis.v1.memory_allocation_benchmark_manager import (
    MemoryAllocationBenchmarkManager,
)
from qlogicae_logis.v1.memory_allocation_benchmark_manager_configurations import (
    MemoryAllocationBenchmarkManagerConfigurations,
)
from qlogicae_logis.v1.object_memory_benchmark_manager import (
    ObjectMemoryBenchmarkManager,
)
from qlogicae_logis.v1.object_memory_benchmark_manager_configurations import (
    ObjectMemoryBenchmarkManagerConfigurations,
)
from qlogicae_logis.v1.object_merge_manager import ObjectMergeManager
from qlogicae_logis.v1.object_merge_manager_configurations import (
    ObjectMergeManagerConfigurations,
)
from qlogicae_logis.v1.placeholder_value_manager import (
    PlaceholderValueManager,
)
from qlogicae_logis.v1.placeholder_value_manager_configurations import (
    PlaceholderValueManagerConfigurations,
)
from qlogicae_logis.v1.script_process_enum_manager import (
    ScriptProcessEnumManager,
)
from qlogicae_logis.v1.script_process_enum_manager_configurations import (
    ScriptProcessEnumManagerConfigurations,
)
from qlogicae_logis.v1.script_process_manager import ScriptProcessManager
from qlogicae_logis.v1.script_process_manager_configurations import (
    ScriptProcessManagerConfigurations,
)
from qlogicae_logis.v1.system_manager import SystemManager
from qlogicae_logis.v1.system_manager_configurations import (
    SystemManagerConfigurations,
)
from qlogicae_logis.v1.text_encoding_manager import TextEncodingManager
from qlogicae_logis.v1.text_encoding_manager_configurations import (
    TextEncodingManagerConfigurations,
)
from qlogicae_logis.v1.text_file_io_manager import TextFileIoManager
from qlogicae_logis.v1.text_file_io_manager_configurations import (
    TextFileIoManagerConfigurations,
)
from qlogicae_logis.v1.text_manager import TextManager
from qlogicae_logis.v1.text_manager_configurations import (
    TextManagerConfigurations,
)
from qlogicae_logis.v1.time_manager import TimeManager
from qlogicae_logis.v1.time_manager_configurations import (
    TimeManagerConfigurations,
)
from qlogicae_logis.v1.time_unit_enum_manager import (
    TimeUnitEnumManager,
)
from qlogicae_logis.v1.time_unit_enum_manager_configurations import (
    TimeUnitEnumManagerConfigurations,
)
from qlogicae_logis.v1.time_zone_enum_manager import (
    TimeZoneEnumManager,
)
from qlogicae_logis.v1.time_zone_enum_manager_configurations import (
    TimeZoneEnumManagerConfigurations,
)
from qlogicae_logis.v1.timer_manager import TimerManager
from qlogicae_logis.v1.timer_manager_configurations import (
    TimerManagerConfigurations,
)
from qlogicae_logis.v1.timestamp_manager import TimestampManager
from qlogicae_logis.v1.timestamp_manager_configurations import (
    TimestampManagerConfigurations,
)
from qlogicae_logis.v1.toml_file_io_manager import TomlFileIoManager
from qlogicae_logis.v1.toml_file_io_manager_configurations import (
    TomlFileIoManagerConfigurations,
)
from qlogicae_logis.v1.toml_manager import TomlManager
from qlogicae_logis.v1.toml_manager_configurations import (
    TomlManagerConfigurations,
)
from qlogicae_logis.v1.toml_text_manager import TomlTextManager
from qlogicae_logis.v1.toml_text_manager_configurations import (
    TomlTextManagerConfigurations,
)
from qlogicae_logis.v1.value_cache_manager import ValueCacheManager
from qlogicae_logis.v1.value_cache_manager_configurations import (
    ValueCacheManagerConfigurations,
)
from qlogicae_logis.v1.value_cache_storage_manager import (
    ValueCacheStorageManager,
)
from qlogicae_logis.v1.value_cache_storage_manager_configurations import (
    ValueCacheStorageManagerConfigurations,
)
from qlogicae_logis.v1.workspace_export_manager import (
    WorkspaceExportManager,
)
from qlogicae_logis.v1.workspace_export_manager_configurations import (
    WorkspaceExportManagerConfigurations,
)
from qlogicae_logis.v1.workspace_filesystem_manager import (
    WorkspaceFilesystemManager,
)
from qlogicae_logis.v1.workspace_filesystem_manager_configurations import (
    WorkspaceFilesystemManagerConfigurations,
)
from qlogicae_logis.v1.workspace_log_manager import WorkspaceLogManager
from qlogicae_logis.v1.workspace_log_manager_configurations import (
    WorkspaceLogManagerConfigurations,
)
from qlogicae_logis.v1.workspace_macros_manager import (
    WorkspaceMacrosManager,
)
from qlogicae_logis.v1.workspace_macros_manager_configurations import (
    WorkspaceMacrosManagerConfigurations,
)
from qlogicae_logis.v1.workspace_manager import WorkspaceManager
from qlogicae_logis.v1.workspace_manager_configurations import (
    WorkspaceManagerConfigurations,
)
from qlogicae_logis.v1.workspace_script_manager import (
    WorkspaceScriptManager,
)
from qlogicae_logis.v1.workspace_script_manager_configurations import (
    WorkspaceScriptManagerConfigurations,
)
from qlogicae_logis.v1.workspace_system_manager import (
    WorkspaceSystemManager,
)
from qlogicae_logis.v1.workspace_system_manager_configurations import (
    WorkspaceSystemManagerConfigurations,
)
from qlogicae_logis.v1.workspace_value_cache_manager import (
    WorkspaceValueCacheManager,
)
from qlogicae_logis.v1.workspace_value_cache_manager_configurations import (
    WorkspaceValueCacheManagerConfigurations,
)
from qlogicae_logis.v1.yaml_file_io_manager import YamlFileIoManager
from qlogicae_logis.v1.yaml_file_io_manager_configurations import (
    YamlFileIoManagerConfigurations,
)
from qlogicae_logis.v1.yaml_manager import YamlManager
from qlogicae_logis.v1.yaml_manager_configurations import (
    YamlManagerConfigurations,
)
from qlogicae_logis.v1.yaml_text_manager import YamlTextManager
from qlogicae_logis.v1.yaml_text_manager_configurations import (
    YamlTextManagerConfigurations,
)

total_memory_usage = 0

def get_memory_usage(name: str, value: object) -> None:
    size = asizeof.asizeof(value)

    print(f"{name:<50} {size:>8} bytes")

    return size


total_memory_usage += get_memory_usage("CliCommandManager", CliCommandManager())
total_memory_usage += get_memory_usage(
    "CliCommandManagerConfigurations",
    CliCommandManagerConfigurations(),
)

total_memory_usage += get_memory_usage("CliDisplayManager", CliDisplayManager())
total_memory_usage += get_memory_usage(
    "CliDisplayManagerConfigurations",
    CliDisplayManagerConfigurations(),
)

total_memory_usage += get_memory_usage("CliManager", CliManager())
total_memory_usage += get_memory_usage(
    "CliManagerConfigurations",
    CliManagerConfigurations(),
)

total_memory_usage += get_memory_usage("ConsoleLogManager", ConsoleLogManager())
total_memory_usage += get_memory_usage(
    "ConsoleLogManagerConfigurations",
    ConsoleLogManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "EnumConversionOutputEnumManager",
    EnumConversionOutputEnumManager(),
)
total_memory_usage += get_memory_usage(
    "EnumConversionOutputEnumManagerConfigurations",
    EnumConversionOutputEnumManagerConfigurations(),
)

total_memory_usage += get_memory_usage("FileIoManager", FileIoManager())
total_memory_usage += get_memory_usage(
    "FileIoManagerConfigurations",
    FileIoManagerConfigurations(),
)

total_memory_usage += get_memory_usage("FileLogManager", FileLogManager())
total_memory_usage += get_memory_usage(
    "FileLogManagerConfigurations",
    FileLogManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "FilesystemCompressionManager",
    FilesystemCompressionManager(),
)
total_memory_usage += get_memory_usage(
    "FilesystemCompressionManagerConfigurations",
    FilesystemCompressionManagerConfigurations(),
)

total_memory_usage += get_memory_usage("FileSystemManager", FileSystemManager())
total_memory_usage += get_memory_usage(
    "FileSystemManagerConfigurations",
    FileSystemManagerConfigurations(),
)

total_memory_usage += get_memory_usage("JsonFileIoManager", JsonFileIoManager())
total_memory_usage += get_memory_usage(
    "JsonFileIoManagerConfigurations",
    JsonFileIoManagerConfigurations(),
)

total_memory_usage += get_memory_usage("JsonManager", JsonManager())
total_memory_usage += get_memory_usage(
    "JsonManagerConfigurations",
    JsonManagerConfigurations(),
)

total_memory_usage += get_memory_usage("JsonTextManager", JsonTextManager())
total_memory_usage += get_memory_usage(
    "JsonTextManagerConfigurations",
    JsonTextManagerConfigurations(),
)

total_memory_usage += get_memory_usage("LogManager", LogManager())
total_memory_usage += get_memory_usage(
    "LogManagerConfigurations",
    LogManagerConfigurations(),
)

total_memory_usage += get_memory_usage("LogOptionsManager", LogOptionsManager())
total_memory_usage += get_memory_usage(
    "LogOptionsManagerConfigurations",
    LogOptionsManagerConfigurations(),
)

total_memory_usage += get_memory_usage("MacrosManager", MacrosManager())
total_memory_usage += get_memory_usage(
    "MacrosManagerConfigurations",
    MacrosManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "MemoryAllocationBenchmarkManager",
    MemoryAllocationBenchmarkManager(),
)
total_memory_usage += get_memory_usage(
    "MemoryAllocationBenchmarkManagerConfigurations",
    MemoryAllocationBenchmarkManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "ObjectMemoryBenchmarkManager",
    ObjectMemoryBenchmarkManager(),
)
total_memory_usage += get_memory_usage(
    "ObjectMemoryBenchmarkManagerConfigurations",
    ObjectMemoryBenchmarkManagerConfigurations(),
)

total_memory_usage += get_memory_usage("ObjectMergeManager", ObjectMergeManager())
total_memory_usage += get_memory_usage(
    "ObjectMergeManagerConfigurations",
    ObjectMergeManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "PlaceholderValueManager",
    PlaceholderValueManager(),
)
total_memory_usage += get_memory_usage(
    "PlaceholderValueManagerConfigurations",
    PlaceholderValueManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "ScriptProcessEnumManager",
    ScriptProcessEnumManager(),
)
total_memory_usage += get_memory_usage(
    "ScriptProcessEnumManagerConfigurations",
    ScriptProcessEnumManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "ScriptProcessManager",
    ScriptProcessManager(),
)
total_memory_usage += get_memory_usage(
    "ScriptProcessManagerConfigurations",
    ScriptProcessManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "SystemManager",
    SystemManager(),
)
total_memory_usage += get_memory_usage(
    "SystemManagerConfigurations",
    SystemManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "TextEncodingManager",
    TextEncodingManager(),
)
total_memory_usage += get_memory_usage(
    "TextEncodingManagerConfigurations",
    TextEncodingManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "TextFileIoManager",
    TextFileIoManager(),
)
total_memory_usage += get_memory_usage(
    "TextFileIoManagerConfigurations",
    TextFileIoManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "TextManager",
    TextManager(),
)
total_memory_usage += get_memory_usage(
    "TextManagerConfigurations",
    TextManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "TimeManager",
    TimeManager(),
)
total_memory_usage += get_memory_usage(
    "TimeManagerConfigurations",
    TimeManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "TimeUnitEnumManager",
    TimeUnitEnumManager(),
)
total_memory_usage += get_memory_usage(
    "TimeUnitEnumManagerConfigurations",
    TimeUnitEnumManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "TimeZoneEnumManager",
    TimeZoneEnumManager(),
)
total_memory_usage += get_memory_usage(
    "TimeZoneEnumManagerConfigurations",
    TimeZoneEnumManagerConfigurations(),
)

total_memory_usage += get_memory_usage("TimerManager", TimerManager())
total_memory_usage += get_memory_usage(
    "TimerManagerConfigurations",
    TimerManagerConfigurations(),
)

total_memory_usage += get_memory_usage("TimestampManager", TimestampManager())
total_memory_usage += get_memory_usage(
    "TimestampManagerConfigurations",
    TimestampManagerConfigurations(),
)

total_memory_usage += get_memory_usage("TomlFileIoManager", TomlFileIoManager())
total_memory_usage += get_memory_usage(
    "TomlFileIoManagerConfigurations",
    TomlFileIoManagerConfigurations(),
)

total_memory_usage += get_memory_usage("TomlManager", TomlManager())
total_memory_usage += get_memory_usage(
    "TomlManagerConfigurations",
    TomlManagerConfigurations(),
)

total_memory_usage += get_memory_usage("TomlTextManager", TomlTextManager())
total_memory_usage += get_memory_usage(
    "TomlTextManagerConfigurations",
    TomlTextManagerConfigurations(),
)

total_memory_usage += get_memory_usage("ValueCacheManager", ValueCacheManager())
total_memory_usage += get_memory_usage(
    "ValueCacheManagerConfigurations",
    ValueCacheManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "ValueCacheStorageManager",
    ValueCacheStorageManager(),
)
total_memory_usage += get_memory_usage(
    "ValueCacheStorageManagerConfigurations",
    ValueCacheStorageManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "WorkspaceExportManager",
    WorkspaceExportManager(),
)
total_memory_usage += get_memory_usage(
    "WorkspaceExportManagerConfigurations",
    WorkspaceExportManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "WorkspaceFilesystemManager",
    WorkspaceFilesystemManager(),
)
total_memory_usage += get_memory_usage(
    "WorkspaceFilesystemManagerConfigurations",
    WorkspaceFilesystemManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "WorkspaceLogManager",
    WorkspaceLogManager(),
)
total_memory_usage += get_memory_usage(
    "WorkspaceLogManagerConfigurations",
    WorkspaceLogManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "WorkspaceMacrosManager",
    WorkspaceMacrosManager(),
)
total_memory_usage += get_memory_usage(
    "WorkspaceMacrosManagerConfigurations",
    WorkspaceMacrosManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "WorkspaceManager",
    WorkspaceManager(),
)
total_memory_usage += get_memory_usage(
    "WorkspaceManagerConfigurations",
    WorkspaceManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "WorkspaceScriptManager",
    WorkspaceScriptManager(),
)
total_memory_usage += get_memory_usage(
    "WorkspaceScriptManagerConfigurations",
    WorkspaceScriptManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "WorkspaceSystemManager",
    WorkspaceSystemManager(),
)
total_memory_usage += get_memory_usage(
    "WorkspaceSystemManagerConfigurations",
    WorkspaceSystemManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "WorkspaceValueCacheManager",
    WorkspaceValueCacheManager(),
)
total_memory_usage += get_memory_usage(
    "WorkspaceValueCacheManagerConfigurations",
    WorkspaceValueCacheManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "YamlFileIoManager",
    YamlFileIoManager(),
)
total_memory_usage += get_memory_usage(
    "YamlFileIoManagerConfigurations",
    YamlFileIoManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "YamlManager",
    YamlManager(),
)
total_memory_usage += get_memory_usage(
    "YamlManagerConfigurations",
    YamlManagerConfigurations(),
)

total_memory_usage += get_memory_usage(
    "YamlTextManager",
    YamlTextManager(),
)
total_memory_usage += get_memory_usage(
    "YamlTextManagerConfigurations",
    YamlTextManagerConfigurations(),
)


print(
    f"{total_memory_usage} bytes"
)
