from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    pass

_SingletonManager: Any = None
_ValueCacheManager: Any = None
_TimeManager: Any = None
_SystemManager: Any = None
_TargetCacheValue: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _SingletonManager
    global _ValueCacheManager
    global _TimeManager
    global _SystemManager
    global _TargetCacheValue

    from qlogicae_cor.v1.library import (
        singleton_manager,
        system_manager,
        target_cache_value,
        time_manager,
        value_cache_manager,
    )

    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _ValueCacheManager = (
        value_cache_manager.ValueCacheManager
    )
    _TimeManager = (
        time_manager.TimeManager
    )
    _SystemManager = (
        system_manager.SystemManager
    )
    _TargetCacheValue = (
        target_cache_value.TargetCacheValue
    )

    _handle_dynamic_imports = lambda: None


class ConsoleDatabaseManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()

    @property
    def timestamp_setup_execution_start(self) -> int:
        result: int = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            ("timestamp_setup_execution_start",),
            output_type=_TargetCacheValue.DEFINED,
        )

        return result

    def setup_timestamp_setup_execution_start(self) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            ("timestamp_setup_execution_start",),
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
            ("timestamp_setup_execution_complete",),
            output_type=_TargetCacheValue.DEFINED,
        )

        return result

    def setup_timestamp_setup_execution_complete(self) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            ("timestamp_setup_execution_complete",),
            _SingletonManager.get_singleton(
                _TimeManager
            ).current_nanosecond,
            output_type=_TargetCacheValue.DEFINED,
        )


    @property
    def current_root_workspace_filesystem_path(self) -> str:
        result: str = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            ("current_root_workspace_filesystem_path",),
            output_type=_TargetCacheValue.FOLDER_PATH,
        )

        return result

    def setup_current_root_workspace_filesystem_path(self) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            ("current_root_workspace_filesystem_path",),
            _SingletonManager.get_singleton(
                _SystemManager
            ).current_executing_console_filesystem_path,
            output_type=_TargetCacheValue.FOLDER_PATH,
        )

    @property
    def current_executing_script_filesystem_path(self) -> str:
        result: str = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            ("current_executing_script_filesystem_path",),
            output_type=_TargetCacheValue.FILE_PATH,
        )

        return result

    @current_executing_script_filesystem_path.setter
    def current_executing_script_filesystem_path(self, value: str) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            ("current_executing_script_filesystem_path",),
            value,
            output_type=_TargetCacheValue.FILE_PATH,
        )


    @property
    def initial_executing_console_filesystem_path(self) -> str:
        result: str = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            ("initial_executing_console_filesystem_path",),
            output_type=_TargetCacheValue.FOLDER_PATH,
        )

        return result

    @initial_executing_console_filesystem_path.setter
    def initial_executing_console_filesystem_path(self, value: str) -> None:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).set_one_value(
            ("initial_executing_console_filesystem_path",),
            value,
            output_type=_TargetCacheValue.FOLDER_PATH,
        )


    @property
    def previous_executing_console_filesystem_path(self) -> str:
        result: str = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            ("previous_executing_console_filesystem_path",),
            output_type=_TargetCacheValue.FOLDER_PATH,
        )

        return result

    @previous_executing_console_filesystem_path.setter
    def previous_executing_console_filesystem_path(self, value: str) -> None:
        _value_cache_manager = _SingletonManager.get_singleton(
            _ValueCacheManager
        )

        _value_cache_manager.set_one_value(
            ("previous_executing_console_filesystem_path",),
            value,
            output_type=_TargetCacheValue.FOLDER_PATH,
        )


    @property
    def current_executing_console_filesystem_path(self) -> str:
        result: str = _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            ("current_executing_console_filesystem_path",),
            output_type=_TargetCacheValue.FOLDER_PATH,
        )

        return result

    @current_executing_console_filesystem_path.setter
    def current_executing_console_filesystem_path(self, value: str) -> None:
        _value_cache_manager = _SingletonManager.get_singleton(
            _ValueCacheManager
        )

        _value_cache_manager.set_one_value(
            ("current_executing_console_filesystem_path",),
            value,
            output_type=_TargetCacheValue.FOLDER_PATH,
        )


    @property
    def workspace_data(self) -> Any:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            ("workspace", "data",),
            output_type=_TargetCacheValue.DEFINED,
        )

    @property
    def workspace_metadata(self) -> Any:
        _SingletonManager.get_singleton(
            _ValueCacheManager
        ).get_one_value(
            ("workspace", "metadata",),
            output_type=_TargetCacheValue.DEFINED,
        )


