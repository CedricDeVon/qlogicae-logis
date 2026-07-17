import typer

from qlogicae_logis.v1 import (
    cli_manager,
    file_log_manager,
    value_cache_manager,
    workspace_manager,
)
from qlogicae_logis.v1.target_cache_value import TargetCacheValue

app_about = typer.Typer()


def handle_loading() -> bool:
    cli_manager.singleton.render_progress_bar(
        {
            "items": [
                {
                    "callback": workspace_manager.singleton.handle_toolset_configuration_file_data_extraction_setup
                },
                {
                    "callback": workspace_manager.singleton.handle_toolset_configuration_data_setup
                },
            ]
        }
    )


@app_about.command(name="version", help="Current version.")
def version() -> bool:
    file_log_manager.singleton.log_info("'about version' - start")

    handle_loading()
    toolset_about = (
        value_cache_manager.singleton.get_one_value(
            [
                "toolset-about",
            ],
            output_type=TargetCacheValue.ANY,
        )
        or {}
    )

    toolset_about_version = (
        toolset_about["project-version"]["value"]
        if "project-version" in toolset_about
        and "value" in toolset_about["project-version"]
        else "None"
    )

    cli_manager.singleton.render_one(f"[green]{toolset_about_version}[/]")

    file_log_manager.singleton.log_info("'about version' - complete")
    workspace_manager.singleton.shutdown()

    return True


@app_about.command(name="me", help="All information.")
def me() -> bool:
    file_log_manager.singleton.log_info("'about me' - start")

    handle_loading()
    toolset_about = (
        value_cache_manager.singleton.get_one_value(
            [
                "toolset-about",
            ],
            output_type=TargetCacheValue.ANY,
        )
        or {}
    )
    toolset_about_table = (
        value_cache_manager.singleton.get_one_value(
            [
                "toolset-about-table",
            ],
            output_type=TargetCacheValue.ANY,
        )
        or {}
    )
    toolset_about_table_rows = []
    for _key, item in toolset_about_table.items():
        item_name = item["name"] if "name" in item else "None"
        item_value = str(item["value"]) if "value" in item else "None"
        toolset_about_table_rows.append([item_name, item_value])
    toolset_about_table_data = {
        "headers": ["key", "value"],
        "rows": toolset_about_table_rows,
    }
    toolset_about_company_name = (
        toolset_about["company-name"]["value"]
        if "company-name" in toolset_about and "value" in toolset_about["company-name"]
        else "QLogicae"
    )
    toolset_about_project_name = (
        toolset_about["project-name"]["value"]
        if "project-name" in toolset_about and "value" in toolset_about["project-name"]
        else "Logis"
    )
    toolset_about_brand_name = (
        toolset_about["brand-name"]["value"]
        if "brand-name" in toolset_about and "value" in toolset_about["brand-name"]
        else f"{toolset_about_company_name} {toolset_about_project_name}"
    )
    toolset_about_project_description = (
        toolset_about["project-description"]["value"]
        if "project-description" in toolset_about
        and "value" in toolset_about["project-description"]
        else "The project management tool for QLogicae projects"
    )

    cli_manager.singleton.render_many(
        [
            cli_manager.singleton.setup_branding(
                toolset_about_brand_name, toolset_about_project_description
            ),
            cli_manager.singleton.setup_horizontal_rule(),
            cli_manager.singleton.setup_table(toolset_about_table_data),
            cli_manager.singleton.setup_end_padding(),
        ]
    )

    file_log_manager.singleton.log_info("'about me' - complete")
    workspace_manager.singleton.shutdown()

    return True
