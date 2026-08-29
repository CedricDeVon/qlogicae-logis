from typing import Any
__all__='TextManager',
class A:
	__slots__='_valid_file_extensions',
	def __init__(A):A._valid_file_extensions={'.txt'}
	@property
	def valid_file_extensions(self):return self._valid_file_extensions
	def is_valid(A,file_path):
		if file_path.suffix.lower()not in A.valid_file_extensions:return False
		return True