from __future__ import annotations

import os
import secrets
import shutil
import string
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

ROUNDS = 30
ITERATIONS = 10_000
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
    data: bytes,
) -> None:
    for index in range(FILES_PER_DIRECTORY):
        (
            directory
            / f"file_{index}.bin"
        ).write_bytes(data)

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
            data,
        )


@pytest.fixture(scope="session")
def file_data() -> bytes:
    return os.urandom(FILE_SIZE)


def pathlib_unlink(
    data: bytes,
) -> None:
    with TemporaryDirectory(
        prefix="filesystem_",
    ) as workspace:
        path = (
            Path(workspace)
            / f"{random_name()}.bin"
        )

        path.write_bytes(data)

        path.unlink()


def os_remove(
    data: bytes,
) -> None:
    with TemporaryDirectory(
        prefix="filesystem_",
    ) as workspace:
        path = (
            Path(workspace)
            / f"{random_name()}.bin"
        )

        path.write_bytes(data)

        os.remove(path)


def os_unlink(
    data: bytes,
) -> None:
    with TemporaryDirectory(
        prefix="filesystem_",
    ) as workspace:
        path = (
            Path(workspace)
            / f"{random_name()}.bin"
        )

        path.write_bytes(data)

        os.unlink(path)


def pathlib_rmdir() -> None:
    with TemporaryDirectory(
        prefix="filesystem_",
    ) as workspace:
        path = (
            Path(workspace)
            / random_name()
        )

        path.mkdir()

        path.rmdir()


def os_rmdir() -> None:
    with TemporaryDirectory(
        prefix="filesystem_",
    ) as workspace:
        path = (
            Path(workspace)
            / random_name()
        )

        path.mkdir()

        os.rmdir(path)


def shutil_rmtree(
    data: bytes,
) -> None:
    with TemporaryDirectory(
        prefix="filesystem_",
    ) as workspace:
        root = (
            Path(workspace)
            / random_name()
        )

        root.mkdir()

        populate(
            root,
            DEPTH,
            data,
        )

        shutil.rmtree(root)


def test_pathlib_unlink(
    benchmark: pytest.BenchmarkFixture,
    file_data: bytes,
) -> None:
    benchmark.pedantic(
        pathlib_unlink,
        args=(file_data,),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


def test_os_remove(
    benchmark: pytest.BenchmarkFixture,
    file_data: bytes,
) -> None:
    benchmark.pedantic(
        os_remove,
        args=(file_data,),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


def test_os_unlink(
    benchmark: pytest.BenchmarkFixture,
    file_data: bytes,
) -> None:
    benchmark.pedantic(
        os_unlink,
        args=(file_data,),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


def test_pathlib_rmdir(
    benchmark: pytest.BenchmarkFixture,
) -> None:
    benchmark.pedantic(
        pathlib_rmdir,
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


def test_os_rmdir(
    benchmark: pytest.BenchmarkFixture,
) -> None:
    benchmark.pedantic(
        os_rmdir,
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_remove.py
# ================================================================================================== test session starts ===================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 5 items                                                                                                                                                                                                        

# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_remove.py::test_pathlib_unlink PASSED                                                                                                                     [ 20%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_remove.py::test_os_remove PASSED                                                                                                                          [ 40%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_remove.py::test_os_unlink PASSED                                                                                                                          [ 60%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_remove.py::test_pathlib_rmdir PASSED                                                                                                                      [ 80%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_remove.py::test_os_rmdir PASSED                                                                                                                           [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0272_latest.json



# ------------------------------------------------------------------------ benchmark: 5 tests ------------------------------------------------------------------------
# Name (time in us)           Min                Max               Mean            StdDev             Median               IQR            Outliers  Rounds  Iterations
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_os_rmdir           39.8586 (1.0)      45.6080 (1.07)     40.8418 (1.0)      1.2091 (1.47)     40.5579 (1.0)      0.6505 (1.81)          3;3      30       10000
# test_pathlib_rmdir      40.5052 (1.02)     42.7516 (1.0)      41.7525 (1.02)     0.8200 (1.0)      41.9910 (1.04)     1.6775 (4.66)         14;0      30       10000
# test_os_remove          52.2706 (1.31)     58.8644 (1.38)     53.5433 (1.31)     1.9034 (2.32)     52.6899 (1.30)     0.3604 (1.0)           5;5      30       10000
# test_pathlib_unlink     52.5050 (1.32)     58.8828 (1.38)     54.4870 (1.33)     2.4640 (3.00)     53.1620 (1.31)     3.6280 (10.07)         7;0      30       10000
# test_os_unlink          52.4888 (1.32)     59.9538 (1.40)     55.0037 (1.35)     2.8123 (3.43)     53.6161 (1.32)     6.0096 (16.68)         8;0      30       10000
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ============================================================================================== 5 passed in 99.85s (0:01:39) ==============================================================================================