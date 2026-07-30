from __future__ import annotations

import random
import string

import pytest

ROUNDS = 30
ITERATIONS = 1_000_000
WARMUP_ROUNDS = 10

PART_COUNTS = (
    2,
    10,
)

PART_SIZES = (
    10,
)


def create_parts(
    *,
    part_count: int,
    part_size: int,
) -> tuple[str, ...]:
    alphabet = string.ascii_letters

    return tuple(
        "".join(
            random.choices(
                alphabet,
                k=part_size,
            ),
        )
        for _ in range(part_count)
    )


@pytest.fixture(
    params=[
        (count, size)
        for count in PART_COUNTS
        for size in PART_SIZES
    ],
    ids=lambda value: (
        f"{value[0]}_parts_{value[1]}_chars"
    ),
)
def sample(
    request: pytest.FixtureRequest,
) -> tuple[tuple[str, ...], str]:
    count, size = request.param

    parts = create_parts(
        part_count=count,
        part_size=size,
    )

    return (
        parts,
        "".join(parts),
    )


def concat_no_throw(
    parts: tuple[str, ...],
) -> str:
    return "".join(parts)


def concat_throw(
    parts: tuple[str, ...],
) -> str:
    try:
        raise ValueError

    except ValueError:
        return "".join(parts)


FUNCTIONS = (
    concat_no_throw,
    concat_throw,
)


@pytest.mark.parametrize(
    "function",
    FUNCTIONS,
)
def test_concat(
    benchmark: pytest.BenchmarkFixture,
    sample: tuple[tuple[str, ...], str],
    function,
) -> None:
    parts, expected = sample

    result = benchmark.pedantic(
        function,
        args=(parts,),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )

    assert result == expected


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_throw.py
# ============================================================================================================ test session starts ============================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 4 items                                                                                                                                                                                                                           

# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[2_parts_10_chars-concat_no_throw] PASSED                                                                                                                          [ 25%]
# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[2_parts_10_chars-concat_throw] PASSED                                                                                                                             [ 50%]
# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[10_parts_10_chars-concat_no_throw] PASSED                                                                                                                         [ 75%]
# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[10_parts_10_chars-concat_throw] PASSED                                                                                                                            [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0234_latest.json



# ---------------------------------------------------------------------------------------- benchmark: 4 tests ---------------------------------------------------------------------------------------
# Name (time in ns)                                       Min                 Max                Mean            StdDev              Median               IQR            Outliers  Rounds  Iterations
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_concat[2_parts_10_chars-concat_no_throw]       74.1284 (1.0)       79.0028 (1.0)       76.1187 (1.0)      0.9117 (1.98)      76.2016 (1.0)      0.5310 (1.0)           6;6      30     1000000
# test_concat[10_parts_10_chars-concat_no_throw]     114.1225 (1.54)     116.3229 (1.47)     114.7821 (1.51)     0.4611 (1.0)      114.6916 (1.51)     0.5867 (1.10)          7;1      30     1000000
# test_concat[2_parts_10_chars-concat_throw]         190.6410 (2.57)     194.1472 (2.46)     192.4675 (2.53)     0.8348 (1.81)     192.5524 (2.53)     1.2322 (2.32)          9;0      30     1000000
# test_concat[10_parts_10_chars-concat_throw]        236.4185 (3.19)     262.8355 (3.33)     240.2114 (3.16)     6.2116 (13.47)    237.8427 (3.12)     1.3744 (2.59)          4;5      30     1000000
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ============================================================================================================ 4 passed in 26.16s =============================================================================================================