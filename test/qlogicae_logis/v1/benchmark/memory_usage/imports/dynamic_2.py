from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
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

asyncio: Any = None
email: Any = None
inspect: Any = None
logging: Any = None
multiprocessing: Any = None
sqlite3: Any = None
ssl: Any = None
tkinter: Any = None
urllib: Any = None
xml: Any = None
yaml: Any = None


def _initialize() -> None:
    global _initialize

    global asyncio
    global email
    global inspect
    global logging
    global multiprocessing
    global sqlite3
    global ssl
    global tkinter
    global urllib
    global xml
    global yaml

    import asyncio as _asyncio
    import email as _email
    import inspect as _inspect
    import logging as _logging
    import multiprocessing as _multiprocessing
    import sqlite3 as _sqlite3
    import ssl as _ssl
    import tkinter as _tkinter
    import urllib.request as _urllib
    import xml.etree.ElementTree as _xml

    import yaml as _yaml

    asyncio = _asyncio
    email = _email
    inspect = _inspect
    logging = _logging
    multiprocessing = _multiprocessing
    sqlite3 = _sqlite3
    ssl = _ssl
    tkinter = _tkinter
    urllib = _urllib
    xml = _xml
    yaml = _yaml

    _initialize = lambda: None 


def sum(
    a: int,
    b: int,
) -> int:
    _initialize()

    return a + b