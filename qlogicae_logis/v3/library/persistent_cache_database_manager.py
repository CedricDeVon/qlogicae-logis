from __future__ import annotations
_E='path'
_D='accessibility_type'
_C=None
_B=True
_A=False
from typing import Any
__all__='PersistentCacheDatabasManager'
_TaskManager=_C
_ImportManager=_C
_DatabaseManager=_C
_CommandStorageManager=_C
def _handle_dynamic_imports():global _handle_dynamic_imports;global _TaskManager;global _ImportManager;global _DatabaseManager;global _CommandStorageManager;from..library import database_manager as A,import_manager as B,task_manager as C;_TaskManager=C.TaskManager;_ImportManager=B.ImportManager;_DatabaseManager=A.DatabaseManager;_handle_dynamic_imports=lambda:_C
class PersistentCacheDatabasManager:
	__slots__='_import_manager','_database_manager'
	def __init__(A):_handle_dynamic_imports();A._import_manager=_ImportManager.read_singleton(_ImportManager);A._database_manager=_ImportManager.read_singleton(_DatabaseManager)
	def read_key_path(B,key_path):
		A=key_path
		if not A:return''
		return'-'.join((*B._database_manager.read_root_key_path(),A))
	def read_many_values(B,key_paths):
		A=key_paths
		if not A or len(A)<1:return{}
		C=[]
		for D in A:C.append(B.read_key_path(D))
		E=B._import_manager.read_many_values_via_disk_cache(key_paths=C)or{};return E
	def read_all_values(A):B=A._import_manager.read_all_values_via_disk_cache()or{};return B
	def write_many_values(B,values):
		A=values
		if not A or len(A)<1:return _A
		C={}
		for(D,E)in A.items():C[B.read_key_path(D)]=E
		B._import_manager.write_many_values_via_disk_cache(values=C);return _B
	def read_configuration_workspace_key_path(C,**A):
		if not A:return''
		B=A.get('value','');return f"configuration-workspace-{B}"
	def read_configuration_workspace_raw_value_key_path(B,**A):
		if not A:return''
		C=A.get(_D,'');D=A.get(_E,'');return B.read_configuration_workspace_key_path(value=f"raw-{C}-{D}-value")
	def read_configuration_workspace_raw_count_value_key_path(B,**A):
		if not A:return''
		C=A.get(_D,'');return B.read_configuration_workspace_key_path(value=f"raw-count-{C}-value")
	def read_configuration_workspace_raw_metadata_value_key_path(B,**A):
		if not A:return''
		C=A.get(_D,'');D=A.get(_E,'');return B.read_configuration_workspace_key_path(value=f"raw-{C}-{D}-metadata-value")
	def read_configuration_workspace_data_value_key_path(B,**A):
		if not A:return''
		C=A.get(_D,'');D=A.get(_E,'');return B.read_configuration_workspace_key_path(value=f"data-{C}-{D}-value")
	def read_configuration_workspace_data_key_path(A):return A.read_configuration_workspace_key_path(value='data')
	def read_refresh_data_key_path(A):return'refresh-data'
	def read_configuration_workspace_file(A,accessibility_type,path):
		B=accessibility_type
		if not B or not path:return{}
		C=A.read_configuration_workspace_raw_value_key_path(accessibility_type=B,path=path);D=A.read_many_values((C,));return D.get(A.read_key_path(C),{})or{}
	def write_configuration_workspace_file(A,accessibility_type,path,values):
		C=values;B=accessibility_type
		if not B or not path or not C:return _A
		D=A.read_configuration_workspace_raw_value_key_path(accessibility_type=B,path=path);A.write_many_values({D:C});return _B
	def read_configuration_workspace_metadata(A,accessibility_type,path):
		B=accessibility_type
		if not B or not path:return{}
		C=A.read_configuration_workspace_raw_metadata_value_key_path(accessibility_type=B,path=path);D=A.read_many_values((C,));return D.get(A.read_key_path(C),{})or{}
	def write_configuration_workspace_metadata(A,accessibility_type,path,values):
		C=values;B=accessibility_type
		if not B or not path or not C:return _A
		D=A.read_configuration_workspace_raw_metadata_value_key_path(accessibility_type=B,path=path);A.write_many_values({D:C});return _B
	def read_configuration_workspace_data(A,accessibility_type,path):
		B=accessibility_type
		if not B or not path:return{}
		C=A.read_configuration_workspace_data_value_key_path(accessibility_type=B,path=path);D=A.read_many_values((C,));return D.get(A.read_key_path(C),{})or{}
	def write_configuration_workspace_data(A,accessibility_type,path,values):
		C=values;B=accessibility_type
		if not B or not path or not C:return _A
		D=A.read_configuration_workspace_data_value_key_path(accessibility_type=B,path=path);A.write_many_values({D:C});return _B
	def read_configuration_workspace_file_count(A,accessibility_type):
		B=accessibility_type
		if not B:return 0
		C=A.read_configuration_workspace_raw_count_value_key_path(accessibility_type=B);D=A.read_many_values((C,));return D.get(A.read_key_path(C),0)or 0
	def write_configuration_workspace_file_count(A,accessibility_type,value):
		C=value;B=accessibility_type
		if not B or not C:return _A
		D=A.read_configuration_workspace_raw_count_value_key_path(accessibility_type=B);A.write_many_values({D:C});return _B
	def read_merged_configuration_workspace_data(A):B=A.read_configuration_workspace_data_key_path();C=A.read_many_values((B,));return C.get(A.read_key_path(B),{})or{}
	def write_merged_configuration_workspace_data(B,value):
		A=value
		if not A or len(A)<1:return _A
		C=B.read_configuration_workspace_data_key_path();B.write_many_values({C:A});return _B
	def read_refresh_data(A):B=A.read_refresh_data_key_path();C=A.read_many_values((B,));return C.get(A.read_key_path(B),{})or{}
	def write_refresh_data(B,value):
		A=value
		if not A or len(A)<1:return _A
		C=B.read_refresh_data_key_path();B.write_many_values({C:A});return _B