from __future__ import annotations
J='path'
G='accessibility_type'
F=len
E=None
C=True
B=False
A=''
from typing import Any
__all__='PersistentCacheDatabasManager'
K=E
D=E
H=E
L=E
def I():global I;global K;global D;global H;global L;from..library import database_manager as A,import_manager as B,task_manager as C;K=C.TaskManager;D=B.ImportManager;H=A.DatabaseManager;I=lambda:E
class M:
	__slots__='_import_manager','_database_manager'
	def __init__(A):I();A._import_manager=D.read_singleton(D);A._database_manager=D.read_singleton(H)
	def read_key_path(C,key_path):
		B=key_path
		if not B:return A
		return'-'.join((*C._database_manager.read_root_key_path(),B))
	def read_many_values(B,key_paths):
		A=key_paths
		if not A or F(A)<1:return{}
		C=[]
		for D in A:C.append(B.read_key_path(D))
		E=B._import_manager.read_many_values_via_disk_cache(key_paths=C)or{};return E
	def read_all_values(A):B=A._import_manager.read_all_values_via_disk_cache()or{};return B
	def write_many_values(D,values):
		A=values
		if not A or F(A)<1:return B
		E={}
		for(G,H)in A.items():E[D.read_key_path(G)]=H
		D._import_manager.write_many_values_via_disk_cache(values=E);return C
	def read_configuration_workspace_key_path(D,**B):
		if not B:return A
		C=B.get('value',A);return f"configuration-workspace-{C}"
	def read_configuration_workspace_raw_value_key_path(C,**B):
		if not B:return A
		D=B.get(G,A);E=B.get(J,A);return C.read_configuration_workspace_key_path(value=f"raw-{D}-{E}-value")
	def read_configuration_workspace_raw_count_value_key_path(C,**B):
		if not B:return A
		D=B.get(G,A);return C.read_configuration_workspace_key_path(value=f"raw-count-{D}-value")
	def read_configuration_workspace_raw_metadata_value_key_path(C,**B):
		if not B:return A
		D=B.get(G,A);E=B.get(J,A);return C.read_configuration_workspace_key_path(value=f"raw-{D}-{E}-metadata-value")
	def read_configuration_workspace_data_value_key_path(C,**B):
		if not B:return A
		D=B.get(G,A);E=B.get(J,A);return C.read_configuration_workspace_key_path(value=f"data-{D}-{E}-value")
	def read_configuration_workspace_data_key_path(A):return A.read_configuration_workspace_key_path(value='data')
	def read_refresh_data_key_path(A):return'refresh-data'
	def read_configuration_workspace_file(A,accessibility_type,path):
		B=accessibility_type
		if not B or not path:return{}
		C=A.read_configuration_workspace_raw_value_key_path(accessibility_type=B,path=path);D=A.read_many_values((C,));return D.get(A.read_key_path(C),{})or{}
	def write_configuration_workspace_file(A,accessibility_type,path,values):
		E=values;D=accessibility_type
		if not D or not path or not E:return B
		F=A.read_configuration_workspace_raw_value_key_path(accessibility_type=D,path=path);A.write_many_values({F:E});return C
	def read_configuration_workspace_metadata(A,accessibility_type,path):
		B=accessibility_type
		if not B or not path:return{}
		C=A.read_configuration_workspace_raw_metadata_value_key_path(accessibility_type=B,path=path);D=A.read_many_values((C,));return D.get(A.read_key_path(C),{})or{}
	def write_configuration_workspace_metadata(A,accessibility_type,path,values):
		E=values;D=accessibility_type
		if not D or not path or not E:return B
		F=A.read_configuration_workspace_raw_metadata_value_key_path(accessibility_type=D,path=path);A.write_many_values({F:E});return C
	def read_configuration_workspace_data(A,accessibility_type,path):
		B=accessibility_type
		if not B or not path:return{}
		C=A.read_configuration_workspace_data_value_key_path(accessibility_type=B,path=path);D=A.read_many_values((C,));return D.get(A.read_key_path(C),{})or{}
	def write_configuration_workspace_data(A,accessibility_type,path,values):
		E=values;D=accessibility_type
		if not D or not path or not E:return B
		F=A.read_configuration_workspace_data_value_key_path(accessibility_type=D,path=path);A.write_many_values({F:E});return C
	def read_configuration_workspace_file_count(A,accessibility_type):
		B=accessibility_type
		if not B:return 0
		C=A.read_configuration_workspace_raw_count_value_key_path(accessibility_type=B);D=A.read_many_values((C,));return D.get(A.read_key_path(C),0)or 0
	def write_configuration_workspace_file_count(A,accessibility_type,value):
		E=value;D=accessibility_type
		if not D or not E:return B
		F=A.read_configuration_workspace_raw_count_value_key_path(accessibility_type=D);A.write_many_values({F:E});return C
	def read_merged_configuration_workspace_data(A):B=A.read_configuration_workspace_data_key_path();C=A.read_many_values((B,));return C.get(A.read_key_path(B),{})or{}
	def write_merged_configuration_workspace_data(D,value):
		A=value
		if not A or F(A)<1:return B
		E=D.read_configuration_workspace_data_key_path();D.write_many_values({E:A});return C
	def read_refresh_data(A):B=A.read_refresh_data_key_path();C=A.read_many_values((B,));return C.get(A.read_key_path(B),{})or{}
	def write_refresh_data(D,value):
		A=value
		if not A or F(A)<1:return B
		E=D.read_refresh_data_key_path();D.write_many_values({E:A});return C