from __future__ import annotations

import os
import secrets
import shutil
import string
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

ROUNDS = 100
ITERATIONS = 1
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
        ).write_bytes(file_data)

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
def filesystem_fixture() -> dict[str, Path]:
    with TemporaryDirectory(
        prefix="filesystem_",
    ) as directory:
        workspace = Path(directory)

        template = workspace / "template"
        template.mkdir()

        populate(
            template,
            DEPTH,
            os.urandom(FILE_SIZE),
        )

        yield {
            "workspace": workspace,
            "template": template,
        }

def setup_move(
    workspace: Path,
    template: Path,
) -> tuple[tuple[Path, Path], dict[str, object]]:
    source = workspace / "source"
    destination = workspace / "destination"

    shutil.rmtree(source, ignore_errors=True)
    shutil.rmtree(destination, ignore_errors=True)

    shutil.copytree(
        template,
        source,
    )

    return (
        (
            source,
            destination,
        ),
        {},
    )

def teardown_move(
    workspace: Path,
) -> None:
    shutil.rmtree(
        workspace / "source",
        ignore_errors=True,
    )

    shutil.rmtree(
        workspace / "destination",
        ignore_errors=True,
    )


def pathlib_move(
    source: Path,
    destination: Path,
) -> None:
    source.rename(destination)


def pathlib_replace(
    source: Path,
    destination: Path,
) -> None:
    source.replace(destination)


def os_move(
    source: Path,
    destination: Path,
) -> None:
    os.rename(
        source,
        destination,
    )


def os_replace(
    source: Path,
    destination: Path,
) -> None:
    os.replace(
        source,
        destination,
    )


def shutil_move(
    source: Path,
    destination: Path,
) -> None:
    shutil.move(
        source,
        destination,
    )


def benchmark_move(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
    function,
) -> None:
    benchmark.pedantic(
        function,
        setup=lambda: setup_move(
            filesystem_fixture["workspace"],
            filesystem_fixture["template"],
        ),
        teardown=lambda *_: teardown_move(
            filesystem_fixture["workspace"],
        ),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


def test_pathlib_move(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
) -> None:
    benchmark_move(
        benchmark,
        filesystem_fixture,
        pathlib_move,
    )


def test_pathlib_replace(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
) -> None:
    benchmark_move(
        benchmark,
        filesystem_fixture,
        pathlib_replace,
    )


def test_os_move(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
) -> None:
    benchmark_move(
        benchmark,
        filesystem_fixture,
        os_move,
    )


def test_os_replace(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
) -> None:
    benchmark_move(
        benchmark,
        filesystem_fixture,
        os_replace,
    )


def test_shutil_move(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
) -> None:
    benchmark_move(
        benchmark,
        filesystem_fixture,
        shutil_move,
    )


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_move.py
# ================================================================================================== test session starts ===================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 5 items

# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_move.py::test_pathlib_move PASSED                                                                                                                         [ 20%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_move.py::test_pathlib_replace PASSED                                                                                                                      [ 40%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_move.py::test_os_move PASSED                                                                                                                              [ 60%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_move.py::test_os_replace PASSED                                                                                                                           [ 80%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_move.py::test_shutil_move PASSED                                                                                                                          [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0262_latest.json



# ----------------------------------------------------------------------- benchmark: 5 tests -----------------------------------------------------------------------
# Name (time in us)           Min                Max              Mean            StdDev            Median               IQR            Outliers  Rounds  Iterations
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_os_replace          3.7250 (1.0)       8.2490 (1.0)      4.2380 (1.0)      0.7322 (1.0)      3.9550 (1.0)      0.5765 (1.63)          9;4     100           1
# test_os_move             3.7450 (1.01)      9.1970 (1.11)     4.3276 (1.02)     1.0013 (1.37)     3.9910 (1.01)     0.3540 (1.0)          7;10     100           1
# test_pathlib_replace     4.0400 (1.08)     11.8450 (1.44)     5.3007 (1.25)     1.7114 (2.34)     4.3705 (1.11)     1.7205 (4.86)        15;10     100           1
# test_pathlib_move        4.1470 (1.11)     15.2830 (1.85)     5.7211 (1.35)     2.1061 (2.88)     4.6430 (1.17)     2.5650 (7.25)         16;3     100           1
# test_shutil_move         6.3620 (1.71)     16.5050 (2.00)     6.9826 (1.65)     1.2743 (1.74)     6.6555 (1.68)     0.3560 (1.01)         5;10     100           1
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# =================================================================================================== 5 passed in 4.11s ====================================================================================================
