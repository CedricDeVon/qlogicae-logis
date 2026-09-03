from __future__ import annotations

__all__ = (
    "LogMessageStorageManager",
)

from typing import Any


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports

    _handle_dynamic_imports = lambda: None


class LogMessageStorageManager:
    __slots__ = (
        "_cache_values",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._cache_values: list[str] = []

    def write_one_cache_value(self, value: str) -> bool:
        if not value:
            return False

        self._cache_values.append(
            value
        )

        return True

    def read_all_string_formatted_cache_values(self) -> str:
        result: str = ""
        maximum_end_of_line_count: int = len(self._cache_values) - 1
        for index, value in enumerate(self._cache_values):
            if not value:
                continue

            result += f"{value}"
            if index < maximum_end_of_line_count:
                result += "\n"
            
        return result

    def clear_all_cache_values(self) -> bool:
        self._cache_values.clear()

        return True
