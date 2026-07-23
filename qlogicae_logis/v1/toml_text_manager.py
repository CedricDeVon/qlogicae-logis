import tomllib
from typing import Any

import tomli_w
from qlogicae_cor.v1.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1.toml_text_manager_configurations import (
    TomlTextManagerConfigurations,
)


class TomlTextManager(AbstractManager[TomlTextManagerConfigurations]):
    def __init__(self) -> None:
        super().__init__(TomlTextManagerConfigurations())

    def is_valid(
        self,
        value: str,
    ) -> bool:
        try:
            tomllib.loads(value)
            return True

        except Exception:
            return False

    def convert_to_object(
        self,
        value: str,
    ) -> Any:
        try:
            return tomllib.loads(value)

        except Exception:
            return {}

    def convert_to_string(
        self,
        value: Any,
    ) -> str:
        try:
            return tomli_w.dumps(value)

        except Exception:
            return ""


singleton = TomlTextManager()
