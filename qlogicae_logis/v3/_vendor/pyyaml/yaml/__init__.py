_A=None
from.dumper import*
from.error import*
from.events import*
from.loader import*
from.nodes import*
from.tokens import*
__version__='6.0.3'
try:from.cyaml import*;__with_libyaml__=True
except ImportError:__with_libyaml__=False
import io
def warnings(settings=_A):
	if settings is _A:return{}
def scan(stream,Loader=Loader):
	loader=Loader(stream)
	try:
		while loader.check_token():yield loader.get_token()
	finally:loader.dispose()
def parse(stream,Loader=Loader):
	loader=Loader(stream)
	try:
		while loader.check_event():yield loader.get_event()
	finally:loader.dispose()
def compose(stream,Loader=Loader):
	loader=Loader(stream)
	try:return loader.get_single_node()
	finally:loader.dispose()
def compose_all(stream,Loader=Loader):
	loader=Loader(stream)
	try:
		while loader.check_node():yield loader.get_node()
	finally:loader.dispose()
def load(stream,Loader):
	loader=Loader(stream)
	try:return loader.get_single_data()
	finally:loader.dispose()
def load_all(stream,Loader):
	loader=Loader(stream)
	try:
		while loader.check_data():yield loader.get_data()
	finally:loader.dispose()
def full_load(stream):return load(stream,FullLoader)
def full_load_all(stream):return load_all(stream,FullLoader)
def safe_load(stream):return load(stream,SafeLoader)
def safe_load_all(stream):return load_all(stream,SafeLoader)
def unsafe_load(stream):return load(stream,UnsafeLoader)
def unsafe_load_all(stream):return load_all(stream,UnsafeLoader)
def emit(events,stream=_A,Dumper=Dumper,canonical=_A,indent=_A,width=_A,allow_unicode=_A,line_break=_A):
	getvalue=_A
	if stream is _A:stream=io.StringIO();getvalue=stream.getvalue
	dumper=Dumper(stream,canonical=canonical,indent=indent,width=width,allow_unicode=allow_unicode,line_break=line_break)
	try:
		for event in events:dumper.emit(event)
	finally:dumper.dispose()
	if getvalue:return getvalue()
def serialize_all(nodes,stream=_A,Dumper=Dumper,canonical=_A,indent=_A,width=_A,allow_unicode=_A,line_break=_A,encoding=_A,explicit_start=_A,explicit_end=_A,version=_A,tags=_A):
	getvalue=_A
	if stream is _A:
		if encoding is _A:stream=io.StringIO()
		else:stream=io.BytesIO()
		getvalue=stream.getvalue
	dumper=Dumper(stream,canonical=canonical,indent=indent,width=width,allow_unicode=allow_unicode,line_break=line_break,encoding=encoding,version=version,tags=tags,explicit_start=explicit_start,explicit_end=explicit_end)
	try:
		dumper.open()
		for node in nodes:dumper.serialize(node)
		dumper.close()
	finally:dumper.dispose()
	if getvalue:return getvalue()
def serialize(node,stream=_A,Dumper=Dumper,**kwds):return serialize_all([node],stream,Dumper=Dumper,**kwds)
def dump_all(documents,stream=_A,Dumper=Dumper,default_style=_A,default_flow_style=False,canonical=_A,indent=_A,width=_A,allow_unicode=_A,line_break=_A,encoding=_A,explicit_start=_A,explicit_end=_A,version=_A,tags=_A,sort_keys=True):
	getvalue=_A
	if stream is _A:
		if encoding is _A:stream=io.StringIO()
		else:stream=io.BytesIO()
		getvalue=stream.getvalue
	dumper=Dumper(stream,default_style=default_style,default_flow_style=default_flow_style,canonical=canonical,indent=indent,width=width,allow_unicode=allow_unicode,line_break=line_break,encoding=encoding,version=version,tags=tags,explicit_start=explicit_start,explicit_end=explicit_end,sort_keys=sort_keys)
	try:
		dumper.open()
		for data in documents:dumper.represent(data)
		dumper.close()
	finally:dumper.dispose()
	if getvalue:return getvalue()
def dump(data,stream=_A,Dumper=Dumper,**kwds):return dump_all([data],stream,Dumper=Dumper,**kwds)
def safe_dump_all(documents,stream=_A,**kwds):return dump_all(documents,stream,Dumper=SafeDumper,**kwds)
def safe_dump(data,stream=_A,**kwds):return dump_all([data],stream,Dumper=SafeDumper,**kwds)
def add_implicit_resolver(tag,regexp,first=_A,Loader=_A,Dumper=Dumper):
	if Loader is _A:loader.Loader.add_implicit_resolver(tag,regexp,first);loader.FullLoader.add_implicit_resolver(tag,regexp,first);loader.UnsafeLoader.add_implicit_resolver(tag,regexp,first)
	else:Loader.add_implicit_resolver(tag,regexp,first)
	Dumper.add_implicit_resolver(tag,regexp,first)
def add_path_resolver(tag,path,kind=_A,Loader=_A,Dumper=Dumper):
	if Loader is _A:loader.Loader.add_path_resolver(tag,path,kind);loader.FullLoader.add_path_resolver(tag,path,kind);loader.UnsafeLoader.add_path_resolver(tag,path,kind)
	else:Loader.add_path_resolver(tag,path,kind)
	Dumper.add_path_resolver(tag,path,kind)
def add_constructor(tag,constructor,Loader=_A):
	if Loader is _A:loader.Loader.add_constructor(tag,constructor);loader.FullLoader.add_constructor(tag,constructor);loader.UnsafeLoader.add_constructor(tag,constructor)
	else:Loader.add_constructor(tag,constructor)
def add_multi_constructor(tag_prefix,multi_constructor,Loader=_A):
	if Loader is _A:loader.Loader.add_multi_constructor(tag_prefix,multi_constructor);loader.FullLoader.add_multi_constructor(tag_prefix,multi_constructor);loader.UnsafeLoader.add_multi_constructor(tag_prefix,multi_constructor)
	else:Loader.add_multi_constructor(tag_prefix,multi_constructor)
def add_representer(data_type,representer,Dumper=Dumper):Dumper.add_representer(data_type,representer)
def add_multi_representer(data_type,multi_representer,Dumper=Dumper):Dumper.add_multi_representer(data_type,multi_representer)
class YAMLObjectMetaclass(type):
	def __init__(cls,name,bases,kwds):
		A='yaml_tag';super().__init__(name,bases,kwds)
		if A in kwds and kwds[A]is not _A:
			if isinstance(cls.yaml_loader,list):
				for loader in cls.yaml_loader:loader.add_constructor(cls.yaml_tag,cls.from_yaml)
			else:cls.yaml_loader.add_constructor(cls.yaml_tag,cls.from_yaml)
			cls.yaml_dumper.add_representer(cls,cls.to_yaml)
class YAMLObject(metaclass=YAMLObjectMetaclass):
	__slots__=();yaml_loader=[Loader,FullLoader,UnsafeLoader];yaml_dumper=Dumper;yaml_tag=_A;yaml_flow_style=_A
	@classmethod
	def from_yaml(cls,loader,node):return loader.construct_yaml_object(node,cls)
	@classmethod
	def to_yaml(cls,dumper,data):return dumper.represent_yaml_object(cls.yaml_tag,data,cls,flow_style=cls.yaml_flow_style)