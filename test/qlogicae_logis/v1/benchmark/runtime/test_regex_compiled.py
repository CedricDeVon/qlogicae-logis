from __future__ import annotations

import random
import re
import string

import pytest
import regex
import rure

ROUNDS = 30
ITERATIONS = 10_000
WARMUP_ROUNDS = 10


PATTERN = r"\$\{\{\s*([A-Za-z0-9._-]+)\s*\}\}"


def compile_re():
    re.purge()
    return re.compile(PATTERN)


def compile_regex():
    regex.purge()
    return regex.compile(PATTERN)


def compile_rure():
    return rure.compile(PATTERN)


RE = re.compile(PATTERN)
REGEX = regex.compile(PATTERN)
RURE = rure.compile(PATTERN)


COMPILE_FUNCTIONS = (
    compile_re,
    compile_regex,
    compile_rure,
)


@pytest.mark.parametrize(
    "function",
    COMPILE_FUNCTIONS,
)
def test_compile(
    benchmark: pytest.BenchmarkFixture,
    function,
) -> None:
    benchmark.pedantic(
        function,
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_regex_compiled.py
# ================================================================================================== test session starts ===================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 3 items                                                                                                                                                                                                        

# test/qlogicae_logis/v1/benchmark/runtime/test_regex_compiled.py::test_compile[compile_re] PASSED                                                                                                                   [ 33%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex_compiled.py::test_compile[compile_regex] PASSED                                                                                                                [ 66%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex_compiled.py::test_compile[compile_rure] PASSED                                                                                                                 [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0288_latest.json



# ------------------------------------------------------------------------------ benchmark: 3 tests ------------------------------------------------------------------------------
# Name (time in us)                    Min                 Max                Mean            StdDev              Median               IQR            Outliers  Rounds  Iterations
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_compile[compile_re]         46.6167 (1.0)       50.8253 (1.0)       47.1113 (1.0)      1.0437 (1.0)       46.7175 (1.0)      0.3145 (1.0)           2;4      30       10000
# test_compile[compile_rure]       88.7495 (1.90)      95.5986 (1.88)      90.8310 (1.93)     1.9101 (1.83)      90.7812 (1.94)     2.8723 (9.13)         10;0      30       10000
# test_compile[compile_regex]     129.9843 (2.79)     140.4536 (2.76)     132.3688 (2.81)     2.7115 (2.60)     131.0407 (2.80)     2.5450 (8.09)          6;2      30       10000
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ============================================================================================= 3 passed in 116.28s (0:01:56) ==============================================================================================