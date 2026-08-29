from __future__ import annotations
__all__='JsonManager',
from typing import Any
_Path=None
def _handle_dynamic_imports():global _handle_dynamic_imports;global _Path;from pathlib import Path;_Path=Path;_handle_dynamic_imports=lambda:None
class JsonManager:
	__slots__='_valid_file_extensions','_is_ascii_format_enabled','_indent_count','_is_key_sortable'
	def __init__(A):B=False;_handle_dynamic_imports();A._valid_file_extensions={'.json'};A._is_ascii_format_enabled=B;A._indent_count=4;A._is_key_sortable=B
	@property
	def valid_file_extensions(self):return self._valid_file_extensions
	def is_valid(A,file_path):B=_Path(file_path);return B.suffix.lower()in A.valid_file_extensions
	@property
	def is_ascii_format_enabled(self):return self._is_ascii_format_enabled
	@is_ascii_format_enabled.setter
	def is_ascii_format_enabled(self,value):self._is_ascii_format_enabled=value
	@property
	def indent_count(self):return self._indent_count
	@indent_count.setter
	def indent_count(self,value):
		A=value
		if A<0:raise ValueError('indent_count must be non-negative.')
		self._indent_count=A
	@property
	def is_key_sortable(self):return self._is_key_sortable
	@is_key_sortable.setter
	def is_key_sortable(self,value):self._is_key_sortable=value