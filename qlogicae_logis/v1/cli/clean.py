import typer

from qlogicae_logis.v1 import (
    cli_manager,
    file_log_manager,
    filesystem_manager,
    log_manager,
    value_cache_manager,
    workspace_manager,
)
from qlogicae_logis.v1.target_cache_value import TargetCacheValue

app_clean = typer.Typer()
app_clean_list = typer.Typer()

app_clean.add_typer(
    app_clean_list,
    name="list",
    help="Show list information.",
)


def handle_loading() -> bool:
    cli_manager.singleton.render_progress_bar(
        {
            "items": [
                {
                    "callback": (
                        workspace_manager.singleton.handle_clean_scripts_setup
                    ),
                },
            ],
        }
    )

    return True


@app_clean.command(
    name="selection", help="Clean filesystem paths based on a selection."
)
def selection(
    targets: list[str] = typer.Argument(
        ...,
        help="List of cleaning targets.",
    ),
) -> bool:
    file_log_manager.singleton.log_info("'clean selection' - start")

    handle_loading()
    clean_include_selections = (
        value_cache_manager.singleton.get_one_value(
            ["clean-include-selections"],
            output_type=TargetCacheValue.ANY,
        )
        or {}
    )
    clean_exclude_selections = (
        value_cache_manager.singleton.get_one_value(
            ["clean-exclude-selections"],
            output_type=TargetCacheValue.ANY,
        )
        or {}
    )
    is_enabled = (
        value_cache_manager.singleton.get_one_value(
            ["workspace", "data", "script", "clean", "is-enabled", "value"],
            output_type=TargetCacheValue.ANY,
        )
        or True
    )
    if not is_enabled:
        log_manager.singleton.log_warning(
            "'clean selection' - workspace property 'data.script.clean.is-enabled.value' is set to 'false'"
        )
        return False

    for current_target in targets:
        if current_target not in clean_include_selections:
            log_manager.singleton.log_warning(
                f"'clean selection' - '{current_target}' is not an item within the 'data.script.clean.include' workspace property"
            )

            continue

        current_item_targets = clean_include_selections[current_target]
        for current_item_target in current_item_targets:
            if "full-path" not in current_item_target:
                log_manager.singleton.log_warning(
                    "'clean selection' - workspace property 'data.script.clean.include.targets' items must include a 'full-path' filesystem property"
                )
                continue

            current_filesystem_path = current_item_target["full-path"]
            if current_filesystem_path in clean_exclude_selections:
                log_manager.singleton.log_warning(
                    f"'clean selection' - '{current_filesystem_path}' is a blacklisted filesystem path"
                )
                continue

            filesystem_manager.singleton.clean_filesystem_path(current_filesystem_path)

    file_log_manager.singleton.log_info("'clean selection' - complete")
    workspace_manager.singleton.shutdown()

    return True


@app_clean_list.command(
    name="included", help="Show selections and whitelisted filesystem paths."
)
def included() -> bool:
    file_log_manager.singleton.log_info("'clean list included' - start")

    handle_loading()
    clean_include_selections = (
        value_cache_manager.singleton.get_one_value(
            ["clean-include-selections"],
            output_type=TargetCacheValue.ANY,
        )
        or {}
    )

    for (
        clean_include_target_key,
        clean_include_target_items,
    ) in clean_include_selections.items():
        for clean_include_target_item in clean_include_target_items:
            if "full-path" not in clean_include_target_item:
                log_manager.singleton.log_warning(
                    f"'clean list included' - workspace property 'data.script.clean.include.targets.{clean_include_target_key}' items must include a 'full-path' filesystem property"
                )
                continue

            current_path = clean_include_target_item["full-path"]

            cli_manager.singleton.render_one(
                f"[red]{clean_include_target_key} <- {current_path}[/]"
            )

    file_log_manager.singleton.log_info("'clean list included' - complete")
    workspace_manager.singleton.shutdown()

    return True


@app_clean_list.command(name="excluded", help="Show blacklisted filesystem paths.")
def excluded() -> bool:
    file_log_manager.singleton.log_info("'clean list excluded' - start")

    handle_loading()
    clean_exclude_selections = list(
        value_cache_manager.singleton.get_one_value(
            ["clean-exclude-selections"],
            output_type=TargetCacheValue.ANY,
        )
        or {}
    )
    clean_exclude_selections.sort()

    for target_selection in clean_exclude_selections:
        cli_manager.singleton.render_one(f"[green]{target_selection}[/]")

    file_log_manager.singleton.log_info("'clean list excluded' - complete")
    workspace_manager.singleton.shutdown()

    return True
