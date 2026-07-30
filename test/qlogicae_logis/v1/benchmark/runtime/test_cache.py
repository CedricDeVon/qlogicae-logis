from __future__ import annotations

from functools import cache
from typing import Any

import pytest

ROUNDS = 30
ITERATIONS = 2_000_000
WARMUP_ROUNDS = 10

DEPTHS = (
    1,
    10,
    100,
)


def create_nested_dict(
    *,
    depth: int,
    value: Any,
) -> dict[str, Any]:
    current = value

    for index in reversed(range(depth)):
        current = {
            f"node_{index}": current,
        }

    return current


def create_key_path(
    depth: int,
) -> tuple[str, ...]:
    return tuple(
        f"node_{index}"
        for index in range(depth)
    )


def resolve_key_path(
    data: dict[str, Any],
    key_path: tuple[str, ...],
) -> Any:
    current: Any = data

    for key in key_path:
        current = current[key]

    return current


@pytest.fixture(
    scope="session",
    params=DEPTHS,
    ids=lambda depth: f"{depth}_levels",
)
def sample(
    request: pytest.FixtureRequest,
) -> tuple[dict[str, Any], tuple[str, ...]]:
    depth = request.param

    return (
        create_nested_dict(
            depth=depth,
            value=123,
        ),
        create_key_path(depth),
    )


def lookup(
    data: dict[str, Any],
    key_path: tuple[str, ...],
) -> Any:
    return resolve_key_path(
        data,
        key_path,
    )


_DATA: dict[str, Any]


@cache
def cached_lookup(
    key_path: tuple[str, ...],
) -> Any:
    return resolve_key_path(
        _DATA,
        key_path,
    )


@pytest.mark.parametrize(
    "function",
    (
        lookup,
        cached_lookup,
    ),
)
def test_lookup(
    benchmark: pytest.BenchmarkFixture,
    sample: tuple[dict[str, Any], tuple[str, ...]],
    function,
) -> None:
    global _DATA

    data, key_path = sample
    _DATA = data

    cached_lookup.cache_clear()
    cached_lookup(key_path)

    if function is lookup:
        benchmark.pedantic(
            function,
            args=(data, key_path),
            rounds=ROUNDS,
            iterations=ITERATIONS,
            warmup_rounds=WARMUP_ROUNDS,
        )
    else:
        benchmark.pedantic(
            function,
            args=(key_path,),
            rounds=ROUNDS,
            iterations=ITERATIONS,
            warmup_rounds=WARMUP_ROUNDS,
        )


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_cache.py
# ============================================================================================================ test session starts ============================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 6 items                                                                                                                                                                                                                           

# test/qlogicae_logis/v1/benchmark/runtime/test_cache.py::test_lookup[1_levels-lookup] PASSED                                                                                                                                           [ 16%]
# test/qlogicae_logis/v1/benchmark/runtime/test_cache.py::test_lookup[1_levels-cached_lookup] PASSED                                                                                                                                    [ 33%]
# test/qlogicae_logis/v1/benchmark/runtime/test_cache.py::test_lookup[10_levels-lookup] PASSED                                                                                                                                          [ 50%]
# test/qlogicae_logis/v1/benchmark/runtime/test_cache.py::test_lookup[10_levels-cached_lookup] PASSED                                                                                                                                   [ 66%]
# test/qlogicae_logis/v1/benchmark/runtime/test_cache.py::test_lookup[100_levels-lookup] PASSED                                                                                                                                         [ 83%]
# test/qlogicae_logis/v1/benchmark/runtime/test_cache.py::test_lookup[100_levels-cached_lookup] PASSED                                                                                                                                  [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0220_latest.json



# ---------------------------------------------------------------------------------------- benchmark: 6 tests ---------------------------------------------------------------------------------------
# Name (time in ns)                                Min                   Max                  Mean            StdDev                Median                IQR            Outliers  Rounds  Iterations
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_lookup[1_levels-cached_lookup]          56.9519 (1.0)         57.8455 (1.0)         57.1812 (1.0)      0.1698 (1.60)        57.1606 (1.0)       0.1754 (1.04)          7;1      30     2000000
# test_lookup[10_levels-cached_lookup]         58.5440 (1.03)        58.9846 (1.02)        58.7312 (1.03)     0.1062 (1.0)         58.7102 (1.03)      0.1887 (1.11)         10;0      30     2000000
# test_lookup[100_levels-cached_lookup]        60.0187 (1.05)        60.6436 (1.05)        60.2786 (1.05)     0.1394 (1.31)        60.2560 (1.05)      0.1693 (1.0)           8;1      30     2000000
# test_lookup[1_levels-lookup]                104.2280 (1.83)       106.0894 (1.83)       105.2431 (1.84)     0.5515 (5.19)       105.3021 (1.84)      0.9804 (5.79)         15;0      30     2000000
# test_lookup[10_levels-lookup]               273.4558 (4.80)       280.8872 (4.86)       276.5205 (4.84)     1.8313 (17.24)      277.0390 (4.85)      2.8454 (16.81)        12;0      30     2000000
# test_lookup[100_levels-lookup]            2,039.1163 (35.80)    2,082.1152 (35.99)    2,053.0616 (35.90)    9.9887 (94.02)    2,051.5591 (35.89)    10.7922 (63.76)         6;2      30     2000000
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ======================================================================================================= 6 passed in 209.66s (0:03:29) =======================================================================================================