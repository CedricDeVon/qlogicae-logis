__all__='TextEncodingManager',
class A:
	__slots__='_selected_encoding',
	def __init__(A):A._selected_encoding='utf-8'
	@property
	def selected_encoding(self):return self._selected_encoding
	@selected_encoding.setter
	def selected_encoding(self,value):self._selected_encoding=value