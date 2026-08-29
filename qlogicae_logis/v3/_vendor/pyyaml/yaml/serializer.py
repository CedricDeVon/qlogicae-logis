_E='serializer is not opened'
_D='serializer is closed'
_C=False
_B=True
_A=None
__all__=['Serializer','SerializerError']
from.error import YAMLError
from.events import*
from.nodes import*
class SerializerError(YAMLError):0
class Serializer:
	ANCHOR_TEMPLATE='id%03d'
	def __init__(self,encoding=_A,explicit_start=_A,explicit_end=_A,version=_A,tags=_A):self.use_encoding=encoding;self.use_explicit_start=explicit_start;self.use_explicit_end=explicit_end;self.use_version=version;self.use_tags=tags;self.serialized_nodes={};self.anchors={};self.last_anchor_id=0;self.closed=_A
	def open(self):
		if self.closed is _A:self.emit(StreamStartEvent(encoding=self.use_encoding));self.closed=_C
		elif self.closed:raise SerializerError(_D)
		else:raise SerializerError('serializer is already opened')
	def close(self):
		if self.closed is _A:raise SerializerError(_E)
		elif not self.closed:self.emit(StreamEndEvent());self.closed=_B
	def serialize(self,node):
		if self.closed is _A:raise SerializerError(_E)
		elif self.closed:raise SerializerError(_D)
		self.emit(DocumentStartEvent(explicit=self.use_explicit_start,version=self.use_version,tags=self.use_tags));self.anchor_node(node);self.serialize_node(node,_A,_A);self.emit(DocumentEndEvent(explicit=self.use_explicit_end));self.serialized_nodes={};self.anchors={};self.last_anchor_id=0
	def anchor_node(self,node):
		if node in self.anchors:
			if self.anchors[node]is _A:self.anchors[node]=self.generate_anchor(node)
		else:
			self.anchors[node]=_A
			if isinstance(node,SequenceNode):
				for item in node.value:self.anchor_node(item)
			elif isinstance(node,MappingNode):
				for(key,value)in node.value:self.anchor_node(key);self.anchor_node(value)
	def generate_anchor(self,node):self.last_anchor_id+=1;return self.ANCHOR_TEMPLATE%self.last_anchor_id
	def serialize_node(self,node,parent,index):
		alias=self.anchors[node]
		if node in self.serialized_nodes:self.emit(AliasEvent(alias))
		else:
			self.serialized_nodes[node]=_B;self.descend_resolver(parent,index)
			if isinstance(node,ScalarNode):detected_tag=self.resolve(ScalarNode,node.value,(_B,_C));default_tag=self.resolve(ScalarNode,node.value,(_C,_B));implicit=node.tag==detected_tag,node.tag==default_tag;self.emit(ScalarEvent(alias,node.tag,implicit,node.value,style=node.style))
			elif isinstance(node,SequenceNode):
				implicit=node.tag==self.resolve(SequenceNode,node.value,_B);self.emit(SequenceStartEvent(alias,node.tag,implicit,flow_style=node.flow_style));index=0
				for item in node.value:self.serialize_node(item,node,index);index+=1
				self.emit(SequenceEndEvent())
			elif isinstance(node,MappingNode):
				implicit=node.tag==self.resolve(MappingNode,node.value,_B);self.emit(MappingStartEvent(alias,node.tag,implicit,flow_style=node.flow_style))
				for(key,value)in node.value:self.serialize_node(key,node,_A);self.serialize_node(value,node,key)
				self.emit(MappingEndEvent())
			self.ascend_resolver()