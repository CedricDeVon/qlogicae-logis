from collections.abc import Set

from qlogicae_cor.v1.library.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1.workspace_log_manager_configurations import (
    WorkspaceLogManagerConfigurations,
)


class WorkspaceLogManager(AbstractManager[WorkspaceLogManagerConfigurations]):
    __slots__ = (
        "_log_targets",
    )

    def __init__(self) -> None:
        super().__init__(WorkspaceLogManagerConfigurations())

        self._log_targets: Set[str] = {"file", "console"}

    @property
    def log_targets(self) -> Set[str]:
        return self._log_targets


singleton = WorkspaceLogManager()
