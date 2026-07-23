from qlogicae_cor.v1.abstract_manager import (
    AbstractManager,
)

from qlogicae_logis.v1 import time_manager
from qlogicae_logis.v1.time_unit import TimeUnit
from qlogicae_logis.v1.timer_manager_configurations import (
    TimerManagerConfigurations,
)


class TimerManager(AbstractManager[TimerManagerConfigurations]):
    def __init__(self) -> None:
        super().__init__(TimerManagerConfigurations())

        self._start_timestamp = 0
        self._stop_timestamp = 0

    @property
    def start_timestamp(self):
        return self._start_timestamp

    @property
    def stop_timestamp(self):
        return self._stop_timestamp

    def start_time(self) -> bool:
        self._start_timestamp = time_manager.singleton.current_nanosecond

        return True

    def stop_time(self) -> bool:
        self._stop_timestamp = time_manager.singleton.current_nanosecond

        return True

    def clear_time(self) -> bool:
        self._start_timestamp = 0
        self._stop_timestamp = 0

        return True

    def reset_time(self) -> bool:
        self._start_timestamp = time_manager.singleton.current_nanosecond
        self._stop_timestamp = 0

        return True

    def calculate_elapsed_time(
        self,
        time_unit: TimeUnit = TimeUnit.SECOND,
    ) -> float:
        return time_manager.singleton.convert_time_unit(
            time_manager.singleton.current_nanosecond - self._start_timestamp
        )

    def calculate_duration_time(
        self,
        time_unit: TimeUnit = TimeUnit.SECOND,
    ) -> float:
        return time_manager.singleton.convert_time_unit(
            self._stop_timestamp - self._start_timestamp
        )


singleton = TimerManager()
