from __future__ import annotations

import json
from typing import Any

import pytest
import yaml

ROUNDS = 30
ITERATIONS = 40_000
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
            "items": list(range(list_size)),
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
) -> tuple[str, str, tuple[str, ...]]:
    config = request.param

    data = create_data(**config)

    return (
        json.dumps(data),
        yaml.safe_dump(
            data,
            sort_keys=False,
        ),
        create_key_path(config["depth"]),
    )


def parse_json(
    text: str,
) -> Any:
    return json.loads(text)


def parse_yaml(
    text: str,
) -> Any:
    return yaml.safe_load(text)


def parse_json_property(
    text: str,
    key_path: tuple[str, ...],
) -> Any:
    return resolve_key_path(
        json.loads(text),
        key_path,
    )


def parse_yaml_property(
    text: str,
    key_path: tuple[str, ...],
) -> Any:
    return resolve_key_path(
        yaml.safe_load(text),
        key_path,
    )


PARSERS = (
    (0, parse_json),
    (1, parse_yaml),
)

PROPERTY_PARSERS = (
    (0, parse_json_property),
    (1, parse_yaml_property),
)


@pytest.mark.parametrize(
    ("index", "parser"),
    PARSERS,
)
def test_parse(
    benchmark: pytest.BenchmarkFixture,
    sample_data: tuple[str, str, tuple[str, ...]],
    index: int,
    parser,
) -> None:
    benchmark.pedantic(
        parser,
        args=(sample_data[index],),
        rounds=ROUNDS,
        iterations=ITERATIONS,
    )


@pytest.mark.parametrize(
    ("index", "parser"),
    PROPERTY_PARSERS,
)
def test_parse_property(
    benchmark: pytest.BenchmarkFixture,
    sample_data: tuple[str, str, tuple[str, ...]],
    index: int,
    parser,
) -> None:
    benchmark.pedantic(
        parser,
        args=(
            sample_data[index],
            sample_data[2],
        ),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )


# pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_text_io_read.py
# ============================================================================================================ test session starts ============================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 2 items

# test/qlogicae_logis/v1/benchmark/runtime/test_text_io_read.py::test_parse[sample_data0-0-parse_json] PASSED                                                                                                                           [ 50%]
# test/qlogicae_logis/v1/benchmark/runtime/test_text_io_read.py::test_parse_property[sample_data0-0-parse_json_property] PASSED                                                                                                         [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0197_latest.json



# ------------------------------------------------------------------------------------------ benchmark: 2 tests ------------------------------------------------------------------------------------------
# Name (time in us)                                               Min                Max               Mean            StdDev             Median               IQR            Outliers  Rounds  Iterations
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_parse[sample_data0-0-parse_json]                       20.7073 (1.0)      22.2286 (1.0)      21.2054 (1.0)      0.2985 (4.40)     21.1874 (1.0)      0.3510 (3.69)          6;1      30       40000
# test_parse_property[sample_data0-0-parse_json_property]     22.0008 (1.06)     22.2906 (1.00)     22.1647 (1.05)     0.0678 (1.0)      22.1649 (1.05)     0.0951 (1.0)           9;0      30       40000
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ======================================================================================================= 2 passed in 62.10s (0:01:02) ========================================================================================================



# from __future__ import annotations

# import json
# from typing import Any

# import pytest
# import yaml

# ROUNDS = 30
# ITERATIONS = 100
# WARMUP_ROUNDS = 10

# DATASETS = (
#     {
#         "depth": 5,
#         "branches": 2,
#         "list_size": 10,
#     },
# )


# def create_tree(
#     *,
#     depth: int,
#     branches: int,
#     list_size: int,
# ) -> dict[str, Any]:
#     if depth == 0:
#         return {
#             "items": list(range(list_size)),
#         }

#     return {
#         f"node_{index}": create_tree(
#             depth=depth - 1,
#             branches=branches,
#             list_size=list_size,
#         )
#         for index in range(branches)
#     }


# def create_data(
#     *,
#     depth: int,
#     branches: int,
#     list_size: int,
# ) -> dict[str, Any]:
#     return {
#         "tree": create_tree(
#             depth=depth,
#             branches=branches,
#             list_size=list_size,
#         ),
#     }


# def create_key_path(
#     depth: int,
# ) -> tuple[str, ...]:
#     return (
#         "tree",
#         *(("node_0",) * depth),
#     )


# def resolve_key_path(
#     value: Any,
#     key_path: tuple[str, ...],
# ) -> Any:
#     current = value

#     for part in key_path:
#         if isinstance(current, list):
#             current = current[int(part)]
#         else:
#             current = current[part]

