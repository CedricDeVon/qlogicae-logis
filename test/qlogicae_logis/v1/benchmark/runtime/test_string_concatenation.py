from __future__ import annotations

import functools
import io
import operator
import random
import string

import pytest

ROUNDS = 30
ITERATIONS = 500_000
WARMUP_ROUNDS = 10

PART_COUNTS = [
    2,
    10,
]

PART_SIZES = (
    2,
    10,
)


def create_parts(
    *,
    part_count: int,
    part_size: int,
) -> list[str]:
    alphabet = string.ascii_letters

    return [
        "".join(
            random.choices(
                alphabet,
                k=part_size,
            ),
        )
        for _ in range(part_count)
    ]


def plus_operator(parts: list[str]) -> str:
    result = parts[0]

    for part in parts[1:]:
        result = result + part

    return result


def plus_equal(parts: list[str]) -> str:
    result = ""

    for part in parts:
        result += part

    return result


def join_method(parts: list[str]) -> str:
    return "".join(parts)


def list_append_join(parts: list[str]) -> str:
    values: list[str] = []

    for part in parts:
        values.append(part)

    return "".join(values)


def stringio_method(parts: list[str]) -> str:
    buffer = io.StringIO()

    for part in parts:
        buffer.write(part)

    return buffer.getvalue()


def reduce_method(parts: list[str]) -> str:
    return functools.reduce(
        operator.add,
        parts,
    )


FUNCTIONS = (
    plus_operator,
    plus_equal,
    join_method,
    list_append_join,
    stringio_method,
    reduce_method,
)


@pytest.fixture(
    params=[
        (count, size)
        for count in PART_COUNTS
        for size in PART_SIZES
    ],
    ids=lambda x: f"{x[0]}_parts_{x[1]}_chars",
)
def sample(
    request: pytest.FixtureRequest,
) -> tuple[list[str], str]:
    count, size = request.param

    parts = create_parts(
        part_count=count,
        part_size=size,
    )

    return (
        parts,
        "".join(parts),
    )


