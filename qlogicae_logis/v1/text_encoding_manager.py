from qlogicae_cor.v1.library.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1.text_encoding_manager_configurations import (
    TextEncodingManagerConfigurations,
)


class TextEncodingManager(AbstractManager[TextEncodingManagerConfigurations]):
    __slots__ = (
        "_encoding",
    )

    def __init__(self) -> None:
        super().__init__(TextEncodingManagerConfigurations())

        self._encoding: str = "utf-8"

    @property
    def encoding(self) -> str:
        return self._encoding


singleton = TextEncodingManager()
