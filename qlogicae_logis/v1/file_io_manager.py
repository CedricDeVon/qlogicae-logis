from pathlib import Path
from typing import Any

from qlogicae_cor.v1.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1 import (
    text_encoding_manager,
)
from qlogicae_logis.v1.file_io_manager_configurations import (
    FileIoManagerConfigurations,
)


class FileIoManager(AbstractManager[FileIoManagerConfigurations]):
    def __init__(self) -> None:
        super().__init__(FileIoManagerConfigurations())

    @property
    def file_encoding(self) -> str:
        return text_encoding_manager.singleton.encoding

    def read_file(self, file_path: Any) -> str:
        try:
            output_data = ""
            with file_path.open(
                mode="r",
                encoding=text_encoding_manager.singleton.encoding,
            ) as file:
                output_data = file.read() or ""

            return output_data

        except Exception:
            return ""

    def write_file(self, file_path: Any, data: Any) -> bool:
        try:
            file_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )
            with file_path.open(
                mode="w",
                encoding=text_encoding_manager.singleton.encoding,
            ) as file:
                Path(file).write_text(
                    str(data),
                    encoding=self.file_encoding,
                )

            return True

        except Exception:
            return False


singleton = FileIoManager()
