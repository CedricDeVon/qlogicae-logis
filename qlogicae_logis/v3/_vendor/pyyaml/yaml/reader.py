_A=None
__all__=['Reader','ReaderError']
import codecs,re
from.error import Mark,YAMLError
class ReaderError(YAMLError):
	def __init__(A,name,position,character,encoding,reason):A.name=name;A.character=character;A.position=position;A.encoding=encoding;A.reason=reason
	def __str__(A):
		if isinstance(A.character,bytes):return'\'%s\' codec can\'t decode byte #x%02x: %s\n  in "%s", position %d'%(A.encoding,ord(A.character),A.reason,A.name,A.position)
		else:return'unacceptable character #x%04x: %s\n  in "%s", position %d'%(A.character,A.reason,A.name,A.position)
class Reader:
	def __init__(A,stream):
		B=stream;A.name=_A;A.stream=_A;A.stream_pointer=0;A.eof=True;A.buffer='';A.pointer=0;A.raw_buffer=_A;A.raw_decode=_A;A.encoding=_A;A.index=0;A.line=0;A.column=0
		if isinstance(B,str):A.name='<unicode string>';A.check_printable(B);A.buffer=B+'\x00'
		elif isinstance(B,bytes):A.name='<byte string>';A.raw_buffer=B;A.determine_encoding()
		else:A.stream=B;A.name=getattr(B,'name','<file>');A.eof=False;A.raw_buffer=_A;A.determine_encoding()
	def peek(A,index=0):
		B=index
		try:return A.buffer[A.pointer+B]
		except IndexError:A.update(B+1);return A.buffer[A.pointer+B]
	def prefix(A,length=1):
		B=length
		if A.pointer+B>=len(A.buffer):A.update(B)
		return A.buffer[A.pointer:A.pointer+B]
	def forward(A,length=1):
		B=length
		if A.pointer+B+1>=len(A.buffer):A.update(B+1)
		while B:
			C=A.buffer[A.pointer];A.pointer+=1;A.index+=1
			if C in'\n\x85\u2028\u2029'or C=='\r'and A.buffer[A.pointer]!='\n':A.line+=1;A.column=0
			elif C!='\ufeff':A.column+=1
			B-=1
	def get_mark(A):
		if A.stream is _A:return Mark(A.name,A.index,A.line,A.column,A.buffer,A.pointer)
		else:return Mark(A.name,A.index,A.line,A.column,_A,_A)
	def determine_encoding(A):
		while not A.eof and(A.raw_buffer is _A or len(A.raw_buffer)<2):A.update_raw()
		if isinstance(A.raw_buffer,bytes):
			if A.raw_buffer.startswith(codecs.BOM_UTF16_LE):A.raw_decode=codecs.utf_16_le_decode;A.encoding='utf-16-le'
			elif A.raw_buffer.startswith(codecs.BOM_UTF16_BE):A.raw_decode=codecs.utf_16_be_decode;A.encoding='utf-16-be'
			else:A.raw_decode=codecs.utf_8_decode;A.encoding='utf-8'
		A.update(1)
	NON_PRINTABLE=re.compile('[^\t\n\r -~\x85\xa0-\ud7ff\ue000-�𐀀-\U0010ffff]')
	def check_printable(A,data):
		B=A.NON_PRINTABLE.search(data)
		if B:C=B.group();D=A.index+(len(A.buffer)-A.pointer)+B.start();raise ReaderError(A.name,D,ord(C),'unicode','special characters are not allowed')
	def update(A,length):
		if A.raw_buffer is _A:return
		A.buffer=A.buffer[A.pointer:];A.pointer=0
		while len(A.buffer)<length:
			if not A.eof:A.update_raw()
			if A.raw_decode is not _A:
				try:C,D=A.raw_decode(A.raw_buffer,'strict',A.eof)
				except UnicodeDecodeError as B:
					F=A.raw_buffer[B.start]
					if A.stream is not _A:E=A.stream_pointer-len(A.raw_buffer)+B.start
					else:E=B.start
					raise ReaderError(A.name,E,F,B.encoding,B.reason)
			else:C=A.raw_buffer;D=len(C)
			A.check_printable(C);A.buffer+=C;A.raw_buffer=A.raw_buffer[D:]
			if A.eof:A.buffer+='\x00';A.raw_buffer=_A;break
	def update_raw(A,size=4096):
		B=A.stream.read(size)
		if A.raw_buffer is _A:A.raw_buffer=B
		else:A.raw_buffer+=B
		A.stream_pointer+=len(B)
		if not B:A.eof=True