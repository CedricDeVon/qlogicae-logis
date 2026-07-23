from typing import Any

import yaml
from qlogicae_cor.v1.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1 import (
    text_encoding_manager,
    yaml_manager,
)
from qlogicae_logis.v1.yaml_file_io_manager_configurations import (
    YamlFileIoManagerConfigurations,
)


class YamlFileIoManager(AbstractManager[YamlFileIoManagerConfigurations]):
    def __init__(self) -> None:
        super().__init__(YamlFileIoManagerConfigurations())

    def read_file(self, file_path: Any) -> Any:
        try:
            output_data = {}
            with file_path.open(
                mode="r",
                encoding=text_encoding_manager.singleton.encoding,
            ) as file:
                output_data = yaml.safe_load(file) or {}

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
                yaml.safe_dump(
                    data,
                    file,
                    sort_keys=yaml_manager.singleton.is_key_sorting_enabled,
                    default_flow_style=yaml_manager.singleton.is_default_flow_state_enabled,
                    allow_unicode=yaml_manager.singleton.is_unicode_enabled,
                    indent=yaml_manager.singleton.indent_count,
                )

            return True

        except Exception:
            return False

    def format_to_string(self, value: str) -> Any:
        return (
            yaml.dump(
                value,
                sort_keys=yaml_manager.singleton.is_key_sorting_enabled,
                default_flow_style=yaml_manager.singleton.is_default_flow_state_enabled,
                allow_unicode=yaml_manager.singleton.is_unicode_enabled,
                indent=yaml_manager.singleton.indent_count,
            )
            or ""
        )


singleton = YamlFileIoManager()