#     return current


# @pytest.fixture(scope="session", params=DATASETS)
# def sample_data(
#     request: pytest.FixtureRequest,
# ) -> tuple[str, str, tuple[str, ...]]:
#     config = request.param

#     data = create_data(**config)

#     return (
#         json.dumps(data),
#         yaml.safe_dump(
#             data,
#             sort_keys=False,
#         ),
#         create_key_path(config["depth"]),
#     )


# def parse_json(
#     text: str,
# ) -> Any:
#     return json.loads(text)


# def parse_yaml(
#     text: str,
# ) -> Any:
#     return yaml.safe_load(text)


# def parse_json_property(
#     text: str,
#     key_path: tuple[str, ...],
# ) -> Any:
#     return resolve_key_path(
#         json.loads(text),
#         key_path,
#     )


# def parse_yaml_property(
#     text: str,
#     key_path: tuple[str, ...],
# ) -> Any:
#     return resolve_key_path(
#         yaml.safe_load(text),
#         key_path,
#     )


# PARSERS = (
#     (0, parse_json),
#     (1, parse_yaml),
# )

# PROPERTY_PARSERS = (
#     (0, parse_json_property),
#     (1, parse_yaml_property),
# )


# @pytest.mark.parametrize(
#     ("index", "parser"),
#     PARSERS,
# )
# def test_parse(
#     benchmark: pytest.BenchmarkFixture,
#     sample_data: tuple[str, str, tuple[str, ...]],
#     index: int,
#     parser,
# ) -> None:
#     benchmark.pedantic(
#         parser,
#         args=(sample_data[index],),
#         rounds=ROUNDS,
#         iterations=ITERATIONS,
#     )


# @pytest.mark.parametrize(
#     ("index", "parser"),
#     PROPERTY_PARSERS,
# )
# def test_parse_property(
#     benchmark: pytest.BenchmarkFixture,
#     sample_data: tuple[str, str, tuple[str, ...]],
#     index: int,
#     parser,
# ) -> None:
#     benchmark.pedantic(
#         parser,
#         args=(
#             sample_data[index],
#             sample_data[2],
#         ),
#         rounds=ROUNDS,
#         iterations=ITERATIONS,
#         warmup_rounds=WARMUP_ROUNDS,
#     )


#  pytest -vv --benchmark-only --benchmark-disable-gc --benchmark-verbose --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,median,iqr,outliers,rounds,iterations --benchmark-json=benchmark.json --benchmark-histogram=benchmark --benchmark-save=latest --benchmark-disable-gc test/qlogicae_logis/v1/benchmark/runtime/test_text_io_read.py
# ============================================================================================================ test session starts ============================================================================================================
# platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.6.0 -- /home/cedricdevon/workspace/qlogicae/.venv/bin/python3
# cachedir: .pytest_cache
# benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=True min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: /home/cedricdevon/workspace/qlogicae
# configfile: pyproject.toml
# plugins: cov-7.1.0, anyio-4.14.1, benchmark-5.2.3
# collected 2 items

# test/qlogicae_logis/v1/benchmark/runtime/test_text_io_read.py::test_parse[sample_data0-1-parse_yaml] PASSED                                                                                                                           [ 50%]
# test/qlogicae_logis/v1/benchmark/runtime/test_text_io_read.py::test_parse_property[sample_data0-1-parse_yaml_property] PASSED                                                                                                         [100%]
# Wrote benchmark data in: <_io.BufferedWriter name='benchmark.json'>

# Saved benchmark data in: /home/cedricdevon/workspace/qlogicae/.benchmarks/Linux-CPython-3.14-64bit/0198_latest.json



# ------------------------------------------------------------------------------------------ benchmark: 2 tests ------------------------------------------------------------------------------------------
# Name (time in ms)                                               Min                Max               Mean            StdDev             Median               IQR            Outliers  Rounds  Iterations
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_parse[sample_data0-1-parse_yaml]                        9.6124 (1.0)       9.9876 (1.0)       9.8284 (1.0)      0.1087 (1.44)      9.8281 (1.0)      0.1816 (2.18)         11;0      30         100
# test_parse_property[sample_data0-1-parse_yaml_property]     10.1431 (1.06)     10.4024 (1.04)     10.2182 (1.04)     0.0757 (1.0)      10.1888 (1.04)     0.0833 (1.0)           4;3      30         100
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Generated histogram: benchmark.svg
# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
#   OPS: Operations Per Second, computed as 1 / Mean
# ======================================================================================================= 2 passed in 71.51s (0:01:11) ========================================================================================================
