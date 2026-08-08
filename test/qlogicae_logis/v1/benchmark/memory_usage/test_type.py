from __future__ import annotations

import functools
import re
import sys
import types
import weakref
from array import array
from collections import (
    ChainMap,
    Counter,
    OrderedDict,
    UserDict,
    UserList,
    UserString,
    defaultdict,
    deque,
)
from dataclasses import dataclass
from datetime import UTC, date, datetime, time, timedelta
from decimal import Decimal
from enum import Enum, Flag, IntEnum, IntFlag, StrEnum, auto
from fractions import Fraction
from io import BytesIO, FileIO, StringIO
from pathlib import Path
from types import MappingProxyType, SimpleNamespace

from pympler import asizeof


class Color(Enum):
    RED = 1


class Number(IntEnum):
    ONE = 1


class Permission(Flag):
    READ = auto()
    WRITE = auto()


class PermissionInt(IntFlag):
    READ = 1
    WRITE = 2


class Direction(StrEnum):
    LEFT = "left"


@dataclass
class DataClass:
    value: int = 123


@dataclass(frozen=True)
class FrozenDataClass:
    value: int = 123


class CustomClass:
    def __init__(self):
        self.value = 123


class SlotsClass:
    __slots__ = ("value",)

    def __init__(self):
        self.value = 123


def sample_function():
    return 42


lambda_function = lambda: 42


class Example:
    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method():
        pass

    @property
    def value(self):
        return 123


example = Example()

generator = (x for x in range(3))
enumeration = enumerate([1, 2, 3])
zip_object = zip([1], [2])
map_object = map(str, [1, 2, 3])
filter_object = filter(bool, [0, 1])
reversed_object = reversed([1, 2, 3])

compiled_regex = re.compile(r"\d+")

user_dict = UserDict({"a": 1})
user_list = UserList([1, 2, 3])
user_string = UserString("hello")

chain_map = ChainMap({"a": 1}, {"b": 2})

memory = bytearray(b"hello world")
memory_view = memoryview(memory)

weak_target = CustomClass()
weak_reference = weakref.ref(weak_target)

