from __future__ import annotations

import os
import secrets
import shutil
import string
from pathlib import Path

import pytest

ROUNDS = 30
ITERATIONS = 100
WARMUP_ROUNDS = 10

DEPTH = 5
DIRECTORIES_PER_LEVEL = 2
FILES_PER_DIRECTORY = 2
FILE_SIZE = 128

NAME_LENGTH = 10


def random_name(length: int = NAME_LENGTH) -> str:
    alphabet = string.ascii_letters + string.digits

    return "".join(
        secrets.choice(alphabet)
        for _ in range(length)
    )


def populate(
    directory: Path,
    depth: int,
) -> None:
    for _ in range(FILES_PER_DIRECTORY):
        (
            directory
            / f"{random_name()}.bin"
        ).write_bytes(
            os.urandom(FILE_SIZE)
        )

    if depth == 0:
        return

    for _ in range(DIRECTORIES_PER_LEVEL):
        child = directory / random_name()
        child.mkdir()

        populate(
            child,
            depth - 1,
        )


@pytest.fixture(scope="session")
def filesystem_fixture(
    tmp_path_factory: pytest.TempPathFactory,
) -> dict[str, Path]:
    workspace = tmp_path_factory.mktemp("filesystem")

    source = workspace / "source"
    destination = workspace / "destination"

    source.mkdir()
    destination.mkdir()

    populate(
        source,
        DEPTH,
    )

    yield {
        "workspace": workspace,
        "source": source,
        "destination": destination,
    }

    shutil.rmtree(
        workspace,
        ignore_errors=True,
    )


def benchmark_copytree(
    source: Path,
    destination_root: Path,
    copy_function,
) -> int:
    destination = destination_root / random_name()

    shutil.copytree(
        src=source,
        dst=destination,
        copy_function=copy_function,
    )

    count = sum(
        1
        for _ in destination.rglob("*")
    )

    shutil.rmtree(
        destination,
        ignore_errors=True,
    )

    return count


def test_copytree_copyfile(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
) -> None:
    result = benchmark.pedantic(
        benchmark_copytree,
        args=(
            filesystem_fixture["source"],
            filesystem_fixture["destination"],
            shutil.copyfile,
        ),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )

    assert result > 0


def test_copytree_copy(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
) -> None:
    result = benchmark.pedantic(
        benchmark_copytree,
        args=(
            filesystem_fixture["source"],
            filesystem_fixture["destination"],
            shutil.copy,
        ),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )

    assert result > 0


def test_copytree_copy2(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
) -> None:
    result = benchmark.pedantic(
        benchmark_copytree,
        args=(
            filesystem_fixture["source"],
            filesystem_fixture["destination"],
            shutil.copy2,
        ),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )

    assert result > 0


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_copy.py
# ================================================================================================== test session starts ===================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 3 items

# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_copy.py::test_copytree_copyfile PASSED                                                                                                                    [ 33%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_copy.py::test_copytree_copy PASSED                                                                                                                        [ 66%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_copy.py::test_copytree_copy2 PASSED                                                                                                                       [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0265_latest.json



# ------------------------------------------------------------------------ benchmark: 3 tests -----------------------------------------------------------------------
# Name (time in ms)             Min               Max              Mean            StdDev            Median               IQR            Outliers  Rounds  Iterations
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_copytree_copyfile     4.8895 (1.0)      5.0042 (1.0)      4.9357 (1.0)      0.0312 (1.17)     4.9292 (1.0)      0.0418 (1.31)         10;0      30         100
# test_copytree_copy         5.3575 (1.10)     5.4677 (1.09)     5.4010 (1.09)     0.0266 (1.0)      5.4023 (1.10)     0.0321 (1.0)           8;1      30         100
# test_copytree_copy2        5.7616 (1.18)     5.9982 (1.20)     5.8706 (1.19)     0.0712 (2.68)     5.8495 (1.19)     0.1269 (3.96)          8;0      30         100
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ============================================================================================== 3 passed in 66.30s (0:01:06) ==============================================================================================
