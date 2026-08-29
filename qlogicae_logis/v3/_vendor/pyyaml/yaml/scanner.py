_a='while scanning a quoted scalar'
_Z='0123456789ABCDEFabcdef'
_Y=' \r\n\x85\u2028\u2029'
_X='expected a comment or a line break, but found %r'
_W='directive'
_V="could not find expected ':'"
_U='while scanning a simple key'
_T="expected ' ', but found %r"
_S='while scanning a %s'
_R='while scanning a block scalar'
_Q=' \t'
_P='expected alphabetic or numeric character, but found %r'
_O='...'
_N='---'
_M='\r\n\x85\u2028\u2029'
_L='\n'
_K='\x00'
_J='\x00 \r\n\x85\u2028\u2029'
_I='0'
_H='\x00\r\n\x85\u2028\u2029'
_G='!'
_F='while scanning a directive'
_E='\x00 \t\r\n\x85\u2028\u2029'
_D=None
_C=' '
_B=False
_A=True
__all__=['Scanner','ScannerError']
from.error import MarkedYAMLError
from.tokens import*
class ScannerError(MarkedYAMLError):0
class SimpleKey:
	def __init__(self,token_number,required,index,line,column,mark):self.token_number=token_number;self.required=required;self.index=index;self.line=line;self.column=column;self.mark=mark
