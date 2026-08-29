from __future__ import annotations
B=None
__all__='FileIoManager',
from typing import Any
A=B
C=B
D=B
def E():global E;global A;global C;global D;from pathlib import Path;from.singleton_manager import SingletonManager as F;from.text_encoding_manager import TextEncodingManager as G;A=Path;C=F;D=G;E=lambda:B
class F:
	__slots__='_text_encoding_manager',
	def __init__(A):E();A._text_encoding_manager=C.get_singleton(D)
	def read_file(B,file_path):
		C=A(file_path)
		with C.open(mode='r',encoding=B._text_encoding_manager.selected_encoding)as D:return D.read()or''
	def write_file(D,file_path,data):
		B=True;C=A(file_path);C.parent.mkdir(parents=B,exist_ok=B)
		with C.open(mode='w',encoding=D._text_encoding_manager.selected_encoding)as E:E.write(str(data))
		return B