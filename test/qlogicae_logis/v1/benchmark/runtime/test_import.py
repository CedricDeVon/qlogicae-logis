from __future__ import annotations

import subprocess

import pytest

ROUNDS = 30
ITERATIONS = 100
WARMUP_ROUNDS = 10

MODULES = (
    "collections",
)


def benchmark_static_import(module: str) -> None:
    subprocess.run(
        ["python", "-c", f"import {module}"],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def benchmark_dynamic_import(module: str) -> None:
    subprocess.run(
        [
            "python",
            "-c",
            (
                "import importlib;"
                f"importlib.import_module('{module}')"
            ),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


@pytest.mark.parametrize("module", MODULES)
def test_static_import(
    benchmark: pytest.BenchmarkFixture,
    module: str,
) -> None:
    benchmark.pedantic(
        benchmark_static_import,
        args=(module,),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


@pytest.mark.parametrize("module", MODULES)
def test_dynamic_import(
    benchmark: pytest.BenchmarkFixture,
    module: str,
) -> None:
    benchmark.pedantic(
        benchmark_dynamic_import,
        args=(module,),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_import.py
# ============================================================================================================ test session starts ============================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 2 items

# test/qlogicae_logis/v1/benchmark/runtime/test_import.py::test_static_import[collections] PASSED                                                                                                                                       [ 50%]
# test/qlogicae_logis/v1/benchmark/runtime/test_import.py::test_dynamic_import[collections] PASSED                                                                                                                                      [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0177_latest.json



# ------------------------------------------------------------------------------- benchmark: 2 tests ------------------------------------------------------------------------------
# Name (time in ms)                        Min                Max               Mean            StdDev             Median               IQR            Outliers  Rounds  Iterations
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_static_import[collections]      10.8232 (1.0)      10.9398 (1.0)      10.8716 (1.0)      0.0217 (1.0)      10.8684 (1.0)      0.0213 (1.0)           5;2      30         100
# test_dynamic_import[collections]     10.9243 (1.01)     11.0605 (1.01)     10.9846 (1.01)     0.0332 (1.53)     10.9849 (1.01)     0.0379 (1.78)          9;0      30         100
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ======================================================================================================= 2 passed in 88.73s (0:01:28) ========================================================================================================
