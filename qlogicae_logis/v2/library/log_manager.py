from __future__ import annotations

from typing import Any

_sys: Any = None
_LogOptions: Any = None
_LogManager: Any = None
_FileLogManager: Any = None
_DatabaseManager: Any = None
_SingletonManager: Any = None
_CorFileLogManager: Any = None
_CorConsoleLogManager: Any = None
_CommandUtilityManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _sys
    global _LogOptions
    global _LogManager
    global _FileLogManager
    global _DatabaseManager
    global _SingletonManager
    global _CorFileLogManager
    global _CorConsoleLogManager
    global _CommandUtilityManager

    import sys

    from qlogicae_cor.v1.library import (
        console_log_manager as cor_console_log_manager,
    )
    from qlogicae_cor.v1.library import (
        file_log_manager,
        log_manager,
        log_options,
        singleton_manager,
    )
    from qlogicae_cor.v1.library import (
        file_log_manager as cor_file_log_manager,
    )

    from qlogicae_logis.v2.library import (
        command_utility_manager,
        database_manager,
    )

    _sys = sys
    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _DatabaseManager = (
        database_manager.DatabaseManager
    )
    _CorConsoleLogManager = (
        cor_console_log_manager.ConsoleLogManager
    )
    _CorFileLogManager = (
        cor_file_log_manager.FileLogManager
    )
    _CommandUtilityManager = (
        command_utility_manager.CommandUtilityManager
    )
    _LogOptions = (
        log_options.LogOptions
    )
    _FileLogManager = (
        file_log_manager.FileLogManager
    )
    _LogManager = (
        log_manager.LogManager
    )

    _handle_dynamic_imports = lambda: None

class LogManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()

    def run_command_log_setup(self) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        workspace_data_log_default_file_output_is_enabled_value = (
            database_manager.workspace_data_log_default_file_output_is_enabled_value
        )
        workspace_data_log_is_enabled_value = (
            database_manager.workspace_data_log_is_enabled_value
        )
        workspace_data_log_is_enabled_override = (
            database_manager.workspace_data_log_is_enabled_override
        )
        workspace_data_log_is_verbose_value = (
            database_manager.workspace_data_log_is_verbose_value
        )
        workspace_data_log_is_verbose_override = (
            database_manager.workspace_data_log_is_verbose_override
        )
        workspace_data_log_console_is_enabled_value = (
            database_manager.workspace_data_log_console_is_enabled_value
        )
        workspace_data_log_console_is_verbose_value = (
            database_manager.workspace_data_log_console_is_verbose_value
        )
        workspace_data_log_file_is_enabled_value = (
            database_manager.workspace_data_log_file_is_enabled_value
        )
        workspace_data_log_file_is_verbose_value = (
            database_manager.workspace_data_log_file_is_verbose_value
        )
        workspace_data_log_file_targets = (
            database_manager.workspace_data_log_file_targets,
        )

        self.setup_log_console_options(
            is_enabled=workspace_data_log_is_enabled_value
            if workspace_data_log_is_enabled_override
            else workspace_data_log_console_is_enabled_value,
            is_verbose_enabled=workspace_data_log_is_verbose_value
            if workspace_data_log_is_verbose_override
            else (workspace_data_log_console_is_verbose_value),
        )
        self.setup_log_file_options(
            is_enabled=workspace_data_log_is_enabled_value
            if workspace_data_log_is_enabled_override
            else workspace_data_log_file_is_enabled_value,
            is_verbose_enabled=workspace_data_log_is_verbose_value
            if workspace_data_log_is_verbose_override
            else (workspace_data_log_file_is_verbose_value),
        )
        self.setup_log_file_outputs(
            database_manager.root_filesystem_path,
            workspace_data_log_file_targets,
            (
                workspace_data_log_is_enabled_value
                if workspace_data_log_is_enabled_override
                else workspace_data_log_file_is_enabled_value
            ),
            workspace_data_log_default_file_output_is_enabled_value
        )

        return True

    def log_execution_start(self) -> bool:
        _SingletonManager.get_singleton(
            _FileLogManager
        ).log_info(
            self.log_format(
                "start",
                3
            )
        )

        return True

    def log_execution_complete(self) -> bool:
        _SingletonManager.get_singleton(
            _FileLogManager
        ).log_info(
            self.log_format(
                "complete",
                3
            )
        )

        return True

    def file_log_info(self, content: Any) -> bool:
        _SingletonManager.get_singleton(
            _FileLogManager
        ).log_info(
            self.log_format(
                content,
                2
            )
        )

        return True

    def full_log_warning(self, content: Any) -> bool:
        _SingletonManager.get_singleton(
            _LogManager
        ).log_warning(
            self.log_format(
                content,
                2
            )
        )

        return True

    def log_format(self, content: Any, level: int) -> str:
        return f"'{_sys._getframe(level).f_code.co_name}' - {content}"


    def setup_log_console_options(
        self,
        is_enabled: bool,
        is_verbose_enabled: bool,
    ) -> bool:
        _SingletonManager.get_singleton(
            _CorConsoleLogManager
        ).options = _LogOptions(
            is_enabled=is_enabled,
            is_verbose_enabled=is_verbose_enabled
        )

        return True

    def setup_log_file_options(
        self,
        is_enabled: bool,
        is_verbose_enabled: bool,
    ) -> bool:
        _SingletonManager.get_singleton(
            _CorFileLogManager
        ).options = _LogOptions(
            is_enabled=is_enabled,
            is_verbose_enabled=is_verbose_enabled
        )

        return True

    def setup_log_file_outputs(
        self,
        root_filesystem_path: Any,
        target_filesystem_paths: Any,
        is_file_output_enabled: bool,
        is_default_enabled: bool,
    ) -> bool:
        cor_file_log_manager = _SingletonManager.get_singleton(
            _CorFileLogManager
        )

        log_file_outputs = []
        for filesystem_path in target_filesystem_paths:
            if filesystem_path and "filesystem-path" in filesystem_path:
                log_file_outputs.append(
                    filesystem_path["filesystem-path"]
                )

        if is_default_enabled:
            log_file_outputs = [
                *log_file_outputs,
                self.setup_default_log_filesystem_paths(
                    root_filesystem_path
                )
            ]

        if is_file_output_enabled:
            for log_file_output in log_file_outputs:
                cor_file_log_manager.add_file_output(
                    log_file_output
                )

        return True

    def setup_default_log_filesystem_paths(
        self,
        root_filesystem_path: str,
    ) -> str:
        return (
            f"{
                _SingletonManager.get_singleton(
                    _CommandUtilityManager
                ).setup_default_log_output_filesystem_path()
            }"
        )

    def shutdown(self) -> bool:
        _SingletonManager.get_singleton(
            _LogManager
        ).shutdown()

        return True
