from __future__ import annotations

from typing import Any


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports

    _handle_dynamic_imports = lambda: None

class CommandStorageManager:
    __slots__ = ("_commands")

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._commands: dict[str, Any] = {}

    @property
    def commands(self) -> dict[str, Any]:
        return self._commands

    @commands.setter
    def commands(self, value: dict[str, Any]) -> None:
        self._commands = value

    def add_command(self, name: str, callback: Any) -> bool:
        self._commands[name] = callback

        return True

    def run_command(self, name: str) -> bool:
        self._commands[name]()

        return True

    def get_command(self, name: str) -> Any:
        return  self._commands[name]

    def remove_command(self, name: str) -> bool:
        del self._commands[name]

        return True

