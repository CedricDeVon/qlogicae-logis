from __future__ import annotations

from typing import Any

# if TYPE_CHECKING:
#     pass

_SingletonManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _SingletonManager

    import qlogicae_cor.v1.library.singleton_manager

    _SingletonManager = (
        qlogicae_cor.v1.library.singleton_manager.SingletonManager
    )

    _handle_dynamic_imports = lambda: None


class CliCommandManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()

    def handle_about_version(self) -> bool:
        return True

    def handle_about_me(self) -> bool:
        return True

