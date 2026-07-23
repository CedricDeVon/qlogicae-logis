from pathlib import Path
from zipfile import (
    ZIP_BZIP2,
    ZIP_DEFLATED,
    ZIP_LZMA,
    ZIP_STORED,
    ZipFile,
)

from qlogicae_cor.v1.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1.filesystem_compression_manager_configurations import (
    FilesystemCompressionManagerConfigurations,
)


class FilesystemCompressionManager(
    AbstractManager[FilesystemCompressionManagerConfigurations]
):
    def __init__(self) -> None:
        super().__init__(FilesystemCompressionManagerConfigurations())

    def get_zip_format_compression(self, value: str) -> int:
        match value.lower():
            case "store" | "stored" | "none":
                return ZIP_STORED

            case "deflate" | "deflated":
                return ZIP_DEFLATED

            case "bz2" | "bzip2":
                return ZIP_BZIP2

            case "lzma" | "xz":
                return ZIP_LZMA

            case _:
                return ZIP_DEFLATED

        return True

    def zip_extract(
        self,
        archive_path: Path | str,
        destination: Path | str,
        overwrite: bool = False,
    ) -> bool:
        archive_path = Path(archive_path)
        destination = Path(destination).resolve()

        destination.mkdir(
            parents=True,
            exist_ok=True,
        )

        with ZipFile(archive_path, "r") as archive:
            for member in archive.infolist():
                target = (destination / member.filename).resolve()

                if destination not in target.parents and target != destination:
                    raise Exception(
                        f"unsafe archive filesystem path '{member.filename}'"
                    )

                if not overwrite and target.exists():
                    continue

                archive.extract(member, destination)

        return True


singleton = FilesystemCompressionManager()
