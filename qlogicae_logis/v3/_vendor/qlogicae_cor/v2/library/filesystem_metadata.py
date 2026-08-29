from __future__ import annotations
B=float
A=int
__all__='FilesystemMetadata',
from dataclasses import dataclass as C
@C(frozen=True,slots=True)
class D:mode:A;inode:A;device:A;hard_links:A;uid:A;gid:A;size:A;access_time:B;modification_time:B;status_change_time:B