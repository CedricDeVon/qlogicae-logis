from qlogicae_logis.v2 import cli_task_manager
from qlogicae_cor.v1 import (
    singleton_manager,
)

singleton_manager.SingletonManager.get_singleton(
    cli_task_manager.CliTaskManager
).handle_value_cache()
