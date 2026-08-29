from __future__ import annotations
A=property
__all__='JsonManager',
from typing import Any
B=None
def C():global C;global B;from pathlib import Path;B=Path;C=lambda:None
class D:
	__slots__='_valid_file_extensions','_is_ascii_format_enabled','_indent_count','_is_key_sortable'
	def __init__(A):B=False;C();A._valid_file_extensions={'.json'};A._is_ascii_format_enabled=B;A._indent_count=4;A._is_key_sortable=B
	@A
	def valid_file_extensions(self):return self._valid_file_extensions
	def is_valid(A,file_path):C=B(file_path);return C.suffix.lower()in A.valid_file_extensions
	@A
	def is_ascii_format_enabled(self):return self._is_ascii_format_enabled
	@is_ascii_format_enabled.setter
	def is_ascii_format_enabled(self,value):self._is_ascii_format_enabled=value
	@A
	def indent_count(self):return self._indent_count
	@indent_count.setter
	def indent_count(self,value):
		A=value
		if A<0:raise ValueError('indent_count must be non-negative.')
		self._indent_count=A
	@A
	def is_key_sortable(self):return self._is_key_sortable
	@is_key_sortable.setter
	def is_key_sortable(self,value):self._is_key_sortable=value