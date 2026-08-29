_Q='\ufeff'
_P='\ue000'
_O='\ud7ff'
_N='%%%02X'
_M='\xa0'
_L=' \n\x85\u2028\u2029'
_K='...'
_J='\\'
_I="'"
_H='"'
_G='!'
_F='\n'
_E='\n\x85\u2028\u2029'
_D=' '
_C=None
_B=False
_A=True
__all__=['Emitter','EmitterError']
from.error import YAMLError
from.events import*
class EmitterError(YAMLError):0
class ScalarAnalysis:
	def __init__(self,scalar,empty,multiline,allow_flow_plain,allow_block_plain,allow_single_quoted,allow_double_quoted,allow_block):self.scalar=scalar;self.empty=empty;self.multiline=multiline;self.allow_flow_plain=allow_flow_plain;self.allow_block_plain=allow_block_plain;self.allow_single_quoted=allow_single_quoted;self.allow_double_quoted=allow_double_quoted;self.allow_block=allow_block
class Emitter:
	DEFAULT_TAG_PREFIXES={_G:_G,'tag:yaml.org,2002:':'!!'}
	def __init__(self,stream,canonical=_C,indent=_C,width=_C,allow_unicode=_C,line_break=_C):
		self.stream=stream;self.encoding=_C;self.states=[];self.state=self.expect_stream_start;self.events=[];self.event=_C;self.indents=[];self.indent=_C;self.flow_level=0;self.root_context=_B;self.sequence_context=_B;self.mapping_context=_B;self.simple_key_context=_B;self.line=0;self.column=0;self.whitespace=_A;self.indention=_A;self.open_ended=_B;self.canonical=canonical;self.allow_unicode=allow_unicode;self.best_indent=2
		if indent and 1<indent<10:self.best_indent=indent
		self.best_width=80
		if width and width>self.best_indent*2:self.best_width=width
		self.best_line_break=_F
		if line_break in['\r',_F,'\r\n']:self.best_line_break=line_break
		self.tag_prefixes=_C;self.prepared_anchor=_C;self.prepared_tag=_C;self.analysis=_C;self.style=_C
	def dispose(self):self.states=[];self.state=_C
	def emit(self,event):
		self.events.append(event)
		while not self.need_more_events():self.event=self.events.pop(0);self.state();self.event=_C
	def need_more_events(self):
		if not self.events:return _A
		event=self.events[0]
		if isinstance(event,DocumentStartEvent):return self.need_events(1)
		elif isinstance(event,SequenceStartEvent):return self.need_events(2)
		elif isinstance(event,MappingStartEvent):return self.need_events(3)
		else:return _B
	def need_events(self,count):
		level=0
		for event in self.events[1:]:
			if isinstance(event,(DocumentStartEvent,CollectionStartEvent)):level+=1
			elif isinstance(event,(DocumentEndEvent,CollectionEndEvent)):level-=1
			elif isinstance(event,StreamEndEvent):level=-1
			if level<0:return _B
		return len(self.events)<count+1
	def increase_indent(self,flow=_B,indentless=_B):
		self.indents.append(self.indent)
		if self.indent is _C:
			if flow:self.indent=self.best_indent
			else:self.indent=0
		elif not indentless:self.indent+=self.best_indent
	def expect_stream_start(self):
		if isinstance(self.event,StreamStartEvent):
			if self.event.encoding and not hasattr(self.stream,'encoding'):self.encoding=self.event.encoding
			self.write_stream_start();self.state=self.expect_first_document_start
		else:raise EmitterError('expected StreamStartEvent, but got %s'%self.event)
	def expect_nothing(self):raise EmitterError('expected nothing, but got %s'%self.event)
	def expect_first_document_start(self):return self.expect_document_start(first=_A)
	def expect_document_start(self,first=_B):
		if isinstance(self.event,DocumentStartEvent):
			if(self.event.version or self.event.tags)and self.open_ended:self.write_indicator(_K,_A);self.write_indent()
			if self.event.version:version_text=self.prepare_version(self.event.version);self.write_version_directive(version_text)
			self.tag_prefixes=self.DEFAULT_TAG_PREFIXES.copy()
			if self.event.tags:
				handles=sorted(self.event.tags.keys())
				for handle in handles:prefix=self.event.tags[handle];self.tag_prefixes[prefix]=handle;handle_text=self.prepare_tag_handle(handle);prefix_text=self.prepare_tag_prefix(prefix);self.write_tag_directive(handle_text,prefix_text)
			implicit=first and not self.event.explicit and not self.canonical and not self.event.version and not self.event.tags and not self.check_empty_document()
			if not implicit:
				self.write_indent();self.write_indicator('---',_A)
				if self.canonical:self.write_indent()
			self.state=self.expect_document_root
		elif isinstance(self.event,StreamEndEvent):
			if self.open_ended:self.write_indicator(_K,_A);self.write_indent()
			self.write_stream_end();self.state=self.expect_nothing
		else:raise EmitterError('expected DocumentStartEvent, but got %s'%self.event)
	def expect_document_end(self):
		if isinstance(self.event,DocumentEndEvent):
			self.write_indent()
			if self.event.explicit:self.write_indicator(_K,_A);self.write_indent()
			self.flush_stream();self.state=self.expect_document_start
		else:raise EmitterError('expected DocumentEndEvent, but got %s'%self.event)
	def expect_document_root(self):self.states.append(self.expect_document_end);self.expect_node(root=_A)
	def expect_node(self,root=_B,sequence=_B,mapping=_B,simple_key=_B):
		self.root_context=root;self.sequence_context=sequence;self.mapping_context=mapping;self.simple_key_context=simple_key
		if isinstance(self.event,AliasEvent):self.expect_alias()
		elif isinstance(self.event,(ScalarEvent,CollectionStartEvent)):
			self.process_anchor('&');self.process_tag()
			if isinstance(self.event,ScalarEvent):self.expect_scalar()
			elif isinstance(self.event,SequenceStartEvent):
				if self.flow_level or self.canonical or self.event.flow_style or self.check_empty_sequence():self.expect_flow_sequence()
				else:self.expect_block_sequence()
			elif isinstance(self.event,MappingStartEvent):
				if self.flow_level or self.canonical or self.event.flow_style or self.check_empty_mapping():self.expect_flow_mapping()
				else:self.expect_block_mapping()
		else:raise EmitterError('expected NodeEvent, but got %s'%self.event)
	def expect_alias(self):
		if self.event.anchor is _C:raise EmitterError('anchor is not specified for alias')
		self.process_anchor('*');self.state=self.states.pop()
	def expect_scalar(self):self.increase_indent(flow=_A);self.process_scalar();self.indent=self.indents.pop();self.state=self.states.pop()
	def expect_flow_sequence(self):self.write_indicator('[',_A,whitespace=_A);self.flow_level+=1;self.increase_indent(flow=_A);self.state=self.expect_first_flow_sequence_item
	def expect_first_flow_sequence_item(self):
		if isinstance(self.event,SequenceEndEvent):self.indent=self.indents.pop();self.flow_level-=1;self.write_indicator(']',_B);self.state=self.states.pop()
		else:
			if self.canonical or self.column>self.best_width:self.write_indent()
			self.states.append(self.expect_flow_sequence_item);self.expect_node(sequence=_A)
	def expect_flow_sequence_item(self):
		if isinstance(self.event,SequenceEndEvent):
			self.indent=self.indents.pop();self.flow_level-=1
			if self.canonical:self.write_indicator(',',_B);self.write_indent()
			self.write_indicator(']',_B);self.state=self.states.pop()
		else:
			self.write_indicator(',',_B)
			if self.canonical or self.column>self.best_width:self.write_indent()
			self.states.append(self.expect_flow_sequence_item);self.expect_node(sequence=_A)
	def expect_flow_mapping(self):self.write_indicator('{',_A,whitespace=_A);self.flow_level+=1;self.increase_indent(flow=_A);self.state=self.expect_first_flow_mapping_key
	def expect_first_flow_mapping_key(self):
		if isinstance(self.event,MappingEndEvent):self.indent=self.indents.pop();self.flow_level-=1;self.write_indicator('}',_B);self.state=self.states.pop()
		else:
			if self.canonical or self.column>self.best_width:self.write_indent()
			if not self.canonical and self.check_simple_key():self.states.append(self.expect_flow_mapping_simple_value);self.expect_node(mapping=_A,simple_key=_A)
			else:self.write_indicator('?',_A);self.states.append(self.expect_flow_mapping_value);self.expect_node(mapping=_A)
	def expect_flow_mapping_key(self):
		if isinstance(self.event,MappingEndEvent):
			self.indent=self.indents.pop();self.flow_level-=1
			if self.canonical:self.write_indicator(',',_B);self.write_indent()
			self.write_indicator('}',_B);self.state=self.states.pop()
		else:
			self.write_indicator(',',_B)
			if self.canonical or self.column>self.best_width:self.write_indent()
			if not self.canonical and self.check_simple_key():self.states.append(self.expect_flow_mapping_simple_value);self.expect_node(mapping=_A,simple_key=_A)
			else:self.write_indicator('?',_A);self.states.append(self.expect_flow_mapping_value);self.expect_node(mapping=_A)
	def expect_flow_mapping_simple_value(self):self.write_indicator(':',_B);self.states.append(self.expect_flow_mapping_key);self.expect_node(mapping=_A)
	def expect_flow_mapping_value(self):
		if self.canonical or self.column>self.best_width:self.write_indent()
		self.write_indicator(':',_A);self.states.append(self.expect_flow_mapping_key);self.expect_node(mapping=_A)
	def expect_block_sequence(self):indentless=self.mapping_context and not self.indention;self.increase_indent(flow=_B,indentless=indentless);self.state=self.expect_first_block_sequence_item
	def expect_first_block_sequence_item(self):return self.expect_block_sequence_item(first=_A)
	def expect_block_sequence_item(self,first=_B):
		if not first and isinstance(self.event,SequenceEndEvent):self.indent=self.indents.pop();self.state=self.states.pop()
		else:self.write_indent();self.write_indicator('-',_A,indention=_A);self.states.append(self.expect_block_sequence_item);self.expect_node(sequence=_A)
	def expect_block_mapping(self):self.increase_indent(flow=_B);self.state=self.expect_first_block_mapping_key
	def expect_first_block_mapping_key(self):return self.expect_block_mapping_key(first=_A)
	def expect_block_mapping_key(self,first=_B):
		if not first and isinstance(self.event,MappingEndEvent):self.indent=self.indents.pop();self.state=self.states.pop()
		else:
			self.write_indent()
			if self.check_simple_key():self.states.append(self.expect_block_mapping_simple_value);self.expect_node(mapping=_A,simple_key=_A)
			else:self.write_indicator('?',_A,indention=_A);self.states.append(self.expect_block_mapping_value);self.expect_node(mapping=_A)
	def expect_block_mapping_simple_value(self):self.write_indicator(':',_B);self.states.append(self.expect_block_mapping_key);self.expect_node(mapping=_A)
	def expect_block_mapping_value(self):self.write_indent();self.write_indicator(':',_A,indention=_A);self.states.append(self.expect_block_mapping_key);self.expect_node(mapping=_A)
	def check_empty_sequence(self):return isinstance(self.event,SequenceStartEvent)and self.events and isinstance(self.events[0],SequenceEndEvent)
	def check_empty_mapping(self):return isinstance(self.event,MappingStartEvent)and self.events and isinstance(self.events[0],MappingEndEvent)
	def check_empty_document(self):
		if not isinstance(self.event,DocumentStartEvent)or not self.events:return _B
		event=self.events[0];return isinstance(event,ScalarEvent)and event.anchor is _C and event.tag is _C and event.implicit and event.value==''
	def check_simple_key(self):
		length=0
		if isinstance(self.event,NodeEvent)and self.event.anchor is not _C:
			if self.prepared_anchor is _C:self.prepared_anchor=self.prepare_anchor(self.event.anchor)
			length+=len(self.prepared_anchor)
		if isinstance(self.event,(ScalarEvent,CollectionStartEvent))and self.event.tag is not _C:
			if self.prepared_tag is _C:self.prepared_tag=self.prepare_tag(self.event.tag)
			length+=len(self.prepared_tag)
		if isinstance(self.event,ScalarEvent):
			if self.analysis is _C:self.analysis=self.analyze_scalar(self.event.value)
			length+=len(self.analysis.scalar)
		return length<128 and(isinstance(self.event,AliasEvent)or isinstance(self.event,ScalarEvent)and not self.analysis.empty and not self.analysis.multiline or self.check_empty_sequence()or self.check_empty_mapping())
	def process_anchor(self,indicator):
		if self.event.anchor is _C:self.prepared_anchor=_C;return
		if self.prepared_anchor is _C:self.prepared_anchor=self.prepare_anchor(self.event.anchor)
		if self.prepared_anchor:self.write_indicator(indicator+self.prepared_anchor,_A)
		self.prepared_anchor=_C
	def process_tag(self):
		tag=self.event.tag
		if isinstance(self.event,ScalarEvent):
			if self.style is _C:self.style=self.choose_scalar_style()
			if(not self.canonical or tag is _C)and(self.style==''and self.event.implicit[0]or self.style!=''and self.event.implicit[1]):self.prepared_tag=_C;return
			if self.event.implicit[0]and tag is _C:tag=_G;self.prepared_tag=_C
		elif(not self.canonical or tag is _C)and self.event.implicit:self.prepared_tag=_C;return
		if tag is _C:raise EmitterError('tag is not specified')
		if self.prepared_tag is _C:self.prepared_tag=self.prepare_tag(tag)
		if self.prepared_tag:self.write_indicator(self.prepared_tag,_A)
		self.prepared_tag=_C
	def choose_scalar_style(self):
		if self.analysis is _C:self.analysis=self.analyze_scalar(self.event.value)
		if self.event.style==_H or self.canonical:return _H
		if not self.event.style and self.event.implicit[0]:
			if not(self.simple_key_context and(self.analysis.empty or self.analysis.multiline))and(self.flow_level and self.analysis.allow_flow_plain or not self.flow_level and self.analysis.allow_block_plain):return''
		if self.event.style and self.event.style in'|>':
			if not self.flow_level and not self.simple_key_context and self.analysis.allow_block:return self.event.style
		if not self.event.style or self.event.style==_I:
			if self.analysis.allow_single_quoted and not(self.simple_key_context and self.analysis.multiline):return _I
		return _H
	def process_scalar(self):
		if self.analysis is _C:self.analysis=self.analyze_scalar(self.event.value)
		if self.style is _C:self.style=self.choose_scalar_style()
		split=not self.simple_key_context
		if self.style==_H:self.write_double_quoted(self.analysis.scalar,split)
		elif self.style==_I:self.write_single_quoted(self.analysis.scalar,split)
		elif self.style=='>':self.write_folded(self.analysis.scalar)
		elif self.style=='|':self.write_literal(self.analysis.scalar)
		else:self.write_plain(self.analysis.scalar,split)
		self.analysis=_C;self.style=_C
	def prepare_version(self,version):
		major,minor=version
		if major!=1:raise EmitterError('unsupported YAML version: %d.%d'%(major,minor))
		return'%d.%d'%(major,minor)
	def prepare_tag_handle(self,handle):
		if not handle:raise EmitterError('tag handle must not be empty')
		if handle[0]!=_G or handle[-1]!=_G:raise EmitterError("tag handle must start and end with '!': %r"%handle)
		for ch in handle[1:-1]:
			if not('0'<=ch<='9'or'A'<=ch<='Z'or'a'<=ch<='z'or ch in'-_'):raise EmitterError('invalid character %r in the tag handle: %r'%(ch,handle))
		return handle
	def prepare_tag_prefix(self,prefix):
		if not prefix:raise EmitterError('tag prefix must not be empty')
		chunks=[];start=end=0
		if prefix[0]==_G:end=1
		while end<len(prefix):
			ch=prefix[end]
			if'0'<=ch<='9'or'A'<=ch<='Z'or'a'<=ch<='z'or ch in"-;/?!:@&=+$,_.~*'()[]":end+=1
			else:
				if start<end:chunks.append(prefix[start:end])
				start=end=end+1;data=ch.encode('utf-8')
				for ch in data:chunks.append(_N%ord(ch))
		if start<end:chunks.append(prefix[start:end])
		return''.join(chunks)
	def prepare_tag(self,tag):
		if not tag:raise EmitterError('tag must not be empty')
		if tag==_G:return tag
		handle=_C;suffix=tag;prefixes=sorted(self.tag_prefixes.keys())
		for prefix in prefixes:
			if tag.startswith(prefix)and(prefix==_G or len(prefix)<len(tag)):handle=self.tag_prefixes[prefix];suffix=tag[len(prefix):]
		chunks=[];start=end=0
		while end<len(suffix):
			ch=suffix[end]
			if'0'<=ch<='9'or'A'<=ch<='Z'or'a'<=ch<='z'or ch in"-;/?:@&=+$,_.~*'()[]"or ch==_G and handle!=_G:end+=1
			else:
				if start<end:chunks.append(suffix[start:end])
				start=end=end+1;data=ch.encode('utf-8')
				for ch in data:chunks.append(_N%ch)
		if start<end:chunks.append(suffix[start:end])
		suffix_text=''.join(chunks)
		if handle:return'%s%s'%(handle,suffix_text)
		else:return'!<%s>'%suffix_text
	def prepare_anchor(self,anchor):
		if not anchor:raise EmitterError('anchor must not be empty')
		for ch in anchor:
			if not('0'<=ch<='9'or'A'<=ch<='Z'or'a'<=ch<='z'or ch in'-_'):raise EmitterError('invalid character %r in the anchor: %r'%(ch,anchor))
		return anchor
	def analyze_scalar(self,scalar):
		A='\x00 \t\r\n\x85\u2028\u2029'
		if not scalar:return ScalarAnalysis(scalar=scalar,empty=_A,multiline=_B,allow_flow_plain=_B,allow_block_plain=_A,allow_single_quoted=_A,allow_double_quoted=_A,allow_block=_B)
		block_indicators=_B;flow_indicators=_B;line_breaks=_B;special_characters=_B;leading_space=_B;leading_break=_B;trailing_space=_B;trailing_break=_B;break_space=_B;space_break=_B
		if scalar.startswith('---')or scalar.startswith(_K):block_indicators=_A;flow_indicators=_A
		preceded_by_whitespace=_A;followed_by_whitespace=len(scalar)==1 or scalar[1]in A;previous_space=_B;previous_break=_B;index=0
		while index<len(scalar):
			ch=scalar[index]
			if index==0:
				if ch in'#,[]{}&*!|>\'"%@`':flow_indicators=_A;block_indicators=_A
				if ch in'?:':
					flow_indicators=_A
					if followed_by_whitespace:block_indicators=_A
				if ch=='-'and followed_by_whitespace:flow_indicators=_A;block_indicators=_A
			else:
				if ch in',?[]{}':flow_indicators=_A
				if ch==':':
					flow_indicators=_A
					if followed_by_whitespace:block_indicators=_A
				if ch=='#'and preceded_by_whitespace:flow_indicators=_A;block_indicators=_A
			if ch in _E:line_breaks=_A
			if not(ch==_F or _D<=ch<='~'):
				if(ch=='\x85'or _M<=ch<=_O or _P<=ch<='�'or'𐀀'<=ch<'\U0010ffff')and ch!=_Q:
					unicode_characters=_A
					if not self.allow_unicode:special_characters=_A
				else:special_characters=_A
			if ch==_D:
				if index==0:leading_space=_A
				if index==len(scalar)-1:trailing_space=_A
				if previous_break:break_space=_A
				previous_space=_A;previous_break=_B
			elif ch in _E:
				if index==0:leading_break=_A
				if index==len(scalar)-1:trailing_break=_A
				if previous_space:space_break=_A
				previous_space=_B;previous_break=_A
			else:previous_space=_B;previous_break=_B
			index+=1;preceded_by_whitespace=ch in A;followed_by_whitespace=index+1>=len(scalar)or scalar[index+1]in A
		allow_flow_plain=_A;allow_block_plain=_A;allow_single_quoted=_A;allow_double_quoted=_A;allow_block=_A
		if leading_space or leading_break or trailing_space or trailing_break:allow_flow_plain=allow_block_plain=_B
		if trailing_space:allow_block=_B
		if break_space:allow_flow_plain=allow_block_plain=allow_single_quoted=_B
		if space_break or special_characters:allow_flow_plain=allow_block_plain=allow_single_quoted=allow_block=_B
		if line_breaks:allow_flow_plain=allow_block_plain=_B
		if flow_indicators:allow_flow_plain=_B
		if block_indicators:allow_block_plain=_B
		return ScalarAnalysis(scalar=scalar,empty=_B,multiline=line_breaks,allow_flow_plain=allow_flow_plain,allow_block_plain=allow_block_plain,allow_single_quoted=allow_single_quoted,allow_double_quoted=allow_double_quoted,allow_block=allow_block)
	def flush_stream(self):
		if hasattr(self.stream,'flush'):self.stream.flush()
	def write_stream_start(self):
		if self.encoding and self.encoding.startswith('utf-16'):self.stream.write(_Q.encode(self.encoding))
	def write_stream_end(self):self.flush_stream()
	def write_indicator(self,indicator,need_whitespace,whitespace=_B,indention=_B):
		if self.whitespace or not need_whitespace:data=indicator
		else:data=_D+indicator
		self.whitespace=whitespace;self.indention=self.indention and indention;self.column+=len(data);self.open_ended=_B
		if self.encoding:data=data.encode(self.encoding)
		self.stream.write(data)
	def write_indent(self):
		indent=self.indent or 0
		if not self.indention or self.column>indent or self.column==indent and not self.whitespace:self.write_line_break()
		if self.column<indent:
			self.whitespace=_A;data=_D*(indent-self.column);self.column=indent
			if self.encoding:data=data.encode(self.encoding)
			self.stream.write(data)
	def write_line_break(self,data=_C):
		if data is _C:data=self.best_line_break
		self.whitespace=_A;self.indention=_A;self.line+=1;self.column=0
		if self.encoding:data=data.encode(self.encoding)
		self.stream.write(data)
	def write_version_directive(self,version_text):
		data='%%YAML %s'%version_text
		if self.encoding:data=data.encode(self.encoding)
		self.stream.write(data);self.write_line_break()
	def write_tag_directive(self,handle_text,prefix_text):
		data='%%TAG %s %s'%(handle_text,prefix_text)
		if self.encoding:data=data.encode(self.encoding)
		self.stream.write(data);self.write_line_break()
	def write_single_quoted(self,text,split=_A):
		self.write_indicator(_I,_A);spaces=_B;breaks=_B;start=end=0
		while end<=len(text):
			ch=_C
			if end<len(text):ch=text[end]
			if spaces:
				if ch is _C or ch!=_D:
					if start+1==end and self.column>self.best_width and split and start!=0 and end!=len(text):self.write_indent()
					else:
						data=text[start:end];self.column+=len(data)
						if self.encoding:data=data.encode(self.encoding)
						self.stream.write(data)
					start=end
			elif breaks:
				if ch is _C or ch not in _E:
					if text[start]==_F:self.write_line_break()
					for br in text[start:end]:
						if br==_F:self.write_line_break()
						else:self.write_line_break(br)
					self.write_indent();start=end
			elif ch is _C or ch in _L or ch==_I:
				if start<end:
					data=text[start:end];self.column+=len(data)
					if self.encoding:data=data.encode(self.encoding)
					self.stream.write(data);start=end
			if ch==_I:
				data="''";self.column+=2
				if self.encoding:data=data.encode(self.encoding)
				self.stream.write(data);start=end+1
			if ch is not _C:spaces=ch==_D;breaks=ch in _E
			end+=1
		self.write_indicator(_I,_B)
	ESCAPE_REPLACEMENTS={'\x00':'0','\x07':'a','\x08':'b','\t':'t',_F:'n','\x0b':'v','\x0c':'f','\r':'r','\x1b':'e',_H:_H,_J:_J,'\x85':'N',_M:'_','\u2028':'L','\u2029':'P'}
	def write_double_quoted(self,text,split=_A):
		self.write_indicator(_H,_A);start=end=0
		while end<=len(text):
			ch=_C
			if end<len(text):ch=text[end]
			if ch is _C or ch in'"\\\x85\u2028\u2029\ufeff'or not(_D<=ch<='~'or self.allow_unicode and(_M<=ch<=_O or _P<=ch<='�')):
				if start<end:
					data=text[start:end];self.column+=len(data)
					if self.encoding:data=data.encode(self.encoding)
					self.stream.write(data);start=end
				if ch is not _C:
					if ch in self.ESCAPE_REPLACEMENTS:data=_J+self.ESCAPE_REPLACEMENTS[ch]
					elif ch<='ÿ':data='\\x%02X'%ord(ch)
					elif ch<='\uffff':data='\\u%04X'%ord(ch)
					else:data='\\U%08X'%ord(ch)
					self.column+=len(data)
					if self.encoding:data=data.encode(self.encoding)
					self.stream.write(data);start=end+1
			if 0<end<len(text)-1 and(ch==_D or start>=end)and self.column+(end-start)>self.best_width and split:
				data=text[start:end]+_J
				if start<end:start=end
				self.column+=len(data)
				if self.encoding:data=data.encode(self.encoding)
				self.stream.write(data);self.write_indent();self.whitespace=_B;self.indention=_B
				if text[start]==_D:
					data=_J;self.column+=len(data)
					if self.encoding:data=data.encode(self.encoding)
					self.stream.write(data)
			end+=1
		self.write_indicator(_H,_B)
	def determine_block_hints(self,text):
		hints=''
		if text:
			if text[0]in _L:hints+=str(self.best_indent)
			if text[-1]not in _E:hints+='-'
			elif len(text)==1 or text[-2]in _E:hints+='+'
		return hints
	def write_folded(self,text):
		hints=self.determine_block_hints(text);self.write_indicator('>'+hints,_A)
		if hints[-1:]=='+':self.open_ended=_A
		self.write_line_break();leading_space=_A;spaces=_B;breaks=_A;start=end=0
		while end<=len(text):
			ch=_C
			if end<len(text):ch=text[end]
			if breaks:
				if ch is _C or ch not in _E:
					if not leading_space and ch is not _C and ch!=_D and text[start]==_F:self.write_line_break()
					leading_space=ch==_D
					for br in text[start:end]:
						if br==_F:self.write_line_break()
						else:self.write_line_break(br)
					if ch is not _C:self.write_indent()
					start=end
			elif spaces:
				if ch!=_D:
					if start+1==end and self.column>self.best_width:self.write_indent()
					else:
						data=text[start:end];self.column+=len(data)
						if self.encoding:data=data.encode(self.encoding)
						self.stream.write(data)
					start=end
			elif ch is _C or ch in _L:
				data=text[start:end];self.column+=len(data)
				if self.encoding:data=data.encode(self.encoding)
				self.stream.write(data)
				if ch is _C:self.write_line_break()
				start=end
			if ch is not _C:breaks=ch in _E;spaces=ch==_D
			end+=1
	def write_literal(self,text):
		hints=self.determine_block_hints(text);self.write_indicator('|'+hints,_A)
		if hints[-1:]=='+':self.open_ended=_A
		self.write_line_break();breaks=_A;start=end=0
		while end<=len(text):
			ch=_C
			if end<len(text):ch=text[end]
			if breaks:
				if ch is _C or ch not in _E:
					for br in text[start:end]:
						if br==_F:self.write_line_break()
						else:self.write_line_break(br)
					if ch is not _C:self.write_indent()
					start=end
			elif ch is _C or ch in _E:
				data=text[start:end]
				if self.encoding:data=data.encode(self.encoding)
				self.stream.write(data)
				if ch is _C:self.write_line_break()
				start=end
			if ch is not _C:breaks=ch in _E
			end+=1
	def write_plain(self,text,split=_A):
		if self.root_context:self.open_ended=_A
		if not text:return
		if not self.whitespace:
			data=_D;self.column+=len(data)
			if self.encoding:data=data.encode(self.encoding)
			self.stream.write(data)
		self.whitespace=_B;self.indention=_B;spaces=_B;breaks=_B;start=end=0
		while end<=len(text):
			ch=_C
			if end<len(text):ch=text[end]
			if spaces:
				if ch!=_D:
					if start+1==end and self.column>self.best_width and split:self.write_indent();self.whitespace=_B;self.indention=_B
					else:
						data=text[start:end];self.column+=len(data)
						if self.encoding:data=data.encode(self.encoding)
						self.stream.write(data)
					start=end
			elif breaks:
				if ch not in _E:
					if text[start]==_F:self.write_line_break()
					for br in text[start:end]:
						if br==_F:self.write_line_break()
						else:self.write_line_break(br)
					self.write_indent();self.whitespace=_B;self.indention=_B;start=end
			elif ch is _C or ch in _L:
				data=text[start:end];self.column+=len(data)
				if self.encoding:data=data.encode(self.encoding)
				self.stream.write(data);start=end
			if ch is not _C:spaces=ch==_D;breaks=ch in _E
			end+=1