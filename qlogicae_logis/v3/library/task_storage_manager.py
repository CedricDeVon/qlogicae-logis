from __future__ import annotations

from typing import Any

__all__ = (
    "TaskStorageManager"
)

_ImportManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _ImportManager

    from ..library import (
        import_manager,
    )

    _ImportManager = (
        import_manager
            .ImportManager
    )

    _handle_dynamic_imports = lambda: None

class TaskStorageManager:
    __slots__ = (
        "_tasks",
        "_import_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._tasks: dict[str, Any] = {}
        self._import_manager = (
            _ImportManager.read_singleton(
                _ImportManager
            )
        )

    def read_tasks(self) -> dict[str, Any]:
        return self._tasks

    def read_task(self, name: str) -> Any:
        return  self._tasks[name]

    def write_task(self, name: str, value: dict[str, Any]) -> None:
        self._tasks[name] = value

    def write_tasks(self, value: dict[str, Any]) -> None:
        self._tasks = value

    def remove_task(self, name: str) -> bool:
        del self._tasks[name]

        return True

    def is_executed(
        self,
        label: str = "",
    ) -> bool:
        key: str = f"{label}"
        value: bool = self._tasks.get(key, False)
        self._tasks[key] = True

        return value
