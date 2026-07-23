import os
import platform
from pathlib import Path

from qlogicae_cor.v1.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1.system_manager_configurations import (
    SystemManagerConfigurations,
)


class SystemManager(AbstractManager[SystemManagerConfigurations]):
    def __init__(self) -> None:
        super().__init__(SystemManagerConfigurations())

    @property
    def current_executing_console_filesystem_path(
        self,
    ) -> Path:
        return Path.cwd()

    @property
    def operating_system_name(self) -> str:
        return platform.system()

    @property
    def operating_system_architecture(
        self,
    ) -> str:
        return platform.machine()

    @property
    def script_executable_filesystem_path(
        self,
    ) -> str:
        pass

    @current_executing_console_filesystem_path.setter
    def current_executing_console_filesystem_path(
        self,
        value: Path,
    ) -> bool:
        path = Path(value).expanduser().resolve()

        if not path.exists():
            raise Exception(
                f"directory '{path}' does not exist",
            )

        if not path.is_dir():
            raise Exception(
                f"'{path}' is not a directory",
            )

        os.chdir(path)

        return True


singleton = SystemManager()
