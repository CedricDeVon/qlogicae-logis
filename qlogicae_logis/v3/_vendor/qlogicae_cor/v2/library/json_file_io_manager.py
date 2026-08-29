from __future__ import annotations
A=None
__all__='JsonFileIoManager',
from typing import Any
B=A
C=A
D=A
E=A
F=A
def G():global G;global B;global C;global D;global E;global F;import json;from pathlib import Path;from.json_manager import JsonManager as H;from.singleton_manager import SingletonManager as I;from.text_encoding_manager import TextEncodingManager as J;B=json;C=Path;D=I;E=H;F=J;G=lambda:A
class H:
	def __init__(A):G();A._json_manager=D.get_singleton(E);A._text_encoding_manager=D.get_singleton(F)
	def read_file(D,file_path):
		E=C(file_path);A={}
		with E.open(mode='r',encoding=D._text_encoding_manager.selected_encoding)as F:A=B.load(F)or{}
		return A
	def write_file(A,file_path,data):
		D=True;E=C(file_path);E.parent.mkdir(parents=D,exist_ok=D)
		with E.open(mode='w',encoding=A._text_encoding_manager.selected_encoding)as F:B.dump(data,F,indent=A._json_manager.indent_count,ensure_ascii=A._json_manager.is_ascii_format_enabled,sort_keys=A._json_manager.is_key_sortable)
		return D