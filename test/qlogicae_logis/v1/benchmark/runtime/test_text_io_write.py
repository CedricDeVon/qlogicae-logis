from __future__ import annotations

import json
from typing import Any

import pytest
import yaml

ROUNDS = 30
ITERATIONS = 400
WARMUP_ROUNDS = 10

DATASETS = (
    {
        "depth": 5,
        "branches": 2,
        "list_size": 10,
    },
)


def create_tree(
    *,
    depth: int,
    branches: int,
    list_size: int,
) -> dict[str, Any]:
    if depth == 0:
        return {
            "value": 123,
            "text": "hello world",
            "list": list(range(list_size)),
        }

    return {
        f"node_{index}": create_tree(
            depth=depth - 1,
            branches=branches,
            list_size=list_size,
        )
        for index in range(branches)
    }


def create_data(
    *,
    depth: int,
    branches: int,
    list_size: int,
) -> dict[str, Any]:
    return {
        "tree": create_tree(
            depth=depth,
            branches=branches,
            list_size=list_size,
        ),
    }


def create_key_path(
    depth: int,
) -> tuple[str, ...]:
    return (
        "tree",
        *(("node_0",) * depth),
        "value",
    )


def resolve_key_path(
    value: Any,
    key_path: tuple[str, ...],
) -> Any:
    current = value

    for part in key_path:
        if isinstance(current, list):
            current = current[int(part)]
        else:
            current = current[part]

    return current


@pytest.fixture(scope="session", params=DATASETS)
def sample_data(
    request: pytest.FixtureRequest,
) -> tuple[dict[str, Any], tuple[str, ...]]:
    config = request.param

    return (
        create_data(**config),
        create_key_path(config["depth"]),
    )


def write_json(
    data: dict[str, Any],
) -> str:
    return json.dumps(data)


def write_yaml(
    data: dict[str, Any],
) -> str:
    return yaml.safe_dump(
        data,
        sort_keys=False,
    )


def write_json_property(
    data: dict[str, Any],
    key_path: tuple[str, ...],
) -> str:
    return json.dumps(
        resolve_key_path(
            data,
            key_path,
        ),
    )


def write_yaml_property(
    data: dict[str, Any],
    key_path: tuple[str, ...],
) -> str:
    return yaml.safe_dump(
        resolve_key_path(
            data,
            key_path,
        ),
        sort_keys=False,
    )


WRITERS = (
    write_json,
    write_yaml,
)

PROPERTY_WRITERS = (
    write_json_property,
    write_yaml_property,
)


@pytest.mark.parametrize(
    "writer",
    WRITERS,
)
def test_write(
    benchmark: pytest.BenchmarkFixture,
    sample_data: tuple[dict[str, Any], tuple[str, ...]],
    writer,
) -> None:
    benchmark.pedantic(
        writer,
        args=(sample_data[0],),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


@pytest.mark.parametrize(
    "writer",
    PROPERTY_WRITERS,
)
def test_write_property(
    benchmark: pytest.BenchmarkFixture,
    sample_data: tuple[dict[str, Any], tuple[str, ...]],
    writer,
) -> None:
    benchmark.pedantic(
        writer,
        args=(
            sample_data[0],
            sample_data[1],
        ),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_text_io_write.py
# ============================================================================================================ test session starts ============================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 4 items                                                                                                                                                                                                                           

# test/qlogicae_logis/v1/benchmark/runtime/test_text_io_write.py::test_write[sample_data0-write_json] PASSED                                                                                                                            [ 25%]
# test/qlogicae_logis/v1/benchmark/runtime/test_text_io_write.py::test_write[sample_data0-write_yaml] PASSED                                                                                                                            [ 50%]
# test/qlogicae_logis/v1/benchmark/runtime/test_text_io_write.py::test_write_property[sample_data0-write_json_property] PASSED                                                                                                          [ 75%]
# test/qlogicae_logis/v1/benchmark/runtime/test_text_io_write.py::test_write_property[sample_data0-write_yaml_property] PASSED                                                                                                          [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0203_latest.json



# ------------------------------------------------------------------------------------------------ benchmark: 4 tests ------------------------------------------------------------------------------------------------
# Name (time in us)                                                Min                   Max                  Mean             StdDev                Median                IQR            Outliers  Rounds  Iterations
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_write_property[sample_data0-write_json_property]         1.3415 (1.0)          2.1181 (1.0)          1.4842 (1.0)       0.1553 (1.0)          1.4138 (1.0)       0.1001 (1.0)           2;2      30         400
# test_write_property[sample_data0-write_yaml_property]        21.6840 (16.16)       22.2742 (10.52)       21.9120 (14.76)     0.1615 (1.04)        21.9031 (15.49)     0.2140 (2.14)          9;0      30         400
# test_write[sample_data0-write_json]                          27.0444 (20.16)       28.2099 (13.32)       27.3707 (18.44)     0.2216 (1.43)        27.3373 (19.34)     0.1942 (1.94)          5;2      30         400
# test_write[sample_data0-write_yaml]                       5,500.4287 (>1000.0)  5,656.6295 (>1000.0)  5,593.7453 (>1000.0)  37.9506 (244.34)   5,596.8310 (>1000.0)  37.6973 (376.63)        8;3      30         400
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ======================================================================================================= 4 passed in 90.91s (0:01:30) ========================================================================================================