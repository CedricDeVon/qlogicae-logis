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
    100,
)

PART_SIZES = (
    10,
    100,
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
) -> tuple[str, ...]:
    count, size = request.param

    return create_parts(
        part_count=count,
        part_size=size,
    )


def concat_no_try(
    parts: tuple[str, ...],
) -> str:
    return "".join(parts)


def concat_try(
    parts: tuple[str, ...],
) -> str:
    try:
        return "".join(parts)
    except Exception:
        return ""


FUNCTIONS = (
    concat_no_try,
    concat_try,
)


@pytest.mark.parametrize(
    "function",
    FUNCTIONS,
)
def test_concat(
    benchmark: pytest.BenchmarkFixture,
    sample: tuple[str, ...],
    function,
) -> None:
    result = benchmark.pedantic(
        function,
        args=(sample,),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )

    assert result == "".join(sample)


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_try_catch.py
# ============================================================================================================ test session starts ============================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 12 items                                                                                                                                                                                                                          

# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[2_parts_10_chars-concat_no_try] PASSED                                                                                                                            [  8%]
# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[2_parts_10_chars-concat_try] PASSED                                                                                                                               [ 16%]
# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[2_parts_100_chars-concat_no_try] PASSED                                                                                                                           [ 25%]
# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[2_parts_100_chars-concat_try] PASSED                                                                                                                              [ 33%]
# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[10_parts_10_chars-concat_no_try] PASSED                                                                                                                           [ 41%]
# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[10_parts_10_chars-concat_try] PASSED                                                                                                                              [ 50%]
# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[10_parts_100_chars-concat_no_try] PASSED                                                                                                                          [ 58%]
# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[10_parts_100_chars-concat_try] PASSED                                                                                                                             [ 66%]
# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[100_parts_10_chars-concat_no_try] PASSED                                                                                                                          [ 75%]
# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[100_parts_10_chars-concat_try] PASSED                                                                                                                             [ 83%]
# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[100_parts_100_chars-concat_no_try] PASSED                                                                                                                         [ 91%]
# test/qlogicae_logis/v1/benchmark/runtime/test_throw.py::test_concat[100_parts_100_chars-concat_try] PASSED                                                                                                                            [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0225_latest.json



# --------------------------------------------------------------------------------------- benchmark: 12 tests ---------------------------------------------------------------------------------------
# Name (time in ns)                                       Min                 Max                Mean            StdDev              Median               IQR            Outliers  Rounds  Iterations
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_concat[2_parts_10_chars-concat_no_try]         74.9995 (1.0)       78.0391 (1.01)      75.7342 (1.0)      0.8191 (3.75)      75.4993 (1.0)      0.4503 (1.78)          3;3      30     1000000
# test_concat[2_parts_10_chars-concat_try]            75.2894 (1.00)      78.3836 (1.02)      75.9009 (1.00)     0.5364 (2.46)      75.8508 (1.00)     0.3635 (1.43)          2;1      30     1000000
# test_concat[2_parts_100_chars-concat_no_try]        75.9471 (1.01)      76.9132 (1.0)       76.3694 (1.01)     0.2183 (1.0)       76.3648 (1.01)     0.2535 (1.0)           9;1      30     1000000
# test_concat[2_parts_100_chars-concat_try]           77.6946 (1.04)      80.3772 (1.05)      78.2534 (1.03)     0.6132 (2.81)      78.1246 (1.03)     0.2642 (1.04)          3;4      30     1000000
# test_concat[10_parts_10_chars-concat_no_try]       113.4713 (1.51)     115.6944 (1.50)     114.5011 (1.51)     0.5667 (2.60)     114.4344 (1.52)     0.7345 (2.90)         10;0      30     1000000
# test_concat[10_parts_10_chars-concat_try]          117.3566 (1.56)     120.2698 (1.56)     118.4193 (1.56)     0.6060 (2.78)     118.4242 (1.57)     0.7415 (2.92)          8;1      30     1000000
# test_concat[10_parts_100_chars-concat_no_try]      160.7647 (2.14)     163.1044 (2.12)     161.9251 (2.14)     0.6065 (2.78)     161.8908 (2.14)     0.9610 (3.79)         11;0      30     1000000
# test_concat[10_parts_100_chars-concat_try]         163.5145 (2.18)     165.2844 (2.15)     164.6956 (2.17)     0.4312 (1.98)     164.7366 (2.18)     0.5334 (2.10)          7;2      30     1000000
# test_concat[100_parts_10_chars-concat_no_try]      567.3606 (7.56)     571.6553 (7.43)     569.6294 (7.52)     0.9924 (4.55)     569.5557 (7.54)     0.9957 (3.93)          8;1      30     1000000
# test_concat[100_parts_10_chars-concat_try]         573.5442 (7.65)     579.1236 (7.53)     575.2076 (7.60)     1.2764 (5.85)     574.8182 (7.61)     2.0632 (8.14)          8;0      30     1000000
# test_concat[100_parts_100_chars-concat_no_try]     695.5751 (9.27)     725.9311 (9.44)     698.7075 (9.23)     5.2740 (24.16)    697.7248 (9.24)     1.6100 (6.35)          1;1      30     1000000
# test_concat[100_parts_100_chars-concat_try]        710.2258 (9.47)     716.0022 (9.31)     713.4522 (9.42)     1.7154 (7.86)     713.7429 (9.45)     3.1123 (12.28)        13;0      30     1000000
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ====================================================================================================== 12 passed in 138.23s (0:02:18) =======================================================================================================
# (.venv) cedricdevon@cedricdevon-Inspiron-3501:~/workspace/qlogicae$ 