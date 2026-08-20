from __future__ import annotations

from typing import Any

__all__ = (
    "CommandAboutManager"
)

_metadata: Any = None
_TaskManager: Any = None
_ImportManager: Any = None
_CommandStorageManager: Any = None


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _metadata
    global _TaskManager
    global _ImportManager
    global _CommandStorageManager

    from importlib import metadata

    from ..library import (
        command_storage_manager,
        import_manager,
        task_manager,
    )

    _metadata = (
        metadata
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

class CommandAboutManager:
    __slots__ = (
        "_command_storage_manager",
        "_task_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._command_storage_manager = _ImportManager.get_singleton(
            _CommandStorageManager
        )

        self._task_manager = (
            _ImportManager.get_singleton(
                _TaskManager
            )
        )

        self._command_storage_manager.add_commands((
            (
                self._task_manager.setup_command_name("about_version"),
                self.run_command_about_version,
            ),
            (
                self._task_manager.setup_command_name("about_me"),
                self.run_command_about_me,
            ),
        ))

    def run_command_about_version(self, **kwargs: Any) -> bool:
        print(
            _metadata
                .version('qlogicae-logis')
        )

        return True

    def run_command_about_me(self, **kwargs: Any) -> bool:

        return True
