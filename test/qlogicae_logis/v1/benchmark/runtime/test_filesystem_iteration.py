from __future__ import annotations

import glob
import os
import secrets
import shutil
import string
from pathlib import Path

import pytest

ROUNDS = 5
ITERATIONS = 2_000
WARMUP_ROUNDS = 10

DEPTH = 5
DIRECTORIES_PER_LEVEL = 2
FILES_PER_DIRECTORY = 2

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
            / f"{random_name()}.txt"
        ).write_text("benchmark")

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
) -> Path:
    root = tmp_path_factory.mktemp("filesystem")

    try:
        populate(
            root,
            DEPTH,
        )

        yield root

    finally:
        shutil.rmtree(
            root,
            ignore_errors=True,
        )


def count_pathlib_rglob(
    root: Path,
) -> int:
    return sum(
        1
        for _ in root.rglob("*")
    )


def count_pathlib_glob(
    root: Path,
) -> int:
    return sum(
        1
        for _ in root.glob("**/*")
    )


def count_os_walk(
    root: str,
) -> int:
    total = 0

    for _, directories, files in os.walk(root):
        total += len(directories)
        total += len(files)

    return total


def count_glob_iglob(
    pattern: str,
) -> int:
    return sum(
        1
        for _ in glob.iglob(
            pattern,
            recursive=True,
        )
    )


def count_glob_glob(
    pattern: str,
) -> int:
    return len(
        glob.glob(
            pattern,
            recursive=True,
        )
    )


def test_pathlib_rglob(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: Path,
) -> None:
    result = benchmark.pedantic(
        count_pathlib_rglob,
        args=(filesystem_fixture,),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )

    assert result > 0


def test_pathlib_glob(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: Path,
) -> None:
    result = benchmark.pedantic(
        count_pathlib_glob,
        args=(filesystem_fixture,),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )

    assert result > 0


def test_os_walk(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: Path,
) -> None:
    result = benchmark.pedantic(
        count_os_walk,
        args=(os.fspath(filesystem_fixture),),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )

    assert result > 0


def test_glob_iglob(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: Path,
) -> None:
    pattern = os.path.join(
        os.fspath(filesystem_fixture),
        "**",
        "*",
    )

    result = benchmark.pedantic(
        count_glob_iglob,
        args=(pattern,),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )

    assert result > 0


def test_glob_glob(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: Path,
) -> None:
    pattern = os.path.join(
        os.fspath(filesystem_fixture),
        "**",
        "*",
    )

    result = benchmark.pedantic(
        count_glob_glob,
        args=(pattern,),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )

    assert result > 0


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_iteration.py
# ================================================================================================== test session starts ===================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 5 items                                                                                                                                                                                                        

# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_iteration.py::test_pathlib_rglob PASSED                                                                                                                   [ 20%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_iteration.py::test_pathlib_glob PASSED                                                                                                                    [ 40%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_iteration.py::test_os_walk PASSED                                                                                                                         [ 60%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_iteration.py::test_glob_iglob PASSED                                                                                                                      [ 80%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_iteration.py::test_glob_glob PASSED                                                                                                                       [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0254_latest.json



# -------------------------------------------------------------------------- benchmark: 5 tests -------------------------------------------------------------------------
# Name (time in us)           Min                 Max                Mean            StdDev              Median               IQR            Outliers  Rounds  Iterations
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_os_walk           303.8866 (1.0)      304.8116 (1.0)      304.1813 (1.0)      0.3616 (1.0)      304.0777 (1.0)      0.2696 (1.0)           1;1       5        2000
# test_pathlib_rglob     571.8158 (1.88)     576.9256 (1.89)     575.2744 (1.89)     2.0169 (5.58)     575.7890 (1.89)     2.0138 (7.47)          1;0       5        2000
# test_pathlib_glob      580.7850 (1.91)     583.4664 (1.91)     582.7890 (1.92)     1.1311 (3.13)     583.2681 (1.92)     0.9164 (3.40)          1;1       5        2000
# test_glob_glob         740.8212 (2.44)     742.6667 (2.44)     741.6996 (2.44)     0.7801 (2.16)     741.4905 (2.44)     1.3338 (4.95)          2;0       5        2000
# test_glob_iglob        743.3932 (2.45)     746.3886 (2.45)     744.8213 (2.45)     1.2116 (3.35)     745.1647 (2.45)     1.8823 (6.98)          2;0       5        2000
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ============================================================================================== 5 passed in 89.64s (0:01:29) ==============================================================================================