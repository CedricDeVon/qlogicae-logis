from __future__ import annotations

import os
import secrets
import shutil
import string
from pathlib import Path

import pytest

ROUNDS = 30
ITERATIONS = 50_000
WARMUP_ROUNDS = 10

DEPTH = 5
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


def populate(
    directory: Path,
    depth: int,
    file_data: bytes,
) -> None:
    for index in range(FILES_PER_DIRECTORY):
        (
            directory
            / f"file_{index}.bin"
        ).write_bytes(
            file_data,
        )

    if depth == 0:
        return

    for index in range(DIRECTORIES_PER_LEVEL):
        child = (
            directory
            / f"directory_{index}"
        )

        child.mkdir()

        populate(
            child,
            depth - 1,
            file_data,
        )


@pytest.fixture(scope="session")
def filesystem_fixture(
    tmp_path_factory: pytest.TempPathFactory,
) -> dict[str, Path]:
    workspace = tmp_path_factory.mktemp(
        "filesystem",
    )

    try:
        source = workspace / "source"
        source.mkdir()

        populate(
            source,
            DEPTH,
            os.urandom(FILE_SIZE),
        )

        renamed = workspace / "renamed"

        yield {
            "workspace": workspace,
            "source": source,
            "renamed": renamed,
        }

    finally:
        shutil.rmtree(
            workspace,
            ignore_errors=True,
        )


def benchmark_pathlib_rename(
    source: Path,
    destination: Path,
) -> None:
    source.rename(destination)
    destination.rename(source)


def benchmark_pathlib_replace(
    source: Path,
    destination: Path,
) -> None:
    source.replace(destination)
    destination.replace(source)


def benchmark_os_rename(
    source: Path,
    destination: Path,
) -> None:
    os.rename(
        source,
        destination,
    )

    os.rename(
        destination,
        source,
    )


def benchmark_os_replace(
    source: Path,
    destination: Path,
) -> None:
    os.replace(
        source,
        destination,
    )

    os.replace(
        destination,
        source,
    )


def test_pathlib_rename(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
) -> None:
    benchmark.pedantic(
        benchmark_pathlib_rename,
        args=(
            filesystem_fixture["source"],
            filesystem_fixture["renamed"],
        ),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


def test_pathlib_replace(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
) -> None:
    benchmark.pedantic(
        benchmark_pathlib_replace,
        args=(
            filesystem_fixture["source"],
            filesystem_fixture["renamed"],
        ),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


def test_os_rename(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
) -> None:
    benchmark.pedantic(
        benchmark_os_rename,
        args=(
            filesystem_fixture["source"],
            filesystem_fixture["renamed"],
        ),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


def test_os_replace(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
) -> None:
    benchmark.pedantic(
        benchmark_os_replace,
        args=(
            filesystem_fixture["source"],
            filesystem_fixture["renamed"],
        ),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_rename.py
# ================================================================================================== test session starts ===================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 4 items

# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_rename.py::test_pathlib_rename PASSED                                                                                                                     [ 25%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_rename.py::test_pathlib_replace PASSED                                                                                                                    [ 50%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_rename.py::test_os_rename PASSED                                                                                                                          [ 75%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_rename.py::test_os_replace PASSED                                                                                                                         [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0276_latest.json



# ----------------------------------------------------------------------- benchmark: 4 tests ----------------------------------------------------------------------
# Name (time in us)           Min               Max              Mean            StdDev            Median               IQR            Outliers  Rounds  Iterations
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_os_replace          4.2589 (1.0)      4.4764 (1.0)      4.3659 (1.0)      0.0399 (1.23)     4.3582 (1.0)      0.0375 (1.0)           5;3      30       50000
# test_os_rename           4.3505 (1.02)     4.4898 (1.00)     4.4014 (1.01)     0.0324 (1.0)      4.4047 (1.01)     0.0405 (1.08)          9;1      30       50000
# test_pathlib_rename      4.4181 (1.04)     4.5570 (1.02)     4.4692 (1.02)     0.0329 (1.01)     4.4617 (1.02)     0.0480 (1.28)         10;0      30       50000
# test_pathlib_replace     4.4271 (1.04)     4.5875 (1.02)     4.4754 (1.03)     0.0335 (1.04)     4.4683 (1.03)     0.0465 (1.24)          7;1      30       50000
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# =================================================================================================== 4 passed in 36.80s ==================================================================================================
