from typing import Any

from qlogicae_cor.v1.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1.toml_manager_configurations import (
    TomlManagerConfigurations,
)


class TomlManager(AbstractManager[TomlManagerConfigurations]):
    def __init__(self) -> None:
        super().__init__(TomlManagerConfigurations())

        self._valid_file_extensions: set[str] = {".toml"}

    @property
    def valid_file_extensions(self) -> set[str]:
        return self._valid_file_extensions

    def is_valid(self, file_path: Any) -> bool:
        try:
            if file_path.suffix.lower() not in self.valid_file_extensions:
                return False

            return True

        except Exception:
            return False


singleton = TomlManager()
