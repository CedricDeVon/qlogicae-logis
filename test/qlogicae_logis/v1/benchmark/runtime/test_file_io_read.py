from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

import pytest
import yaml


ROUNDS = 30
ITERATIONS = 1_000
WARMUP_ROUNDS = 10

DATA_SIZES = (
    1,
    10,
    100,
)


def create_data(size: int) -> dict[str, Any]:
    return {
        "items": list(range(size)),
    }


@pytest.fixture(scope="function", params=DATA_SIZES)
def sample_files(
    request: pytest.FixtureRequest,
    tmp_path_factory: pytest.TempPathFactory,
) -> tuple[Path, Path]:
    data = create_data(request.param)

    directory = tmp_path_factory.mktemp(f"benchmark_{request.param}")

    json_file = directory / "sample.json"
    yaml_file = directory / "sample.yaml"

    with json_file.open("w", encoding="utf-8") as file:
        json.dump(data, file)

    with yaml_file.open("w", encoding="utf-8") as file:
        yaml.safe_dump(
            data,
            file,
            sort_keys=False,
        )

    try:
        yield json_file, yaml_file
    finally:
        shutil.rmtree(directory, ignore_errors=True)


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def read_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def read_text(path: Path) -> str:
    with path.open("r", encoding="utf-8") as file:
        return file.read()


@pytest.mark.parametrize(
    ("name", "index", "reader"),
    [
        ("json", 0, read_json),
        ("text", 1, read_text),
        ("yaml", 1, read_yaml),
    ],
)
def test_read(
    benchmark: pytest.BenchmarkFixture,
    sample_files: tuple[Path, Path],
    name: str,
    index: int,
    reader,
) -> None:
    benchmark.pedantic(
        reader,
        args=(sample_files[index],),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_file_io_read.py
# ============================================================================================================ test session starts ============================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 9 items                                                                                                                                                                                                                           

# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_read.py::test_read[1-json-0-read_json] PASSED                                                                                                                                   [ 11%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_read.py::test_read[1-text-1-read_text] PASSED                                                                                                                                   [ 22%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_read.py::test_read[1-yaml-1-read_yaml] PASSED                                                                                                                                   [ 33%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_read.py::test_read[10-json-0-read_json] PASSED                                                                                                                                  [ 44%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_read.py::test_read[10-text-1-read_text] PASSED                                                                                                                                  [ 55%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_read.py::test_read[10-yaml-1-read_yaml] PASSED                                                                                                                                  [ 66%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_read.py::test_read[100-json-0-read_json] PASSED                                                                                                                                 [ 77%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_read.py::test_read[100-text-1-read_text] PASSED                                                                                                                                 [ 88%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_read.py::test_read[100-yaml-1-read_yaml] PASSED                                                                                                                                 [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0205_latest.json



# ------------------------------------------------------------------------------------- benchmark: 9 tests -------------------------------------------------------------------------------------
# Name (time in us)                          Min                   Max                  Mean             StdDev                Median                IQR            Outliers  Rounds  Iterations
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_read[1-text-1-read_text]           5.2289 (1.0)          5.4932 (1.0)          5.3210 (1.0)       0.0688 (1.92)         5.3003 (1.0)       0.0747 (2.27)          7;3      30        1000
# test_read[10-text-1-read_text]          5.3624 (1.03)         5.5249 (1.01)         5.4220 (1.02)      0.0417 (1.16)         5.4168 (1.02)      0.0596 (1.81)         10;0      30        1000
# test_read[100-text-1-read_text]         5.3917 (1.03)         5.5374 (1.01)         5.4519 (1.02)      0.0359 (1.0)          5.4436 (1.03)      0.0329 (1.0)           9;2      30        1000
# test_read[1-json-0-read_json]           7.0496 (1.35)         7.3741 (1.34)         7.1493 (1.34)      0.0837 (2.33)         7.1393 (1.35)      0.1131 (3.43)          6;1      30        1000
# test_read[10-json-0-read_json]          7.5772 (1.45)         7.7256 (1.41)         7.6454 (1.44)      0.0432 (1.20)         7.6519 (1.44)      0.0601 (1.82)         11;0      30        1000
# test_read[100-json-0-read_json]        10.8877 (2.08)        11.0910 (2.02)        10.9744 (2.06)      0.0450 (1.25)        10.9691 (2.07)      0.0468 (1.42)         10;1      30        1000
# test_read[1-yaml-1-read_yaml]          88.5270 (16.93)       91.5363 (16.66)       88.7730 (16.68)     0.5362 (14.93)       88.6526 (16.73)     0.1502 (4.56)          1;3      30        1000
# test_read[10-yaml-1-read_yaml]        233.6819 (44.69)      236.9384 (43.13)      234.2473 (44.02)     0.6772 (18.86)      234.1019 (44.17)     0.3821 (11.61)         2;2      30        1000
# test_read[100-yaml-1-read_yaml]     1,740.7641 (332.91)   1,784.8746 (324.93)   1,769.5814 (332.56)   12.3917 (345.09)   1,774.7310 (334.84)   14.9600 (454.42)        8;0      30        1000
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ======================================================================================================= 9 passed in 86.26s (0:01:26) ========================================================================================================
