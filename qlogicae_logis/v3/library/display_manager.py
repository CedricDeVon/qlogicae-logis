from __future__ import annotations

from typing import Any

__all__ = (
    "DisplayManager"
)

_sys: Any = None
_Mapping: Any = None
_Sequence: Any = None
_TaskManager: Any = None
_ImportManager: Any = None
_DatabaseManager: Any = None
_CommandStorageManager: Any = None
_ValueCacheDatabaseManager: Any = None


def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _sys
    global _Mapping
    global _Sequence
    global _TaskManager
    global _ImportManager
    global _DatabaseManager
    global _CommandStorageManager
    global _ValueCacheDatabaseManager

    import sys
    from collections.abc import Mapping, Sequence

    from ..library import (
        database_manager,
        import_manager,
        task_manager,
        value_cache_database_manager,
    )

    _sys = sys
    _Mapping = Mapping
    _Sequence = Sequence
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
    _ValueCacheDatabaseManager = (
        value_cache_database_manager.ValueCacheDatabaseManager
    )

    _handle_dynamic_imports = lambda: None

class DisplayManager:
    __slots__ = (
        "_color_codes",
        "_import_manager",
        "_database_manager",
        "_special_characters",
        "_value_cache_database_manager",
    )

    def __init__(self) -> None:
        _handle_dynamic_imports()

        self._special_characters: tuple[str, ...] = (
            ":",
            "#",
            "{",
            "}",
            "[",
            "]",
            ",",
            "&",
            "*",
            "!",
            "|",
            ">",
            "'",
            '"',
            "%",
            "@",
            "`",
        )

        self._color_codes: dict[str, str] = {
            "none": "",
            "reset": "\x1b[0m",
            "black": "\x1b[30m",
            "red": "\x1b[31m",
            "green": "\x1b[32m",
            "yellow": "\x1b[33m",
            "blue": "\x1b[34m",
            "magenta": "\x1b[35m",
            "cyan": "\x1b[36m",
            "white": "\x1b[37m",
            "grey": "\x1b[90m",
            "bright-black": "\x1b[90m",
            "bright-red": "\x1b[91m",
            "bright-green": "\x1b[92m",
            "bright-yellow": "\x1b[93m",
            "bright-blue": "\x1b[94m",
            "bright-magenta": "\x1b[95m",
            "bright-cyan": "\x1b[96m",
            "bright-white": "\x1b[97m",
        }

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
        self._value_cache_database_manager = (
            _ImportManager.read_singleton(
                _ValueCacheDatabaseManager
            )
        )

    def color_key(self, value: str) -> str:
        return self.color_text(
            self.map_color_code(
                self._value_cache_database_manager
                    .read_configuration_workspace_data_display_console_style_base_1_value()
            ),
            value,
            self.map_color_code(
                self._value_cache_database_manager
                    .read_configuration_workspace_data_display_console_style_reset_value()
            ),
        )

    def color_value(self, value: str) -> str:
        return self.color_text(
            self.map_color_code(
                self._value_cache_database_manager
                    .read_configuration_workspace_data_display_console_style_highlight_1_value()
            ),
            value,
            self.map_color_code(
                self._value_cache_database_manager
                    .read_configuration_workspace_data_display_console_style_reset_value()
            ),
        )

    def color_tree(self, value: str) -> str:
        return self.color_text(
            self.map_color_code(
                self._value_cache_database_manager
                    .read_configuration_workspace_data_display_console_style_base_2_value()
            ),
            value,
            self.map_color_code(
                self._value_cache_database_manager
                    .read_configuration_workspace_data_display_console_style_reset_value()
            ),
        )

    def color_text(self, color: str, value: str, reset: str) -> str:
        return f"{color}{value}{reset}"

    def map_color_code(
        self,
        color: str,
    ) -> str:
        if not _sys.stdout.isatty() or not color:
            return ""

        return self._color_codes.get(
            color.lower(), ""
        ) or ""

    def display_highlight_value(
        self,
        **kwargs: Any,
    ) -> None:
        if not kwargs:
            return

        print(
            self.color_value(
                kwargs.get("value", "") or ""
            )
        )

    def display_tree_object(
        self,
        **kwargs: Any,
    ) -> None:
        if not kwargs:
            return

        maximum_depth: int | None = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_display_console_style_maximum_depth_value()
        )
        is_skipped: bool = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_display_console_style_is_skipped_value()
        )
        indent_count: int = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_display_console_style_indent_count_value()
        )
        vertical_space_count: int = (
            self._value_cache_database_manager
                .read_configuration_workspace_data_display_console_style_vertical_count_value()
        )

        value = kwargs.get("value")
        is_skipped = kwargs.get(
            "is_skipped",
            is_skipped,
        ) or is_skipped
        indent_count = kwargs.get(
            "indent_count",
            indent_count,
        ) or indent_count
        maximum_depth = kwargs.get(
            "maximum_depth",
            maximum_depth,
        ) or maximum_depth
        vertical_space_count = kwargs.get(
            "vertical_space_count",
            vertical_space_count,
        ) or vertical_space_count

        visited: set[int] = set()

        def scalar(value: Any) -> str:
            if value is None:
                return "null"

            if value is True:
                return "true"

            if value is False:
                return "false"

            if isinstance(value, str):
                if not value:
                    return "''"

                if "\n" in value:
                    return repr(value)

                if any(
                    character in value
                    for character in self._special_characters
                ):
                    return repr(value)

                return value

            if isinstance(value, bytes):
                return repr(value)

            if isinstance(value, (int, float)):
                return str(value)

            return repr(value)

        def is_set(value: Any) -> bool:
            return isinstance(
                value,
                (set, frozenset),
            )

        def is_sequence(value: Any) -> bool:
            return (
                isinstance(value, _Sequence)
                and not isinstance(
                    value,
                    (str, bytes, bytearray),
                )
            )

        def get_attributes(
            value: Any,
        ) -> dict[str, Any]:
            attributes: dict[str, Any] = {}

            if hasattr(value, "__dict__"):
                attributes.update(vars(value))

            for cls in type(value).__mro__:
                slots = getattr(
                    cls,
                    "__slots__",
                    (),
                )

                if isinstance(slots, str):
                    slots = (slots,)

                for name in slots:
                    if hasattr(value, name):
                        attributes[name] = getattr(
                            value,
                            name,
                        )

            return attributes

        # def is_container(value: Any) -> bool:
        #     return (
        #         isinstance(value, _Mapping)
        #         or is_sequence(value)
        #         or is_set(value)
        #         or bool(get_attributes(value))
        #     )

        def tree_prefix(
            prefixes: tuple[bool, ...],
        ) -> str:
            result = ""

            for has_next in prefixes:
                if has_next:
                    result += self.color_tree(
                        "│"
                        + " " * (indent_count - 1)
                    )
                else:
                    result += " " * indent_count

            return result

        def tree_branch(
            is_last: bool,
        ) -> str:
            return self.color_tree(
                "└── "
                if is_last
                else "├── "
            )

        def print_line(
            prefixes: tuple[bool, ...],
            is_last: bool,
            text: str,
            *,
            root: bool = False,
        ) -> None:
            if root:
                if is_skipped:
                    print(text)
                else:
                    input(text)

                return

            output = (
                tree_prefix(prefixes)
                + tree_branch(is_last)
                + text
            )

            if is_skipped:
                print(output)
            else:
                input(output)

        def print_spacing(
            prefixes: tuple[bool, ...],
        ) -> None:
            for _ in range(
                max(vertical_space_count, 0),
            ):
                print(
                    tree_prefix(prefixes)
                    + self.color_tree("│"),
                )

        def push_spacing(
            stack: list[
                tuple[
                    str,
                    Any,
                    int,
                    tuple[bool, ...],
                    bool,
                    str | None,
                ]
            ],
            prefixes: tuple[bool, ...],
        ) -> None:
            if vertical_space_count <= 0:
                return

            stack.append(
                (
                    "space",
                    None,
                    0,
                    prefixes,
                    True,
                    None,
                )
            )

        stack: list[
            tuple[
                str,
                Any,
                int,
                tuple[bool, ...],
                bool,
                str | None,
            ]
        ] = [
            (
                "render",
                value,
                0,
                (),
                True,
                None,
            )
        ]

        while stack:
            (
                action,
                current,
                depth,
                prefixes,
                is_last,
                label,
            ) = stack.pop()

            if action == "space":
                print_spacing(prefixes)
                continue

            if (
                maximum_depth is not None
                and depth > maximum_depth
            ):
                text = self.color_tree("...")

                if label is not None:
                    text = (
                        f"{label} "
                        f"{text}"
                    )

                print_line(
                    prefixes,
                    is_last,
                    text,
                )
                continue

            current_id = id(current)

            if current_id in visited:
                text = self.color_value(
                    f"'{type(current).__name__} "
                    "recursive'"
                )

                if label is not None:
                    text = (
                        f"{label} "
                        f"{text}"
                    )

                print_line(
                    prefixes,
                    is_last,
                    text,
                )
                continue

            if isinstance(current, _Mapping):
                visited.add(current_id)

                items = list(current.items())

                if not items:
                    text = self.color_value("{}")

                    if label is not None:
                        text = (
                            f"{label} "
                            f"{text}"
                        )

                    print_line(
                        prefixes,
                        is_last,
                        text,
                    )
                    continue

                if label is not None:
                    print_line(
                        prefixes,
                        is_last,
                        label,
                    )

                child_prefixes = (
                    prefixes
                    if depth == 0
                    else prefixes + (not is_last,)
                )

                for index in range(
                    len(items) - 1,
                    -1,
                    -1,
                ):
                    key, item = items[index]

                    child_is_last = (
                        index == len(items) - 1
                    )

                    key_text = self.color_key(
                        scalar(key),
                    )

                    if not child_is_last:
                        push_spacing(
                            stack,
                            child_prefixes,
                        )

                    stack.append(
                        (
                            "render",
                            item,
                            depth + 1,
                            child_prefixes,
                            child_is_last,
                            key_text,
                        )
                    )

                continue

            if is_sequence(current):
                visited.add(current_id)

                if not current:
                    text = self.color_value("[]")

                    if label is not None:
                        text = (
                            f"{label} "
                            f"{text}"
                        )

                    print_line(
                        prefixes,
                        is_last,
                        text,
                    )
                    continue

                if label is not None:
                    print_line(
                        prefixes,
                        is_last,
                        label,
                    )

                child_prefixes = (
                    prefixes
                    if depth == 0
                    else prefixes + (not is_last,)
                )

                items = list(current)

                for index in range(
                    len(items) - 1,
                    -1,
                    -1,
                ):
                    item = items[index]

                    child_is_last = (
                        index == len(items) - 1
                    )

                    if not child_is_last:
                        push_spacing(
                            stack,
                            child_prefixes,
                        )

                    stack.append(
                        (
                            "render",
                            item,
                            depth + 1,
                            child_prefixes,
                            child_is_last,
                            None,
                        )
                    )

                continue

            if is_set(current):
                visited.add(current_id)

                if not current:
                    text = self.color_value("set()")

                    if label is not None:
                        text = (
                            f"{label} "
                            f"{text}"
                        )

                    print_line(
                        prefixes,
                        is_last,
                        text,
                    )
                    continue

                if label is not None:
                    print_line(
                        prefixes,
                        is_last,
                        label,
                    )

                child_prefixes = (
                    prefixes
                    if depth == 0
                    else prefixes + (not is_last,)
                )

                items = list(current)

                for index in range(
                    len(items) - 1,
                    -1,
                    -1,
                ):
                    item = items[index]

                    child_is_last = (
                        index == len(items) - 1
                    )

                    if not child_is_last:
                        push_spacing(
                            stack,
                            child_prefixes,
                        )

                    stack.append(
                        (
                            "render",
                            item,
                            depth + 1,
                            child_prefixes,
                            child_is_last,
                            None,
                        )
                    )

                continue

            attributes = get_attributes(current)

            if attributes:
                visited.add(current_id)

                if label is not None:
                    print_line(
                        prefixes,
                        is_last,
                        label,
                    )

                child_prefixes = (
                    prefixes
                    if depth == 0
                    else prefixes + (not is_last,)
                )

                items = list(attributes.items())

                for index in range(
                    len(items) - 1,
                    -1,
                    -1,
                ):
                    name, item = items[index]

                    child_is_last = (
                        index == len(items) - 1
                    )

                    name_text = self.color_key(name)

                    if not child_is_last:
                        push_spacing(
                            stack,
                            child_prefixes,
                        )

                    stack.append(
                        (
                            "render",
                            item,
                            depth + 1,
                            child_prefixes,
                            child_is_last,
                            name_text,
                        )
                    )

                continue

            text = self.color_value(
                scalar(current),
            )

            if label is not None:
                text = (
                    f"{label} "
                    f"{text}"
                )

            print_line(
                prefixes,
                is_last,
                text,
                root=(
                    not prefixes
                    and label is None
                ),
            )

        print()
