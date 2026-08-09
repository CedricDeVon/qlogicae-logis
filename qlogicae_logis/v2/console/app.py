
def main() -> None:
    from qlogicae_cor.v1.library.singleton_manager import (
        SingletonManager,
    )

    from qlogicae_logis.v2.library.console_manager import ConsoleManager

    SingletonManager.get_singleton(
        ConsoleManager
    ).run()

if __name__ == "__main__":
    main()