@pytest.mark.parametrize(
    "function",
    FUNCTIONS,
)
def test_string_concatenation(
    benchmark: pytest.BenchmarkFixture,
    sample: tuple[list[str], str],
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


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py
# ============================================================================================================ test session starts ============================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 24 items                                                                                                                                                                                                                          

# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[2_parts_2_chars-plus_operator] PASSED                                                                                                [  4%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[2_parts_2_chars-plus_equal] PASSED                                                                                                   [  8%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[2_parts_2_chars-join_method] PASSED                                                                                                  [ 12%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[2_parts_2_chars-list_append_join] PASSED                                                                                             [ 16%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[2_parts_2_chars-stringio_method] PASSED                                                                                              [ 20%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[2_parts_2_chars-reduce_method] PASSED                                                                                                [ 25%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[2_parts_10_chars-plus_operator] PASSED                                                                                               [ 29%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[2_parts_10_chars-plus_equal] PASSED                                                                                                  [ 33%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[2_parts_10_chars-join_method] PASSED                                                                                                 [ 37%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[2_parts_10_chars-list_append_join] PASSED                                                                                            [ 41%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[2_parts_10_chars-stringio_method] PASSED                                                                                             [ 45%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[2_parts_10_chars-reduce_method] PASSED                                                                                               [ 50%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[10_parts_2_chars-plus_operator] PASSED                                                                                               [ 54%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[10_parts_2_chars-plus_equal] PASSED                                                                                                  [ 58%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[10_parts_2_chars-join_method] PASSED                                                                                                 [ 62%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[10_parts_2_chars-list_append_join] PASSED                                                                                            [ 66%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[10_parts_2_chars-stringio_method] PASSED                                                                                             [ 70%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[10_parts_2_chars-reduce_method] PASSED                                                                                               [ 75%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[10_parts_10_chars-plus_operator] PASSED                                                                                              [ 79%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[10_parts_10_chars-plus_equal] PASSED                                                                                                 [ 83%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[10_parts_10_chars-join_method] PASSED                                                                                                [ 87%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[10_parts_10_chars-list_append_join] PASSED                                                                                           [ 91%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[10_parts_10_chars-stringio_method] PASSED                                                                                            [ 95%]
# test/qlogicae_logis/v1/benchmark/runtime/test_string_concatenation.py::test_string_concatenation[10_parts_10_chars-reduce_method] PASSED                                                                                              [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0172_latest.json



# ---------------------------------------------------------------------------------------------- benchmark: 24 tests -----------------------------------------------------------------------------------------------
# Name (time in ns)                                                      Min                 Max                Mean            StdDev              Median               IQR            Outliers  Rounds  Iterations
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_string_concatenation[2_parts_2_chars-join_method]             76.6106 (1.0)       78.8024 (1.0)       78.1410 (1.0)      0.4015 (1.29)      78.1750 (1.0)      0.4207 (1.37)          6;1      30      500000
# test_string_concatenation[2_parts_10_chars-join_method]            79.9873 (1.04)      83.3433 (1.06)      80.6036 (1.03)     0.6234 (2.00)      80.5217 (1.03)     0.4104 (1.33)          3;3      30      500000
# test_string_concatenation[10_parts_2_chars-join_method]           114.6077 (1.50)     118.1680 (1.50)     115.3446 (1.48)     0.8196 (2.63)     115.2111 (1.47)     0.5623 (1.83)          2;2      30      500000
# test_string_concatenation[2_parts_2_chars-plus_equal]             119.0201 (1.55)     120.7682 (1.53)     119.5915 (1.53)     0.4548 (1.46)     119.4901 (1.53)     0.7102 (2.31)         10;0      30      500000
# test_string_concatenation[10_parts_10_chars-join_method]          119.9964 (1.57)     123.8324 (1.57)     120.9861 (1.55)     0.8156 (2.62)     120.8266 (1.55)     0.5573 (1.81)          3;2      30      500000
# test_string_concatenation[2_parts_10_chars-plus_equal]            121.7626 (1.59)     122.9029 (1.56)     122.2588 (1.56)     0.3113 (1.0)      122.2116 (1.56)     0.4583 (1.49)         12;0      30      500000
# test_string_concatenation[2_parts_2_chars-plus_operator]          139.3141 (1.82)     149.3549 (1.90)     140.6606 (1.80)     1.9291 (6.20)     140.0107 (1.79)     0.9943 (3.23)          3;3      30      500000
# test_string_concatenation[2_parts_10_chars-plus_operator]         143.1159 (1.87)     151.3775 (1.92)     144.5712 (1.85)     1.6998 (5.46)     144.0192 (1.84)     0.9302 (3.02)          3;3      30      500000
# test_string_concatenation[2_parts_2_chars-reduce_method]          148.6797 (1.94)     150.0729 (1.90)     149.2403 (1.91)     0.3256 (1.05)     149.2295 (1.91)     0.4707 (1.53)          8;0      30      500000
# test_string_concatenation[2_parts_10_chars-reduce_method]         148.8874 (1.94)     156.5922 (1.99)     149.9682 (1.92)     1.3051 (4.19)     149.7141 (1.92)     0.3081 (1.0)           1;4      30      500000
# test_string_concatenation[2_parts_2_chars-list_append_join]       153.4657 (2.00)     156.7431 (1.99)     154.4140 (1.98)     0.6256 (2.01)     154.2869 (1.97)     0.6167 (2.00)          4;2      30      500000
# test_string_concatenation[2_parts_10_chars-list_append_join]      155.3080 (2.03)     156.8028 (1.99)     155.9413 (2.00)     0.3860 (1.24)     155.9525 (1.99)     0.5921 (1.92)         10;0      30      500000
# test_string_concatenation[10_parts_10_chars-list_append_join]     306.5989 (4.00)     315.0936 (4.00)     308.8710 (3.95)     1.9727 (6.34)     308.0642 (3.94)     2.9730 (9.65)          6;1      30      500000
# test_string_concatenation[10_parts_2_chars-list_append_join]      307.7983 (4.02)     315.0507 (4.00)     309.6174 (3.96)     1.7202 (5.53)     309.0480 (3.95)     2.3392 (7.59)          7;1      30      500000
# test_string_concatenation[2_parts_2_chars-stringio_method]        316.9631 (4.14)     321.3846 (4.08)     318.6395 (4.08)     1.0878 (3.49)     318.4449 (4.07)     1.1541 (3.75)         11;1      30      500000
# test_string_concatenation[2_parts_10_chars-stringio_method]       330.7267 (4.32)     338.1171 (4.29)     332.2541 (4.25)     1.5572 (5.00)     331.7869 (4.24)     0.9317 (3.02)          3;3      30      500000
# test_string_concatenation[10_parts_2_chars-plus_equal]            338.7688 (4.42)     342.8754 (4.35)     340.2630 (4.35)     1.1339 (3.64)     340.0089 (4.35)     1.3897 (4.51)         10;0      30      500000
# test_string_concatenation[10_parts_2_chars-plus_operator]         373.0061 (4.87)     376.0521 (4.77)     374.4694 (4.79)     0.7289 (2.34)     374.3567 (4.79)     1.0184 (3.31)         12;0      30      500000
# test_string_concatenation[10_parts_10_chars-plus_equal]           372.9769 (4.87)     381.6063 (4.84)     375.4271 (4.80)     2.1527 (6.91)     374.6448 (4.79)     2.3802 (7.73)          8;2      30      500000
# test_string_concatenation[10_parts_2_chars-reduce_method]         388.8887 (5.08)     395.2515 (5.02)     392.4214 (5.02)     1.4078 (4.52)     392.7658 (5.02)     0.9723 (3.16)          6;5      30      500000
# test_string_concatenation[10_parts_10_chars-plus_operator]        406.9764 (5.31)     410.0616 (5.20)     408.1561 (5.22)     0.8281 (2.66)     407.9664 (5.22)     1.2896 (4.19)         10;0      30      500000
# test_string_concatenation[10_parts_10_chars-reduce_method]        413.8511 (5.40)     419.4797 (5.32)     415.9294 (5.32)     1.1056 (3.55)     415.7116 (5.32)     1.0666 (3.46)          6;2      30      500000
# test_string_concatenation[10_parts_2_chars-stringio_method]       578.3224 (7.55)     585.7717 (7.43)     581.5548 (7.44)     2.0474 (6.58)     581.2664 (7.44)     3.3636 (10.92)        11;0      30      500000
# test_string_concatenation[10_parts_10_chars-stringio_method]      604.9800 (7.90)     612.8803 (7.78)     608.2273 (7.78)     1.5990 (5.14)     608.1380 (7.78)     1.9173 (6.22)          7;1      30      500000
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ====================================================================================================== 24 passed in 127.43s (0:02:07) =======================================================================================================