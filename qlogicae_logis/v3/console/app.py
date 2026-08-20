from __future__ import annotations


def main() -> None:
    from ..library import (
        console_manager,
        import_manager,
    )

    import_manager.ImportManager.get_singleton(
        console_manager.ConsoleManager
    ).run()


if __name__ == "__main__":
    main()

