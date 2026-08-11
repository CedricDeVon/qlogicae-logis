
def main() -> None:
    from qlogicae_logis.v3._vendor import (
        pyyaml
    )
    from pathlib import Path


    data = pyyaml.safe_load(
        Path("root.yaml").read_text(
            encoding="utf-8",
        ),
    )

    print(
        data
    )

if __name__ == "__main__":
    main()

