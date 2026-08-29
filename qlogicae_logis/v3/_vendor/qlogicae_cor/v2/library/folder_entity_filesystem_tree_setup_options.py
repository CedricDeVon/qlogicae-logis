from dataclasses import dataclass as A,field
from typing import Any
__all__='FolderEntityFileSystemTreeSetupOptions',
@A(frozen=True,slots=True)
class B:name:str='folder';entities:list[Any]=field(default_factory=list)