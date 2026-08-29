__all__='PlaceholderValueManager',
class PlaceholderValueManager:
	__slots__='_none','_not_a_number','_redacted','_expunged'
	def __init__(A):A._none='none';A._not_a_number='nan';A._redacted='redacted';A._expunged='expunged'
	@property
	def none(self):return self._none
	@none.setter
	def none(self,value):self._none=value
	@property
	def not_a_number(self):return self._not_a_number
	@not_a_number.setter
	def not_a_number(self,value):self._not_a_number=value
	@property
	def redacted(self):return self._redacted
	@redacted.setter
	def redacted(self,value):self._redacted=value
	@property
	def expunged(self):return self._expunged
	@expunged.setter
	def expunged(self,value):self._expunged=value