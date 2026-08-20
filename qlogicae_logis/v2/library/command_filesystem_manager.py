from __future__ import annotations

from typing import Any

_Path: Any = None
_chain: Any = None
_LogManager: Any = None
_DatabaseManager: Any = None
_SingletonManager: Any = None
_FilesystemManager: Any = None
_ThreadPoolExecutor: Any = None
_ConsoleDisplayManager: Any = None
_CommandUtilityManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _Path
    global _chain
    global _LogManager
    global _DatabaseManager
    global _SingletonManager
    global _FilesystemManager
    global _ThreadPoolExecutor
    global _ConsoleDisplayManager
    global _CommandUtilityManager

    from concurrent.futures import ThreadPoolExecutor
    from itertools import chain
    from pathlib import Path

    from qlogicae_cor.v1.library import (
        console_display_manager,
        filesystem_manager,
        singleton_manager,
    )

    from qlogicae_logis.v2.library import (
        command_utility_manager,
        database_manager,
        log_manager,
    )

    _Path = Path
    _chain = chain
    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _DatabaseManager = (
        database_manager.DatabaseManager
    )
    _ConsoleDisplayManager = (
        console_display_manager.ConsoleDisplayManager
    )
    _LogManager = (
        log_manager.LogManager
    )
    _FilesystemManager = (
        filesystem_manager.FilesystemManager
    )
    _ThreadPoolExecutor = (
        ThreadPoolExecutor
    )
    _CommandUtilityManager = (
        command_utility_manager.CommandUtilityManager
    )

    _handle_dynamic_imports = lambda: None

