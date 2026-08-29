from __future__ import annotations
_V='is_verbose'
_U='is_enabled'
_T='encoding'
_S='key_paths'
_R='source_path'
_Q='target_paths'
_P='indent'
_O='allow_unicode'
_N='default_flow_style'
_M='sort_keys'
_L='command'
_K='utf-8'
_J='values'
_I='filesystem_path'
_H='target_path'
_G='file_path'
_F='message'
_E='key_path'
_D='value'
_C=None
_B=True
_A=False
from typing import Any
__all__='ImportManager'
_gc=_C
_sys=_C
_time=_C
_uuid=_C
_yaml=_C
_Path=_C
_shutil=_C
_logging=_C
_ZipFile=_C
_metadata=_C
_resource=_C
_Timestamp=_C
_LogOptions=_C
_LogManager=_C
_TimeManager=_C
_tracemalloc=_C
_MacrosManager=_C
_SystemManager=_C
_ScriptProcess=_C
_FileIoManager=_C
_TimeZoneManager=_C
_module_from_spec=_C
_SingletonManager=_C
_TimestampManager=_C
_TargetCacheValue=_C
_ConsoleLogManager=_C
_ValueCacheManager=_C
_CorFileLogManager=_C
_ObjectMergeManager=_C
_TextEncodingManager=_C
_ScriptProcessManager=_C
_GroupSelectionManager=_C
_spec_from_file_location=_C
_DiskCacheStorageManager=_C
_ScriptProcessEnumManager=_C
_FilesystemCompressionManager=_C
_FileEntityFileSystemTreeSetupOptions=_C
_FolderEntityFileSystemTreeSetupOptions=_C
def _handle_dynamic_imports():global _handle_dynamic_imports;global _gc;global _sys;global _time;global _uuid;global _yaml;global _Path;global _shutil;global _logging;global _ZipFile;global _metadata;global _resource;global _Timestamp;global _LogOptions;global _LogManager;global _tracemalloc;global _TimeManager;global _MacrosManager;global _SystemManager;global _ScriptProcess;global _FileIoManager;global _module_from_spec;global _TimeZoneManager;global _SingletonManager;global _TimestampManager;global _TargetCacheValue;global _ConsoleLogManager;global _ValueCacheManager;global _CorFileLogManager;global _ObjectMergeManager;global _TextEncodingManager;global _ScriptProcessManager;global _GroupSelectionManager;global _spec_from_file_location;global _DiskCacheStorageManager;global _ScriptProcessEnumManager;global _FilesystemCompressionManager;global _FileEntityFileSystemTreeSetupOptions;global _FolderEntityFileSystemTreeSetupOptions;import gc,logging as A,resource as B,shutil as C,sys,time,tracemalloc as D,uuid;from importlib import metadata as E;from importlib.util import module_from_spec as F,spec_from_file_location as G;from pathlib import Path;from zipfile import ZipFile as H;from.._vendor.pyyaml import yaml;from.._vendor.qlogicae_cor.v2.library import console_log_manager as I,disk_cache_storage_manager as J,file_entity_filesystem_tree_setup_options as K,file_io_manager as L,file_log_manager as M,filesystem_compression_manager as N,folder_entity_filesystem_tree_setup_options as O,group_selection_manager as P,log_manager as Q,log_options as R,macros_manager as S,object_merge_manager as T,script_process as U,script_process_manager as V,singleton_manager as W,system_manager as X,target_cache_value as Y,text_encoding_manager as Z,time_manager as a,time_zone_manager as b,timestamp as c,timestamp_manager as d,value_cache_manager as e;_gc=gc;_sys=sys;_uuid=uuid;_yaml=yaml;_Path=Path;_time=time;_shutil=C;_ZipFile=H;_logging=A;_metadata=E;_resource=B;_tracemalloc=D;_Timestamp=c.Timestamp;_LogOptions=R.LogOptions;_LogManager=Q.LogManager;_module_from_spec=F;_TimeManager=a.TimeManager;_MacrosManager=S.MacrosManager;_SystemManager=X.SystemManager;_spec_from_file_location=G;_TimeZoneManager=b.TimeZoneManager;_CorFileLogManager=M.FileLogManager;_SingletonManager=W.SingletonManager;_TimestampManager=d.TimestampManager;_TargetCacheValue=Y.TargetCacheValue;_ValueCacheManager=e.ValueCacheManager;_ObjectMergeManager=T.ObjectMergeManager;_ScriptProcessManager=V.ScriptProcessManager;_FilesystemCompressionManager=N.FilesystemCompressionManager;_FileEntityFileSystemTreeSetupOptions=K.FileEntityFileSystemTreeSetupOptions;_FolderEntityFileSystemTreeSetupOptions=O.FolderEntityFileSystemTreeSetupOptions;_ConsoleLogManager=I.ConsoleLogManager;_DiskCacheStorageManager=J.DiskCacheStorageManager;_ScriptProcess=U.ScriptProcess;_FileIoManager=L.FileIoManager;_GroupSelectionManager=P.GroupSelectionManager;_TextEncodingManager=Z.TextEncodingManager;_handle_dynamic_imports=lambda:_C
def _handle_singleton_manager_imports():global _handle_singleton_manager_imports;global _SingletonManager;from.._vendor.qlogicae_cor.v2.library import singleton_manager as A;_SingletonManager=A.SingletonManager;_handle_singleton_manager_imports=lambda:_C
class ImportManager:
	__slots__='_time_manager','_disk_cache_storage_manager','_value_cache_manager','_time_zone_manager','_timestamp_manager','_text_encoding_manager','_script_process_manager','_macros_manager','_object_merge_manager','_group_selection_manager','_filesystem_compression_manager','_system_manager','_file_io_manager','_file_log_manager','_console_log_manager','_log_manager'
	def __init__(A):_handle_dynamic_imports();A._time_manager=A.read_singleton(_TimeManager);A._disk_cache_storage_manager=A.read_singleton(_DiskCacheStorageManager);A._value_cache_manager=A.read_singleton(_ValueCacheManager);A._time_zone_manager=A.read_singleton(_TimeZoneManager);A._timestamp_manager=A.read_singleton(_TimestampManager);A._text_encoding_manager=A.read_singleton(_TextEncodingManager);A._script_process_manager=A.read_singleton(_ScriptProcessManager);A._macros_manager=A.read_singleton(_MacrosManager);A._object_merge_manager=A.read_singleton(_ObjectMergeManager);A._group_selection_manager=A.read_singleton(_GroupSelectionManager);A._filesystem_compression_manager=A.read_singleton(_FilesystemCompressionManager);A._system_manager=A.read_singleton(_SystemManager);A._file_io_manager=A.read_singleton(_FileIoManager);A._file_log_manager=A.read_singleton(_CorFileLogManager);A._console_log_manager=A.read_singleton(_ConsoleLogManager);A._log_manager=A.read_singleton(_LogManager)
	@classmethod
	def read_singleton(B,value):
		A=value
		if not A:return{}
		_handle_singleton_manager_imports();return _SingletonManager.get_singleton(A)
	def convert_to_os_specific_path_value(C,**A):B=A.get(_I,'');return f"{_Path(B)}"
	def compress(G,**A):
		if not A:return _A
		B=A.get('source','');D=A.get('destination','');E=A.get('mode','')
		if not D or not E:return _A
		B=_Path(B);C=A.get('compression','deflated');C=G.read_zip_format_compression(value=C);H=A.get('compresslevel',6);I=A.get('allowZip64',_B);J=A.get('strict_timestamps',_B)
		with _ZipFile(D,mode=E,compression=C,compresslevel=H,allowZip64=I,strict_timestamps=J)as K:
			for F in B.rglob('*'):K.write(F,arcname=F.relative_to(B))
		return _B
	def read_metadata_version(C,target):
		B='v0.0.0';A=target
		if not A:return B
		return _metadata.version(A)or B
	def snapshot_memory_usage(D):
		B,C=_tracemalloc.get_traced_memory()if _tracemalloc.is_tracing()else(0,0);A=_resource.getrusage(_resource.RUSAGE_SELF).ru_maxrss
		if _sys.platform!='darwin':A*=1024
		return{'tracemalloc-current':{_D:B},'tracemalloc-peak':{_D:C},'process-peak-rss':{_D:A},'gc-tracked-objects':{_D:len(_gc.get_objects())}}
	def time_delay(C,**A):
		if not A:return _A
		B=A.get(_D,0)
		if not B:return _A
		_time.sleep(B);return _B
	def read_current_iso8601_date(A):B=A._time_manager.current_iso8601_date;return B
	def read_current_nanosecond(A):B=A._time_manager.current_nanosecond;return B
	def read_current_day(A):B=A._time_manager.current_day;return B
	def read_current_month(A):B=A._time_manager.current_month;return B
	def read_current_year(A):B=A._time_manager.current_year;return B
	def is_key_found_via_disk_cache(B,**A):
		if not A:return _A
		C=B._disk_cache_storage_manager.is_keys_found(key_path=A.get(_E,''));return C
	def is_item_expired_via_disk_cache(B,**A):
		if not A:return _A
		C=B._disk_cache_storage_manager.is_item_expired(key_path=A.get(_E,''));return C
	def read_all_values_via_disk_cache(A):B=A._disk_cache_storage_manager.read_all_values();return B
	def read_many_values_via_disk_cache(B,**A):
		if not A:return{}
		C=B._disk_cache_storage_manager.get_many_values(key_paths=A.get(_S,tuple()));return C
	def write_many_values_via_disk_cache(B,**A):
		if not A:return _A
		B._disk_cache_storage_manager.set_many_values(values=A.get(_J,{}));return _B
	def remove_many_values_via_disk_cache(B,**A):
		if not A:return{}
		C=B._disk_cache_storage_manager.remove_many_values(key_paths=A.get(_S,tuple()));return C
	def open_via_disk_cache(A):A._disk_cache_storage_manager.open();return _B
	def close_via_disk_cache(A):A._disk_cache_storage_manager.close();return _B
	def clear_all_values_via_disk_cache(A):A._disk_cache_storage_manager.clear_all_values();return _B
	def remove_expired_values_via_disk_cache(A):B=A._disk_cache_storage_manager.remove_expired_values();return B
	def sync_via_disk_cache(A):A._disk_cache_storage_manager.sync();return _B
	def reorganize_via_disk_cache(A):A._disk_cache_storage_manager.reorganize();return _B
	def display_all_items_via_disk_cache(A):A._disk_cache_storage_manager.display_all_items();return _B
	def write_database_path_via_disk_cache(B,value):
		A=value
		if not A:return _A
		B._disk_cache_storage_manager.database_path=A;return _B
	def read_any_value_via_value_cache(B,**A):
		if not A:return{}
		C=B._value_cache_manager.get_one_value(key_path=A.get(_E,tuple()),output_type=_TargetCacheValue.ANY);return C
	def read_defined_value_via_value_cache(B,**A):
		if not A:return{}
		C=B._value_cache_manager.get_one_value(key_path=A.get(_E,tuple()),output_type=_TargetCacheValue.DEFINED);return C
	def write_any_value_via_value_cache(B,**A):
		if not A:return _A
		B._value_cache_manager.set_one_value(key_path=A.get(_E,tuple()),value=A.get(_D,{}),output_type=_TargetCacheValue.ANY);return _B
	def write_defined_value_via_value_cache(B,**A):
		if not A:return _A
		B._value_cache_manager.set_one_value(key_path=A.get(_E,tuple()),value=A.get(_D,{}),output_type=_TargetCacheValue.DEFINED);return _B
	def write_file_path_value_via_value_cache(B,**A):
		if not A:return _A
		B._value_cache_manager.set_one_value(key_path=A.get(_E,tuple()),value=A.get(_D,{}),output_type=_TargetCacheValue.FILE_PATH);return _B
	def write_folder_path_value_via_value_cache(B,**A):
		if not A:return _A
		B._value_cache_manager.set_one_value(key_path=A.get(_E,tuple()),value=A.get(_D,{}),output_type=_TargetCacheValue.FOLDER_PATH);return _B
	def write_filesystem_path_value_via_value_cache(B,**A):
		if not A:return _A
		B._value_cache_manager.set_one_value(key_path=A.get(_E,tuple()),value=A.get(_D,{}),output_type=_TargetCacheValue.FILESYSTEM_PATH);return _B
	def display_all_items_via_value_cache(A):A._value_cache_manager.display_all_items();return _B
	def remove_one_value_via_value_cache(B,**A):
		if not A:return _A
		B._value_cache_manager.remove_one_value(key_path=A.get(_E,tuple()));return _B
	def clear_all_values_via_value_cache(A):A._value_cache_manager.clear_all_values();return _B
	def read_selected_time_zone(A):B=A._time_zone_manager.selected_time_zone_type;return B
	def write_selected_time_zone(B,**A):
		if not A:return _A
		B._time_zone_manager.selected_time_zone_type=A.get(_D,'local'),;return _B
	def generate_current_date_timestamp(A):B=A._timestamp_manager.generate_current_timestamp(_Timestamp.ISO_DATE_STRING);return B
	def generate_current_filesystem_timestamp(A):B=A._timestamp_manager.generate_current_timestamp(_Timestamp.ISO_FILESYSTEM_STRING);return B
	def read_selected_encoding(A):B=A._text_encoding_manager.selected_encoding;return B
	def write_selected_encoding(B,**A):
		if not A:return _A
		B._text_encoding_manager.selected_encoding=A.get(_D,_K),;return _B
	def run_shell_command(B,**A):
		if not A:return _A
		C=B._script_process_manager.execute_command(command=A.get(_L,''),script_process_type=_ScriptProcess.SHELL);return C
	def run_subprocess_command(B,**A):
		if not A:return _A
		C=B._script_process_manager.execute_command(command=A.get(_L,''),script_process_type=_ScriptProcess.SUBPROCESS);return C
	def run_command(D,**A):
		F='shell'
		if not A:return{}
		E=A.get('script_process',F);B=A.get(_L,'')
		if not B:return{}
		C={}
		if E==F:C=D.run_shell_command(command=B)
		elif E=='subprocess':C=D.run_subprocess_command(command=B)
		return C
	def macros_resolve_many(B,**A):
		if not A:return _A
		C=B._macros_manager.resolve_many(A.get(_J,{}));return C
	def macros_parse_many(B,**A):
		if not A:return _A
		C=B._macros_manager.parse_many(values=A.get(_J,''),resolved=A.get('resolved',{}));return C
	def macros_parse_filesystem(B,**A):
		if not A:return _A
		C=B._macros_manager.parse_filesystem(filesystem_path=A.get(_I,''),workspace_macros=A.get('workspace_macros',{}));return C
	def object_deep_merge(B,**A):
		if not A:return _A
		C=B._object_merge_manager.deep_merge(left=A.get('left',{}),right=A.get('right',{}));return C
	def object_deep_merge_fragments(B,**A):
		if not A:return _A
		C=B._object_merge_manager.deep_merge_fragments(left=A.get('left',{}),right=A.get('right',{}));return C
	def object_flatten_group(B,**A):
		if not A:return _A
		return B._group_selection_manager.flatten_group(A.get('target',''),A.get('data',{}))or{}
	def convert_yaml_string_to_object(B,**A):
		if not A:return{}
		return _yaml.safe_load(A.get(_D,''))or{}
	def convert_yaml_object_to_string(B,**A):
		if not A:return''
		return _yaml.safe_dump(A.get(_D,''),sort_keys=A.get(_M,_A),default_flow_style=A.get(_N,_A),allow_unicode=A.get(_O,_B),indent=A.get(_P,4))or''
	def format_yaml_to_string(B,**A):
		if not A:return _A
		return _yaml.dump(A.get(_D,''),sort_keys=A.get(_M,_A),default_flow_style=A.get(_N,_A),allow_unicode=A.get(_O,_B),indent=A.get(_P,4))
	def read_yaml_file(D,**A):
		if not A:return _A
		B=_Path(A.get(_G,''))
		with B.open(mode='r',encoding=A.get(_T,_K))as C:return _yaml.safe_load(C)or{}
	def write_yaml_file(D,**A):
		if not A:return _A
		B=_Path(A.get(_G,''))
		with B.open(mode='w',encoding=A.get(_T,_K))as C:_yaml.safe_dump(A.get(_D,''),C,sort_keys=A.get(_M,_A),default_flow_style=A.get(_N,_A),allow_unicode=A.get(_O,_B),indent=A.get(_P,4))
		return _B
	def read_python_file(F,**A):
		if not A:return _A
		B=_Path(A.get(_G,''));E=B.stem;C=_spec_from_file_location(E,B);D=_module_from_spec(C);C.loader.exec_module(D);return D or{}
	def read_child_folder_paths(B,**A):
		if not A:return _A
		return _Path(A.get(_D,'')).iterdir()
	def read_file_suffix(B,**A):
		if not A:return _A
		return _Path(A.get(_D,'')).suffix
	def read_filesystem_modification_timestamp(C,**A):
		if not A:return _A
		B=_Path(A.get(_D,'')).stat().st_mtime;return B
	def read_filesystem_status_change_timestamp(C,**A):
		if not A:return _A
		B=_Path(A.get(_D,'')).stat().st_ctime;return B
	def read_filesystem_access_timestamp(C,**A):
		if not A:return _A
		B=_Path(A.get(_D,'')).stat().st_atime;return B
	def read_filesystem_via_pattern(E,**A):
		if not A:return _A
		B=A.get(_I,'');C=A.get('pattern','');D=tuple(_Path(B).glob(C));return D
	def uncompress_zip(D,**A):
		if not A:return _A
		B=A.get('archive_path','');C=A.get('destination_path','')
		if not B or not C:return _A
		E=A.get('overwrite',_A);F=D._filesystem_compression_manager.zip_extract(archive_path=B,destination_path=C,overwrite=E);return F
	def read_zip_format_compression(C,**B):
		if not B:return _A
		A=B.get(_D,'')
		if not A:return _A
		A=C._filesystem_compression_manager.get_zip_format_compression(A);return A
	def is_filesystem_path_valid(C,**A):
		if not A:return _A
		B=_Path(A.get(_D,'')).exists();return B
	def is_file_path_valid(C,**A):
		if not A:return _A
		B=_Path(A.get(_D,'')).is_file();return B
	def is_folder_path_valid(C,**A):
		if not A:return _A
		B=_Path(A.get(_D,'')).is_dir();return B
	def setup_filesystem_tree_paths(D,**B):
		if not B:return _A
		A=B.get(_Q,[])
		if not A or len(A)<1:return _A
		for C in A:
			if not C:continue
			_Path(C).mkdir(parents=_B,exist_ok=_B)
		return _B
	def setup_filesystem_tree_path(C,**B):
		if not B:return _A
		A=B.get(_H,'')
		if not A or not A:return _A
		A=_Path(A)
		if A.exists():return _A
		A.mkdir(parents=_B,exist_ok=_B);return _B
	def setup_filesystem_tree(G,**D):
		if not D:return _A
		E=D.get('root_path','');F=D.get('tree',_C)
		if not E or not F:return _A
		B=_Path(E)
		if not B.exists():raise ValueError(f"filesystem path '{B}' is invalid")
		B.mkdir(parents=_B,exist_ok=_B)
		for A in F.entities or[]:
			C=B/A.name
			if isinstance(A,_FolderEntityFileSystemTreeSetupOptions):C.mkdir(parents=_B,exist_ok=_B);G.setup_filesystem_tree(root_path=C,tree=A)
			elif isinstance(A,_FileEntityFileSystemTreeSetupOptions):
				if not C.exists():C.write_text(A.content,encoding=A.encoding)
		return _B
	def move_filesystem_path(D,**C):
		if not C:return _A
		B=C.get(_R,'');A=C.get(_H,'')
		if not B or not A:return _A
		B=_Path(B);A=_Path(A);A.parent.mkdir(parents=_B,exist_ok=_B);_shutil.move(str(B),str(A));return _B
	def copy_filesystem_paths(E,**C):
		if not C:return _A
		A=C.get(_R,'');D=C.get(_Q,[])
		if not A or len(D)<1:return _A
		A=_Path(A).resolve()
		for B in D:
			if not B:continue
			B=_Path(B).resolve()
			if A==B:return _A
			if A.is_dir():_shutil.copytree(A,B,dirs_exist_ok=_B)
			elif A.is_file():B.parent.mkdir(parents=_B,exist_ok=_B);_shutil.copy2(A,B)
		return _B
	def copy_filesystem_path(D,**C):
		if not C:return _A
		A=C.get(_R,'');B=C.get(_H,'')
		if not A or not B:return _A
		A=_Path(A).resolve()
		if not B:return _A
		B=_Path(B).resolve()
		if A==B:return _A
		if A.is_dir():_shutil.copytree(A,B,dirs_exist_ok=_B)
		elif A.is_file():B.parent.mkdir(parents=_B,exist_ok=_B);_shutil.copy2(A,B)
		return _B
	def clean_filesystem_paths(F,**D):
		if not D:return _A
		C=D.get(_Q,[])
		if not C or len(C)<1:return _A
		for A in C:
			if not A:continue
			A=_Path(A).resolve();E={_Path(''),_Path('/'),_Path.home()}
			if A in E:raise ValueError(f"folder path '{A}' is protected")
			if not A.exists():return _B
			if not A.is_dir():raise ValueError(f"file path '{A}' is not a folder")
			for B in A.iterdir():
				if B.is_file()or B.is_symlink():B.unlink()
				elif B.is_dir():_shutil.rmtree(B)
		return _B
	def clean_filesystem_path(E,**C):
		if not C:return _A
		A=C.get(_H,'')
		if not A:return _A
		A=_Path(A).resolve();D={_Path(''),_Path('/'),_Path.home()}
		if A in D:raise ValueError(f"folder path '{A}' is protected")
		if not A.exists():return _B
		if not A.is_dir():raise ValueError(f"file path '{A}' is not a folder")
		for B in A.iterdir():
			if B.is_file()or B.is_symlink():B.unlink()
			elif B.is_dir():_shutil.rmtree(B)
		return _B
	def read_filesystem_entity_parents(F,**B):
		if not B:return set()
		A=set();C=B.get(_H,'')
		if not C:return A
		D=_Path(C).parents
		if not D:return A
		for E in D:
			if not E:continue
			A.add(f"{E}")
		return A
	def rename_filesystem_entity(D,**A):
		if not A:return _A
		B=A.get('old_path','');C=A.get('new_path','')
		if not B or not C:return _A
		_Path(B).rename(A.get(C));return _B
	def read_python_filesystem_paths(D,**A):
		if not A:return _A
		B=_Path(A.get('path',''));C=tuple(str(A)for A in B.rglob('*.py')if'__pycache__'not in A.parts);return C
	def generate_uuidv4(B):A=_uuid.uuid4();return A
	def generate_uuidv5(D,**A):
		B='key'
		if not A:return''
		C=_uuid.uuid5(_uuid.NAMESPACE_DNS,A.get(B,B));return C
	def generate_uuidv7(B):A=_uuid.uuid7();return A
	def read_method_name(B,level=2):A=f"{_sys._getframe(level).f_code.co_name}";return A
	def read_operating_system_name(A):B=A._system_manager.operating_system_name;return B
	def read_operating_system_architecture(A):B=A._system_manager.operating_system_architecture;return B
	def read_current_executing_script_filesystem_path(A):B=A._system_manager.current_executing_script_filesystem_path;return B
	def read_current_executing_console_filesystem_path(A):B=A._system_manager.current_executing_console_filesystem_path;return B
	def write_current_executing_console_filesystem_path(B,**A):
		if not A:return _A
		B._system_manager.current_executing_console_filesystem_path=A.get(_I,'');return _B
	def read_original_executing_console_filesystem_path(A):B=A._system_manager.original_executing_console_filesystem_path;return B
	def read_file(B,**A):
		if not A:return''
		C=B._file_io_manager.read_file(file_path=A.get(_G,''));return C
	def write_file(B,**A):
		if not A:return _A
		B._file_io_manager.write_file(file_path=A.get(_G,''),data=A.get('data',{}));return _B
	def setup_file_log_settings(B,**A):
		if not A:return _A
		C=A.get(_U,_B);D=A.get(_V,_B);B._file_log_manager.options=_LogOptions(is_enabled=C,is_verbose_enabled=D)
		if C:
			E=A.get('file_outputs',tuple())
			for F in E:B._file_log_manager.add_file_output(F)
		return _B
	def setup_console_log_settings(B,**A):
		if not A:return _A
		C=A.get(_U,_B);D=A.get(_V,_B);B._console_log_manager.options=_LogOptions(is_enabled=C,is_verbose_enabled=D);return _B
	def log_info_to_file(B,**A):
		if not A:return _A
		B._file_log_manager.log_info(message=A.get(_F,''));return _B
	def log_warning_to_file(B,**A):
		if not A:return _A
		B._file_log_manager.log_warning(message=A.get(_F,''));return _B
	def log_debug_to_file(B,**A):
		if not A:return _A
		B._file_log_manager.log_info(message=A.get(_F,''));return _B
	def log_info_to_all(B,**A):
		if not A:return _A
		B._log_manager.log_info(message=A.get(_F,''));return _B
	def log_cache_info_to_file(B,**A):
		if not A:return _A
		B._file_log_manager.cache_log(message=A.get(_F,''),log_level=_logging.INFO);return _B
	def log_cache_debug_to_file(B,**A):
		if not A:return _A
		B._file_log_manager.cache_log(message=A.get(_F,''),log_level=_logging.DEBUG);return _B
	def log_cache_warning_to_file(B,**A):
		if not A:return _A
		B._file_log_manager.cache_log(message=A.get(_F,''),log_level=_logging.WARNING);return _B
	def log_shutdown(A):A._log_manager.shutdown();return _B