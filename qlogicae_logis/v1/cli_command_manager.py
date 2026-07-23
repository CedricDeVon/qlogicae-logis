import time
from pathlib import Path
from zipfile import ZipFile
from itertools import chain
from concurrent.futures import ThreadPoolExecutor
from collections.abc import Callable

from qlogicae_cor.v1.abstract_manager import AbstractManager

from qlogicae_logis.v1 import (
    cli_display_manager,
    console_log_manager,
    file_io_manager,
    file_log_manager,
    filesystem_compression_manager,
    filesystem_manager,
    log_manager,
    macros_manager,
    object_merge_manager,
    placeholder_value_manager,
    script_process_enum_manager,
    script_process_manager,
    system_manager,
    value_cache_manager,
    workspace_export_manager,
    workspace_filesystem_manager,
    workspace_manager,
)
from qlogicae_logis.v1.cli_command_manager_configurations import (
    CliCommandManagerConfigurations,
)
from qlogicae_logis.v1.enum_conversion_output import EnumConversionOutput
from qlogicae_logis.v1.target_cache_value import TargetCacheValue


class CliCommandManager(AbstractManager[CliCommandManagerConfigurations]):
    def __init__(self) -> None:
        super().__init__(CliCommandManagerConfigurations())

        self._commands = {
            "command-about-version":
                self.handle_about_version_command,
            "command-about-me":
                self.handle_about_me_command,
            "command-clean-list-included":
                self.handle_clean_list_included_command,
            "command-clean-list-excluded":
                self.handle_clean_list_excluded_command,
            "command-clean-selection":
                self.handle_clean_selection_command,
            "command-workspace-setup":
                self.handle_workspace_setup_command,
            "command-workspace-export":
                self.handle_workspace_export_command,
            "command-workspace-import":
                self.handle_workspace_import_command,
            "command-workspace-list-exports":
                self.handle_workspace_list_exports_command,
            "command-template-list-selections":
                self.handle_template_list_selections_command,
            "command-template-apply":
                self.handle_template_apply_command,
            "command-workflow-run":
                self.handle_workflow_run_command,
            "command-workflow-list-selections":
                self.handle_workflow_list_selections_command,
        }

    @property
    def commands(self):
        return self._commands

    def handle_about_version_command(self) -> bool:
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
            toolset_about["project-version"]
            if toolset_about and "project-version"
            else placeholder_value_manager.singleton.none
        ) or placeholder_value_manager.singleton.none

        toolset_about_version_value = (
            toolset_about_version["value"]
            if toolset_about_version and "value" in toolset_about_version
            else placeholder_value_manager.singleton.none
        ) or placeholder_value_manager.singleton.none

        cli_display_manager.singleton.render_one(
            f"[green]{toolset_about_version_value}[/]"
        )

        return True

    def handle_about_me_command(self) -> bool:
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
            item_name = (
                item["name"]
                if "name" in item
                else placeholder_value_manager.singleton.none
            )
            item_value = (
                str(item["value"])
                if "value" in item
                else placeholder_value_manager.singleton.none
            )
            toolset_about_table_rows.append([item_name, item_value])

        toolset_about_table_data = {
            "headers": ["key", "value"],
            "rows": toolset_about_table_rows,
        }
        toolset_about_brand_name = (
            toolset_about["brand-name"]["value"]
            if toolset_about
            and "brand-name" in toolset_about
            and "value" in toolset_about["brand-name"]
            else placeholder_value_manager.singleton.none
        ) or placeholder_value_manager.singleton.none
        toolset_about_project_description = (
            toolset_about["project-description"]["value"]
            if toolset_about
            and "project-description" in toolset_about
            and "value" in toolset_about["project-description"]
            else placeholder_value_manager.singleton.none
        ) or placeholder_value_manager.singleton.none

        cli_display_manager.singleton.render_many(
            [
                cli_display_manager.singleton.setup_branding(
                    toolset_about_brand_name, toolset_about_project_description
                ),
                cli_display_manager.singleton.setup_horizontal_rule(),
                cli_display_manager.singleton.setup_table(
                    toolset_about_table_data
                ),
                cli_display_manager.singleton.setup_end_padding(),
            ]
        )

        return True

    def handle_clean_selection_command(self, **kwargs) -> bool:
        file_log_manager.singleton.log_info(
        "'clean selection' - start"
    )
        targets = kwargs.get("targets", [])

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
                [
                    "workspace",
                    "data",
                    "command",
                    "clean",
                    "is-enabled",
                    "value",
                ],
                output_type=TargetCacheValue.ANY,
            )
        )

        if not is_enabled:
            log_manager.singleton.log_warning(
                "'clean selection' - workspace property "
                "'data.command.clean.is-enabled.value' "
                "has been set to 'false'"
            )
            return False

        filesystem_paths: list[str] = []

        for target in targets:
            if (
                not target
                or target not in clean_include_selections
            ):
                log_manager.singleton.log_warning(
                    f"'clean selection' - '{target}' "
                    "is not an item within the "
                    "'data.command.clean.include' workspace property"
                )
                return False

            for current_item_target in clean_include_selections[target]:
                if (
                    not current_item_target
                    or "full-path" not in current_item_target
                ):
                    log_manager.singleton.log_warning(
                        "'clean selection' - workspace property "
                        "'data.command.clean.include.targets' "
                        "items must include a 'full-path' "
                        "filesystem property"
                    )
                    return False

                current_filesystem_path = (
                    current_item_target["full-path"]
                )

                if (
                    not current_filesystem_path
                    or current_filesystem_path
                    in clean_exclude_selections
                ):
                    log_manager.singleton.log_warning(
                        f"'clean selection' - "
                        f"'{current_filesystem_path}' "
                        "is a blacklisted filesystem path"
                    )
                    return False

                filesystem_paths.append(
                    current_filesystem_path
                )

        max_workers = min(
            32,
            len(filesystem_paths) or 1,
        )

        with ThreadPoolExecutor(
            max_workers=max_workers,
        ) as executor:
            list(
                executor.map(
                    filesystem_manager.singleton.clean_filesystem_path,
                    filesystem_paths,
                )
            )

        file_log_manager.singleton.log_info(
            "'clean selection' - complete"
        )

        return True

    def handle_clean_list_included_command(self) -> bool:
        file_log_manager.singleton.log_info("'clean list included' - start")

        clean_include_selections = (
            value_cache_manager.singleton.get_one_value(
                ["clean-include-selections"],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        )

        output_lines: list[str] = []

        for (
            clean_include_target_key,
            clean_include_target_items,
        ) in clean_include_selections.items():
            if not clean_include_target_items:
                continue

            for clean_include_target_item in clean_include_target_items:
                if (
                    not clean_include_target_item
                    or "full-path" not in clean_include_target_item
                ):
                    log_manager.singleton.log_warning(
                        "'clean list included' - workspace property "
                        "'data.command.clean.include."
                        f"targets.{clean_include_target_key}' "
                        "items must include a 'full-path' "
                        "filesystem property"
                    )
                    continue

                current_path = clean_include_target_item["full-path"]

                output_lines.append(
                    f"[red]{clean_include_target_key} <- {current_path}[/]"
                )

        output_content = "\n".join(output_lines)

        cli_display_manager.singleton.render_one(
            output_content
        )

        file_log_manager.singleton.log_info(
            "'clean list included' - complete"
        )

        return True

    def handle_clean_list_excluded_command(self) -> bool:
        file_log_manager.singleton.log_info("'clean list excluded' - start")

        clean_exclude_selections = list(
            value_cache_manager.singleton.get_one_value(
                ["clean-exclude-selections"],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        )
        clean_exclude_selections.sort()

        output_content = "\n".join(
            f"[green]{target_selection}[/]"
            for target_selection in clean_exclude_selections
        )

        cli_display_manager.singleton.render_one(
            output_content
        )

        file_log_manager.singleton.log_info(
            "'clean list excluded' - complete"
        )

        return True

    def handle_workspace_export_command(self, targets) -> bool:
        def handle_a(input_value):
            value = (
                filesystem_compression_manager.singleton.get_zip_format_compression(
                    input_value
                )   
            )

            return value

        def handle_workspace_export_selection(target: str) -> bool:
            if not target or target not in workspace_export_selections:
                log_manager.singleton.log_warning(
                    f"'workspace export' - workspace property "
                    f"'data.export.selection.{target} "
                    "may not exist"
                )
                return False

            export_data_selection = {}
            if target != workspace_export_manager.singleton.default_export_selection:
                export_data_selection = export_data_selections[target]


            export_data_selection_is_enabled = (
                export_data_selection["is-enabled"]
                if export_data_selection and "is-enabled" in export_data_selection
                else {}
            ) or {}
            export_data_selection_is_enabled_value = (
                export_data_selection_is_enabled["value"]
                if export_data_selection_is_enabled
                and "value" in export_data_selection_is_enabled
                else True
            )
            if not export_data_selection_is_enabled_value:
                log_manager.singleton.log_warning(
                    f"'workspace export' - workspace property "
                    f"'data.export.selection.{target}."
                    "is-enabled.value' may have been set to 'false'"
                )
                return False

            export_data_selection_output = (
                export_data_selection["output"]
                if export_data_selection and "output" in export_data_selection
                else {}
            ) or {}

            export_data_selection_output_full_path = (
                export_data_selection_output["full-path"]
                if export_data_selection_output
                and "full-path" in export_data_selection_output
                else current_root_full_path
            ) or current_root_full_path

            export_data_selection_input = (
                export_data_selection["input"]
                if export_data_selection and "input" in export_data_selection
                else {}
            ) or {}
            export_data_selection_input_root_path = (
                export_data_selection_input["root-path"]
                if export_data_selection_input
                and "root-path" in export_data_selection_input
                else {}
            ) or {}
            export_data_selection_input_root_path_value = (
                export_data_selection_input_root_path["value"]
                if export_data_selection_input_root_path
                and "value" in export_data_selection_input_root_path
                else current_root_full_path
            ) or current_root_full_path

            export_data_selection_input_targets = (
                export_data_selection_input["targets"]
                if export_data_selection_input
                and "targets" in export_data_selection_input
                else []
            ) or []

            if export_data_default_filesystem_input_is_enabled_value:
                export_data_selection_input_targets = [
                    *export_data_selection_input_targets,
                    *workspace_export_default_filesystem_input,
                ]

            export_data_selection_compression = (
                export_data_selection["compression"]
                if export_data_selection and "compression" in export_data_selection
                else {}
            ) or {}
            export_data_selection_compression_format = (
                export_data_selection_compression["format"]
                if export_data_selection_compression
                and "format" in export_data_selection_compression
                else {}
            ) or {}
            export_data_selection_compression_format_value = (
                export_data_selection_compression_format["value"]
                if export_data_selection_compression_format
                and "value" in export_data_selection_compression_format
                else "zip"
            ) or "zip"
            export_data_selection_compression_format_value = (
                export_data_selection_compression_format_value
                if export_data_selection_compression_format_value
                and "zip" != export_data_selection_compression_format_value
                else "zip"
            ) or "zip"

            export_data_selection_compression_type = (
                export_data_selection_compression["type"]
                if export_data_selection_compression
                and "type" in export_data_selection_compression
                else {}
            ) or {}
            export_data_selection_compression_type_value = (
                export_data_selection_compression_type["value"]
                if export_data_selection_compression_type
                and "value" in export_data_selection_compression_type
                else "deflated"
            ) or "deflated"

            export_data_selection_compression_type_value = handle_a(
                    export_data_selection_compression_type_value
                )

            export_data_selection_compression_level = (
                export_data_selection_compression["level"]
                if export_data_selection_compression
                and "level" in export_data_selection_compression
                else {}
            ) or {}
            export_data_selection_compression_level_value = (
                export_data_selection_compression_level["value"]
                if export_data_selection_compression_level
                and "value" in export_data_selection_compression_level
                else 6
            ) or 6

            export_data_selection_compression_is_zip_64_allowed = (
                export_data_selection_compression["is-zip-64-allowed"]
                if export_data_selection_compression
                and "is-zip-64-allowed" in export_data_selection_compression
                else {}
            )
            export_data_selection_compression_is_zip_64_allowed_value = (
                export_data_selection_compression_is_zip_64_allowed["value"]
                if export_data_selection_compression_is_zip_64_allowed
                and "value" in export_data_selection_compression_is_zip_64_allowed
                else True
            )

            export_data_selection_compression_is_timestamp_strict = (
                export_data_selection_compression["is-timestamp-strict"]
                if export_data_selection_compression
                and "is-timestamp-strict" in export_data_selection_compression
                else {}
            ) or {}
            export_data_selection_compression_is_timestamp_strict_value = (
                export_data_selection_compression_is_timestamp_strict["value"]
                if export_data_selection_compression_is_timestamp_strict
                and "value"
                in export_data_selection_compression_is_timestamp_strict
                else True
            )

            for (
                current_export_data_selection_input
            ) in export_data_selection_input_targets:
                if (
                    not current_export_data_selection_input
                    or "relative-path" not in current_export_data_selection_input
                ):
                    log_manager.singleton.log_warning(
                        "'workspace export' - workspace property "
                        f"'data.export.selection.{target}.input.targets' "
                        "items must require a "
                        "'relative-path' filesystem value"
                    )
                    return False

                current_export_data_selection_input_relative_path = (
                    current_export_data_selection_input["relative-path"]
                )

                filesystem_manager.singleton.copy_filesystem_path(
                    f"{export_data_selection_input_root_path_value}/{current_export_data_selection_input_relative_path}",
                    f"{current_root_full_path}/workspace/private/temporary/export/targets/{target}/{current_export_data_selection_input_relative_path}",
                )

            source = Path(
                f"{current_root_full_path}/workspace/private/temporary/export/targets/{target}"
            )
            destination = Path(
                f"{export_data_selection_output_full_path}/{target}"
            )
            with ZipFile(
                destination,
                mode="w",
                compression=export_data_selection_compression_type_value,
                compresslevel=export_data_selection_compression_level_value,
                allowZip64=export_data_selection_compression_is_zip_64_allowed_value,
                strict_timestamps=export_data_selection_compression_is_timestamp_strict_value,
            ) as archive:
                for path in source.rglob("*"):
                    archive.write(
                        path,
                        arcname=path.relative_to(source),
                    )

            return True

        def handle_workspace_export_group(target: str) -> bool:
            if not target or target not in export_data_groups:
                log_manager.singleton.log_warning(
                    f"'workspace export' - workspace property "
                    f"'data.export.group.{target} "
                    "may not exist"
                )
                return False

            export_data_group = export_data_groups[target]
            export_data_group_is_enabled = (
                export_data_group["is-enabled"]
                if export_data_group and "is-enabled" in export_data_group
                else {}
            ) or {}
            export_data_group_is_enabled_value = (
                export_data_group_is_enabled["value"]
                if export_data_group_is_enabled
                and "value" in export_data_group_is_enabled
                else True
            )
            if not export_data_group_is_enabled_value:
                log_manager.singleton.log_warning(
                    f"'workspace export' - workspace property "
                    f"'data.export.group.{target}."
                    "is-enabled.value' may have been set to 'false'"
                )
                return False

            export_data_group_selections = (
                export_data_group["selection"]
                if "selection" in export_data_group else {}
            ) or {}
                        
            with ThreadPoolExecutor(
                max_workers=min(
                    32,
                    len(export_data_group_selections) or 1,
                ),
            ) as executor:
                futures = []

                for key in export_data_group_selections:
                    if key in export_data_groups:
                        futures.append(
                            executor.submit(
                                handle_workspace_export_group,
                                key,
                            )
                        )

                    elif key in export_data_selections:
                        futures.append(
                            executor.submit(
                                handle_workspace_export_selection,
                                key,
                            )
                        )

                for future in futures:
                    future.result()

            return True


        file_log_manager.singleton.log_info("'workspace export' - start")

        current_root_full_path = value_cache_manager.singleton.get_one_value(
            ["current-root-full-path"],
            output_type=TargetCacheValue.FOLDER_PATH,
        )

        export_data = (
            value_cache_manager.singleton.get_one_value(
                ["workspace", "data", "command", "export"],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        )

        export_data_is_enabled = (
            export_data["is-enabled"]
            if export_data and "is-enabled" in export_data
            else {}
        ) or {}

        export_data_is_enabled_value = (
            export_data_is_enabled["value"]
            if export_data_is_enabled and "value" in export_data_is_enabled
            else True
        )
        if not export_data_is_enabled_value:
            log_manager.singleton.log_warning(
                "'workspace export' - workspace property "
                "'data.export.is-enabled.value' "
                "may have been set to 'false'"
            )
            return False

        export_data_default = (
            export_data["default"] if export_data
            and "default" in export_data else {}
        ) or {}

        export_data_default_filesystem_input = (
            export_data_default["filesystem-input"] if export_data_default
            and "filesystem-input" in export_data_default else {}
        ) or {}

        export_data_default_filesystem_input_is_enabled = (
            export_data_default_filesystem_input["is-enabled"]
            if export_data_default_filesystem_input
            and "is-enabled" in export_data_default_filesystem_input else {}
        ) or {}

        export_data_default_filesystem_input_is_enabled_value = (
            export_data_default_filesystem_input_is_enabled["value"]
            if export_data_default_filesystem_input_is_enabled
            and "value" in export_data_default_filesystem_input_is_enabled else True
        )

        export_data_cleanup = (
            export_data["cleanup"]
            if export_data and "cleanup" in export_data
            else {}
        ) or {}

        export_data_cleanup_is_enabled = (
            export_data_cleanup["is-enabled"]
            if export_data_cleanup and "is-enabled" in export_data_cleanup
            else {}
        ) or {}

        export_data_cleanup_is_enabled_value = (
            export_data_cleanup_is_enabled["value"]
            if export_data_cleanup_is_enabled
            and "value" in export_data_cleanup_is_enabled
            else True
        )

        export_data_groups = (
            export_data["group"]
            if export_data and "group" in export_data
            else {}
        ) or {}

        export_data_selections = (
            export_data["selection"]
            if export_data and "selection" in export_data
            else {}
        ) or {}

        workspace_export_selections = (
            value_cache_manager.singleton.get_one_value(
                ["workspace-export-selections"],
                output_type=TargetCacheValue.DEFINED,
            )
        )
        workspace_export_groups = (
            value_cache_manager.singleton.get_one_value(
                ["workspace-export-groups"],
                output_type=TargetCacheValue.DEFINED,
            )
        )

        workspace_export_default_filesystem_input = (
            value_cache_manager.singleton.get_one_value(
                ["workspace-export-default-filesystem-input"],
                output_type=TargetCacheValue.DEFINED,
            )
        )

        if export_data_cleanup_is_enabled_value:
            filesystem_manager.singleton.clean_filesystem_path(
                f"{current_root_full_path}/workspace/private/temporary/export"
            )
                
        tasks: list[tuple[Callable[[str], None], str]] = []

        for target in targets:
            if target == "all":
                tasks.extend(
                    (
                        handle_workspace_export_selection,
                        selection,
                    )
                    for selection in workspace_export_selections
                )

            elif target in workspace_export_groups:
                tasks.append(
                    (
                        handle_workspace_export_group,
                        target,
                    )
                )

            elif target in workspace_export_selections:
                tasks.append(
                    (
                        handle_workspace_export_selection,
                        target,
                    )
                )

            else:
                log_manager.singleton.log_warning(
                    "'workspace export' - workspace export selection "
                    f"'{target}' does not exist"
                )

        with ThreadPoolExecutor(
            max_workers=min(32, len(tasks) or 1),
        ) as executor:
            list(
                executor.map(
                    lambda task: task[0](task[1]),
                    tasks,
                )
            )

        if export_data_cleanup_is_enabled_value:
            filesystem_manager.singleton.clean_filesystem_path(
                f"{current_root_full_path}/workspace/private/temporary/export"
            )

        file_log_manager.singleton.log_info("'workspace export' - complete")

        return True

    def handle_workspace_import_command(self, **kwargs) -> bool:
        file_log_manager.singleton.log_info("'workspace import' - start")

        input_path = kwargs.get("input_path", None)
        output_path = kwargs.get("output_path", None)

        if not input_path or not output_path:
            log_manager.singleton.log_warning(
                "'workspace import' - 'input_path' and "
                "'output_path' must be valid filesystem paths"
            )

            return False

        filesystem_compression_manager.singleton.zip_extract(
            input_path, output_path
        )

        file_log_manager.singleton.log_info("'workspace import' - complete")

        return True

    def handle_workspace_setup_command(self) -> bool:
        file_log_manager.singleton.log_info("'workspace setup' - start")

        workspace_manager.singleton.handle_workspace_base_filesystem_replenishment_setup()
        workspace_manager.singleton.handle_workspace_selection_filesystem_replenishment_setup()

        file_log_manager.singleton.log_info("'workspace setup' - complete")

        return True

    def handle_workspace_list_exports_command(self) -> bool:
        file_log_manager.singleton.log_info("'workspace list exports' - start")

        workspace_export_groups = list(
            value_cache_manager.singleton.get_one_value(
                ["workspace-export-groups"],
                output_type=TargetCacheValue.DEFINED,
            )
            or {}
        )
        workspace_export_groups.sort()
        workspace_export_selections = list(
            value_cache_manager.singleton.get_one_value(
                ["workspace-export-selections"],
                output_type=TargetCacheValue.DEFINED,
            )
            or {}
        )
        workspace_export_selections.sort()

        output_content = "\n".join(
            chain(
                (
                    f"[yellow]group <- {group}[/]"
                    for group in workspace_export_groups
                ),
                (
                    f"[green]selection <- {selection}[/]"
                    for selection in workspace_export_selections
                ),
            )
        )

        cli_display_manager.singleton.render_one(output_content)
                

        file_log_manager.singleton.log_info("'workspace list exports' - complete")

        return True

    def handle_workflow_run_command(self, **kwargs) -> bool:
        def handle_workflow_run_target(target_name: str) -> bool:
            if target_name not in workflow_data_selection:
                log_manager.singleton.log_warning(
                    f"'workflow run' - workspace property "
                    f"'data.workflow.selection.{target_name}' "
                    "does not exist"
                )
                return False

            workflow_selection_data = workflow_data_selection[target_name]
            workflow_selection_data_is_enabled = (
                workflow_selection_data["is-enabled"]
                if workflow_selection_data and "is-enabled" in workflow_selection_data
                else {}
            )
            workflow_selection_data_is_enabled_value = (
                workflow_selection_data_is_enabled["value"]
                if workflow_selection_data_is_enabled
                and "value" in workflow_selection_data_is_enabled
                else True
            )
            if (
                not workflow_selection_data_is_enabled_value
            ):
                log_manager.singleton.log_warning(
                    f"'workflow run' - workspace property "
                    f"'data.workflow.selection.{target_name}."
                    "is-enabled.value' has been set to 'false'"
                )
                return False

            workflow_data_delay = (
                workflow_data["delay"]
                if workflow_data and "delay" in workflow_data
                else {}
            ) or {}
            workflow_data_delay_value = (
                workflow_data_delay["value"]
                if workflow_data_delay
                and "value" in workflow_data_delay
                and workflow_data_delay["value"] >= 0
                else 0
            )
            workflow_data_process = (
                workflow_data["process"]
                if workflow_data and "process" in workflow_data
                else {}
            ) or {}
            workflow_data_process_value = (
                workflow_data_process["value"]
                if workflow_data_process and "value"
                    in workflow_data_process
                else "subprocess"
            ) or "subprocess"
            workflow_data_process_override = (
                workflow_data_process["override"]
                if workflow_data_process and "override" in workflow_data_process
                else False
            )
            workflow_selection_data_enter_full_path = (
                workflow_selection_data["enter-full-path"]
                if workflow_selection_data and "enter-full-path"
                    in workflow_selection_data
                else {}
            ) or {}
            workflow_selection_data_enter_full_path_valye = (
                workflow_selection_data_enter_full_path["value"]
                if workflow_selection_data_enter_full_path
                and "value" in workflow_selection_data_enter_full_path
                else current_root_full_path
            ) or current_root_full_path
            workflow_selection_data_commands = (
                workflow_selection_data["commands"]
                if workflow_selection_data and "commands"
                    in workflow_selection_data
                else []
            ) or []
            if not len(workflow_selection_data_commands):
                log_manager.singleton.log_warning(
                    f"'workflow run' - workspace property "
                    f"'data.workflow.targets.{target_name}.commands' "
                    "is an empty list"
                )
                return False

            if workflow_data_delay_value:
                time.sleep(workflow_data_delay_value)

            for command in workflow_selection_data_commands:
                if "run" not in command:
                    log_manager.singleton.log_warning(
                        f"'workflow run' - a command within the '{target_name}'"
                        "workflow does not have a 'run' property"
                    )
                    return False

                current_command_is_enabled = (
                    command["is-enabled"]
                    if command
                    and "is-enabled" in command
                    else {}
                ) or {}
                current_command_is_enabled_value = (
                    current_command_is_enabled["value"]
                    if current_command_is_enabled
                    and "value" in current_command_is_enabled
                    else True
                )
                current_run = command["run"]
                current_run_value = (
                    current_run["value"]
                    if current_run and "value" in current_run else (
                        None
                    )
                )

                if not current_command_is_enabled_value or not current_run_value:
                    log_manager.singleton.log_warning(
                        f"'workflow run' - workspace property "
                        f"'data.workflow.targets.{target_name}.commands."
                        f"'{current_run}'' has been set "
                        "to 'false'"
                    )
                    return False

                current_args = (
                    command["argument"]
                    if command and "argument" in command else {}
                ) or {}
                current_process = (
                    command["process"]
                    if command and "process" in command else {}
                ) or {}
                current_process_value = (
                    current_process["value"]
                    if current_process
                    and "value" in current_process else "subprocess"
                ) or "subprocess"
                if workflow_data_process_override:
                    current_process_value = (
                        workflow_data_process_value
                    )

                current_run_delay = (
                    command["delay"]
                    if command
                    and "delay" in command
                    else {}
                ) or {}
                current_run_delay_value = (
                    current_run_delay["value"]
                    if current_run_delay
                    and "value" in current_run_delay
                    and current_run_delay["value"] >= 0
                    else 0
                ) or 0
                current_process_value = (
                    script_process_enum_manager.singleton.convert_value(
                        current_process_value, EnumConversionOutput.ENUM
                    )
                )
                if current_run_delay_value:
                    time.sleep(current_run_delay_value)

                v = workflow_selection_data_enter_full_path_valye
                system_manager.singleton.current_executing_console_filesystem_path = v

                if current_run_value in self._commands:
                    self._commands[current_run_value](**current_args)

                elif current_run_value in workflow_data_selection:
                    handle_workflow_run_target(current_run_value)

                else:
                    cli_output = script_process_manager.singleton.execute_command(
                        current_run_value,
                        script_process_type=current_process_value,
                    )

                    file_log_manager.singleton.log_info(cli_output)
                    console_log_manager.singleton.log_info(
                        cli_output.stdout or cli_output.stderr or ""
                    )

            return True

        file_log_manager.singleton.log_info("'workflow run' - start")

        targets = kwargs.get('targets', [])

        current_root_full_path = value_cache_manager.singleton.get_one_value(
            ["current-root-full-path"],
            output_type=TargetCacheValue.FOLDER_PATH,
        )
        workflow_data = (
            value_cache_manager.singleton.get_one_value(
                ["workspace", "data", "workflow"],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        )
        workflow_data_is_enabled = (
            workflow_data["is-enabled"]
            if workflow_data and "is-enabled" in workflow_data
            else {}
        )
        workflow_data_is_enabled_value = (
            workflow_data_is_enabled["value"]
            if workflow_data_is_enabled and "value" in workflow_data_is_enabled
            else True
        )
        if not workflow_data_is_enabled_value:
            log_manager.singleton.log_warning(
                "'workflow run' - workspace property "
                "'data.workflow.is-enabled.value' has been "
                "set to 'false'"
            )
            return False

        workflow_data_selection = (
            workflow_data["selection"]
            if workflow_data and "selection" in workflow_data
            else {}
        ) or {}

        for target in targets:
            if target not in workflow_data_selection:
                log_manager.singleton.log_warning(
                    "'workflow run' - workspace property "
                    "'data.workflow.selection.[...]' "
                    "does not exist"
                )
                return False

            handle_workflow_run_target(target)

        file_log_manager.singleton.log_info("'workflow run' - complete")

        return True

    def handle_workflow_list_selections_command(self) -> bool:
        file_log_manager.singleton.log_info("'workflow list selections' - start")

        script_data_targets = (
            list(
                value_cache_manager.singleton.get_one_value(
                    ["workspace", "data", "workflow", "selection"],
                    output_type=TargetCacheValue.ANY,
                )
                or {}
            )
            or []
        )
        script_data_targets.sort()
        output_content = "\n".join(
            f"[green]{script_selection}[/]"
            for script_selection in script_data_targets
        )

        if output_content:
            cli_display_manager.singleton.render_one(
                output_content
            )

        file_log_manager.singleton.log_info(
            "'workflow list selections' - complete"
        )

        return True

    def handle_template_list_selections_command(self) -> bool:
        file_log_manager.singleton.log_info(
            "'template list selections' - start"
        )

        default_workspace_selections = list(
            value_cache_manager.singleton.get_one_value(
                ["default-workspace-selections"],
                output_type=TargetCacheValue.DEFINED,
            )
            or {}
        )
        default_workspace_selections.sort()
        group_workspace_selections = list(
            value_cache_manager.singleton.get_one_value(
                ["group-workspace-selections"],
                output_type=TargetCacheValue.DEFINED,
            )
            or {}
        )
        group_workspace_selections.sort()
        project_workspace_selections = list(
            value_cache_manager.singleton.get_one_value(
                ["project-workspace-selections"],
                output_type=TargetCacheValue.DEFINED,
            )
            or {}
        )
        project_workspace_selections.sort()
        
        output_content = "\n".join(
            chain(
                (
                    f"[red]base <- {selection}[/]"
                    for selection in default_workspace_selections
                ),
                (
                    f"[yellow]group <- {selection}[/]"
                    for selection in group_workspace_selections
                ),
                (
                    f"[green]project <- {selection}[/]"
                    for selection in project_workspace_selections
                ),
            )
        )

        cli_display_manager.singleton.render_one(output_content)

        file_log_manager.singleton.log_info(
            "'template list selections' - complete"
        )

        return True

    def handle_template_apply_command(self, **kwargs) -> bool:
        def handle_target_root():
            file_log_manager.singleton.log_info(
                "'template filesystem apply' - 'root' setup execution start"
            )

            filesystem = filesystem_manager.singleton
            workspace_fs = workspace_filesystem_manager.singleton
            merger = object_merge_manager.singleton

            temporary_root = (
                Path(current_root_full_path)
                / "workspace"
                / "private"
                / "temporary"
                / "template"
            )

            copy_tasks: list[tuple[Path, Path]] = []

            for scope in workspace_fs.scope_selections:
                for template_type in ("filesystem", "fragment"):
                    destination = (
                        temporary_root
                        / template_type
                        / "root"
                    )

                    copy_tasks.extend(
                        [
                            (
                                Path(current_root_full_path)
                                / "workspace"
                                / scope
                                / "template"
                                / "all"
                                / template_type,
                                destination,
                            ),
                            (
                                Path(current_root_full_path)
                                / "workspace"
                                / scope
                                / "template"
                                / "root"
                                / template_type,
                                destination,
                            ),
                        ]
                    )

            def copy_task(task: tuple[Path, Path]) -> None:
                filesystem.copy_filesystem_path(
                    task[0],
                    task[1],
                )

            with ThreadPoolExecutor(
                max_workers=min(32, len(copy_tasks) or 1),
            ) as executor:
                list(executor.map(copy_task, copy_tasks))

            parse_paths = [
                temporary_root / "filesystem" / "root",
                temporary_root / "fragment" / "root",
            ]

            with ThreadPoolExecutor(max_workers=2) as executor:
                list(
                    executor.map(
                        handle_filesystem_parsing,
                        parse_paths,
                    )
                )

            filesystem.copy_filesystem_path(
                temporary_root / "filesystem" / "root",
                current_root_full_path,
            )

            fragment_root = (
                temporary_root
                / "fragment"
                / "root"
            )

            relative_paths = [
                path.relative_to(fragment_root)
                for path in fragment_root.rglob("*")
                if path.is_file()
            ]

            def merge_fragment(relative_path: Path) -> None:
                source_path = fragment_root / relative_path
                target_path = (
                    Path(current_root_full_path)
                    / relative_path
                )

                source_data = (
                    workspace_fs.read_file(source_path)
                )

                target_data = (
                    workspace_fs.read_file(target_path)
                )

                merged = (
                    merger.handle_deep_merge_fragments(
                        target_data,
                        source_data,
                    )
                )

                workspace_fs.write_file(
                    target_path,
                    merged,
                )

            with ThreadPoolExecutor(
                max_workers=min(32, len(relative_paths) or 1),
            ) as executor:
                list(
                    executor.map(
                        merge_fragment,
                        relative_paths,
                    )
                )

            file_log_manager.singleton.log_info(
                "'template filesystem apply' - 'root' setup execution complete"
            )

            return True


        def handle_target_group():
            file_log_manager.singleton.log_info(
                "'template filesystem apply' - 'group' "
                "setup execution start"
            )
                       
            with ThreadPoolExecutor(
                max_workers=min(32, len(group_workspace_selections) or 1),
            ) as executor:
                list(
                    executor.map(
                        handle_target_group_selection,
                        group_workspace_selections,
                    )
                )

            file_log_manager.singleton.log_info(
                "'template filesystem apply' - 'group' "
                "setup execution complete"
            )

            return True


        def handle_target_group_selection(group_name):
            file_log_manager.singleton.log_info(
                f"'template filesystem apply' - '{group_name}' "
                "setup execution start"
            )

            group_targets = value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "selection",
                    "group",
                    "targets",
                    group_name,
                    "targets",
                ],
                output_type=TargetCacheValue.DEFINED,
            )

            for (
                current_scope_name
            ) in workspace_filesystem_manager.singleton.scope_selections:
                for current_template_type in ["filesystem", "fragment"]:
                    filesystem_manager.singleton.copy_filesystem_path(
                        f"{current_root_full_path}/workspace/{current_scope_name}/template/all/{current_template_type}",
                        f"{current_root_full_path}/workspace/private/temporary/template/{current_template_type}/{group_name}",
                    )
                    filesystem_manager.singleton.copy_filesystem_path(
                        f"{current_root_full_path}/workspace/{current_scope_name}/template/group/{current_template_type}",
                        f"{current_root_full_path}/workspace/private/temporary/template/{current_template_type}/{group_name}",
                    )
                    filesystem_manager.singleton.copy_filesystem_path(
                        f"{current_root_full_path}/workspace/{
                            current_scope_name
                        }/template/group/selection/{group_name}/{
                            current_template_type
                        }",
                        f"{current_root_full_path}/workspace/private/temporary/template/{current_template_type}/{group_name}",
                    )

            for current_template_type in ["filesystem", "fragment"]:
                handle_filesystem_parsing(
                    f"{current_root_full_path}/workspace/private/temporary/template/{current_template_type}/{group_name}"
                )

            for current_target in group_targets:
                if current_target in project_workspace_selections:
                    filesystem_manager.singleton.copy_filesystem_path(
                        f"{current_root_full_path}/workspace/private/temporary/template/filesystem/{group_name}",
                        f"{current_root_full_path}/workspace/private/temporary/template/filesystem/{current_target}",
                    )
                    handle_target_project_selection(current_target)

                elif current_target == "root":
                    filesystem_manager.singleton.copy_filesystem_path(
                        f"{current_root_full_path}/workspace/private/temporary/template/filesystem/{group_name}",
                        f"{current_root_full_path}/workspace/private/temporary/template/filesystem/root",
                    )
                    handle_target_root()

                elif current_target in group_workspace_selections:
                    handle_target_group_selection(current_target)


            file_log_manager.singleton.log_info(
                f"'template filesystem apply' - '{group_name}' "
                "setup execution complete"
            )

            return True

        def handle_target_project():
            file_log_manager.singleton.log_info(
                "'template filesystem apply' - 'project' "
                "setup execution start"
            )

            with ThreadPoolExecutor(
                max_workers=min(32, len(project_workspace_selections) or 1),
            ) as executor:
                list(
                    executor.map(
                        handle_target_project_selection,
                        project_workspace_selections,
                    )
                )

            file_log_manager.singleton.log_info(
                "'template filesystem apply' - 'project' "
                "setup execution complete"
            )

            return True

        def handle_target_project_selection(project_name):
            file_log_manager.singleton.log_info(
                f"'template filesystem apply' - '{project_name}' "
                "setup execution start"
            )

            selection_project_target_full_paths = (
                value_cache_manager.singleton.get_one_value(
                    [
                        "workspace",
                        "data",
                        "selection",
                        "project",
                        "targets",
                        project_name,
                        "full-path",
                    ],
                    output_type=TargetCacheValue.DEFINED,
                )
            )

            for (
                current_scope_name
            ) in workspace_filesystem_manager.singleton.scope_selections:
                for current_template_type in ["filesystem", "fragment"]:
                    filesystem_manager.singleton.copy_filesystem_path(
                        f"{current_root_full_path}/workspace/{current_scope_name}/template/all/{current_template_type}",
                        f"{current_root_full_path}/workspace/private/temporary/template/{current_template_type}/{project_name}",
                    )
                    filesystem_manager.singleton.copy_filesystem_path(
                        f"{current_root_full_path}/workspace/{current_scope_name}/template/project/{current_template_type}",
                        f"{current_root_full_path}/workspace/private/temporary/template/{current_template_type}/{project_name}",
                    )
                    filesystem_manager.singleton.copy_filesystem_path(
                        f"{current_root_full_path}/workspace/{
                            current_scope_name
                        }/template/project/selection/{project_name}/{
                            current_template_type
                        }",
                        f"{current_root_full_path}/workspace/private/temporary/template/{current_template_type}/{project_name}",
                    )

            for current_template_type in ["filesystem", "fragment"]:
                handle_filesystem_parsing(
                    f"{current_root_full_path}/workspace/private/temporary/template/{current_template_type}/{project_name}"
                )

            filesystem_manager.singleton.copy_filesystem_path(
                f"{current_root_full_path}/workspace/private/temporary/template/filesystem/{project_name}",
                selection_project_target_full_paths,
            )

            template_fragment_root = Path(
                f"{current_root_full_path}/workspace/private/temporary/template/fragment/{project_name}"
            )
            relative_file_paths = [
                current_relative_file_path.relative_to(template_fragment_root)
                for current_relative_file_path in template_fragment_root.rglob("*")
                if current_relative_file_path.is_file()
            ]
            for file in relative_file_paths:
                source_path = Path(
                    f"{current_root_full_path}/workspace/private/temporary/template/fragment/{project_name}/{file}"
                )
                source_data = workspace_filesystem_manager.singleton.read_file(
                    source_path
                )
                target_path = Path(f"{current_root_full_path}/{file}")
                target_data = target_data = (
                    workspace_filesystem_manager.singleton.read_file(target_path)
                )
                output_data = (
                    object_merge_manager.singleton.handle_deep_merge_fragments(
                        target_data,
                        source_data,
                    )
                )
                workspace_filesystem_manager.singleton.write_file(
                    target_path, output_data
                )

            file_log_manager.singleton.log_info(
                f"'template filesystem apply' - '{project_name}' "
                "setup execution complete"
            )

            return True

        def handle_filesystem_parsing(
            filesystem_path,
        ):
            root = Path(filesystem_path)

            for current_root, directories, files in root.walk(
                top_down=False,
            ):
                current_root = Path(current_root)

                for file_name in files:
                    current_path = current_root / file_name

                    try:
                        file_data = current_path.read_text(
                            encoding=file_io_manager.singleton.file_encoding,
                        )
                    except UnicodeDecodeError:
                        pass
                    else:
                        parsed_file_data = macros_manager.singleton.parse_one(
                            file_data,
                            workspace_macros,
                        )

                        if parsed_file_data != file_data:
                            current_path.write_text(
                                parsed_file_data,
                                encoding=file_io_manager.singleton.file_encoding,
                            )

                    parsed_name = macros_manager.singleton.parse_one(
                        current_path.name,
                        workspace_macros,
                    )

                    if parsed_name != current_path.name:
                        current_path = current_path.rename(
                            current_path.with_name(parsed_name),
                        )

                for directory_name in directories:
                    current_path = current_root / directory_name

                    parsed_name = macros_manager.singleton.parse_one(
                        current_path.name,
                        workspace_macros,
                    )

                    if parsed_name != current_path.name:
                        current_path.rename(
                            current_path.with_name(
                                parsed_name,
                            )
                        )

            return True


        file_log_manager.singleton.log_info(
                    "'template filesystem apply' - start"
                )

        targets = kwargs.get("targets", None)

        workspace_data_command_template = (
            value_cache_manager.singleton.get_one_value(
                [
                    "workspace",
                    "data",
                    "command",
                    "template",
                ],
                output_type=TargetCacheValue.ANY,
            )
            or {}
        ) or {}
        workspace_data_command_template_is_enabled = (
            workspace_data_command_template["is-enabled"]
            if workspace_data_command_template
            and "is-enabled" in workspace_data_command_template
            else {}
        ) or {}
        
        workspace_data_command_template_is_enabled_value = (
            workspace_data_command_template_is_enabled["value"]
            if workspace_data_command_template_is_enabled
            and "value" in workspace_data_command_template_is_enabled
            else True
        )

        if not workspace_data_command_template_is_enabled_value:
            log_manager.singleton.log_warning(
                "'template filesystem apply' - workspace property "
                "'data.selection.is-enabled.value' may be set to 'false'"
            )

            return False

        workspace_macros = (
            value_cache_manager.singleton.get_one_value(
                ["workspace-macros"],
                output_type=TargetCacheValue.DEFINED,
            )
            or {}
        ) or {}

        workspace_data_command_template_cleanup = (
            workspace_data_command_template["cleanup"]
            if workspace_data_command_template
            and "cleanup" in workspace_data_command_template
            else {}
        ) or {}

        workspace_data_command_template_cleanup_is_enabled = (
            workspace_data_command_template_cleanup["is-enabled"]
            if workspace_data_command_template_cleanup
            and "is-enabled" in workspace_data_command_template_cleanup
            else {}
        ) or {}

        workspace_data_command_template_cleanup_is_enabled_value = (
            workspace_data_command_template_cleanup_is_enabled["value"]
            if workspace_data_command_template_cleanup_is_enabled
            and "value" in workspace_data_command_template_cleanup_is_enabled
            else True
        )

        workspace_selections = (
            value_cache_manager.singleton.get_one_value(
                ["workspace-selections"],
                output_type=TargetCacheValue.DEFINED,
            )
            or {}
        ) or {}

        project_workspace_selections = (
            value_cache_manager.singleton.get_one_value(
                ["project-workspace-selections"],
                output_type=TargetCacheValue.DEFINED,
            )
            or {}
        ) or {}

        group_workspace_selections = (
            value_cache_manager.singleton.get_one_value(
                ["group-workspace-selections"],
                output_type=TargetCacheValue.DEFINED,
            )
            or {}
        ) or {}

        current_root_full_path = value_cache_manager.singleton.get_one_value(
            ["current-root-full-path"],
            output_type=TargetCacheValue.FOLDER_PATH,
        )

        if workspace_data_command_template_cleanup_is_enabled_value:
            filesystem_manager.singleton.clean_filesystem_path(
                f"{current_root_full_path}/workspace/private/temporary/template"
            )

        tasks = []

        for target in targets:
            if (
                not target
                or target not in workspace_selections
            ):
                log_manager.singleton.log_warning(
                    f"'template filesystem apply' - selection "
                    f"'{target}' does not exist within either "
                    "workspace properties "
                    "'data.selection.project.target', or "
                    "'data.selection.group.target'"
                )
                return False

            if target == "all":
                tasks.extend(
                    [
                        (handle_target_root,),
                        (handle_target_group,),
                        (handle_target_project,),
                    ]
                )

            elif target == "root":
                tasks.append((handle_target_root,))

            elif target == "group":
                tasks.append((handle_target_group,))

            elif target == "project":
                tasks.append((handle_target_project,))

            elif target in group_workspace_selections:
                tasks.append(
                    (
                        handle_target_group_selection,
                        target,
                    )
                )

            elif target in project_workspace_selections:
                tasks.append(
                    (
                        handle_target_project_selection,
                        target,
                    )
                )

        for task in tasks:
            if len(task) == 1:
                task[0]()
            else:
                task[0](task[1])


        file_log_manager.singleton.log_info(
            "'template filesystem apply' - complete"
        )

        return True


singleton = CliCommandManager()