class CommandFilesystemManager:
    def __init__(self) -> None:
        _handle_dynamic_imports()

    def run_command_filesystem_clean_list_included(self) -> bool:
        log_manager = _SingletonManager.get_singleton(
            _LogManager
        )
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )
        console_display_manager = _SingletonManager.get_singleton(
            _ConsoleDisplayManager
        )
        command_utility_manager = _SingletonManager.get_singleton(
            _CommandUtilityManager
        )

        outputs: list[str] = []
        filesystem_clean_selection_include_items = list(
            database_manager
                .filesystem_clean_selection_include.items()
        )
        workspace_data_macros_default_on_parse_is_enabled_value = (
            database_manager
                .workspace_data_macros_default_on_parse_is_enabled_value
        )

        filesystem_clean_selection_include_items.sort()

        for key, item in filesystem_clean_selection_include_items:
            if not item:
                log_manager.full_log_warning(
                    "invalid arguments"
                )
                continue

            item.sort()

            for sub_item in item:
                if not sub_item or "filesystem-path" not in sub_item:
                    log_manager.full_log_warning(
                        "invalid arguments"
                    )
                    continue

                sub_item = sub_item["filesystem-path"]
                if not sub_item:
                    log_manager.full_log_warning(
                        "invalid arguments"
                    )
                    continue

                sub_item = sub_item["value"]
                if not sub_item:
                    log_manager.full_log_warning(
                        "invalid arguments"
                    )
                    continue

                if workspace_data_macros_default_on_parse_is_enabled_value:
                    sub_item = command_utility_manager.parse_many(
                        sub_item
                    )

                outputs.append(
                    f"[red]{key} <- {sub_item}[/]"
                )

        console_display_manager.render_one_component(
            "\n".join(outputs)
        )

        return True

    def run_command_filesystem_clean_list_excluded(self) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )
        console_display_manager = _SingletonManager.get_singleton(
            _ConsoleDisplayManager
        )
        command_utility_manager = _SingletonManager.get_singleton(
            _CommandUtilityManager
        )


        filesystem_clean_selection_exclude_items = list(
            database_manager
                .filesystem_clean_selection_exclude
        )
        workspace_data_macros_default_on_parse_is_enabled_value = (
            database_manager
                .workspace_data_macros_default_on_parse_is_enabled_value
        )


        filesystem_clean_selection_exclude_items.sort()

        outputs: Any = tuple()
        if workspace_data_macros_default_on_parse_is_enabled_value:
            outputs = tuple(
                f"[green]{
                    command_utility_manager.parse_many(
                        item
                    )
                }[/]"
                for item
                in filesystem_clean_selection_exclude_items
            )

        else:
            outputs = tuple(
                f"[green]{
                    item
                }[/]"
                for item
                in filesystem_clean_selection_exclude_items
            )

        console_display_manager.render_one_component(
            "\n".join(
                _chain(
                    outputs,
                )
            )
        )

        return True

    def run_command_filesystem_setup(
        self,
    ) -> bool:
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        workspace_data_command_filesystem_clean_default_include_is_enabled_value = (
            database_manager
                .workspace_data_command_filesystem_clean_default_include_is_enabled_value
        )
        workspace_data_command_filesystem_clean_default_exclude_is_enabled_value = (
            database_manager
                .workspace_data_command_filesystem_clean_default_exclude_is_enabled_value
        )

        filesystem_clean_selection_include: Any = {}
        if workspace_data_command_filesystem_clean_default_include_is_enabled_value:
            filesystem_clean_selection_include = (
                self.setup_default_clean_include_filesystem_paths()
            )

        filesystem_clean_selection_exclude: Any = {}
        if workspace_data_command_filesystem_clean_default_exclude_is_enabled_value:
            filesystem_clean_selection_exclude = (
                self.setup_default_clean_exclude_filesystem_paths()
            )

        database_manager.filesystem_clean_selection_include = (
            filesystem_clean_selection_include |
            self.setup_clean_include_filesystem_paths(
                    database_manager
                        .workspace_data_command_filesystem_clean_include_targets,
            )
        )
        database_manager.filesystem_clean_selection_exclude = (
            filesystem_clean_selection_exclude |
            self.setup_clean_exclude_filesystem_paths(
                    database_manager
                        .workspace_data_command_filesystem_clean_exclude_targets,
            )
        )

        return True


    def run_command_filesystem_copy(
        self,
        **kwargs: Any,
    ) -> bool:
        log_manager = _SingletonManager.get_singleton(
            _LogManager
        )

        source_path = kwargs.get("source_path", None)
        target_paths = kwargs.get("target_paths", [])

        if not source_path or not len(target_paths):
            log_manager.full_log_warning(
                "invalid arguments"
            )
            return False

        filesystem_manager = _SingletonManager.get_singleton(
            _FilesystemManager
        )
        source_path = _Path(
            source_path
        )

        for target_path in target_paths:
            if not target_path:
                log_manager.full_log_warning(
                    "invalid arguments"
                )
                continue

            filesystem_manager.copy_filesystem_path(
                source_path,
                _Path(
                    target_path
                )
            )

        return True

    def run_command_filesystem_move(
        self,
        **kwargs: Any,
    ) -> bool:
        source_path = kwargs.get("source_path", None)
        target_path = kwargs.get("target_path", None)

        if not source_path or not target_path:
            _SingletonManager.get_singleton(
                _LogManager
            ).full_log_warning(
                "invalid arguments"
            )
            return False

        filesystem_manager = _SingletonManager.get_singleton(
            _FilesystemManager
        )
        filesystem_manager.move_filesystem_path(
            _Path(
                source_path
            ),
            _Path(
                target_path
            )
        )

        return True

    def run_command_filesystem_tree_setup(
        self,
        **kwargs: Any,
    ) -> bool:
        log_manager = _SingletonManager.get_singleton(
            _LogManager
        )

        target_paths = kwargs.get("target_paths", [])

        if not target_paths or not len(target_paths):
            log_manager.full_log_warning(
                "invalid arguments"
            )
            return False

        filesystem_manager = _SingletonManager.get_singleton(
            _FilesystemManager
        )
        for target_path in target_paths:
            if not target_path:
                log_manager.full_log_warning(
                    "invalid arguments"
                )
                continue

            filesystem_manager.setup_filesystem_tree_path(
                _Path(
                    target_path
                )
            )

        return True

    def run_command_filesystem_rename(
        self,
        **kwargs: Any,
    ) -> bool:
        old_path = kwargs.get("old_path", None)
        new_path = kwargs.get("new_path", None)

        if not old_path or not new_path:
            _SingletonManager.get_singleton(
                _LogManager
            ).full_log_warning(
                "invalid arguments"
            )
            return False

        _SingletonManager.get_singleton(
            _FilesystemManager
        ).rename_filesystem_entity(
            _Path(
                old_path
            ),
            _Path(
                new_path
            )
        )

        return True


    def run_command_filesystem_clean_path(
        self,
        **kwargs: Any,
    ) -> bool:
        log_manager = _SingletonManager.get_singleton(
            _LogManager
        )

        target_paths = kwargs.get("target_paths", [])

        if not target_paths or not len(target_paths):
            log_manager.full_log_warning(
                "invalid arguments"
            )
            return False

        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )
        filesystem_manager = _SingletonManager.get_singleton(
            _FilesystemManager
        )
        filesystem_clean_selection_exclude = (
            database_manager
                .filesystem_clean_selection_exclude
        )

        for target_path in target_paths:
            if not target_path:
                log_manager.full_log_warning(
                    "invalid arguments"
                )
                continue

            if target_path in filesystem_clean_selection_exclude:
                log_manager.full_log_warning(
                    f"'{target_path}' "
                    "is a blacklisted filesystem path"
                )
                continue

            filesystem_manager.clean_filesystem_path(
                _Path(
                    target_path
                )
            )

        return True

    def run_command_filesystem_clean_selection(
        self,
        **kwargs: Any,
    ) -> bool:
        log_manager = _SingletonManager.get_singleton(
            _LogManager
        )
        database_manager = _SingletonManager.get_singleton(
            _DatabaseManager
        )

        targets = kwargs.get("targets", [])

        is_enabled = (
            database_manager
                .workspace_data_command_filesystem_clean_is_enabled_value
        )

        if not is_enabled:
            log_manager.full_log_warning(
                "workspace property "
                "'data.command.clean.is-enabled.value' "
                "has been set to 'false'"
            )
            return False

        filesystem_manager = _SingletonManager.get_singleton(
            _FilesystemManager
        )
        command_utility_manager = _SingletonManager.get_singleton(
            _CommandUtilityManager
        )
        filesystem_paths: list[str] = []
        filesystem_clean_selection_include = (
            database_manager
                .filesystem_clean_selection_include
        )
        filesystem_clean_selection_exclude = (
            database_manager
                .filesystem_clean_selection_exclude
        )
        workspace_data_macros_default_on_parse_is_enabled_value = (
            database_manager
                .workspace_data_macros_default_on_parse_is_enabled_value
        )

        for target in targets:
            if (
                not target
                or target not in filesystem_clean_selection_include
            ):
                log_manager.full_log_warning(
                    f"'{target}' "
                    "is not an item within the "
                    "'data.command.clean.include' workspace property"
                )
                return False

            for current_item_target in filesystem_clean_selection_include[target]:
                if (
                    not current_item_target
                    or "filesystem-path" not in current_item_target
                ):
                    log_manager.full_log_warning(
                        "workspace property "
                        "'data.command.clean.include.targets' "
                        "items must include a 'filesystem-path' "
                        "filesystem property"
                    )
                    return False

                current_filesystem_path = (
                    current_item_target["filesystem-path"]
                )

                if (
                    not current_filesystem_path
                    or current_filesystem_path
                    in filesystem_clean_selection_exclude
                ):
                    log_manager.full_log_warning(
                        f"'{current_filesystem_path}' "
                        "is a blacklisted filesystem path"
                    )
                    return False

                if workspace_data_macros_default_on_parse_is_enabled_value:
                    current_filesystem_path = (
                        command_utility_manager.parse_many(
                            current_filesystem_path
                        )
                    )

                filesystem_paths.append(
                    current_filesystem_path
                )


        max_workers = min(
            32,
            len(filesystem_paths) or 1,
        )

        with _ThreadPoolExecutor(
            max_workers=max_workers,
        ) as executor:
            tuple(
                executor.map(
                    filesystem_manager.clean_filesystem_path,
                    filesystem_paths,
                )
            )

            return True

    def setup_default_clean_exclude_filesystem_paths(
        self,
    ) -> set[str]:
        outputs: set[str] = set()

        root_path = _Path().resolve()
        qlogicae_paths = _Path(
            f"{root_path}/.{
                _SingletonManager.get_singleton(
                    _DatabaseManager
                ).company_name
            }"
        )
        selection_paths = _Path(
            f"{root_path}/selection"
        )

        outputs.update(
            f"{path}"
            for path
            in root_path.parents
        )

        if qlogicae_paths.is_dir():
            qlogicae_paths = (
                qlogicae_paths.glob("**/*")
            )

            outputs.update(
                f"{path}"
                for path
                in qlogicae_paths
                if path.is_dir()
            )

        if selection_paths.is_dir():
            selection_paths = selection_paths.iterdir()

            outputs.update(
                f"{path}"
                for path
                in selection_paths
            )

        return outputs

    def setup_default_clean_include_filesystem_paths(
        self,
    ) -> Any:
        outputs: Any = {}
        root_path = _Path().resolve()
        company_project_major_version_path = (
            _SingletonManager.get_singleton(
                _DatabaseManager
            ).setup_company_project_major_version(
                "/"
            )
        )

        outputs = {
            "temporary": {
                "alias": {
                    "targets": [
                        {
                            "name": {
                                "value": "tmp"
                            }
                        }
                    ]
                },
                "targets": [
                    {
                        "filesystem-path": {
                            "value": f"{root_path}/.{
                                company_project_major_version_path
                            }/private/temporary"
                        },
                        "pattern": {
                            "value": "**"
                        }
                    }
                ]
            }
        }

        return outputs

    def setup_clean_exclude_filesystem_paths(
        self,
        targets: Any,
    ) -> Any:
        return self.setup_clean_target_filesystem_paths(
            targets
        )

    def setup_clean_include_filesystem_paths(
        self,
        targets: Any,
    ) -> Any:
        return (targets or {})

    def setup_clean_target_filesystem_paths(
        self,
        targets: Any,
    ) -> set[str]:
        log_manager = _SingletonManager.get_singleton(
            _LogManager
        )
        outputs: set[str] = set()

        for target in targets:
            if not target or "filesystem-path" not in target:
                log_manager.full_log_warning(
                    "invalid arguments"
                )
                continue

            filesystem_path = (
                target["filesystem-path"]
            )

            if not filesystem_path or "value" not in filesystem_path:
                log_manager.full_log_warning(
                    "invalid arguments"
                )
                continue

            filesystem_path = (
                filesystem_path["value"]
            )

            if not filesystem_path:
                log_manager.full_log_warning(
                    "invalid arguments"
                )
                continue

            pattern = (
                target["pattern"]
                if target
                and "pattern" in target
                else {}
            ) or {}
            pattern = (
                pattern["value"]
                if pattern
                and"value" in pattern
                else  None
            )

            if pattern:
                matches = tuple(
                    _Path(
                        filesystem_path
                    ).glob(pattern)
                )
                if matches:
                    outputs.update(
                        matches
                    )
                else:
                    outputs.add(
                        filesystem_path
                    )
            else:
                outputs.add(
                    filesystem_path
                )

        return outputs
