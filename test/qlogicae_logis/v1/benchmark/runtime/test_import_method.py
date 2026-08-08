from __future__ import annotations

from types import ModuleType

import pytest

ROUNDS = 30
ITERATIONS = 1_000_000
WARMUP_ROUNDS = 10

import asyncio
import email
import inspect
import logging
import multiprocessing
import sqlite3
import ssl
import tkinter
import urllib.request
import xml.etree.ElementTree

import yaml


def static_sum(
    a: int,
    b: int,
) -> int:
    return a + b


_asyncio: ModuleType | None = None
_email: ModuleType | None = None
_inspect: ModuleType | None = None
_logging: ModuleType | None = None
_multiprocessing: ModuleType | None = None
_sqlite3: ModuleType | None = None
_ssl: ModuleType | None = None
_tkinter: ModuleType | None = None
_urllib: ModuleType | None = None
_xml: ModuleType | None = None
_yaml: ModuleType | None = None


def _initialized() -> None:
    pass


def _initialize() -> None:
    global _initialize

    global _asyncio
    global _email
    global _inspect
    global _logging
    global _multiprocessing
    global _sqlite3
    global _ssl
    global _tkinter
    global _urllib
    global _xml
    global _yaml


    _asyncio = asyncio
    _email = email
    _inspect = inspect
    _logging = logging
    _multiprocessing = multiprocessing
    _sqlite3 = sqlite3
    _ssl = ssl
    _tkinter = tkinter
    _urllib = urllib.request
    _xml = xml.etree.ElementTree
    _yaml = yaml

    _initialize = _initialized


def lazy_sum(
    a: int,
    b: int,
) -> int:
    _initialize()

    return a + b


def import_every_call_sum(
    a: int,
    b: int,
) -> int:

    return a + b


FUNCTIONS = (
    static_sum,
    lazy_sum,
    import_every_call_sum,
)


@pytest.mark.parametrize(
    "function",
    FUNCTIONS,
)
def test_import_overhead(
    benchmark: pytest.BenchmarkFixture,
    function,
) -> None:
    result = benchmark.pedantic(
        function,
        args=(1, 2),
        rounds=ROUNDS,
        iterations=ITERATIONS,
        warmup_rounds=WARMUP_ROUNDS,
    )

    assert result == 3
