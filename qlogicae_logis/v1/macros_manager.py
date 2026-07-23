import re
from collections.abc import Mapping
from typing import Any

from qlogicae_cor.v1.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1.macros_manager_configurations import (
    MacrosManagerConfigurations,
)


class MacrosManager(AbstractManager[MacrosManagerConfigurations]):
    def __init__(self) -> None:
        super().__init__(MacrosManagerConfigurations())

        self.pattern = re.compile(r"\$\{\{\s*([A-Za-z0-9._-]+)\s*\}\}")

    def resolve_many(self, values: Any) -> Mapping[str, Any]:
        cache: dict[str, Any] = {}

        for root in values:
            if root in cache:
                continue

            stack: list[str] = [root]
            visiting: set[str] = set()

            while stack:
                key = stack[-1]

                if key in cache:
                    stack.pop()
                    visiting.discard(key)
                    continue

                if key not in values:
                    raise Exception(f"key path '{key}' is an unknown macros")

                value = values[key]

                if not isinstance(value, str):
                    cache[key] = value
                    stack.pop()
                    visiting.discard(key)
                    continue

                if key not in visiting:
                    visiting.add(key)

                unresolved: list[str] = []

                for match in self.pattern.finditer(value):
                    dependency = match.group(1)

                    if dependency in cache:
                        continue

                    if dependency in visiting:
                        raise Exception(
                            f"key path '{dependency}' is a circular reference"
                        )

                    unresolved.append(dependency)

                if unresolved:
                    stack.extend(reversed(unresolved))
                    continue

                def replace(
                    match: re.Match[str],
                ) -> str:
                    dependency = match.group(1)
                    return str(cache[dependency])

                cache[key] = self.pattern.sub(replace, value)

                stack.pop()
                visiting.remove(key)

        return cache

    def resolve_one(
        self,
        key: Any,
        values: Any,
        cache: dict[Any, Any],
        stack: set[Any],
    ) -> Any:
        if key in cache:
            return cache[key]

        frames: list[tuple[Any, bool]] = [(key, False)]

        while frames:
            current_key, expanded = frames.pop()

            if current_key in cache:
                continue

            if not expanded:
                if current_key in stack:
                    raise Exception(f"key path '{current_key}' is a circular reference")

                if current_key not in values:
                    raise Exception(f"key path '{current_key}' is an unknown macros")

                value = values[current_key]

                if not isinstance(value, str):
                    cache[current_key] = value
                    continue

                stack.add(current_key)

                frames.append((current_key, True))

                for match in self.pattern.finditer(value):
                    dependency = match.group(1)

                    if dependency not in cache:
                        frames.append((dependency, False))

            else:
                value = values[current_key]

                resolved = self.pattern.sub(
                    lambda match: str(cache[match.group(1)]),
                    value,
                )

                cache[current_key] = resolved
                stack.remove(current_key)

        return cache[key]

    def parse_many(self, values: Any, resolved: Any) -> str:
        return self.parse_one(values, resolved)

    def parse_one(self, value: str, resolved: Any) -> str:
        if isinstance(value, str):
            return self.pattern.sub(
                lambda match: resolved.get(match.group(1), match.group(0)),
                value,
            )

        if isinstance(value, dict):
            return {
                key: self.parse_one(child, resolved) for key, child in value.items()
            }

        if isinstance(value, list):
            return [self.parse_one(child, resolved) for child in value]

        if isinstance(value, tuple):
            return tuple(self.parse_one(child, resolved) for child in value)

        if isinstance(value, set):
            return {self.parse_one(child, resolved) for child in value}

        return value


singleton = MacrosManager()
