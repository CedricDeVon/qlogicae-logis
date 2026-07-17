import time

from pyfiglet import Figlet
from qlogicae_cor.v1.abstract_manager import AbstractManager
from rich.console import Console
from rich.live import Live
from rich.padding import Padding
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
)
from rich.rule import Rule
from rich.table import Table

from qlogicae_logis.v1.cli_manager_configurations import (
    CliManagerConfigurations,
)


class CliManager(AbstractManager[CliManagerConfigurations]):
    def __init__(self) -> None:
        super().__init__(CliManagerConfigurations())

        self._console = Console()

    @property
    def console(self):
        return self._console

    @property
    def table(self):
        return Table(
            show_header=False,
            box=None,
            pad_edge=False,
            padding=(0, 4, 1, 4),
        )

    @property
    def progress_bar(self):
        return Progress(
            SpinnerColumn("dots", style="bold bright_green"),
            TextColumn("[green]{task.description}"),
            BarColumn(bar_width=80, complete_style="green"),
            TextColumn("[green]{task.percentage:>6.2f}%"),
            TimeElapsedColumn(),
        )

    def render_progress_bar(self, data={}) -> bool:
        if not data:
            return False

        progress_bar = self.progress_bar
        progress_bar_task = progress_bar.add_task("", total=100)

        progress_items = data["items"] if "items" in data else []
        progress_refresh = data["refresh"] if "refresh" in data else {}
        progress_refresh_value = (
            progress_refresh["value"] if "value" in progress_refresh else 60
        )
        progress_transient = data["transient"] if "transient" in data else {}
        progress_transient_value = data["value"] if "value" in data else True
        with Live(
            progress_bar,
            console=self.console,
            refresh_per_second=progress_refresh_value,
            transient=progress_transient_value,
        ):
            time_start = time.perf_counter()
            for index, task_data in enumerate(progress_items):
                task_message = (
                    task_data["message"] if "message" in task_data else "Loading"
                )
                task_callback = (
                    task_data["callback"] if "callback" in task_data else None
                )
                task_delay = task_data["delay"] if "delay" in task_data else {}
                task_delay_in_seconds = (
                    task_delay["value"] if "value" in task_delay else 0
                )

                progress_bar.update(progress_bar_task, description=task_message)

                if task_callback:
                    task_callback()

                progress_bar.update(
                    progress_bar_task,
                    completed=min(index / len(progress_items) * 100, 100),
                    elapsed=f"{(time.perf_counter() - time_start):.2f}s",
                )

                if task_delay_in_seconds:
                    time.sleep(task_delay_in_seconds)

        return True

    def setup_table(self, data={}):
        if not data:
            return False

        cli_table = self.table
        cli_table_headers = data["headers"] if "headers" in data else []

        for cli_table_header in cli_table_headers:
            cli_table_header_name = (
                cli_table_header["name"] if "name" in cli_table_header else "name"
            )
            cli_table_header_style = (
                cli_table_header["style"] if "style" in cli_table_header else "white"
            )
            cli_table_header_no_wrap = (
                cli_table_header["no_wrap"] if "no_wrap" in cli_table_header else True
            )

            cli_table.add_column(
                cli_table_header_name,
                style=cli_table_header_style,
                no_wrap=cli_table_header_no_wrap,
            )

        cli_table_rows = data["rows"] if "rows" in data else []
        for cli_table_row in cli_table_rows:
            cli_table.add_row(*cli_table_row)

        return self.setup_padding(cli_table)

    def setup_horizontal_rule(self):
        return Padding(Rule(style="bold green"), (0, 2))

    def setup_branding(self, brand_name: str, brand_description: str):
        brand_name = brand_name or "Brand"
        brand_description = brand_description or "Description"

        return self.setup_padding(
            f"[white]{Figlet(font='slant').renderText(brand_name)}[/]\n[white]{brand_description}[/]"
        )

    def setup_duration_text(self, text=""):
        return self.setup_padding(f"[dim]{text} seconds[/]")

    def setup_end_padding(self):
        return self.setup_padding("", 0, 4)

    def setup_padding(self, text="", vertical=1, horizontal=4):
        return Padding(
            text,
            (vertical, horizontal),
        )

    def render_one(self, text: str = "") -> bool:
        self._console.print(text)

        return True

    def render_many(self, items=[]):
        if not items:
            return False

        for item in items:
            if not item:
                return False

            self.render_one(item)

        return True


singleton = CliManager()
