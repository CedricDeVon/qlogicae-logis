from __future__ import annotations
__all__='FilesystemMetadataManager',
from typing import TYPE_CHECKING,Any,cast
if TYPE_CHECKING:0
_Path=None
_FilesystemMetadata=None
def _handle_dynamic_imports():global _handle_dynamic_imports;global _FilesystemMetadata;from pathlib import Path;from.filesystem_metadata import FilesystemMetadata as A;B=Path;_FilesystemMetadata=A;_handle_dynamic_imports=lambda:None
class FilesystemMetadataManager:
	def __init__(A):_handle_dynamic_imports()
	def read_metadata(B,filesystem_path):A=_Path(filesystem_path).stat();return cast(_FilesystemMetadata,_FilesystemMetadata(mode=A.st_mode,inode=A.st_ino,device=A.st_dev,hard_links=A.st_nlink,uid=A.st_uid,gid=A.st_gid,size=A.st_size,access_time=A.st_atime,modification_time=A.st_mtime,status_change_time=A.st_ctime))