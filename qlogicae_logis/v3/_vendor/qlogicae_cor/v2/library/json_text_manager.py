from __future__ import annotations
B=None
__all__='JsonTextManager',
from typing import Any
A=B
C=B
D=B
def E():global E;global A;global C;global D;import json;from.json_manager import JsonManager as F;from.singleton_manager import SingletonManager as G;A=json;C=G;D=F;E=lambda:B
class F:
	__slots__='_json_manager',
	def __init__(A):E();A._json_manager=C.get_singleton(D)
	def is_valid(B,value):A.loads(value);return True
	def convert_to_object(B,value):return A.loads(value)
	def convert_to_string(B,value):C=A.dumps(value,indent=B._json_manager.indent_count,ensure_ascii=B._json_manager.is_ascii_format_enabled);return C