from __future__ import annotations


def main() -> None:
    from ..library import (
        console_manager,
        import_manager,
    )

    console_application = (
        import_manager.ImportManager.read_singleton(
            console_manager.ConsoleManager
        )
    )

    console_application.run()
    console_application.shutdown()


if __name__ == "__main__":
    main()

