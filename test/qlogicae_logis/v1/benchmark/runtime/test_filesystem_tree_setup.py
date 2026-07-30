from __future__ import annotations

import os
import secrets
import shutil
import string
from pathlib import Path

import pytest

ROUNDS = 30
ITERATIONS = 10
WARMUP_ROUNDS = 10

DEPTH = 10
DIRECTORIES_PER_LEVEL = 2
FILES_PER_DIRECTORY = 2

FILE_SIZE = 128
NAME_LENGTH = 10


def random_name(
    length: int = NAME_LENGTH,
) -> str:
    alphabet = (
        string.ascii_letters
        + string.digits
    )

    return "".join(
        secrets.choice(alphabet)
        for _ in range(length)
    )


@pytest.fixture(scope="session")
def filesystem_fixture(
    tmp_path_factory: pytest.TempPathFactory,
) -> dict[str, object]:
    workspace = tmp_path_factory.mktemp(
        "filesystem",
    )

    file_data = os.urandom(FILE_SIZE)

    yield {
        "workspace": workspace,
        "file_data": file_data,
    }

    shutil.rmtree(
        workspace,
        ignore_errors=True,
    )


def populate_pathlib(
    root: Path,
    depth: int,
    file_data: bytes,
) -> None:
    for _ in range(FILES_PER_DIRECTORY):
        (
            root
            / f"{random_name()}.bin"
        ).write_bytes(
            file_data,
        )

    if depth == 0:
        return

    for _ in range(DIRECTORIES_PER_LEVEL):
        child = (
            root
            / random_name()
        )

        child.mkdir()

        populate_pathlib(
            child,
            depth - 1,
            file_data,
        )


def populate_os(
    root: str,
    depth: int,
    file_data: bytes,
) -> None:
    for _ in range(FILES_PER_DIRECTORY):
        path = os.path.join(
            root,
            f"{random_name()}.bin",
        )

        with open(
            path,
            "wb",
        ) as file:
            file.write(file_data)

    if depth == 0:
        return

    for _ in range(DIRECTORIES_PER_LEVEL):
        child = os.path.join(
            root,
            random_name(),
        )

        os.mkdir(child)

        populate_os(
            child,
            depth - 1,
            file_data,
        )


def benchmark_pathlib(
    workspace: Path,
    file_data: bytes,
) -> None:
    root = workspace / random_name()

    root.mkdir()

    try:
        populate_pathlib(
            root,
            DEPTH,
            file_data,
        )
    finally:
        shutil.rmtree(
            root,
            ignore_errors=True,
        )


def benchmark_os(
    workspace: Path,
    file_data: bytes,
) -> None:
    root = os.path.join(
        workspace,
        random_name(),
    )

    os.mkdir(root)

    try:
        populate_os(
            root,
            DEPTH,
            file_data,
        )
    finally:
        shutil.rmtree(
            root,
            ignore_errors=True,
        )


def test_pathlib_tree_creation(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, object],
) -> None:
    benchmark.pedantic(
        benchmark_pathlib,
        args=(
            filesystem_fixture["workspace"],
            filesystem_fixture["file_data"],
        ),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


def test_os_tree_creation(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, object],
) -> None:
    benchmark.pedantic(
        benchmark_os,
        args=(
            filesystem_fixture["workspace"],
            filesystem_fixture["file_data"],
        ),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )



# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_tree_setup.py
# ================================================================================================== test session starts ===================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 2 items                                                                                                                                                                                                        

# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_tree_setup.py::test_pathlib_tree_creation PASSED                                                                                                          [ 50%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_tree_setup.py::test_os_tree_creation PASSED                                                                                                               [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0243_latest.json



# ------------------------------------------------------------------------------ benchmark: 2 tests -----------------------------------------------------------------------------
# Name (time in ms)                   Min                 Max                Mean            StdDev              Median               IQR            Outliers  Rounds  Iterations
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_os_tree_creation           94.8820 (1.0)       96.8536 (1.0)       95.6275 (1.0)      0.5908 (1.0)       95.4651 (1.0)      0.8245 (1.0)          11;0      30          10
# test_pathlib_tree_creation     132.5954 (1.40)     143.8286 (1.49)     135.9015 (1.42)     3.0358 (5.14)     135.3167 (1.42)     2.9689 (3.60)          7;3      30          10
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ============================================================================================== 2 passed in 93.90s (0:01:33) ==============================================================================================