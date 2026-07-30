from __future__ import annotations

def _initialize() -> None:
    global _initialize

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

    _initialize = lambda: None


def sum(
    a: int,
    b: int,
) -> int:
    _initialize()

    return a + b

