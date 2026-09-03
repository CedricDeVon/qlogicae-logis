from __future__ import annotations


def main() -> int:
    from ..library import (
        console_manager,
        import_manager,
    )

    console_application = (
        import_manager.ImportManager.read_singleton(
            console_manager.ConsoleManager
        )
    )

    result: bool = True
    method_result: bool = True
    method_result = console_application.run()
    if not method_result:
        result = False

    method_result = console_application.shutdown()
    if not method_result:
        result = False

    return 0 if result else 1

if __name__ == "__main__":
    import sys

    sys.exit(
        main()
    )

