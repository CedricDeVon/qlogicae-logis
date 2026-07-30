from __future__ import annotations

import random
import re
import string

import pytest
import regex
import rure

ROUNDS = 30
ITERATIONS = 100_000
WARMUP_ROUNDS = 10

TEXT_LENGTHS = (
    10,
    100,
)

POSITIONS = (
    "beginning",
    "middle",
    "end",
    "absent",
)

PATTERN = r"\$\{\{\s*([A-Za-z0-9._-]+)\s*\}\}"
TOKEN = "${{ example.value }}"


def create_text(
    *,
    length: int,
    position: str,
) -> tuple[str, bool]:
    rng = random.Random(0)

    alphabet = (
        string.ascii_letters
        + string.digits
        + "     "
    )

    text = "".join(
        rng.choices(
            alphabet,
            k=length,
        ),
    )

    if position == "absent":
        return (
            text,
            False,
        )

    if position == "beginning":
        return (
            TOKEN + text,
            True,
        )

    if position == "middle":
        middle = len(text) // 2

        return (
            (
                text[:middle]
                + TOKEN
                + text[middle:]
            ),
            True,
        )

    return (
        text + TOKEN,
        True,
    )


@pytest.fixture(
    scope="session",
    params=[
        (length, position)
        for length in TEXT_LENGTHS
        for position in POSITIONS
    ],
    ids=lambda value: (
        f"{value[0]}_chars_{value[1]}"
    ),
)
def sample(
    request: pytest.FixtureRequest,
) -> tuple[str, bool]:
    length, position = request.param

    return create_text(
        length=length,
        position=position,
    )


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


def search_re(text: str):
    return RE.search(text)


def search_regex(text: str):
    return REGEX.search(text)


def search_rure(text: str):
    return RURE.search(text)


SEARCH_FUNCTIONS = (
    search_re,
    search_regex,
    search_rure,
)


@pytest.mark.parametrize(
    "function",
    SEARCH_FUNCTIONS,
)
def test_search(
    benchmark: pytest.BenchmarkFixture,
    sample: tuple[str, bool],
    function,
) -> None:
    text, expected = sample

    result = benchmark.pedantic(
        function,
        args=(text,),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )

    assert (result is not None) is expected





# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_regex.py
# ================================================================================================== test session starts ===================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 24 items                                                                                                                                                                                                       

# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[10_chars_beginning-search_re] PASSED                                                                                                           [  4%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[10_chars_beginning-search_regex] PASSED                                                                                                        [  8%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[10_chars_beginning-search_rure] PASSED                                                                                                         [ 12%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[10_chars_middle-search_re] PASSED                                                                                                              [ 16%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[10_chars_middle-search_regex] PASSED                                                                                                           [ 20%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[10_chars_middle-search_rure] PASSED                                                                                                            [ 25%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[10_chars_end-search_re] PASSED                                                                                                                 [ 29%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[10_chars_end-search_regex] PASSED                                                                                                              [ 33%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[10_chars_end-search_rure] PASSED                                                                                                               [ 37%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[10_chars_absent-search_re] PASSED                                                                                                              [ 41%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[10_chars_absent-search_regex] PASSED                                                                                                           [ 45%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[10_chars_absent-search_rure] PASSED                                                                                                            [ 50%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[100_chars_beginning-search_re] PASSED                                                                                                          [ 54%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[100_chars_beginning-search_regex] PASSED                                                                                                       [ 58%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[100_chars_beginning-search_rure] PASSED                                                                                                        [ 62%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[100_chars_middle-search_re] PASSED                                                                                                             [ 66%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[100_chars_middle-search_regex] PASSED                                                                                                          [ 70%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[100_chars_middle-search_rure] PASSED                                                                                                           [ 75%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[100_chars_end-search_re] PASSED                                                                                                                [ 79%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[100_chars_end-search_regex] PASSED                                                                                                             [ 83%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[100_chars_end-search_rure] PASSED                                                                                                              [ 87%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[100_chars_absent-search_re] PASSED                                                                                                             [ 91%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[100_chars_absent-search_regex] PASSED                                                                                                          [ 95%]
# test/qlogicae_logis/v1/benchmark/runtime/test_regex.py::test_search[100_chars_absent-search_rure] PASSED                                                                                                           [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0283_latest.json



