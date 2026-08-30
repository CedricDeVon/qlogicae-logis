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

    def read_key_path(self, key_path: Any) -> str:
        if not key_path:
            return ""

        return "-".join(
            (
                *self._database_manager.read_root_key_path(),
                key_path,
            )
        )

    def read_many_values(
        self,
        key_paths: tuple[str, ...]
    ) -> Any:
        if not key_paths or len(key_paths) < 1:
            return {}

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
    ) -> dict[str, Any]:
        result: dict[str, Any] = (
            self._import_manager.read_all_values_via_disk_cache()
        ) or {}

        return result

    def write_many_values(
        self,
        values: dict[str, Any]
    ) -> bool:
        if not values or len(values) < 1:
            return False

        data = {}
        for key_path, value in values.items():
            data[self.read_key_path(key_path)] = value

        self._import_manager.write_many_values_via_disk_cache(
            values=data,
        )

        return True

    def read_configuration_workspace_key_path(
        self,
        **kwargs: Any
    ) -> str:
        if not kwargs:
            return ""

        value = kwargs.get("value", "")

        return (
            f"configuration-workspace-{value}"
        )

    # def read_configuration_workspace_raw_value_key_path(
    #     self,
    #     **kwargs: Any,
    # ) -> str:
    #     if not kwargs:
    #         return ""

    #     accessibility_type = kwargs.get("accessibility_type", "")
    #     path = kwargs.get("path", "")

    #     return (
    #         self.read_configuration_workspace_key_path(
    #             value=f"raw-{accessibility_type}-{path}-value"
    #         )
    #     )

    def read_configuration_workspace_raw_count_value_key_path(
        self,
        **kwargs: Any,
    ) -> str:
        if not kwargs:
            return ""

        accessibility_type = kwargs.get("accessibility_type", "")

        return (
            self.read_configuration_workspace_key_path(
                value=f"raw-count-{accessibility_type}-value"
            )
        )

    def read_configuration_workspace_raw_metadata_value_key_path(
        self,
        **kwargs: Any,
    ) -> str:
        if not kwargs:
            return ""

        accessibility_type = kwargs.get("accessibility_type", "")
        path = kwargs.get("path", "")

        return (
            self.read_configuration_workspace_key_path(
                value=f"raw-{accessibility_type}-{path}-metadata-value"
            )
        )

    def read_configuration_workspace_data_value_key_path(
        self,
        **kwargs: Any,
    ) -> str:
        if not kwargs:
            return ""

        accessibility_type = kwargs.get("accessibility_type", "")
        path = kwargs.get("path", "")

        return (
            self.read_configuration_workspace_key_path(
                value=f"data-{accessibility_type}-{path}-value"
            )
        )

    def read_configuration_workspace_data_key_path(
        self,
    ) -> str:
        return (
            self.read_configuration_workspace_key_path(
                value="data"
            )
        )

    def read_refresh_data_key_path(
        self,
    ) -> str:
        return (
            "refresh-data"
        )

    # def read_configuration_workspace_file(
    #     self,
    #     accessibility_type: str,
    #     path: str,
    # ) -> Any:
    #     if not accessibility_type or not path:
    #         return {}

    #     key_path = (
    #         self.read_configuration_workspace_raw_value_key_path(
    #             accessibility_type=accessibility_type,
    #             path=path
    #         )
    #     )

    #     data: Any = self.read_many_values(
    #         (key_path,)
    #     )

    #     return data.get(
    #         self.read_key_path(
    #             key_path
    #         ), {}
    #     ) or {}

    # def write_configuration_workspace_file(
    #     self,
    #     accessibility_type: str,
    #     path: str,
    #     values: dict[str, Any],
    # ) -> bool:
    #     if not accessibility_type or not path or not values:
    #         return False

    #     key_path = (
    #         self.read_configuration_workspace_raw_value_key_path(
    #             accessibility_type=accessibility_type,
    #             path=path
    #         )
    #     )

    #     self.write_many_values(
    #         { key_path: values }
    #     )

    #     return True

    def read_configuration_workspace_metadata(
        self,
        accessibility_type: str,
        path: str,
    ) -> Any:
        if not accessibility_type or not path:
            return {}

        key_path = (
            self.read_configuration_workspace_raw_metadata_value_key_path(
                accessibility_type=accessibility_type,
                path=path
            )
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
        values: dict[str, Any],
    ) -> bool:
        if not accessibility_type or not path or not values:
            return False

        key_path = (
            self.read_configuration_workspace_raw_metadata_value_key_path(
                accessibility_type=accessibility_type,
                path=path
            )
        )
        self.write_many_values(
            { key_path: values }
        )

        return True

    def read_configuration_workspace_data(
        self,
        accessibility_type: str,
        path: str,
    ) -> dict[str, Any]:
        if not accessibility_type or not path:
            return {}

        key_path = (
            self.read_configuration_workspace_data_value_key_path(
                accessibility_type=accessibility_type,
                path=path
            )
        )
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
        values: dict[str, Any],
    ) -> bool:
        if not accessibility_type or not path or not values:
            return False

        key_path = (
            self.read_configuration_workspace_data_value_key_path(
                accessibility_type=accessibility_type,
                path=path
            )
        )
        self.write_many_values(
            { key_path: values }
        )

        return True

    def read_configuration_workspace_file_count(
        self,
        accessibility_type: str,
    ) -> int:
        if not accessibility_type:
            return 0

        key_path = (
            self.read_configuration_workspace_raw_count_value_key_path(
                accessibility_type=accessibility_type
            )
        )

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
        if not accessibility_type or not value:
            return False

        key_path = (
            self.read_configuration_workspace_raw_count_value_key_path(
                accessibility_type=accessibility_type
            )
        )

        self.write_many_values(
            { key_path: value }
        )

        return True

    def read_merged_configuration_workspace_data(
        self,
    ) -> Any:
        key_path = self.read_configuration_workspace_data_key_path()

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
        value: dict[str, Any]
    ) -> bool:
        if not value or len(value) < 1:
            return False

        key_path = self.read_configuration_workspace_data_key_path()

        self.write_many_values(
            { key_path: value }
        )

        return True

    # def read_refresh_data(
    #     self,
    # ) -> dict[str, Any]:
    #     key_path = self.read_refresh_data_key_path()

    #     data: dict[str, Any] = self.read_many_values(
    #         (key_path,)
    #     )

    #     return data.get(
    #         self.read_key_path(
    #             key_path
    #         ), {}
    #     ) or {}

    def write_refresh_data(
        self,
        value: dict[str, Any]
    ) -> bool:
        if not value or len(value) < 1:
            return False

        key_path = self.read_refresh_data_key_path()

        self.write_many_values(
            { key_path: value }
        )

        return True
