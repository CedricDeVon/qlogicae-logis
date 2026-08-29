from __future__ import annotations
_A=None
__all__='TextFileIoManager',
from typing import TYPE_CHECKING,Any
if TYPE_CHECKING:from pathlib import Path
_pathlib=_A
_SingletonManager=_A
_TextEncodingManager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _pathlib;global _SingletonManager;global _TextEncodingManager;import pathlib as A;from.singleton_manager import SingletonManager as B;from.text_encoding_manager import TextEncodingManager as C;_pathlib=A;_SingletonManager=B;_TextEncodingManager=C;_handle_dynamic_imports=lambda:_A
class TextFileIoManager:
	__slots__='_text_encoding_manager',
	def __init__(A):_handle_dynamic_imports();A._text_encoding_manager=_SingletonManager.get_singleton(_TextEncodingManager)
	def read_file(B,file_path):
		C=_pathlib.Path(file_path);A=''
		with C.open(mode='r',encoding=B._text_encoding_manager.selected_encoding)as D:A=D.read()or''
		return A
	def write_file(C,file_path,data):
		A=True;B=_pathlib.Path(file_path);B.parent.mkdir(parents=A,exist_ok=A)
		with B.open(mode='w',encoding=C._text_encoding_manager.selected_encoding)as D:D.write(str(data))
		return A