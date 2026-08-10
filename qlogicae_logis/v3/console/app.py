
def main() -> None:
    from qlogicae_logis.v3._vendor.pyyaml import (
        yaml
    )
    from qlogicae_logis.v3._vendor.rich import (
        console
    )
    from pathlib import Path


    data = yaml.safe_load(
        Path("root.yaml").read_text(
            encoding="utf-8",
        ),
    )

    console = console.Console()


    console.print(
        data
    )

if __name__ == "__main__":
    main()

