import json
from typing import Any

from qlogicae_cor.v1.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1 import (
    json_manager,
    text_encoding_manager,
)
from qlogicae_logis.v1.json_file_io_manager_configurations import (
    JsonFileIoManagerConfigurations,
)


class JsonFileIoManager(AbstractManager[JsonFileIoManagerConfigurations]):
    def __init__(self) -> None:
        super().__init__(JsonFileIoManagerConfigurations())

    def read_file(self, file_path: Any) -> Any:
        try:
            output_data = {}
            with file_path.open(
                mode="r",
                encoding=text_encoding_manager.singleton.encoding,
            ) as file:
                output_data = json.load(file) or {}

            return output_data

        except Exception:
            return {}

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
                json.dump(
                    data,
                    file,
                    indent=json_manager.singleton.indent_count,
                    ensure_ascii=json_manager.singleton.is_ascii_format_enabled,
                    sort_keys=json_manager.singleton.is_key_sortable,
                )

            return True

        except Exception:
            return False


singleton = JsonFileIoManager()
