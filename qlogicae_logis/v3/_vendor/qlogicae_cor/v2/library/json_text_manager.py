from __future__ import annotations
_A=None
__all__='JsonTextManager',
from typing import Any
_json=_A
_SingletonManager=_A
_JsonManager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _json;global _SingletonManager;global _JsonManager;import json;from.json_manager import JsonManager as A;from.singleton_manager import SingletonManager as B;_json=json;_SingletonManager=B;_JsonManager=A;_handle_dynamic_imports=lambda:_A
class JsonTextManager:
	__slots__='_json_manager',
	def __init__(A):_handle_dynamic_imports();A._json_manager=_SingletonManager.get_singleton(_JsonManager)
	def is_valid(A,value):_json.loads(value);return True
	def convert_to_object(A,value):return _json.loads(value)
	def convert_to_string(A,value):B=_json.dumps(value,indent=A._json_manager.indent_count,ensure_ascii=A._json_manager.is_ascii_format_enabled);return B