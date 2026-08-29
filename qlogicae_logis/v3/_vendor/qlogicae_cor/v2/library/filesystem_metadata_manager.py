from __future__ import annotations
C=None
__all__='FilesystemMetadataManager',
from typing import TYPE_CHECKING as D,Any,cast
if D:0
E=C
B=C
def A():global A;global B;from pathlib import Path;from.filesystem_metadata import FilesystemMetadata as D;E=Path;B=D;A=lambda:C
class F:
	def __init__(B):A()
	def read_metadata(C,filesystem_path):A=E(filesystem_path).stat();return cast(B,B(mode=A.st_mode,inode=A.st_ino,device=A.st_dev,hard_links=A.st_nlink,uid=A.st_uid,gid=A.st_gid,size=A.st_size,access_time=A.st_atime,modification_time=A.st_mtime,status_change_time=A.st_ctime))