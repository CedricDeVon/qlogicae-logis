from __future__ import annotations

from typing import Any

__all__ = (
    "CommandWorkflowManager"
)

_TaskManager: Any = None
_ImportManager: Any = None
_CommandStorageManager: Any = None


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _TaskManager
    global _ImportManager
    global _CommandStorageManager

    from ..library import (
        command_storage_manager,
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
    _CommandStorageManager = (
        command_storage_manager
            .CommandStorageManager
    )

    _handle_dynamic_imports = lambda: None

class CommandWorkflowManager:
    __slots__ = (
        "_command_storage_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._command_storage_manager = _ImportManager.get_singleton(
            _CommandStorageManager
        )

        self._command_storage_manager.add_commands()
