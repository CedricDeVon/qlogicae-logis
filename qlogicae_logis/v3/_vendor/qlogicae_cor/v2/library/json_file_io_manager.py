from __future__ import annotations
_A=None
__all__='JsonFileIoManager',
from typing import Any
_json=_A
_Path=_A
_SingletonManager=_A
_JsonManager=_A
_TextEncodingManager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _json;global _Path;global _SingletonManager;global _JsonManager;global _TextEncodingManager;import json;from pathlib import Path;from.json_manager import JsonManager as A;from.singleton_manager import SingletonManager as B;from.text_encoding_manager import TextEncodingManager as C;_json=json;_Path=Path;_SingletonManager=B;_JsonManager=A;_TextEncodingManager=C;_handle_dynamic_imports=lambda:_A
class JsonFileIoManager:
	def __init__(A):_handle_dynamic_imports();A._json_manager=_SingletonManager.get_singleton(_JsonManager);A._text_encoding_manager=_SingletonManager.get_singleton(_TextEncodingManager)
	def read_file(B,file_path):
		C=_Path(file_path);A={}
		with C.open(mode='r',encoding=B._text_encoding_manager.selected_encoding)as D:A=_json.load(D)or{}
		return A
	def write_file(A,file_path,data):
		B=True;C=_Path(file_path);C.parent.mkdir(parents=B,exist_ok=B)
		with C.open(mode='w',encoding=A._text_encoding_manager.selected_encoding)as D:_json.dump(data,D,indent=A._json_manager.indent_count,ensure_ascii=A._json_manager.is_ascii_format_enabled,sort_keys=A._json_manager.is_key_sortable)
		return B