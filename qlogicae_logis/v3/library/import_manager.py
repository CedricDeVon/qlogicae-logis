from __future__ import annotations
AD='is_verbose'
AC='is_enabled'
AB='encoding'
AA='key_paths'
A9=isinstance
A8='source_path'
A7='target_paths'
A6='indent'
A5='allow_unicode'
A4='default_flow_style'
A3='sort_keys'
A2='command'
A1='utf-8'
A0='values'
Z='filesystem_path'
Y=len
R='target_path'
Q='file_path'
P=ValueError
L='message'
H='key_path'
G=tuple
F='value'
D=None
C=''
B=True
A=False
from typing import Any
__all__='ImportManager'
a=D
S=D
b=D
M=D
K=D
E=D
I=D
N=D
c=D
d=D
T=D
U=D
V=D
e=D
f=D
W=D
g=D
h=D
X=D
i=D
j=D
k=D
O=D
l=D
J=D
m=D
n=D
o=D
p=D
q=D
r=D
s=D
t=D
u=D
AE=D
v=D
w=D
x=D
def y():global y;global a;global S;global b;global M;global K;global E;global I;global N;global c;global d;global T;global U;global V;global e;global W;global f;global g;global h;global X;global i;global k;global j;global O;global l;global J;global m;global n;global o;global p;global q;global r;global s;global t;global u;global AE;global v;global w;global x;import gc,logging as A,resource as B,shutil as C,sys,time,tracemalloc as F,uuid;from importlib import metadata as G;from importlib.util import module_from_spec as H,spec_from_file_location as L;from pathlib import Path;from zipfile import ZipFile as P;from.._vendor.pyyaml import yaml;from.._vendor.qlogicae_cor.v2.library import console_log_manager as Q,disk_cache_storage_manager as R,file_entity_filesystem_tree_setup_options as Y,file_io_manager as Z,file_log_manager as z,filesystem_compression_manager as A0,folder_entity_filesystem_tree_setup_options as A1,group_selection_manager as A2,log_manager as A3,log_options as A4,macros_manager as A5,object_merge_manager as A6,script_process as A7,script_process_manager as A8,singleton_manager as A9,system_manager as AA,target_cache_value as AB,text_encoding_manager as AC,time_manager as AD,time_zone_manager as AF,timestamp as AG,timestamp_manager as AH,value_cache_manager as AI;a=gc;S=sys;M=uuid;K=yaml;E=Path;b=time;I=C;c=P;N=A;d=G;T=B;W=F;U=AG.Timestamp;V=A4.LogOptions;e=A3.LogManager;k=H;f=AD.TimeManager;g=A5.MacrosManager;h=AA.SystemManager;t=L;j=AF.TimeZoneManager;o=z.FileLogManager;O=A9.SingletonManager;l=AH.TimestampManager;J=AB.TargetCacheValue;n=AI.ValueCacheManager;p=A6.ObjectMergeManager;r=A8.ScriptProcessManager;v=A0.FilesystemCompressionManager;w=Y.FileEntityFileSystemTreeSetupOptions;x=A1.FolderEntityFileSystemTreeSetupOptions;m=Q.ConsoleLogManager;u=R.DiskCacheStorageManager;X=A7.ScriptProcess;i=Z.FileIoManager;s=A2.GroupSelectionManager;q=AC.TextEncodingManager;y=lambda:D
def z():global z;global O;from.._vendor.qlogicae_cor.v2.library import singleton_manager as A;O=A.SingletonManager;z=lambda:D
class AF:
	__slots__='_time_manager','_disk_cache_storage_manager','_value_cache_manager','_time_zone_manager','_timestamp_manager','_text_encoding_manager','_script_process_manager','_macros_manager','_object_merge_manager','_group_selection_manager','_filesystem_compression_manager','_system_manager','_file_io_manager','_file_log_manager','_console_log_manager','_log_manager'
	def __init__(A):y();A._time_manager=A.read_singleton(f);A._disk_cache_storage_manager=A.read_singleton(u);A._value_cache_manager=A.read_singleton(n);A._time_zone_manager=A.read_singleton(j);A._timestamp_manager=A.read_singleton(l);A._text_encoding_manager=A.read_singleton(q);A._script_process_manager=A.read_singleton(r);A._macros_manager=A.read_singleton(g);A._object_merge_manager=A.read_singleton(p);A._group_selection_manager=A.read_singleton(s);A._filesystem_compression_manager=A.read_singleton(v);A._system_manager=A.read_singleton(h);A._file_io_manager=A.read_singleton(i);A._file_log_manager=A.read_singleton(o);A._console_log_manager=A.read_singleton(m);A._log_manager=A.read_singleton(e)
	@classmethod
	def read_singleton(B,value):
		A=value
		if not A:return{}
		z();return O.get_singleton(A)
	def convert_to_os_specific_path_value(D,**A):B=A.get(Z,C);return f"{E(B)}"
	def compress(K,**D):
		if not D:return A
		F=D.get('source',C);H=D.get('destination',C);I=D.get('mode',C)
		if not H or not I:return A
		F=E(F);G=D.get('compression','deflated');G=K.read_zip_format_compression(value=G);L=D.get('compresslevel',6);M=D.get('allowZip64',B);N=D.get('strict_timestamps',B)
		with c(H,mode=I,compression=G,compresslevel=L,allowZip64=M,strict_timestamps=N)as O:
			for J in F.rglob('*'):O.write(J,arcname=J.relative_to(F))
		return B
	def read_metadata_version(C,target):
		B='v0.0.0';A=target
		if not A:return B
		return d.version(A)or B
	def snapshot_memory_usage(D):
		B,C=W.get_traced_memory()if W.is_tracing()else(0,0);A=T.getrusage(T.RUSAGE_SELF).ru_maxrss
		if S.platform!='darwin':A*=1024
		return{'tracemalloc-current':{F:B},'tracemalloc-peak':{F:C},'process-peak-rss':{F:A},'gc-tracked-objects':{F:Y(a.get_objects())}}
	def time_delay(E,**C):
		if not C:return A
		D=C.get(F,0)
		if not D:return A
		b.sleep(D);return B
	def read_current_iso8601_date(A):B=A._time_manager.current_iso8601_date;return B
	def read_current_nanosecond(A):B=A._time_manager.current_nanosecond;return B
	def read_current_day(A):B=A._time_manager.current_day;return B
	def read_current_month(A):B=A._time_manager.current_month;return B
	def read_current_year(A):B=A._time_manager.current_year;return B
	def is_key_found_via_disk_cache(D,**B):
		if not B:return A
		E=D._disk_cache_storage_manager.is_keys_found(key_path=B.get(H,C));return E
	def is_item_expired_via_disk_cache(D,**B):
		if not B:return A
		E=D._disk_cache_storage_manager.is_item_expired(key_path=B.get(H,C));return E
	def read_all_values_via_disk_cache(A):B=A._disk_cache_storage_manager.read_all_values();return B
	def read_many_values_via_disk_cache(B,**A):
		if not A:return{}
		C=B._disk_cache_storage_manager.get_many_values(key_paths=A.get(AA,G()));return C
	def write_many_values_via_disk_cache(D,**C):
		if not C:return A
		D._disk_cache_storage_manager.set_many_values(values=C.get(A0,{}));return B
	def remove_many_values_via_disk_cache(B,**A):
		if not A:return{}
		C=B._disk_cache_storage_manager.remove_many_values(key_paths=A.get(AA,G()));return C
	def open_via_disk_cache(A):A._disk_cache_storage_manager.open();return B
	def close_via_disk_cache(A):A._disk_cache_storage_manager.close();return B
	def clear_all_values_via_disk_cache(A):A._disk_cache_storage_manager.clear_all_values();return B
	def remove_expired_values_via_disk_cache(A):B=A._disk_cache_storage_manager.remove_expired_values();return B
	def sync_via_disk_cache(A):A._disk_cache_storage_manager.sync();return B
	def reorganize_via_disk_cache(A):A._disk_cache_storage_manager.reorganize();return B
	def display_all_items_via_disk_cache(A):A._disk_cache_storage_manager.display_all_items();return B
	def write_database_path_via_disk_cache(D,value):
		C=value
		if not C:return A
		D._disk_cache_storage_manager.database_path=C;return B
	def read_any_value_via_value_cache(B,**A):
		if not A:return{}
		C=B._value_cache_manager.get_one_value(key_path=A.get(H,G()),output_type=J.ANY);return C
	def read_defined_value_via_value_cache(B,**A):
		if not A:return{}
		C=B._value_cache_manager.get_one_value(key_path=A.get(H,G()),output_type=J.DEFINED);return C
	def write_any_value_via_value_cache(D,**C):
		if not C:return A
		D._value_cache_manager.set_one_value(key_path=C.get(H,G()),value=C.get(F,{}),output_type=J.ANY);return B
	def write_defined_value_via_value_cache(D,**C):
		if not C:return A
		D._value_cache_manager.set_one_value(key_path=C.get(H,G()),value=C.get(F,{}),output_type=J.DEFINED);return B
	def write_file_path_value_via_value_cache(D,**C):
		if not C:return A
		D._value_cache_manager.set_one_value(key_path=C.get(H,G()),value=C.get(F,{}),output_type=J.FILE_PATH);return B
	def write_folder_path_value_via_value_cache(D,**C):
		if not C:return A
		D._value_cache_manager.set_one_value(key_path=C.get(H,G()),value=C.get(F,{}),output_type=J.FOLDER_PATH);return B
	def write_filesystem_path_value_via_value_cache(D,**C):
		if not C:return A
		D._value_cache_manager.set_one_value(key_path=C.get(H,G()),value=C.get(F,{}),output_type=J.FILESYSTEM_PATH);return B
	def display_all_items_via_value_cache(A):A._value_cache_manager.display_all_items();return B
	def remove_one_value_via_value_cache(D,**C):
		if not C:return A
		D._value_cache_manager.remove_one_value(key_path=C.get(H,G()));return B
	def clear_all_values_via_value_cache(A):A._value_cache_manager.clear_all_values();return B
	def read_selected_time_zone(A):B=A._time_zone_manager.selected_time_zone_type;return B
	def write_selected_time_zone(D,**C):
		if not C:return A
		D._time_zone_manager.selected_time_zone_type=C.get(F,'local'),;return B
	def generate_current_date_timestamp(A):B=A._timestamp_manager.generate_current_timestamp(U.ISO_DATE_STRING);return B
	def generate_current_filesystem_timestamp(A):B=A._timestamp_manager.generate_current_timestamp(U.ISO_FILESYSTEM_STRING);return B
	def read_selected_encoding(A):B=A._text_encoding_manager.selected_encoding;return B
	def write_selected_encoding(D,**C):
		if not C:return A
		D._text_encoding_manager.selected_encoding=C.get(F,A1),;return B
	def run_shell_command(D,**B):
		if not B:return A
		E=D._script_process_manager.execute_command(command=B.get(A2,C),script_process_type=X.SHELL);return E
	def run_subprocess_command(D,**B):
		if not B:return A
		E=D._script_process_manager.execute_command(command=B.get(A2,C),script_process_type=X.SUBPROCESS);return E
	def run_command(E,**A):
		G='shell'
		if not A:return{}
		F=A.get('script_process',G);B=A.get(A2,C)
		if not B:return{}
		D={}
		if F==G:D=E.run_shell_command(command=B)
		elif F=='subprocess':D=E.run_subprocess_command(command=B)
		return D
	def macros_resolve_many(C,**B):
		if not B:return A
		D=C._macros_manager.resolve_many(B.get(A0,{}));return D
	def macros_parse_many(D,**B):
		if not B:return A
		E=D._macros_manager.parse_many(values=B.get(A0,C),resolved=B.get('resolved',{}));return E
	def macros_parse_filesystem(D,**B):
		if not B:return A
		E=D._macros_manager.parse_filesystem(filesystem_path=B.get(Z,C),workspace_macros=B.get('workspace_macros',{}));return E
	def object_deep_merge(C,**B):
		if not B:return A
		D=C._object_merge_manager.deep_merge(left=B.get('left',{}),right=B.get('right',{}));return D
	def object_deep_merge_fragments(C,**B):
		if not B:return A
		D=C._object_merge_manager.deep_merge_fragments(left=B.get('left',{}),right=B.get('right',{}));return D
	def object_flatten_group(D,**B):
		if not B:return A
		return D._group_selection_manager.flatten_group(B.get('target',C),B.get('data',{}))or{}
	def convert_yaml_string_to_object(B,**A):
		if not A:return{}
		return K.safe_load(A.get(F,C))or{}
	def convert_yaml_object_to_string(E,**D):
		if not D:return C
		return K.safe_dump(D.get(F,C),sort_keys=D.get(A3,A),default_flow_style=D.get(A4,A),allow_unicode=D.get(A5,B),indent=D.get(A6,4))or C
	def format_yaml_to_string(E,**D):
		if not D:return A
		return K.dump(D.get(F,C),sort_keys=D.get(A3,A),default_flow_style=D.get(A4,A),allow_unicode=D.get(A5,B),indent=D.get(A6,4))
	def read_yaml_file(G,**B):
		if not B:return A
		D=E(B.get(Q,C))
		with D.open(mode='r',encoding=B.get(AB,A1))as F:return K.safe_load(F)or{}
	def write_yaml_file(I,**D):
		if not D:return A
		G=E(D.get(Q,C))
		with G.open(mode='w',encoding=D.get(AB,A1))as H:K.safe_dump(D.get(F,C),H,sort_keys=D.get(A3,A),default_flow_style=D.get(A4,A),allow_unicode=D.get(A5,B),indent=D.get(A6,4))
		return B
	def read_python_file(I,**B):
		if not B:return A
		D=E(B.get(Q,C));H=D.stem;F=t(H,D);G=k(F);F.loader.exec_module(G);return G or{}
	def read_child_folder_paths(D,**B):
		if not B:return A
		return E(B.get(F,C)).iterdir()
	def read_file_suffix(D,**B):
		if not B:return A
		return E(B.get(F,C)).suffix
	def read_filesystem_modification_timestamp(G,**B):
		if not B:return A
		D=E(B.get(F,C)).stat().st_mtime;return D
	def read_filesystem_status_change_timestamp(G,**B):
		if not B:return A
		D=E(B.get(F,C)).stat().st_ctime;return D
	def read_filesystem_access_timestamp(G,**B):
		if not B:return A
		D=E(B.get(F,C)).stat().st_atime;return D
	def read_filesystem_via_pattern(I,**B):
		if not B:return A
		D=B.get(Z,C);F=B.get('pattern',C);H=G(E(D).glob(F));return H
	def uncompress_zip(F,**B):
		if not B:return A
		D=B.get('archive_path',C);E=B.get('destination_path',C)
		if not D or not E:return A
		G=B.get('overwrite',A);H=F._filesystem_compression_manager.zip_extract(archive_path=D,destination_path=E,overwrite=G);return H
	def read_zip_format_compression(E,**D):
		if not D:return A
		B=D.get(F,C)
		if not B:return A
		B=E._filesystem_compression_manager.get_zip_format_compression(B);return B
	def is_filesystem_path_valid(G,**B):
		if not B:return A
		D=E(B.get(F,C)).exists();return D
	def is_file_path_valid(G,**B):
		if not B:return A
		D=E(B.get(F,C)).is_file();return D
	def is_folder_path_valid(G,**B):
		if not B:return A
		D=E(B.get(F,C)).is_dir();return D
	def setup_filesystem_tree_paths(G,**D):
		if not D:return A
		C=D.get(A7,[])
		if not C or Y(C)<1:return A
		for F in C:
			if not F:continue
			E(F).mkdir(parents=B,exist_ok=B)
		return B
	def setup_filesystem_tree_path(G,**F):
		if not F:return A
		D=F.get(R,C)
		if not D or not D:return A
		D=E(D)
		if D.exists():return A
		D.mkdir(parents=B,exist_ok=B);return B
	def setup_filesystem_tree(L,**I):
		if not I:return A
		J=I.get('root_path',C);K=I.get('tree',D)
		if not J or not K:return A
		G=E(J)
		if not G.exists():raise P(f"filesystem path '{G}' is invalid")
		G.mkdir(parents=B,exist_ok=B)
		for F in K.entities or[]:
			H=G/F.name
			if A9(F,x):H.mkdir(parents=B,exist_ok=B);L.setup_filesystem_tree(root_path=H,tree=F)
			elif A9(F,w):
				if not H.exists():H.write_text(F.content,encoding=F.encoding)
		return B
	def move_filesystem_path(H,**G):
		if not G:return A
		F=G.get(A8,C);D=G.get(R,C)
		if not F or not D:return A
		F=E(F);D=E(D);D.parent.mkdir(parents=B,exist_ok=B);I.move(str(F),str(D));return B
	def copy_filesystem_paths(J,**G):
		if not G:return A
		D=G.get(A8,C);H=G.get(A7,[])
		if not D or Y(H)<1:return A
		D=E(D).resolve()
		for F in H:
			if not F:continue
			F=E(F).resolve()
			if D==F:return A
			if D.is_dir():I.copytree(D,F,dirs_exist_ok=B)
			elif D.is_file():F.parent.mkdir(parents=B,exist_ok=B);I.copy2(D,F)
		return B
	def copy_filesystem_path(H,**G):
		if not G:return A
		D=G.get(A8,C);F=G.get(R,C)
		if not D or not F:return A
		D=E(D).resolve()
		if not F:return A
		F=E(F).resolve()
		if D==F:return A
		if D.is_dir():I.copytree(D,F,dirs_exist_ok=B)
		elif D.is_file():F.parent.mkdir(parents=B,exist_ok=B);I.copy2(D,F)
		return B
	def clean_filesystem_paths(K,**H):
		if not H:return A
		G=H.get(A7,[])
		if not G or Y(G)<1:return A
		for D in G:
			if not D:continue
			D=E(D).resolve();J={E(C),E('/'),E.home()}
			if D in J:raise P(f"folder path '{D}' is protected")
			if not D.exists():return B
			if not D.is_dir():raise P(f"file path '{D}' is not a folder")
			for F in D.iterdir():
				if F.is_file()or F.is_symlink():F.unlink()
				elif F.is_dir():I.rmtree(F)
		return B
	def clean_filesystem_path(J,**G):
		if not G:return A
		D=G.get(R,C)
		if not D:return A
		D=E(D).resolve();H={E(C),E('/'),E.home()}
		if D in H:raise P(f"folder path '{D}' is protected")
		if not D.exists():return B
		if not D.is_dir():raise P(f"file path '{D}' is not a folder")
		for F in D.iterdir():
			if F.is_file()or F.is_symlink():F.unlink()
			elif F.is_dir():I.rmtree(F)
		return B
	def read_filesystem_entity_parents(H,**B):
		if not B:return set()
		A=set();D=B.get(R,C)
		if not D:return A
		F=E(D).parents
		if not F:return A
		for G in F:
			if not G:continue
			A.add(f"{G}")
		return A
	def rename_filesystem_entity(H,**D):
		if not D:return A
		F=D.get('old_path',C);G=D.get('new_path',C)
		if not F or not G:return A
		E(F).rename(D.get(G));return B
	def read_python_filesystem_paths(H,**B):
		if not B:return A
		D=E(B.get('path',C));F=G(str(A)for A in D.rglob('*.py')if'__pycache__'not in A.parts);return F
	def generate_uuidv4(B):A=M.uuid4();return A
	def generate_uuidv5(E,**A):
		B='key'
		if not A:return C
		D=M.uuid5(M.NAMESPACE_DNS,A.get(B,B));return D
	def generate_uuidv7(B):A=M.uuid7();return A
	def read_method_name(B,level=2):A=f"{S._getframe(level).f_code.co_name}";return A
	def read_operating_system_name(A):B=A._system_manager.operating_system_name;return B
	def read_operating_system_architecture(A):B=A._system_manager.operating_system_architecture;return B
	def read_current_executing_script_filesystem_path(A):B=A._system_manager.current_executing_script_filesystem_path;return B
	def read_current_executing_console_filesystem_path(A):B=A._system_manager.current_executing_console_filesystem_path;return B
	def write_current_executing_console_filesystem_path(E,**D):
		if not D:return A
		E._system_manager.current_executing_console_filesystem_path=D.get(Z,C);return B
	def read_original_executing_console_filesystem_path(A):B=A._system_manager.original_executing_console_filesystem_path;return B
	def read_file(B,**A):
		if not A:return C
		D=B._file_io_manager.read_file(file_path=A.get(Q,C));return D
	def write_file(E,**D):
		if not D:return A
		E._file_io_manager.write_file(file_path=D.get(Q,C),data=D.get('data',{}));return B
	def setup_file_log_settings(D,**C):
		if not C:return A
		E=C.get(AC,B);F=C.get(AD,B);D._file_log_manager.options=V(is_enabled=E,is_verbose_enabled=F)
		if E:
			H=C.get('file_outputs',G())
			for I in H:D._file_log_manager.add_file_output(I)
		return B
	def setup_console_log_settings(D,**C):
		if not C:return A
		E=C.get(AC,B);F=C.get(AD,B);D._console_log_manager.options=V(is_enabled=E,is_verbose_enabled=F);return B
	def log_info_to_file(E,**D):
		if not D:return A
		E._file_log_manager.log_info(message=D.get(L,C));return B
	def log_warning_to_file(E,**D):
		if not D:return A
		E._file_log_manager.log_warning(message=D.get(L,C));return B
	def log_debug_to_file(E,**D):
		if not D:return A
		E._file_log_manager.log_info(message=D.get(L,C));return B
	def log_info_to_all(E,**D):
		if not D:return A
		E._log_manager.log_info(message=D.get(L,C));return B
	def log_cache_info_to_file(E,**D):
		if not D:return A
		E._file_log_manager.cache_log(message=D.get(L,C),log_level=N.INFO);return B
	def log_cache_debug_to_file(E,**D):
		if not D:return A
		E._file_log_manager.cache_log(message=D.get(L,C),log_level=N.DEBUG);return B
	def log_cache_warning_to_file(E,**D):
		if not D:return A
		E._file_log_manager.cache_log(message=D.get(L,C),log_level=N.WARNING);return B
	def log_shutdown(A):A._log_manager.shutdown();return B