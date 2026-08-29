from __future__ import annotations
_A=None
__all__='FileIoManager',
from typing import Any
_Path=_A
_singleton_manager=_A
_text_encoding_manager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _Path;global _singleton_manager;global _text_encoding_manager;from pathlib import Path;from.singleton_manager import SingletonManager as A;from.text_encoding_manager import TextEncodingManager as B;_Path=Path;_singleton_manager=A;_text_encoding_manager=B;_handle_dynamic_imports=lambda:_A
class FileIoManager:
	__slots__='_text_encoding_manager',
	def __init__(A):_handle_dynamic_imports();A._text_encoding_manager=_singleton_manager.get_singleton(_text_encoding_manager)
	def read_file(A,file_path):
		B=_Path(file_path)
		with B.open(mode='r',encoding=A._text_encoding_manager.selected_encoding)as C:return C.read()or''
	def write_file(C,file_path,data):
		A=True;B=_Path(file_path);B.parent.mkdir(parents=A,exist_ok=A)
		with B.open(mode='w',encoding=C._text_encoding_manager.selected_encoding)as D:D.write(str(data))
		return A