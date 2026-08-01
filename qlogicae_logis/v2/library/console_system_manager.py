from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    pass

_Path: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _Path

    from pathlib import Path

    _Path = Path

    _handle_dynamic_imports = lambda: None


class ConsoleSystemManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()

    @property
    def current_executing_script_filesystem_path(self) -> str:
        return f"{_Path(__file__).resolve()}"
