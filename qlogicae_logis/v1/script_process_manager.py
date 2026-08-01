import shlex
import subprocess
from subprocess import CompletedProcess

from qlogicae_cor.v1.library.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1 import (
    text_encoding_manager,
)
from qlogicae_logis.v1.script_process import (
    ScriptProcess,
)
from qlogicae_logis.v1.script_process_manager_configurations import (
    ScriptProcessManagerConfigurations,
)


class ScriptProcessManager(AbstractManager[ScriptProcessManagerConfigurations]):
    __slots__ = (
        "_default_script_process",
        "_valid_script_processes",
    )

    def __init__(self) -> None:
        super().__init__(ScriptProcessManagerConfigurations())

        self._default_script_process: str = "shell"
        self._valid_script_processes: set[str] = { "shell", "subprocess" }

    @property
    def default_script_process(self) -> str:
        return self._default_script_process

    @default_script_process.setter
    def default_script_process(self, value: str) -> None:
        if value not in self._valid_script_processes:
            return

        self._default_script_process = value

    @property
    def valid_script_processes(self) -> set[str]:
        return self._valid_script_processes


    def execute_command(
        self,
        command: str,
        script_process_type: ScriptProcess = ScriptProcess.SUBPROCESS,
    ) -> CompletedProcess[str]:
        if not command:
            raise Exception("commands cannot be empty")

        match script_process_type:
            case ScriptProcess.SHELL:
                return subprocess.run(
                    command,
                    encoding=text_encoding_manager.singleton.encoding,
                    text=True,
                    shell=True,
                )

            case ScriptProcess.SUBPROCESS:
                return subprocess.run(
                    shlex.split(command),
                    encoding=text_encoding_manager.singleton.encoding,
                    text=True,
                )

            case _:
                raise Exception("unsupported script process value")


singleton = ScriptProcessManager()
