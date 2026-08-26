from __future__ import annotations

from typing import Any

__all__ = (
    "PersistentCacheDatabasManager"
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

class PersistentCacheDatabasManager:
    __slots__ = (
        "_import_manager",
        "_database_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._import_manager = (
            _ImportManager.read_singleton(
                _ImportManager
            )
        )
        self._database_manager = (
            _ImportManager.read_singleton(
                _DatabaseManager
            )
        )

    def read_key_path(self, key_path: Any) -> Any:
        return "-".join(
            (
                *self._database_manager.read_root_key_path(),
                key_path,
            )
        )

    def read_many_values(
        self,
        key_paths: Any
    ) -> Any:
        values = []
        for key_path in key_paths:
            values.append(self.read_key_path(key_path))

        result: Any = (
            self._import_manager.read_many_values_via_disk_cache(
                key_paths=values,
            )
        ) or {}

        return result

    def read_all_values(
        self,
        **kwargs: Any,
    ) -> dict[str, Any]:
        result: dict[str, Any] = (
            self._import_manager.read_all_values_via_disk_cache()
        ) or {}

        return result

    def write_many_values(
        self,
        values: Any
    ) -> bool:
        data = {}
        for key_path, value in values.items():
            data[self.read_key_path(key_path)] = value

        self._import_manager.write_many_values_via_disk_cache(
            values=data,
        )

        return True

    def read_configuration_workspace_file(
        self,
        accessibility_type: str,
        path: str,
    ) -> Any:
        key_path = f"configuration-workspace-raw-{accessibility_type}-{path}-value"
        data: Any = self.read_many_values(
            (key_path,)
        )

        return data.get(
            self.read_key_path(
                key_path
            ), {}
        ) or {}

    def write_configuration_workspace_file(
        self,
        accessibility_type: str,
        path: str,
        values: Any,
    ) -> bool:
        key_path = f"configuration-workspace-raw-{accessibility_type}-{path}-value"
        self.write_many_values(
            { key_path: values }
        )

        return True

    def read_configuration_workspace_metadata(
        self,
        accessibility_type: str,
        path: str,
    ) -> Any:
        key_path = (
            "configuration-workspace-raw"
            f"-{accessibility_type}-{path}-metadata-value"
        )
        data: Any = self.read_many_values(
            (key_path,)
        )

        return data.get(
            self.read_key_path(
                key_path
            ), {}
        ) or {}

    def write_configuration_workspace_metadata(
        self,
        accessibility_type: str,
        path: str,
        values: Any,
    ) -> bool:
        key_path = (
            "configuration-workspace-raw"
            f"-{accessibility_type}-{path}-metadata-value"
        )
        self.write_many_values(
            { key_path: values }
        )

        return True

    def read_configuration_workspace_data(
        self,
        accessibility_type: str,
        path: str,
    ) -> Any:
        key_path = f"configuration-workspace-raw-{accessibility_type}-{path}-data-value"
        data: Any = self.read_many_values(
            (key_path,)
        )

        return data.get(
            self.read_key_path(
                key_path
            ), {}
        ) or {}

    def write_configuration_workspace_data(
        self,
        accessibility_type: str,
        path: str,
        values: Any,
    ) -> bool:
        key_path = f"configuration-workspace-raw-{accessibility_type}-{path}-data-value"
        self.write_many_values(
            { key_path: values }
        )

        return True

    def read_configuration_workspace_file_count(
        self,
        accessibility_type: str,
    ) -> int:
        key_path = f"configuration-workspace-raw-count-{accessibility_type}-value"

        data: Any = self.read_many_values(
            (key_path,)
        )

        return data.get(
            self.read_key_path(
                key_path
            ), 0
        ) or 0

    def write_configuration_workspace_file_count(
        self,
        accessibility_type: str,
        value: int
    ) -> bool:
        key_path = f"configuration-workspace-raw-count-{accessibility_type}-value"

        self.write_many_values(
            { key_path: value }
        )

        return True

    def read_merged_configuration_workspace_data(
        self,
    ) -> Any:
        key_path = "configuration-workspace-data"

        data: Any = self.read_many_values(
            (key_path,)
        )

        return data.get(
            self.read_key_path(
                key_path
            ), {}
        ) or {}

    def write_merged_configuration_workspace_data(
        self,
        value: Any
    ) -> bool:
        key_path = "configuration-workspace-data"

        self.write_many_values(
            { key_path: value }
        )

        return True


    def read_refresh_data(
        self,
    ) -> Any:
        key_path = "refresh-data"

        data: Any = self.read_many_values(
            (key_path,)
        )

        return data.get(
            self.read_key_path(
                key_path
            ), {}
        ) or {}

    def write_refresh_data(
        self,
        value: Any
    ) -> bool:
        key_path = "refresh-data"

        self.write_many_values(
            { key_path: value }
        )

        return True