class Scanner:
	def __init__(self):self.done=_B;self.flow_level=0;self.tokens=[];self.fetch_stream_start();self.tokens_taken=0;self.indent=-1;self.indents=[];self.allow_simple_key=_A;self.possible_simple_keys={}
	def check_token(self,*choices):
		while self.need_more_tokens():self.fetch_more_tokens()
		if self.tokens:
			if not choices:return _A
			for choice in choices:
				if isinstance(self.tokens[0],choice):return _A
		return _B
	def peek_token(self):
		while self.need_more_tokens():self.fetch_more_tokens()
		if self.tokens:return self.tokens[0]
		else:return
	def get_token(self):
		while self.need_more_tokens():self.fetch_more_tokens()
		if self.tokens:self.tokens_taken+=1;return self.tokens.pop(0)
	def need_more_tokens(self):
		if self.done:return _B
		if not self.tokens:return _A
		self.stale_possible_simple_keys()
		if self.next_possible_simple_key()==self.tokens_taken:return _A
	def fetch_more_tokens(self):
		self.scan_to_next_token();self.stale_possible_simple_keys();self.unwind_indent(self.column);ch=self.peek()
		if ch==_K:return self.fetch_stream_end()
		if ch=='%'and self.check_directive():return self.fetch_directive()
		if ch=='-'and self.check_document_start():return self.fetch_document_start()
		if ch=='.'and self.check_document_end():return self.fetch_document_end()
		if ch=='[':return self.fetch_flow_sequence_start()
		if ch=='{':return self.fetch_flow_mapping_start()
		if ch==']':return self.fetch_flow_sequence_end()
		if ch=='}':return self.fetch_flow_mapping_end()
		if ch==',':return self.fetch_flow_entry()
		if ch=='-'and self.check_block_entry():return self.fetch_block_entry()
		if ch=='?'and self.check_key():return self.fetch_key()
		if ch==':'and self.check_value():return self.fetch_value()
		if ch=='*':return self.fetch_alias()
		if ch=='&':return self.fetch_anchor()
		if ch==_G:return self.fetch_tag()
		if ch=='|'and not self.flow_level:return self.fetch_literal()
		if ch=='>'and not self.flow_level:return self.fetch_folded()
		if ch=="'":return self.fetch_single()
		if ch=='"':return self.fetch_double()
		if self.check_plain():return self.fetch_plain()
		raise ScannerError('while scanning for the next token',_D,'found character %r that cannot start any token'%ch,self.get_mark())
	def next_possible_simple_key(self):
		min_token_number=_D
		for level in self.possible_simple_keys:
			key=self.possible_simple_keys[level]
			if min_token_number is _D or key.token_number<min_token_number:min_token_number=key.token_number
		return min_token_number
	def stale_possible_simple_keys(self):
		for level in list(self.possible_simple_keys):
			key=self.possible_simple_keys[level]
			if key.line!=self.line or self.index-key.index>1024:
				if key.required:raise ScannerError(_U,key.mark,_V,self.get_mark())
				del self.possible_simple_keys[level]
	def save_possible_simple_key(self):
		required=not self.flow_level and self.indent==self.column
		if self.allow_simple_key:self.remove_possible_simple_key();token_number=self.tokens_taken+len(self.tokens);key=SimpleKey(token_number,required,self.index,self.line,self.column,self.get_mark());self.possible_simple_keys[self.flow_level]=key
	def remove_possible_simple_key(self):
		if self.flow_level in self.possible_simple_keys:
			key=self.possible_simple_keys[self.flow_level]
			if key.required:raise ScannerError(_U,key.mark,_V,self.get_mark())
			del self.possible_simple_keys[self.flow_level]
	def unwind_indent(self,column):
		if self.flow_level:return
		while self.indent>column:mark=self.get_mark();self.indent=self.indents.pop();self.tokens.append(BlockEndToken(mark,mark))
	def add_indent(self,column):
		if self.indent<column:self.indents.append(self.indent);self.indent=column;return _A
		return _B
	def fetch_stream_start(self):mark=self.get_mark();self.tokens.append(StreamStartToken(mark,mark,encoding=self.encoding))
	def fetch_stream_end(self):self.unwind_indent(-1);self.remove_possible_simple_key();self.allow_simple_key=_B;self.possible_simple_keys={};mark=self.get_mark();self.tokens.append(StreamEndToken(mark,mark));self.done=_A
	def fetch_directive(self):self.unwind_indent(-1);self.remove_possible_simple_key();self.allow_simple_key=_B;self.tokens.append(self.scan_directive())
	def fetch_document_start(self):self.fetch_document_indicator(DocumentStartToken)
	def fetch_document_end(self):self.fetch_document_indicator(DocumentEndToken)
	def fetch_document_indicator(self,TokenClass):self.unwind_indent(-1);self.remove_possible_simple_key();self.allow_simple_key=_B;start_mark=self.get_mark();self.forward(3);end_mark=self.get_mark();self.tokens.append(TokenClass(start_mark,end_mark))
	def fetch_flow_sequence_start(self):self.fetch_flow_collection_start(FlowSequenceStartToken)
	def fetch_flow_mapping_start(self):self.fetch_flow_collection_start(FlowMappingStartToken)
	def fetch_flow_collection_start(self,TokenClass):self.save_possible_simple_key();self.flow_level+=1;self.allow_simple_key=_A;start_mark=self.get_mark();self.forward();end_mark=self.get_mark();self.tokens.append(TokenClass(start_mark,end_mark))
	def fetch_flow_sequence_end(self):self.fetch_flow_collection_end(FlowSequenceEndToken)
	def fetch_flow_mapping_end(self):self.fetch_flow_collection_end(FlowMappingEndToken)
	def fetch_flow_collection_end(self,TokenClass):self.remove_possible_simple_key();self.flow_level-=1;self.allow_simple_key=_B;start_mark=self.get_mark();self.forward();end_mark=self.get_mark();self.tokens.append(TokenClass(start_mark,end_mark))
	def fetch_flow_entry(self):self.allow_simple_key=_A;self.remove_possible_simple_key();start_mark=self.get_mark();self.forward();end_mark=self.get_mark();self.tokens.append(FlowEntryToken(start_mark,end_mark))
	def fetch_block_entry(self):
		if not self.flow_level:
			if not self.allow_simple_key:raise ScannerError(_D,_D,'sequence entries are not allowed here',self.get_mark())
			if self.add_indent(self.column):mark=self.get_mark();self.tokens.append(BlockSequenceStartToken(mark,mark))
		else:0
		self.allow_simple_key=_A;self.remove_possible_simple_key();start_mark=self.get_mark();self.forward();end_mark=self.get_mark();self.tokens.append(BlockEntryToken(start_mark,end_mark))
	def fetch_key(self):
		if not self.flow_level:
			if not self.allow_simple_key:raise ScannerError(_D,_D,'mapping keys are not allowed here',self.get_mark())
			if self.add_indent(self.column):mark=self.get_mark();self.tokens.append(BlockMappingStartToken(mark,mark))
		self.allow_simple_key=not self.flow_level;self.remove_possible_simple_key();start_mark=self.get_mark();self.forward();end_mark=self.get_mark();self.tokens.append(KeyToken(start_mark,end_mark))
	def fetch_value(self):
		if self.flow_level in self.possible_simple_keys:
			key=self.possible_simple_keys[self.flow_level];del self.possible_simple_keys[self.flow_level];self.tokens.insert(key.token_number-self.tokens_taken,KeyToken(key.mark,key.mark))
			if not self.flow_level:
				if self.add_indent(key.column):self.tokens.insert(key.token_number-self.tokens_taken,BlockMappingStartToken(key.mark,key.mark))
			self.allow_simple_key=_B
		else:
			if not self.flow_level:
				if not self.allow_simple_key:raise ScannerError(_D,_D,'mapping values are not allowed here',self.get_mark())
			if not self.flow_level:
				if self.add_indent(self.column):mark=self.get_mark();self.tokens.append(BlockMappingStartToken(mark,mark))
			self.allow_simple_key=not self.flow_level;self.remove_possible_simple_key()
		start_mark=self.get_mark();self.forward();end_mark=self.get_mark();self.tokens.append(ValueToken(start_mark,end_mark))
	def fetch_alias(self):self.save_possible_simple_key();self.allow_simple_key=_B;self.tokens.append(self.scan_anchor(AliasToken))
	def fetch_anchor(self):self.save_possible_simple_key();self.allow_simple_key=_B;self.tokens.append(self.scan_anchor(AnchorToken))
	def fetch_tag(self):self.save_possible_simple_key();self.allow_simple_key=_B;self.tokens.append(self.scan_tag())
	def fetch_literal(self):self.fetch_block_scalar(style='|')
	def fetch_folded(self):self.fetch_block_scalar(style='>')
	def fetch_block_scalar(self,style):self.allow_simple_key=_A;self.remove_possible_simple_key();self.tokens.append(self.scan_block_scalar(style))
	def fetch_single(self):self.fetch_flow_scalar(style="'")
	def fetch_double(self):self.fetch_flow_scalar(style='"')
	def fetch_flow_scalar(self,style):self.save_possible_simple_key();self.allow_simple_key=_B;self.tokens.append(self.scan_flow_scalar(style))
	def fetch_plain(self):self.save_possible_simple_key();self.allow_simple_key=_B;self.tokens.append(self.scan_plain())
	def check_directive(self):
		if self.column==0:return _A
	def check_document_start(self):
		if self.column==0:
			if self.prefix(3)==_N and self.peek(3)in _E:return _A
	def check_document_end(self):
		if self.column==0:
			if self.prefix(3)==_O and self.peek(3)in _E:return _A
	def check_block_entry(self):return self.peek(1)in _E
	def check_key(self):
		if self.flow_level:return _A
		else:return self.peek(1)in _E
	def check_value(self):
		if self.flow_level:return _A
		else:return self.peek(1)in _E
	def check_plain(self):ch=self.peek();return ch not in'\x00 \t\r\n\x85\u2028\u2029-?:,[]{}#&*!|>\'"%@`'or self.peek(1)not in _E and(ch=='-'or not self.flow_level and ch in'?:')
	def scan_to_next_token(self):
		if self.index==0 and self.peek()=='\ufeff':self.forward()
		found=_B
		while not found:
			while self.peek()==_C:self.forward()
			if self.peek()=='#':
				while self.peek()not in _H:self.forward()
			if self.scan_line_break():
				if not self.flow_level:self.allow_simple_key=_A
			else:found=_A
	def scan_directive(self):
		start_mark=self.get_mark();self.forward();name=self.scan_directive_name(start_mark);value=_D
		if name=='YAML':value=self.scan_yaml_directive_value(start_mark);end_mark=self.get_mark()
		elif name=='TAG':value=self.scan_tag_directive_value(start_mark);end_mark=self.get_mark()
		else:
			end_mark=self.get_mark()
			while self.peek()not in _H:self.forward()
		self.scan_directive_ignored_line(start_mark);return DirectiveToken(name,value,start_mark,end_mark)
	def scan_directive_name(self,start_mark):
		length=0;ch=self.peek(length)
		while _I<=ch<='9'or'A'<=ch<='Z'or'a'<=ch<='z'or ch in'-_':length+=1;ch=self.peek(length)
		if not length:raise ScannerError(_F,start_mark,_P%ch,self.get_mark())
		value=self.prefix(length);self.forward(length);ch=self.peek()
		if ch not in _J:raise ScannerError(_F,start_mark,_P%ch,self.get_mark())
		return value
	def scan_yaml_directive_value(self,start_mark):
		while self.peek()==_C:self.forward()
		major=self.scan_yaml_directive_number(start_mark)
		if self.peek()!='.':raise ScannerError(_F,start_mark,"expected a digit or '.', but found %r"%self.peek(),self.get_mark())
		self.forward();minor=self.scan_yaml_directive_number(start_mark)
		if self.peek()not in _J:raise ScannerError(_F,start_mark,"expected a digit or ' ', but found %r"%self.peek(),self.get_mark())
		return major,minor
	def scan_yaml_directive_number(self,start_mark):
		ch=self.peek()
		if not _I<=ch<='9':raise ScannerError(_F,start_mark,'expected a digit, but found %r'%ch,self.get_mark())
		length=0
		while _I<=self.peek(length)<='9':length+=1
		value=int(self.prefix(length));self.forward(length);return value
	def scan_tag_directive_value(self,start_mark):
		while self.peek()==_C:self.forward()
		handle=self.scan_tag_directive_handle(start_mark)
		while self.peek()==_C:self.forward()
		prefix=self.scan_tag_directive_prefix(start_mark);return handle,prefix
	def scan_tag_directive_handle(self,start_mark):
		value=self.scan_tag_handle(_W,start_mark);ch=self.peek()
		if ch!=_C:raise ScannerError(_F,start_mark,_T%ch,self.get_mark())
		return value
	def scan_tag_directive_prefix(self,start_mark):
		value=self.scan_tag_uri(_W,start_mark);ch=self.peek()
		if ch not in _J:raise ScannerError(_F,start_mark,_T%ch,self.get_mark())
		return value
	def scan_directive_ignored_line(self,start_mark):
		while self.peek()==_C:self.forward()
		if self.peek()=='#':
			while self.peek()not in _H:self.forward()
		ch=self.peek()
		if ch not in _H:raise ScannerError(_F,start_mark,_X%ch,self.get_mark())
		self.scan_line_break()
	def scan_anchor(self,TokenClass):
		A='while scanning an %s';start_mark=self.get_mark();indicator=self.peek()
		if indicator=='*':name='alias'
		else:name='anchor'
		self.forward();length=0;ch=self.peek(length)
		while _I<=ch<='9'or'A'<=ch<='Z'or'a'<=ch<='z'or ch in'-_':length+=1;ch=self.peek(length)
		if not length:raise ScannerError(A%name,start_mark,_P%ch,self.get_mark())
		value=self.prefix(length);self.forward(length);ch=self.peek()
		if ch not in'\x00 \t\r\n\x85\u2028\u2029?:,]}%@`':raise ScannerError(A%name,start_mark,_P%ch,self.get_mark())
		end_mark=self.get_mark();return TokenClass(value,start_mark,end_mark)
	def scan_tag(self):
		A='tag';start_mark=self.get_mark();ch=self.peek(1)
		if ch=='<':
			handle=_D;self.forward(2);suffix=self.scan_tag_uri(A,start_mark)
			if self.peek()!='>':raise ScannerError('while parsing a tag',start_mark,"expected '>', but found %r"%self.peek(),self.get_mark())
			self.forward()
		elif ch in _E:handle=_D;suffix=_G;self.forward()
		else:
			length=1;use_handle=_B
			while ch not in _J:
				if ch==_G:use_handle=_A;break
				length+=1;ch=self.peek(length)
			handle=_G
			if use_handle:handle=self.scan_tag_handle(A,start_mark)
			else:handle=_G;self.forward()
			suffix=self.scan_tag_uri(A,start_mark)
		ch=self.peek()
		if ch not in _J:raise ScannerError('while scanning a tag',start_mark,_T%ch,self.get_mark())
		value=handle,suffix;end_mark=self.get_mark();return TagToken(value,start_mark,end_mark)
	def scan_block_scalar(self,style):
		if style=='>':folded=_A
		else:folded=_B
		chunks=[];start_mark=self.get_mark();self.forward();chomping,increment=self.scan_block_scalar_indicators(start_mark);self.scan_block_scalar_ignored_line(start_mark);min_indent=self.indent+1
		if min_indent<1:min_indent=1
		if increment is _D:breaks,max_indent,end_mark=self.scan_block_scalar_indentation();indent=max(min_indent,max_indent)
		else:indent=min_indent+increment-1;breaks,end_mark=self.scan_block_scalar_breaks(indent)
		line_break=''
		while self.column==indent and self.peek()!=_K:
			chunks.extend(breaks);leading_non_space=self.peek()not in _Q;length=0
			while self.peek(length)not in _H:length+=1
			chunks.append(self.prefix(length));self.forward(length);line_break=self.scan_line_break();breaks,end_mark=self.scan_block_scalar_breaks(indent)
			if self.column==indent and self.peek()!=_K:
				if folded and line_break==_L and leading_non_space and self.peek()not in _Q:
					if not breaks:chunks.append(_C)
				else:chunks.append(line_break)
			else:break
		if chomping is not _B:chunks.append(line_break)
		if chomping is _A:chunks.extend(breaks)
		return ScalarToken(''.join(chunks),_B,start_mark,end_mark,style)
	def scan_block_scalar_indicators(self,start_mark):
		B='expected indentation indicator in the range 1-9, but found 0';A='0123456789';chomping=_D;increment=_D;ch=self.peek()
		if ch in'+-':
			if ch=='+':chomping=_A
			else:chomping=_B
			self.forward();ch=self.peek()
			if ch in A:
				increment=int(ch)
				if increment==0:raise ScannerError(_R,start_mark,B,self.get_mark())
				self.forward()
		elif ch in A:
			increment=int(ch)
			if increment==0:raise ScannerError(_R,start_mark,B,self.get_mark())
			self.forward();ch=self.peek()
			if ch in'+-':
				if ch=='+':chomping=_A
				else:chomping=_B
				self.forward()
		ch=self.peek()
		if ch not in _J:raise ScannerError(_R,start_mark,'expected chomping or indentation indicators, but found %r'%ch,self.get_mark())
		return chomping,increment
	def scan_block_scalar_ignored_line(self,start_mark):
		while self.peek()==_C:self.forward()
		if self.peek()=='#':
			while self.peek()not in _H:self.forward()
		ch=self.peek()
		if ch not in _H:raise ScannerError(_R,start_mark,_X%ch,self.get_mark())
		self.scan_line_break()
	def scan_block_scalar_indentation(self):
		chunks=[];max_indent=0;end_mark=self.get_mark()
		while self.peek()in _Y:
			if self.peek()!=_C:chunks.append(self.scan_line_break());end_mark=self.get_mark()
			else:
				self.forward()
				if self.column>max_indent:max_indent=self.column
		return chunks,max_indent,end_mark
	def scan_block_scalar_breaks(self,indent):
		chunks=[];end_mark=self.get_mark()
		while self.column<indent and self.peek()==_C:self.forward()
		while self.peek()in _M:
			chunks.append(self.scan_line_break());end_mark=self.get_mark()
			while self.column<indent and self.peek()==_C:self.forward()
		return chunks,end_mark
	def scan_flow_scalar(self,style):
		if style=='"':double=_A
		else:double=_B
		chunks=[];start_mark=self.get_mark();quote=self.peek();self.forward();chunks.extend(self.scan_flow_scalar_non_spaces(double,start_mark))
		while self.peek()!=quote:chunks.extend(self.scan_flow_scalar_spaces(double,start_mark));chunks.extend(self.scan_flow_scalar_non_spaces(double,start_mark))
		self.forward();end_mark=self.get_mark();return ScalarToken(''.join(chunks),_B,start_mark,end_mark,style)
	ESCAPE_REPLACEMENTS={_I:_K,'a':'\x07','b':'\x08','t':'\t','\t':'\t','n':_L,'v':'\x0b','f':'\x0c','r':'\r','e':'\x1b',_C:_C,'"':'"','\\':'\\','/':'/','N':'\x85','_':'\xa0','L':'\u2028','P':'\u2029'};ESCAPE_CODES={'x':2,'u':4,'U':8}
	def scan_flow_scalar_non_spaces(self,double,start_mark):
		A='while scanning a double-quoted scalar';chunks=[]
		while _A:
			length=0
			while self.peek(length)not in'\'"\\\x00 \t\r\n\x85\u2028\u2029':length+=1
			if length:chunks.append(self.prefix(length));self.forward(length)
			ch=self.peek()
			if not double and ch=="'"and self.peek(1)=="'":chunks.append("'");self.forward(2)
			elif double and ch=="'"or not double and ch in'"\\':chunks.append(ch);self.forward()
			elif double and ch=='\\':
				self.forward();ch=self.peek()
				if ch in self.ESCAPE_REPLACEMENTS:chunks.append(self.ESCAPE_REPLACEMENTS[ch]);self.forward()
				elif ch in self.ESCAPE_CODES:
					length=self.ESCAPE_CODES[ch];self.forward()
					for k in range(length):
						if self.peek(k)not in _Z:raise ScannerError(A,start_mark,'expected escape sequence of %d hexadecimal numbers, but found %r'%(length,self.peek(k)),self.get_mark())
					code=int(self.prefix(length),16);chunks.append(chr(code));self.forward(length)
				elif ch in _M:self.scan_line_break();chunks.extend(self.scan_flow_scalar_breaks(double,start_mark))
				else:raise ScannerError(A,start_mark,'found unknown escape character %r'%ch,self.get_mark())
			else:return chunks
	def scan_flow_scalar_spaces(self,double,start_mark):
		chunks=[];length=0
		while self.peek(length)in _Q:length+=1
		whitespaces=self.prefix(length);self.forward(length);ch=self.peek()
		if ch==_K:raise ScannerError(_a,start_mark,'found unexpected end of stream',self.get_mark())
		elif ch in _M:
			line_break=self.scan_line_break();breaks=self.scan_flow_scalar_breaks(double,start_mark)
			if line_break!=_L:chunks.append(line_break)
			elif not breaks:chunks.append(_C)
			chunks.extend(breaks)
		else:chunks.append(whitespaces)
		return chunks
	def scan_flow_scalar_breaks(self,double,start_mark):
		chunks=[]
		while _A:
			prefix=self.prefix(3)
			if(prefix==_N or prefix==_O)and self.peek(3)in _E:raise ScannerError(_a,start_mark,'found unexpected document separator',self.get_mark())
			while self.peek()in _Q:self.forward()
			if self.peek()in _M:chunks.append(self.scan_line_break())
			else:return chunks
	def scan_plain(self):
		chunks=[];start_mark=self.get_mark();end_mark=start_mark;indent=self.indent+1;spaces=[]
		while _A:
			length=0
			if self.peek()=='#':break
			while _A:
				ch=self.peek(length)
				if ch in _E or ch==':'and self.peek(length+1)in _E+(',[]{}'if self.flow_level else'')or self.flow_level and ch in',?[]{}':break
				length+=1
			if length==0:break
			self.allow_simple_key=_B;chunks.extend(spaces);chunks.append(self.prefix(length));self.forward(length);end_mark=self.get_mark();spaces=self.scan_plain_spaces(indent,start_mark)
			if not spaces or self.peek()=='#'or not self.flow_level and self.column<indent:break
		return ScalarToken(''.join(chunks),_A,start_mark,end_mark)
	def scan_plain_spaces(self,indent,start_mark):
		chunks=[];length=0
		while self.peek(length)in _C:length+=1
		whitespaces=self.prefix(length);self.forward(length);ch=self.peek()
		if ch in _M:
			line_break=self.scan_line_break();self.allow_simple_key=_A;prefix=self.prefix(3)
			if(prefix==_N or prefix==_O)and self.peek(3)in _E:return
			breaks=[]
			while self.peek()in _Y:
				if self.peek()==_C:self.forward()
				else:
					breaks.append(self.scan_line_break());prefix=self.prefix(3)
					if(prefix==_N or prefix==_O)and self.peek(3)in _E:return
			if line_break!=_L:chunks.append(line_break)
			elif not breaks:chunks.append(_C)
			chunks.extend(breaks)
		elif whitespaces:chunks.append(whitespaces)
		return chunks
	def scan_tag_handle(self,name,start_mark):
		A="expected '!', but found %r";ch=self.peek()
		if ch!=_G:raise ScannerError(_S%name,start_mark,A%ch,self.get_mark())
		length=1;ch=self.peek(length)
		if ch!=_C:
			while _I<=ch<='9'or'A'<=ch<='Z'or'a'<=ch<='z'or ch in'-_':length+=1;ch=self.peek(length)
			if ch!=_G:self.forward(length);raise ScannerError(_S%name,start_mark,A%ch,self.get_mark())
			length+=1
		value=self.prefix(length);self.forward(length);return value
	def scan_tag_uri(self,name,start_mark):
		chunks=[];length=0;ch=self.peek(length)
		while _I<=ch<='9'or'A'<=ch<='Z'or'a'<=ch<='z'or ch in"-;/?:@&=+$,_.!~*'()[]%":
			if ch=='%':chunks.append(self.prefix(length));self.forward(length);length=0;chunks.append(self.scan_uri_escapes(name,start_mark))
			else:length+=1
			ch=self.peek(length)
		if length:chunks.append(self.prefix(length));self.forward(length);length=0
		if not chunks:raise ScannerError('while parsing a %s'%name,start_mark,'expected URI, but found %r'%ch,self.get_mark())
		return''.join(chunks)
	def scan_uri_escapes(self,name,start_mark):
		codes=[];mark=self.get_mark()
		while self.peek()=='%':
			self.forward()
			for k in range(2):
				if self.peek(k)not in _Z:raise ScannerError(_S%name,start_mark,'expected URI escape sequence of 2 hexadecimal numbers, but found %r'%self.peek(k),self.get_mark())
			codes.append(int(self.prefix(2),16));self.forward(2)
		try:value=bytes(codes).decode('utf-8')
		except UnicodeDecodeError as exc:raise ScannerError(_S%name,start_mark,str(exc),mark)
		return value
	def scan_line_break(self):
		ch=self.peek()
		if ch in'\r\n\x85':
			if self.prefix(2)=='\r\n':self.forward(2)
			else:self.forward()
			return _L
		elif ch in'\u2028\u2029':self.forward();return ch
		return''