OBJECTS = {
    "None": None,
    "Ellipsis": Ellipsis,
    "NotImplemented": NotImplemented,

    "bool": True,
    "int": 123,
    "float": 123.456,
    "complex": complex(1, 2),
    "Decimal": Decimal("123.456"),
    "Fraction": Fraction(22, 7),

    "str": "hello world",
    "bytes": b"hello world",
    "bytearray": bytearray(b"hello world"),
    "memoryview": memoryview(bytearray(b"hello world")),

    "list": [1, 2, 3],
    "tuple": (1, 2, 3),
    "range": range(100),
    "array": array("i", [1, 2, 3]),
    "arrayByte": array("b", [1, 2, 3]),
    "arrayDouble": array("d", [1.0, 2.0, 3.0]),
    "deque": deque([1, 2, 3]),
    "dequeEmpty": deque(),
    "UserList": UserList([1, 2, 3]),
    "UserString": UserString("hello"),

    "set": {1, 2, 3},
    "frozenset": frozenset({1, 2, 3}),

    "dict": {"a": 1},
    "defaultdict": defaultdict(int),
    "defaultdictList": defaultdict(list),
    "defaultdictSet": defaultdict(set),
    "OrderedDict": OrderedDict(a=1),
    "OrderedDictEmpty": OrderedDict(),
    "Counter": Counter("banana"),
    "CounterEmpty": Counter(),
    "ChainMap": ChainMap({"a": 1}, {"b": 2}),
    "ChainMapEmpty": ChainMap(),
    "MappingProxy": MappingProxyType({"a": 1}),
    "MappingProxyType": types.MappingProxyType({"a": 1}),
    "UserDict": UserDict({"a": 1}),

    "dict_keys": {}.keys(),
    "dict_values": {}.values(),
    "dict_items": {}.items(),

    "list_iterator": iter([]),
    "tuple_iterator": iter(()),
    "str_iterator": iter("abc"),
    "bytes_iterator": iter(b"abc"),
    "bytearray_iterator": iter(bytearray(b"abc")),
    "range_iterator": iter(range(10)),
    "set_iterator": iter({1, 2, 3}),
    "frozenset_iterator": iter(frozenset({1, 2, 3})),
    "dict_iterator": iter({1: 1}),
    "dict_keyiterator": iter({1: 1}.keys()),
    "dict_valueiterator": iter({1: 1}.values()),
    "dict_itemiterator": iter({1: 1}.items()),
    "enumerate": enumerate([1, 2, 3]),
    "enumerate_empty": enumerate([]),
    "zip": zip([1], [2]),
    "zip_empty": zip(),
    "map": map(str, [1, 2, 3]),
    "map_empty": map(str, []),
    "filter": filter(bool, [0, 1]),
    "filter_empty": filter(None, []),
    "reversed": reversed([1, 2, 3]),
    "generator": (x for x in range(3)),
    "GeneratorType": (i for i in range(1)),

    "function": sample_function,
    "lambda": lambda_function,
    "partial": functools.partial(sample_function),
    "BuiltinFunction": len,
    "BuiltinMethod": [].append,
    "bound_method": example.class_method,
    "classmethod": Example.__dict__["class_method"],
    "staticmethod": Example.__dict__["static_method"],
    "property": Example.__dict__["value"],
    "MethodType": types.MethodType(sample_function, object()),
    "FunctionType": types.FunctionType(
        sample_function.__code__,
        globals(),
        "copy_function",
    ),
    "MethodWrapper": [].__len__,
    "MethodDescriptor": str.join,
    "BuiltinMethodDescriptor": list.append,
    "ClassMethodDescriptor": dict.fromkeys,
    "GetSetDescriptor": type.__dict__["__name__"],
    "MemberDescriptor": SlotsClass.value,

    "Enum": Color.RED,
    "IntEnum": Number.ONE,
    "Flag": Permission.READ,
    "IntFlag": PermissionInt.READ,
    "StrEnum": Direction.LEFT,

    "date": date.today(),
    "time": time(),
    "datetime": datetime.now(),
    "timedelta": timedelta(days=1),
    "timezone": UTC,

    "BytesIO": BytesIO(b"hello"),
    "BytesIOEmpty": BytesIO(),
    "StringIO": StringIO("hello"),
    "StringIOEmpty": StringIO(),
    "FileIO": FileIO(__file__, "rb"),
    "BufferedReader": FileIO(__file__, "rb"),
    "TextIO": open(__file__, encoding="utf-8"),

    "Path": Path.cwd(),
    "PathCurrent": Path(),
    "PathParent": Path(".."),
    "PathRoot": Path("/"),
    "PathHome": Path.home(),
    "PurePosixPath": __import__("pathlib").PurePosixPath("/tmp"),
    "PureWindowsPath": __import__("pathlib").PureWindowsPath(r"C:\\"),

    "Pattern": re.compile(r"\d+"),
    "PatternBytes": re.compile(rb"\d+"),
    "Match": re.match(r"\d+", "123"),
    "MatchBytes": re.match(rb"\d+", b"123"),

    "object": object(),
    "type": type,
    "module": types,
    "ModuleType": types.ModuleType("test"),
    "ModuleTypeEmpty": types.ModuleType("empty"),
    "ModuleTypeCustom": types.ModuleType("custom"),
    "SimpleNamespace": SimpleNamespace(a=1),
    "SimpleNamespaceEmpty": types.SimpleNamespace(),
    "SimpleNamespaceMulti": types.SimpleNamespace(a=1, b=2, c=3),
    "DynamicClassAttribute": types.DynamicClassAttribute(),
    "slice": slice(0, 10),
    "sliceEmpty": slice(None),
    "sliceStep": slice(0, 100, 2),
    "code": sample_function.__code__,
    "CodeType": sample_function.__code__,
    "FrameType": sys._getframe(),
    "FrameCurrent": sys._getframe(),
    "CellType": (lambda x: lambda: x)(1).__closure__[0],
    "Cell": (lambda x: lambda: x)(42).__closure__[0],
    "super": super(Example, example),

    "dataclass": DataClass(),
    "frozen_dataclass": FrozenDataClass(),
    "custom_class": CustomClass(),
    "slots_class": SlotsClass(),

    "weakref": weakref.ref(CustomClass()),
    "WeakSet": weakref.WeakSet(),
    "WeakKeyDictionary": weakref.WeakKeyDictionary(),
    "WeakValueDictionary": weakref.WeakValueDictionary(),

    "GenericAlias": list[int],
    "GenericAliasList": list[int],
    "GenericAliasDict": dict[str, int],
    "GenericAliasTuple": tuple[int, str],
    "GenericAliasSet": set[int],
    "GenericAliasFrozenSet": frozenset[int],
    "GenericAliasDeque": deque[int],
    "GenericAliasDefaultDict": defaultdict[str, int],
    "UnionType": int | str,
    "UnionTypeThree": int | str | float,

    "ascii": ascii,
    "bin": bin,
    "chr": chr,
    "dir": dir,
    "divmod": divmod,
    "globals": globals,
    "hash": hash,
    "hex": hex,
    "id": id,
    "isinstance": isinstance,
    "issubclass": issubclass,
    "iter": iter,
    "len": len,
    "locals": locals,
    "max": max,
    "min": min,
    "next": next,
    "oct": oct,
    "open": open,
    "ord": ord,
    "print": print,
    "repr": repr,
    "round": round,
    "sorted": sorted,
    "sum": sum,
    "vars": vars,
    "BaseException": BaseException(),
    "BaseExceptionGroup": BaseExceptionGroup("group", [Exception()]),

    "GeneratorExit": GeneratorExit(),
    "KeyboardInterrupt": KeyboardInterrupt(),
    "SystemExit": SystemExit(),
    "Exception": Exception(),
    "ExceptionGroup": ExceptionGroup("group", [Exception()]),

    "ArithmeticError": ArithmeticError(),
    "FloatingPointError": FloatingPointError(),
    "OverflowError": OverflowError(),
    "ZeroDivisionError": ZeroDivisionError(),

    "AssertionError": AssertionError(),
    "AttributeError": AttributeError(),
    "BufferError": BufferError(),
    "EOFError": EOFError(),

    "ImportError": ImportError(),
    "ModuleNotFoundError": ModuleNotFoundError(),

    "LookupError": LookupError(),
    "IndexError": IndexError(),
    "KeyError": KeyError(),

    "MemoryError": MemoryError(),

    "NameError": NameError(),
    "UnboundLocalError": UnboundLocalError(),

    "OSError": OSError(),
    "BlockingIOError": BlockingIOError(),
    "ChildProcessError": ChildProcessError(),
    "ConnectionError": ConnectionError(),
    "BrokenPipeError": BrokenPipeError(),
    "ConnectionAbortedError": ConnectionAbortedError(),
    "ConnectionRefusedError": ConnectionRefusedError(),
    "ConnectionResetError": ConnectionResetError(),
    "FileExistsError": FileExistsError(),
    "FileNotFoundError": FileNotFoundError(),
    "InterruptedError": InterruptedError(),
    "IsADirectoryError": IsADirectoryError(),
    "NotADirectoryError": NotADirectoryError(),
    "PermissionError": PermissionError(),
    "ProcessLookupError": ProcessLookupError(),
    "TimeoutError": TimeoutError(),

    "ReferenceError": ReferenceError(),

    "RuntimeError": RuntimeError(),
    "NotImplementedError": NotImplementedError(),
    "RecursionError": RecursionError(),

    "StopAsyncIteration": StopAsyncIteration(),
    "StopIteration": StopIteration(),

    "SyntaxError": SyntaxError(),
    "IndentationError": IndentationError(),
    "TabError": TabError(),

    "SystemError": SystemError(),

    "TypeError": TypeError(),

    "ValueError": ValueError(),
    "UnicodeError": UnicodeError(),
    "UnicodeDecodeError": UnicodeDecodeError(
        "utf-8",
        b"\xff",
        0,
        1,
        "invalid start byte",
    ),
    "UnicodeEncodeError": UnicodeEncodeError(
        "utf-8",
        "\ud800",
        0,
        1,
        "surrogate not allowed",
    ),
    "UnicodeTranslateError": UnicodeTranslateError(
        "abc",
        0,
        1,
        "cannot translate",
    ),

    "Warning": Warning(),
    "BytesWarning": BytesWarning(),
    "DeprecationWarning": DeprecationWarning(),
    "EncodingWarning": EncodingWarning(),
    "FutureWarning": FutureWarning(),
    "ImportWarning": ImportWarning(),
    "PendingDeprecationWarning": PendingDeprecationWarning(),
    "ResourceWarning": ResourceWarning(),
    "RuntimeWarning": RuntimeWarning(),
    "SyntaxWarning": SyntaxWarning(),
    "UnicodeWarning": UnicodeWarning(),
    "UserWarning": UserWarning(),
}

def benchmark() -> None:
    print(
        f"{'Type':<20}"
        f"{'Shallow(Bytes)':>18}"
        f"{'Deep(Bytes)':>18}"
    )

    print('-' * 80)

    for name, obj in OBJECTS.items():
        shallow = sys.getsizeof(obj)
        deep = asizeof.asizeof(obj)

        print(
            f"{name:<20}"
            f"{shallow:>18}"
            f"{deep:>18}"
        )
        print('-' * 80)


if __name__ == "__main__":
    benchmark()


