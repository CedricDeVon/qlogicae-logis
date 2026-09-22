from __future__ import annotations

from typing import Any

__all__ = (
    "CommandStorageManager"
)


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports

    _handle_dynamic_imports = lambda: None

class CommandStorageManager:
    __slots__ = ("_commands")

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._commands: dict[str, Any] = {}

    def read_command_name(
        self,
        value: str
    ) -> str:
        if not value:
            return ""

        return (
            f"command-{value.replace("_", "-")}"
        )

    def read_commands(self) -> dict[str, Any]:
        return self._commands

    def add_commands(self, items: Any) -> bool:
        if not items:
            return False

        for (name, callback) in items:
            if not name or not callback:
                continue

            self._commands[name] = callback

        return True

    def run_command(self, name: str) -> bool:
        if not name:
            return False

        self._commands[name]()

        return True
