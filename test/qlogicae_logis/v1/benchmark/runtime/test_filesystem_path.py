from __future__ import annotations

import os
import secrets
import string
from pathlib import Path

import pytest

ROUNDS = 30
ITERATIONS = 100_000
WARMUP_ROUNDS = 10

DIRECTORY_DEPTH = 100
DIRECTORY_NAME_LENGTH = 10
FILE_NAME_LENGTH = 10


def random_name(length: int) -> str:
    alphabet = string.ascii_letters + string.digits

    return "".join(
        secrets.choice(alphabet)
        for _ in range(length)
    )


@pytest.fixture(scope="session")
def filesystem_fixture(
    tmp_path_factory: pytest.TempPathFactory,
) -> dict[str, Path]:
    root = tmp_path_factory.mktemp("filesystem")

    directory = root

    for _ in range(DIRECTORY_DEPTH):
        directory /= random_name(DIRECTORY_NAME_LENGTH)
        directory.mkdir()

    existing = (
        directory
        / f"{random_name(FILE_NAME_LENGTH)}.txt"
    )
    existing.write_text("benchmark")

    nonexistent = (
        directory
        / f"{random_name(FILE_NAME_LENGTH)}.txt"
    )

    assert not nonexistent.exists()

    return {
        "root": root,
        "directory": directory,
        "existing": existing,
        "nonexistent": nonexistent,
    }


@pytest.mark.parametrize(
    ("name", "exists"),
    [
        ("existing", True),
        ("nonexistent", False),
    ],
)
def test_pathlib_exists(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
    name: str,
    exists: bool,
) -> None:
    path = filesystem_fixture[name]

    result = benchmark.pedantic(
        path.exists,
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )

    assert result is exists


@pytest.mark.parametrize(
    ("name", "exists"),
    [
        ("existing", True),
        ("nonexistent", False),
    ],
)
def test_os_path_exists(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
    name: str,
    exists: bool,
) -> None:
    path = os.fspath(filesystem_fixture[name])

    result = benchmark.pedantic(
        os.path.exists,
        args=(path,),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )

    assert result is exists


@pytest.mark.parametrize(
    ("name", "exists"),
    [
        ("existing", True),
        ("nonexistent", False),
    ],
)
def test_os_stat(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
    name: str,
    exists: bool,
) -> None:
    path = os.fspath(filesystem_fixture[name])

    if exists:
        result = benchmark.pedantic(
            os.stat,
            args=(path,),
            rounds=ROUNDS,
            iterations=ITERATIONS,
            warmup_rounds=WARMUP_ROUNDS,
        )
        assert result is not None
    else:
        with pytest.raises(FileNotFoundError):
            benchmark.pedantic(
                os.stat,
                args=(path,),
                rounds=ROUNDS,
                iterations=ITERATIONS,
                warmup_rounds=WARMUP_ROUNDS,
            )


@pytest.mark.parametrize(
    ("name", "exists"),
    [
        ("existing", True),
        ("nonexistent", False),
    ],
)
def test_os_lstat(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
    name: str,
    exists: bool,
) -> None:
    path = os.fspath(filesystem_fixture[name])

    if exists:
        result = benchmark.pedantic(
            os.lstat,
            args=(path,),
            rounds=ROUNDS,
            iterations=ITERATIONS,
            warmup_rounds=WARMUP_ROUNDS,
        )
        assert result is not None
    else:
        with pytest.raises(FileNotFoundError):
            benchmark.pedantic(
                os.lstat,
                args=(path,),
                rounds=ROUNDS,
                iterations=ITERATIONS,
                warmup_rounds=WARMUP_ROUNDS,
            )


@pytest.mark.parametrize(
    ("name", "exists"),
    [
        ("existing", True),
        ("nonexistent", False),
    ],
)
def test_os_access(
    benchmark: pytest.BenchmarkFixture,
    filesystem_fixture: dict[str, Path],
    name: str,
    exists: bool,
) -> None:
    path = os.fspath(filesystem_fixture[name])

    result = benchmark.pedantic(
        os.access,
        args=(path, os.F_OK),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )

    assert result is exists


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_path.py
# ================================================================================================== test session starts ===================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 10 items                                                                                                                                                                                                       

# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_path.py::test_pathlib_exists[existing-True] PASSED                                                                                                        [ 10%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_path.py::test_pathlib_exists[nonexistent-False] PASSED                                                                                                    [ 20%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_path.py::test_os_path_exists[existing-True] PASSED                                                                                                        [ 30%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_path.py::test_os_path_exists[nonexistent-False] PASSED                                                                                                    [ 40%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_path.py::test_os_stat[existing-True] PASSED                                                                                                               [ 50%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_path.py::test_os_stat[nonexistent-False] PASSED                                                                                                           [ 60%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_path.py::test_os_lstat[existing-True] PASSED                                                                                                              [ 70%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_path.py::test_os_lstat[nonexistent-False] PASSED                                                                                                          [ 80%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_path.py::test_os_access[existing-True] PASSED                                                                                                             [ 90%]
# test/qlogicae_logis/v1/benchmark/runtime/test_filesystem_path.py::test_os_access[nonexistent-False] PASSED                                                                                                         [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0269_latest.json



# -------------------------------------------------------------------------------- benchmark: 8 tests -------------------------------------------------------------------------------
# Name (time in us)                             Min               Max              Mean            StdDev            Median               IQR            Outliers  Rounds  Iterations
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_os_access[existing-True]              3.1871 (1.0)      3.2308 (1.0)      3.2014 (1.0)      0.0087 (1.0)      3.2006 (1.0)      0.0090 (1.0)           6;1      30      100000
# test_os_access[nonexistent-False]          3.6112 (1.13)     3.6595 (1.13)     3.6307 (1.13)     0.0124 (1.43)     3.6268 (1.13)     0.0144 (1.60)          8;1      30      100000
# test_os_stat[existing-True]                3.6996 (1.16)     3.7600 (1.16)     3.7215 (1.16)     0.0113 (1.30)     3.7196 (1.16)     0.0140 (1.56)          5;1      30      100000
# test_os_lstat[existing-True]               3.7016 (1.16)     3.7496 (1.16)     3.7266 (1.16)     0.0127 (1.46)     3.7246 (1.16)     0.0135 (1.50)          9;0      30      100000
# test_os_path_exists[existing-True]         3.7355 (1.17)     4.0415 (1.25)     3.7916 (1.18)     0.0766 (8.81)     3.7702 (1.18)     0.0304 (3.36)          3;4      30      100000
# test_pathlib_exists[existing-True]         3.9182 (1.23)     4.3967 (1.36)     4.0209 (1.26)     0.0993 (11.43)    4.0048 (1.25)     0.0562 (6.22)          4;3      30      100000
# test_os_path_exists[nonexistent-False]     4.4176 (1.39)     4.5137 (1.40)     4.4646 (1.39)     0.0278 (3.20)     4.4678 (1.40)     0.0526 (5.83)         13;0      30      100000
# test_pathlib_exists[nonexistent-False]     4.5837 (1.44)     4.7111 (1.46)     4.6730 (1.46)     0.0299 (3.44)     4.6818 (1.46)     0.0497 (5.50)          9;0      30      100000
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ============================================================================================= 10 passed in 126.10s (0:02:06) =============================================================================================