# ------------------------------------------------------------------------------------------- benchmark: 24 tests --------------------------------------------------------------------------------------------
# Name (time in ns)                                        Min                   Max                  Mean             StdDev                Median                IQR            Outliers  Rounds  Iterations
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_search[10_chars_absent-search_re]              102.1490 (1.0)        105.0619 (1.0)        103.2199 (1.0)       0.6716 (1.0)        103.1995 (1.0)       1.0391 (1.17)         11;0      30      100000
# test_search[100_chars_absent-search_re]             133.2144 (1.30)       136.4965 (1.30)       134.6858 (1.30)      0.8230 (1.23)       134.6102 (1.30)      1.4008 (1.57)         12;0      30      100000
# test_search[10_chars_middle-search_re]              249.7697 (2.45)       263.5063 (2.51)       253.2653 (2.45)      2.1500 (3.20)       252.9300 (2.45)      1.0324 (1.16)          2;2      30      100000
# test_search[10_chars_beginning-search_re]           247.2761 (2.42)       279.6196 (2.66)       254.6162 (2.47)      9.1922 (13.69)      249.5810 (2.42)     14.6369 (16.43)         6;0      30      100000
# test_search[10_chars_end-search_re]                 256.8986 (2.51)       269.5198 (2.57)       260.2932 (2.52)      2.4875 (3.70)       259.7717 (2.52)      0.8909 (1.0)           4;5      30      100000
# test_search[100_chars_beginning-search_re]          260.9974 (2.56)       263.4835 (2.51)       261.9628 (2.54)      0.6930 (1.03)       261.8672 (2.54)      1.1710 (1.31)         12;0      30      100000
# test_search[100_chars_middle-search_re]             272.9498 (2.67)       313.9011 (2.99)       277.5675 (2.69)      6.9480 (10.35)      276.4780 (2.68)      1.0659 (1.20)          1;3      30      100000
# test_search[10_chars_absent-search_regex]           274.1190 (2.68)       318.7385 (3.03)       278.8650 (2.70)      9.2172 (13.73)      276.4436 (2.68)      1.5493 (1.74)          2;3      30      100000
# test_search[100_chars_end-search_re]                294.5452 (2.88)       312.8525 (2.98)       300.0427 (2.91)      3.1005 (4.62)       299.3617 (2.90)      1.4800 (1.66)          3;4      30      100000
# test_search[100_chars_absent-search_regex]          305.4623 (2.99)       316.9260 (3.02)       311.0644 (3.01)      2.1394 (3.19)       311.1799 (3.02)      1.7952 (2.01)          5;3      30      100000
# test_search[10_chars_beginning-search_regex]        584.4151 (5.72)       619.1941 (5.89)       590.8131 (5.72)      7.4497 (11.09)      588.6408 (5.70)      4.6460 (5.21)          3;3      30      100000
# test_search[10_chars_middle-search_regex]           598.4674 (5.86)       612.7686 (5.83)       604.5037 (5.86)      4.0035 (5.96)       603.7705 (5.85)      4.0650 (4.56)         10;1      30      100000
# test_search[10_chars_end-search_regex]              611.4095 (5.99)       625.6677 (5.96)       616.4238 (5.97)      3.2800 (4.88)       615.8379 (5.97)      3.2454 (3.64)          8;2      30      100000
# test_search[100_chars_beginning-search_regex]       615.8037 (6.03)       628.5135 (5.98)       620.3088 (6.01)      3.1388 (4.67)       619.9424 (6.01)      4.0770 (4.58)          9;1      30      100000
# test_search[100_chars_middle-search_regex]          641.9728 (6.28)       653.1032 (6.22)       646.8209 (6.27)      2.8676 (4.27)       645.5032 (6.25)      4.0026 (4.49)          9;0      30      100000
# test_search[100_chars_end-search_regex]             656.6485 (6.43)       678.2677 (6.46)       664.7064 (6.44)      5.9932 (8.92)       663.2559 (6.43)      8.3203 (9.34)          9;0      30      100000
# test_search[10_chars_absent-search_rure]          2,056.9198 (20.14)    2,100.9759 (20.00)    2,070.9604 (20.06)     8.2578 (12.30)    2,070.0273 (20.06)     8.3410 (9.36)          5;1      30      100000
# test_search[100_chars_absent-search_rure]         2,089.8859 (20.46)    2,129.6550 (20.27)    2,100.4921 (20.35)     8.5089 (12.67)    2,098.6035 (20.34)     8.3715 (9.40)          8;2      30      100000
# test_search[10_chars_beginning-search_rure]       2,464.9155 (24.13)    2,514.4398 (23.93)    2,489.2691 (24.12)    11.7591 (17.51)    2,486.9542 (24.10)    14.2492 (15.99)         8;0      30      100000
# test_search[10_chars_middle-search_rure]          2,523.2560 (24.70)    2,554.8915 (24.32)    2,543.8978 (24.65)     8.0659 (12.01)    2,544.1896 (24.65)    13.4310 (15.08)        10;0      30      100000
# test_search[10_chars_end-search_rure]             2,551.0894 (24.97)    2,587.8872 (24.63)    2,567.8189 (24.88)     7.9137 (11.78)    2,565.8045 (24.86)    10.1276 (11.37)         7;0      30      100000
# test_search[100_chars_beginning-search_rure]      2,586.8169 (25.32)    2,630.1872 (25.03)    2,602.5395 (25.21)     9.3672 (13.95)    2,602.4757 (25.22)    11.9561 (13.42)         9;1      30      100000
# test_search[100_chars_middle-search_rure]         2,601.7463 (25.47)    2,650.5851 (25.23)    2,624.3914 (25.43)    10.4288 (15.53)    2,623.0627 (25.42)    14.1595 (15.89)         9;0      30      100000
# test_search[100_chars_end-search_rure]            2,622.9788 (25.68)    2,668.8720 (25.40)    2,643.1694 (25.61)     9.5809 (14.27)    2,642.5427 (25.61)    13.3470 (14.98)        11;0      30      100000
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ============================================================================================= 24 passed in 104.58s (0:01:44) =============================================================================================