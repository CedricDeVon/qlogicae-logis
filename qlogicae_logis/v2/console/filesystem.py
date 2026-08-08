from __future__ import annotations

from pathlib import Path
from typing import Any

import typer

app_filesystem = typer.Typer()
app_filesystem_tree = typer.Typer()
app_filesystem_clean = typer.Typer()
app_filesystem_clean_list = typer.Typer()

app_filesystem.add_typer(
    app_filesystem_tree,
    name="tree",
    help="Filesystem tree management.",
)
app_filesystem.add_typer(
    app_filesystem_clean,
    name="clean",
    help="Safe filesystem cleaning.",
)
app_filesystem_clean.add_typer(
    app_filesystem_clean_list,
    name="list",
    help="Show list information.",
)


_SingletonManager: Any = None
_CommandManager: Any = None

def _handle_dynamic_imports() -> None:
    global _handle_dynamic_imports
    global _SingletonManager
    global _CommandManager

    from qlogicae_cor.v1.library import (
        singleton_manager,
    )

    from qlogicae_logis.v2.library import (
        command_manager,
    )

    _SingletonManager = (
        singleton_manager.SingletonManager
    )
    _CommandManager = (
        command_manager.CommandManager
    )

    _handle_dynamic_imports = lambda: None

@app_filesystem.command(
    name="copy",
    help="Copy filesystem entities.",
)
def copy(
    source_path: Path = typer.Option(
        ...,
        "--source-path",
        "-sp",
        exists=True,
        file_okay=True,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        help="Filesystem source path.",
    ),
    target_paths: list[Path] = typer.Option(
        ...,
        "--target-paths",
        "-tp",
        exists=False,
        file_okay=True,
        dir_okay=True,
        writable=True,
        resolve_path=True,
        help="Filesystem target paths",
    ),
    overwrite: bool = typer.Option(
        False,
        "--overwrite/--no-overwrite",
        "-o/-no",
        help="",
    ),
) -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _CommandManager
    ).run_command_filesystem_copy(
        source_path=source_path,
        target_paths=target_paths,
        overwrite=overwrite,
    )

    return True


@app_filesystem.command(
    name="move",
    help="Move filesystem entities.",
)
def move(
    source_path: Path = typer.Option(
        ...,
        "--source-path",
        "-sp",
        exists=True,
        file_okay=True,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        help="Filesystem source path.",
    ),
    target_path: Path = typer.Option(
        ...,
        "--target-paths",
        "-tp",
        exists=False,
        file_okay=True,
        dir_okay=True,
        writable=True,
        resolve_path=True,
        help="Filesystem target path.",
    ),
    overwrite: bool = typer.Option(
        False,
        "--overwrite/--no-overwrite",
        "-o/-no",
        help="",
    ),
) -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _CommandManager
    ).run_command_filesystem_move(
        source_path=source_path,
        target_path=target_path,
        overwrite=overwrite,
    )

    return True


@app_filesystem.command(
    name="rename",
    help="Rename filesystem entities.",
)
def rename(
    old_path: Path = typer.Option(
        ...,
        "--old-path",
        "-op",
        exists=True,
        file_okay=True,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        help="Old file or folder name.",
    ),
    new_path: Path = typer.Option(
        ...,
        "--new-path",
        "-np",
        exists=False,
        file_okay=True,
        dir_okay=True,
        writable=True,
        resolve_path=True,
        help="New file or folder name.",
    ),
) -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _CommandManager
    ).run_command_filesystem_rename(
        old_path=old_path,
        new_path=new_path,
    )

    return True


@app_filesystem_tree.command(
    name="setup",
    help="Setup filesystem tree.",
)
def setup(
    target_paths: list[Path] = typer.Option(
        ...,
        "--target-paths",
        "-tp",
        exists=False,
        file_okay=False,
        dir_okay=True,
        writable=True,
        resolve_path=True,
        help="Multiple folder paths",
    ),
) -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _CommandManager
    ).run_command_filesystem_tree_setup(
        target_paths=target_paths
    )

    return True


@app_filesystem_clean.command(
    name="path",
    help="Filesystem path cleaning.",
)
def path(
    target_paths: list[Path] = typer.Option(
        ...,
        "--target-paths",
        "-tp",
        exists=True,
        file_okay=True,
        dir_okay=True,
        writable=True,
        resolve_path=True,
        help="List of cleaning filesystem paths.",
    ),
) -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _CommandManager
    ).run_command_filesystem_clean_path(
        target_paths=target_paths
    )

    return True


@app_filesystem_clean.command(
    name="selection",
    help="Filesystem paths based on a selection.",
)
def selection(
    targets: list[str] = typer.Argument(
        ...,
        help="List of cleaning targets.",
    ),
) -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _CommandManager
    ).run_command_filesystem_clean_selection(
        targets=targets
    )

    return True


@app_filesystem_clean_list.command(
    name="included",
    help="Show selections and whitelisted filesystem paths.",
)
def included() -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _CommandManager
    ).run_command_filesystem_clean_list_included()

    return True


@app_filesystem_clean_list.command(
    name="excluded",
    help="Show blacklisted filesystem paths.",
)
def excluded() -> bool:
    _handle_dynamic_imports()

    _SingletonManager.get_singleton(
        _CommandManager
    ).run_command_filesystem_clean_list_excluded()

    return True
