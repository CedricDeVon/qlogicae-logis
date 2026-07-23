from qlogicae_cor.v1.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1.workspace_export_manager_configurations import (
    WorkspaceExportManagerConfigurations,
)


class WorkspaceExportManager(
    AbstractManager[WorkspaceExportManagerConfigurations]
):
    def __init__(self) -> None:
        super().__init__(WorkspaceExportManagerConfigurations())

        self._default_export_selection = "qlogicae-workspace"

    @property
    def default_export_selection(self) -> str:
        return self._default_export_selection

    @default_export_selection.setter
    def default_export_selection(self, value) -> bool:
        self._default_export_selection = value

        return True


singleton = WorkspaceExportManager()
