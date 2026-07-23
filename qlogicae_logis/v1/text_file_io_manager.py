from pathlib import Path
from typing import Any

from qlogicae_cor.v1.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1 import (
    text_encoding_manager,
)
from qlogicae_logis.v1.text_file_io_manager_configurations import (
    TextFileIoManagerConfigurations,
)


class TextFileIoManager(AbstractManager[TextFileIoManagerConfigurations]):
    def __init__(self) -> None:
        super().__init__(TextFileIoManagerConfigurations())

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


singleton = TextFileIoManager()
