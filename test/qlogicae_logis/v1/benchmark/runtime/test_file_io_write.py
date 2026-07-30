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
) -> tuple[dict[str, Any], Path, Path]:
    data = create_data(request.param)

    directory = tmp_path_factory.mktemp(f"benchmark_{request.param}")

    json_file = directory / "sample.json"
    yaml_file = directory / "sample.yaml"

    try:
        yield data, json_file, yaml_file
    finally:
        shutil.rmtree(directory, ignore_errors=True)


def write_json(data: dict[str, Any], path: Path) -> None:
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file)


def write_yaml(data: dict[str, Any], path: Path) -> None:
    with path.open("w", encoding="utf-8") as file:
        yaml.safe_dump(
            data,
            file,
            sort_keys=False,
        )


def write_text(data: dict[str, Any], path: Path) -> None:
    text = yaml.safe_dump(
        data,
        sort_keys=False,
    )

    with path.open("w", encoding="utf-8") as file:
        file.write(text)


@pytest.mark.parametrize(
    ("index", "writer"),
    [
        (0, write_json),
        (1, write_text),
        (1, write_yaml),
    ],
)
def test_write(
    benchmark: pytest.BenchmarkFixture,
    sample_files: tuple[dict[str, Any], Path, Path],
    index: int,
    writer,
) -> None:
    data, json_file, yaml_file = sample_files

    benchmark.pedantic(
        writer,
        args=(
            data,
            (json_file, yaml_file)[index],
        ),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_file_io_write.py
# ============================================================================================================ test session starts ============================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 9 items                                                                                                                                                                                                                           

# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_write.py::test_write[1-0-write_json] PASSED                                                                                                                                     [ 11%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_write.py::test_write[1-1-write_text] PASSED                                                                                                                                     [ 22%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_write.py::test_write[1-1-write_yaml] PASSED                                                                                                                                     [ 33%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_write.py::test_write[10-0-write_json] PASSED                                                                                                                                    [ 44%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_write.py::test_write[10-1-write_text] PASSED                                                                                                                                    [ 55%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_write.py::test_write[10-1-write_yaml] PASSED                                                                                                                                    [ 66%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_write.py::test_write[100-0-write_json] PASSED                                                                                                                                   [ 77%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_write.py::test_write[100-1-write_text] PASSED                                                                                                                                   [ 88%]
# test/qlogicae_logis/v1/benchmark/runtime/test_file_io_write.py::test_write[100-1-write_yaml] PASSED                                                                                                                                   [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0207_latest.json



# ------------------------------------------------------------------------------- benchmark: 9 tests ------------------------------------------------------------------------------
# Name (time in us)                     Min                 Max                Mean            StdDev              Median               IQR            Outliers  Rounds  Iterations
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_write[1-0-write_json]        11.1584 (1.0)       12.5633 (1.0)       11.4818 (1.0)      0.3966 (3.77)      11.3029 (1.0)      0.3070 (3.04)          5;5      30        1000
# test_write[10-0-write_json]       13.3342 (1.19)      13.8465 (1.10)      13.4639 (1.17)     0.1052 (1.0)       13.4326 (1.19)     0.1011 (1.0)           7;1      30        1000
# test_write[100-0-write_json]      34.3057 (3.07)      41.6740 (3.32)      35.2581 (3.07)     1.5463 (14.70)     34.7522 (3.07)     0.4009 (3.96)          3;4      30        1000
# test_write[1-1-write_yaml]        61.4619 (5.51)      64.8119 (5.16)      61.7882 (5.38)     0.6781 (6.45)      61.6221 (5.45)     0.1791 (1.77)          2;3      30        1000
# test_write[1-1-write_text]        61.8504 (5.54)      64.4185 (5.13)      62.1594 (5.41)     0.5321 (5.06)      61.9900 (5.48)     0.1459 (1.44)          2;3      30        1000
# test_write[10-1-write_text]      122.4864 (10.98)    126.7066 (10.09)    123.7976 (10.78)    1.0802 (10.27)    123.4887 (10.93)    1.0974 (10.85)         7;2      30        1000
# test_write[10-1-write_yaml]      123.9711 (11.11)    128.8603 (10.26)    125.1037 (10.90)    1.2218 (11.62)    124.6211 (11.03)    0.5361 (5.30)          5;6      30        1000
# test_write[100-1-write_text]     708.7667 (63.52)    720.7214 (57.37)    714.2744 (62.21)    3.5995 (34.23)    713.5078 (63.13)    5.6941 (56.31)        11;0      30        1000
# test_write[100-1-write_yaml]     721.6304 (64.67)    727.9690 (57.94)    724.8839 (63.13)    1.6160 (15.37)    724.7787 (64.12)    1.8336 (18.13)        11;0      30        1000
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ======================================================================================================= 9 passed in 76.52s (0:01:16) ========================================================================================================