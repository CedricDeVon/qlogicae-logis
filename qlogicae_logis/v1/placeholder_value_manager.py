from qlogicae_cor.v1.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1.placeholder_value_manager_configurations import (
    PlaceholderValueManagerConfigurations,
)


class PlaceholderValueManager(AbstractManager[PlaceholderValueManagerConfigurations]):
    def __init__(self) -> None:
        super().__init__(PlaceholderValueManagerConfigurations())

        self._none = "none"
        self._not_a_number = "nan"
        self._redacted = "redacted"
        self._expunged = "expunged"

    @property
    def none(self) -> str:
        return self._none

    @none.setter
    def none(
        self,
        value: str,
    ) -> None:
        self._none = value

    @property
    def not_a_number(self) -> str:
        return self._not_a_number

    @not_a_number.setter
    def not_a_number(
        self,
        value: str,
    ) -> None:
        self._not_a_number = value

    @property
    def redacted(self) -> str:
        return self._redacted

    @redacted.setter
    def redacted(
        self,
        value: str,
    ) -> None:
        self._redacted = value

    @property
    def expunged(self) -> str:
        return self._expunged

    @expunged.setter
    def expunged(
        self,
        value: str,
    ) -> None:
        self._expunged = value


singleton = PlaceholderValueManager()
