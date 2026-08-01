from __future__ import annotations

from typing import Any

# if TYPE_CHECKING:
#     pass

_singleton_manager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _singleton_manager

    import qlogicae_cor.v1.library.singleton_manager

    _singleton_manager = (
        qlogicae_cor.v1.library.singleton_manager.SingletonManager
    )

    _handle_dynamic_imports = lambda: None


class ConsoleManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()
