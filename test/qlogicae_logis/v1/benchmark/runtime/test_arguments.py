from __future__ import annotations

import pytest

ROUNDS = 30
ITERATIONS = 1_000_000
WARMUP_ROUNDS = 10

VALUES = (
    (1, 2),
    (100, 200),
    (-5, 10),
)


def sum_positional(
    a: int,
    b: int,
) -> int:
    return a + b


def sum_args(
    *args: int,
) -> int:
    return args[0] + args[1]


def sum_keyword(
    *,
    a: int,
    b: int,
) -> int:
    return a + b


def sum_kwargs(
    **kwargs: int,
) -> int:
    return kwargs["a"] + kwargs["b"]


FUNCTIONS = (
    sum_positional,
    sum_args,
    sum_keyword,
    sum_kwargs,
)


@pytest.fixture(
    scope="session",
    params=VALUES,
    ids=lambda value: f"{value[0]}_{value[1]}",
)
def sample(
    request: pytest.FixtureRequest,
) -> tuple[int, int]:
    return request.param


@pytest.mark.parametrize(
    "function",
    FUNCTIONS,
)
def test_sum(
    benchmark: pytest.BenchmarkFixture,
    sample: tuple[int, int],
    function,
) -> None:
    a, b = sample

    if function is sum_positional:
        result = benchmark.pedantic(
            function,
            args=(a, b),
            rounds=ROUNDS,
            iterations=ITERATIONS,
            warmup_rounds=WARMUP_ROUNDS,
        )

    elif function is sum_args:
        result = benchmark.pedantic(
            function,
            args=(a, b),
            rounds=ROUNDS,
            iterations=ITERATIONS,
            warmup_rounds=WARMUP_ROUNDS,
        )

    elif function is sum_keyword:
        result = benchmark.pedantic(
            function,
            kwargs={
                "a": a,
                "b": b,
            },
            rounds=ROUNDS,
            iterations=ITERATIONS,
            warmup_rounds=WARMUP_ROUNDS,
        )

    else:
        result = benchmark.pedantic(
            function,
            kwargs={
                "a": a,
                "b": b,
            },
            rounds=ROUNDS,
            iterations=ITERATIONS,
            warmup_rounds=WARMUP_ROUNDS,
        )

    assert result == a + b



# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_arguments.py
# ============================================================================================== test session starts ==============================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 12 items

# test/qlogicae_logis/v1/benchmark/runtime/test_arguments.py::test_sum[1_2-sum_positional] PASSED                                                                                                           [  8%]
# test/qlogicae_logis/v1/benchmark/runtime/test_arguments.py::test_sum[1_2-sum_args] PASSED                                                                                                                 [ 16%]
# test/qlogicae_logis/v1/benchmark/runtime/test_arguments.py::test_sum[1_2-sum_keyword] PASSED                                                                                                              [ 25%]
# test/qlogicae_logis/v1/benchmark/runtime/test_arguments.py::test_sum[1_2-sum_kwargs] PASSED                                                                                                               [ 33%]
# test/qlogicae_logis/v1/benchmark/runtime/test_arguments.py::test_sum[100_200-sum_positional] PASSED                                                                                                       [ 41%]
# test/qlogicae_logis/v1/benchmark/runtime/test_arguments.py::test_sum[100_200-sum_args] PASSED                                                                                                             [ 50%]
# test/qlogicae_logis/v1/benchmark/runtime/test_arguments.py::test_sum[100_200-sum_keyword] PASSED                                                                                                          [ 58%]
# test/qlogicae_logis/v1/benchmark/runtime/test_arguments.py::test_sum[100_200-sum_kwargs] PASSED                                                                                                           [ 66%]
# test/qlogicae_logis/v1/benchmark/runtime/test_arguments.py::test_sum[-5_10-sum_positional] PASSED                                                                                                         [ 75%]
# test/qlogicae_logis/v1/benchmark/runtime/test_arguments.py::test_sum[-5_10-sum_args] PASSED                                                                                                               [ 83%]
# test/qlogicae_logis/v1/benchmark/runtime/test_arguments.py::test_sum[-5_10-sum_keyword] PASSED                                                                                                            [ 91%]
# test/qlogicae_logis/v1/benchmark/runtime/test_arguments.py::test_sum[-5_10-sum_kwargs] PASSED                                                                                                             [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0294_latest.json



# -------------------------------------------------------------------------------- benchmark: 12 tests --------------------------------------------------------------------------------
# Name (time in ns)                         Min                 Max                Mean            StdDev              Median               IQR            Outliers  Rounds  Iterations
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_sum[1_2-sum_positional]          51.8229 (1.0)       54.8692 (1.01)      52.6335 (1.0)      0.9357 (4.86)      52.2745 (1.0)      0.4745 (2.12)          6;6      30     1000000
# test_sum[-5_10-sum_positional]        53.2099 (1.03)      54.3241 (1.0)       53.6335 (1.02)     0.2385 (1.24)      53.6096 (1.03)     0.2810 (1.26)          8;1      30     1000000
# test_sum[100_200-sum_positional]      56.1960 (1.08)      57.0391 (1.05)      56.4737 (1.07)     0.2161 (1.12)      56.4371 (1.08)     0.2238 (1.0)          10;2      30     1000000
# test_sum[1_2-sum_args]                70.8300 (1.37)      72.1925 (1.33)      71.2026 (1.35)     0.3624 (1.88)      71.1048 (1.36)     0.2364 (1.06)          4;3      30     1000000
# test_sum[-5_10-sum_args]              72.1319 (1.39)      72.9053 (1.34)      72.4855 (1.38)     0.1925 (1.0)       72.5158 (1.39)     0.2463 (1.10)         12;0      30     1000000
# test_sum[100_200-sum_args]            76.3536 (1.47)      78.7446 (1.45)      76.6886 (1.46)     0.4230 (2.20)      76.6653 (1.47)     0.2592 (1.16)          1;1      30     1000000
# test_sum[1_2-sum_keyword]             99.7440 (1.92)     101.9084 (1.88)     100.9202 (1.92)     0.5932 (3.08)     101.1004 (1.93)     0.7583 (3.39)          9;0      30     1000000
# test_sum[-5_10-sum_keyword]          101.7269 (1.96)     103.6442 (1.91)     102.2867 (1.94)     0.3507 (1.82)     102.1931 (1.95)     0.3315 (1.48)          6;1      30     1000000
# test_sum[100_200-sum_keyword]        105.8447 (2.04)     107.4436 (1.98)     106.5225 (2.02)     0.3954 (2.05)     106.4776 (2.04)     0.4335 (1.94)         11;2      30     1000000
# test_sum[1_2-sum_kwargs]             159.7368 (3.08)     161.6278 (2.98)     160.5314 (3.05)     0.4911 (2.55)     160.5074 (3.07)     0.6223 (2.78)         11;0      30     1000000
# test_sum[-5_10-sum_kwargs]           160.0587 (3.09)     166.7341 (3.07)     161.3048 (3.06)     1.2029 (6.25)     161.0114 (3.08)     0.5590 (2.50)          3;3      30     1000000
# test_sum[100_200-sum_kwargs]         165.4146 (3.19)     167.8386 (3.09)     166.1808 (3.16)     0.5399 (2.80)     166.0833 (3.18)     0.7899 (3.53)          9;1      30     1000000
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ============================================================================================== 12 passed in 48.55s ==============================================================================================
