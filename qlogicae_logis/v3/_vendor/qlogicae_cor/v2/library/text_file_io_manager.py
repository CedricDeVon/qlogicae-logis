from __future__ import annotations
B=None
__all__='TextFileIoManager',
from typing import TYPE_CHECKING as F,Any
if F:from pathlib import Path
A=B
C=B
D=B
def E():global E;global A;global C;global D;import pathlib as F;from.singleton_manager import SingletonManager as G;from.text_encoding_manager import TextEncodingManager as H;A=F;C=G;D=H;E=lambda:B
class G:
	__slots__='_text_encoding_manager',
	def __init__(A):E();A._text_encoding_manager=C.get_singleton(D)
	def read_file(C,file_path):
		D=A.Path(file_path);B=''
		with D.open(mode='r',encoding=C._text_encoding_manager.selected_encoding)as E:B=E.read()or''
		return B
	def write_file(D,file_path,data):
		B=True;C=A.Path(file_path);C.parent.mkdir(parents=B,exist_ok=B)
		with C.open(mode='w',encoding=D._text_encoding_manager.selected_encoding)as E:E.write(str(data))
		return B