_B=False
_A=None
__all__=['BaseDumper','SafeDumper','Dumper']
from.emitter import*
from.representer import*
from.resolver import*
from.serializer import*
class BaseDumper(Emitter,Serializer,BaseRepresenter,BaseResolver):
	def __init__(self,stream,default_style=_A,default_flow_style=_B,canonical=_A,indent=_A,width=_A,allow_unicode=_A,line_break=_A,encoding=_A,explicit_start=_A,explicit_end=_A,version=_A,tags=_A,sort_keys=True):Emitter.__init__(self,stream,canonical=canonical,indent=indent,width=width,allow_unicode=allow_unicode,line_break=line_break);Serializer.__init__(self,encoding=encoding,explicit_start=explicit_start,explicit_end=explicit_end,version=version,tags=tags);Representer.__init__(self,default_style=default_style,default_flow_style=default_flow_style,sort_keys=sort_keys);Resolver.__init__(self)
class SafeDumper(Emitter,Serializer,SafeRepresenter,Resolver):
	def __init__(self,stream,default_style=_A,default_flow_style=_B,canonical=_A,indent=_A,width=_A,allow_unicode=_A,line_break=_A,encoding=_A,explicit_start=_A,explicit_end=_A,version=_A,tags=_A,sort_keys=True):Emitter.__init__(self,stream,canonical=canonical,indent=indent,width=width,allow_unicode=allow_unicode,line_break=line_break);Serializer.__init__(self,encoding=encoding,explicit_start=explicit_start,explicit_end=explicit_end,version=version,tags=tags);SafeRepresenter.__init__(self,default_style=default_style,default_flow_style=default_flow_style,sort_keys=sort_keys);Resolver.__init__(self)
class Dumper(Emitter,Serializer,Representer,Resolver):
	def __init__(self,stream,default_style=_A,default_flow_style=_B,canonical=_A,indent=_A,width=_A,allow_unicode=_A,line_break=_A,encoding=_A,explicit_start=_A,explicit_end=_A,version=_A,tags=_A,sort_keys=True):Emitter.__init__(self,stream,canonical=canonical,indent=indent,width=width,allow_unicode=allow_unicode,line_break=line_break);Serializer.__init__(self,encoding=encoding,explicit_start=explicit_start,explicit_end=explicit_end,version=version,tags=tags);Representer.__init__(self,default_style=default_style,default_flow_style=default_flow_style,sort_keys=sort_keys);Resolver.__init__(self)