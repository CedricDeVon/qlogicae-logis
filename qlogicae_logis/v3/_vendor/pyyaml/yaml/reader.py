H='\x00'
F=bytes
E=isinstance
C=len
B=None
__all__=['Reader','ReaderError']
import codecs as D,re
from.error import Mark as G,YAMLError as A
class ReaderError(A):
	def __init__(A,name,position,character,encoding,reason):A.name=name;A.character=character;A.position=position;A.encoding=encoding;A.reason=reason
	def __str__(A):
		if E(A.character,F):return'\'%s\' codec can\'t decode byte #x%02x: %s\n  in "%s", position %d'%(A.encoding,ord(A.character),A.reason,A.name,A.position)
		else:return'unacceptable character #x%04x: %s\n  in "%s", position %d'%(A.character,A.reason,A.name,A.position)
class Reader:
	def __init__(A,stream):
		C=stream;A.name=B;A.stream=B;A.stream_pointer=0;A.eof=True;A.buffer='';A.pointer=0;A.raw_buffer=B;A.raw_decode=B;A.encoding=B;A.index=0;A.line=0;A.column=0
		if E(C,str):A.name='<unicode string>';A.check_printable(C);A.buffer=C+H
		elif E(C,F):A.name='<byte string>';A.raw_buffer=C;A.determine_encoding()
		else:A.stream=C;A.name=getattr(C,'name','<file>');A.eof=False;A.raw_buffer=B;A.determine_encoding()
	def peek(A,index=0):
		B=index
		try:return A.buffer[A.pointer+B]
		except IndexError:A.update(B+1);return A.buffer[A.pointer+B]
	def prefix(A,length=1):
		B=length
		if A.pointer+B>=C(A.buffer):A.update(B)
		return A.buffer[A.pointer:A.pointer+B]
	def forward(A,length=1):
		B=length
		if A.pointer+B+1>=C(A.buffer):A.update(B+1)
		while B:
			D=A.buffer[A.pointer];A.pointer+=1;A.index+=1
			if D in'\n\x85\u2028\u2029'or D=='\r'and A.buffer[A.pointer]!='\n':A.line+=1;A.column=0
			elif D!='\ufeff':A.column+=1
			B-=1
	def get_mark(A):
		if A.stream is B:return G(A.name,A.index,A.line,A.column,A.buffer,A.pointer)
		else:return G(A.name,A.index,A.line,A.column,B,B)
	def determine_encoding(A):
		while not A.eof and(A.raw_buffer is B or C(A.raw_buffer)<2):A.update_raw()
		if E(A.raw_buffer,F):
			if A.raw_buffer.startswith(D.BOM_UTF16_LE):A.raw_decode=D.utf_16_le_decode;A.encoding='utf-16-le'
			elif A.raw_buffer.startswith(D.BOM_UTF16_BE):A.raw_decode=D.utf_16_be_decode;A.encoding='utf-16-be'
			else:A.raw_decode=D.utf_8_decode;A.encoding='utf-8'
		A.update(1)
	NON_PRINTABLE=re.compile('[^\t\n\r -~\x85\xa0-\ud7ff\ue000-�𐀀-\U0010ffff]')
	def check_printable(A,data):
		B=A.NON_PRINTABLE.search(data)
		if B:D=B.group();E=A.index+(C(A.buffer)-A.pointer)+B.start();raise ReaderError(A.name,E,ord(D),'unicode','special characters are not allowed')
	def update(A,length):
		if A.raw_buffer is B:return
		A.buffer=A.buffer[A.pointer:];A.pointer=0
		while C(A.buffer)<length:
			if not A.eof:A.update_raw()
			if A.raw_decode is not B:
				try:E,F=A.raw_decode(A.raw_buffer,'strict',A.eof)
				except UnicodeDecodeError as D:
					I=A.raw_buffer[D.start]
					if A.stream is not B:G=A.stream_pointer-C(A.raw_buffer)+D.start
					else:G=D.start
					raise ReaderError(A.name,G,I,D.encoding,D.reason)
			else:E=A.raw_buffer;F=C(E)
			A.check_printable(E);A.buffer+=E;A.raw_buffer=A.raw_buffer[F:]
			if A.eof:A.buffer+=H;A.raw_buffer=B;break
	def update_raw(A,size=4096):
		D=A.stream.read(size)
		if A.raw_buffer is B:A.raw_buffer=D
		else:A.raw_buffer+=D
		A.stream_pointer+=C(D)
		if not D:A.eof=True