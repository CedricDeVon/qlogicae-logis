from __future__ import annotations
_C="'values' must be a mapping"
_B=False
_A=None
__all__='MacrosManager',
from typing import Any
_re=_A
_Path=_A
_Mapping=_A
_SingletonManager=_A
_TextEncodingManager=_A
def _handle_dynamic_imports():global _handle_dynamic_imports;global _re;global _Path;global _Mapping;global _SingletonManager;global _TextEncodingManager;import re;from collections.abc import Mapping as A;from pathlib import Path;from.singleton_manager import SingletonManager as B;from.text_encoding_manager import TextEncodingManager as C;_re=re;_Path=Path;_Mapping=A;_SingletonManager=B;_TextEncodingManager=C;_handle_dynamic_imports=lambda:_A
class MacrosManager:
	__slots__='_selected_identifier_pattern','_selected_macros_pattern','_text_encoding_manager'
	def __init__(A):_handle_dynamic_imports();A._text_encoding_manager=_SingletonManager.get_singleton(_TextEncodingManager);A._selected_identifier_pattern=_re.compile('^[A-Za-z0-9._-]+$');A._selected_macros_pattern=_re.compile('\\$\\{\\{\\s*([A-Za-z0-9._-]+)\\s*\\}\\}')
	@property
	def selected_identifier_pattern(self):return self._selected_identifier_pattern
	@selected_identifier_pattern.setter
	def selected_identifier_pattern(self,value):self._selected_identifier_pattern=_re.compile(value)
	@property
	def selected_macros_pattern(self):return self._selected_macros_pattern
	@selected_macros_pattern.setter
	def selected_macros_pattern(self,value):self._selected_macros_pattern=_re.compile(value)
	def _resolve_value(B,value):
		A=value
		if callable(A):return A()
		return A
	def resolve_many(G,values):
		D=values
		if not isinstance(D,_Mapping):raise TypeError(_C)
		for A in D:
			if not isinstance(A,str):raise TypeError('macro names must be strings')
			if not G._selected_identifier_pattern.fullmatch(A):raise ValueError(f"invalid macro name: '{A}'")
		B={}
		for J in D:
			if J in B:continue
			E=[J];F=set()
			while E:
				A=E[-1]
				if A in B:E.pop();F.discard(A);continue
				if A not in D:raise ValueError(f"key path '{A}' is an unknown macro")
				H=D[A]
				if not isinstance(H,str):B[A]=G._resolve_value(H);E.pop();F.discard(A);continue
				F.add(A);I=[]
				for K in G._selected_macros_pattern.finditer(H):
					C=K.group(1)
					if C in B:continue
					if C not in D:raise ValueError(f"key path '{A}' references unknown macro '{C}'")
					if C in F:raise ValueError(f"circular macro reference: '{A}' -> '{C}'")
					if C not in I:I.append(C)
				if I:E.extend(reversed(I));continue
				def L(match):A=match.group(1);return str(B[A])
				B[A]=G._selected_macros_pattern.sub(L,H);E.pop();F.remove(A)
		return B
	def resolve_one(H,key,values,cache,stack):
		G=stack;F=values;C=key;B=cache
		if not isinstance(C,str):raise TypeError("'key' must be a string")
		if not isinstance(F,_Mapping):raise TypeError(_C)
		if not isinstance(B,dict):raise TypeError("'cache' must be a dictionary")
		if not isinstance(G,set):raise TypeError("'stack' must be a set")
		if C not in F:raise KeyError(f"unknown macro '{C}'")
		if C in B:return B[C]
		I=[(C,_B)]
		while I:
			A,K=I.pop()
			if A in B:continue
			if not K:
				if A in G:raise ValueError(f"key path '{A}' is a circular reference")
				if A not in F:raise ValueError(f"key path '{A}' is an unknown macro")
				D=F[A]
				if not isinstance(D,str):B[A]=H._resolve_value(D);continue
				G.add(A);I.append((A,True));J=[]
				for L in H._selected_macros_pattern.finditer(D):
					E=L.group(1)
					if E not in F:raise KeyError(f"macro '{A}' references unknown macro '{E}'")
					if E in G:raise ValueError(f"circular macro reference: '{A}' -> '{E}'")
					if E not in B:
						if E not in J:J.append(E)
				I.extend((A,_B)for A in reversed(J))
			else:
				D=F[A]
				if not isinstance(D,str):B[A]=H._resolve_value(D)
				else:B[A]=H._selected_macros_pattern.sub(lambda match:str(B[match.group(1)]),D)
				G.remove(A)
		return B[C]
	def parse_many(A,values,resolved):return A.parse_one(values,resolved)
	def parse_one(B,value,resolved):
		C=resolved;A=value
		if isinstance(A,str):
			def D(match):
				A=match;D=A.group(1)
				if D not in C:return str(A.group(0))
				return str(B._resolve_value(C[D]))
			return B._selected_macros_pattern.sub(D,A)
		if isinstance(A,dict):return{A:B.parse_one(D,C)for(A,D)in A.items()}
		if isinstance(A,list):return[B.parse_one(A,C)for A in A]
		if isinstance(A,tuple):return tuple(B.parse_one(A,C)for A in A)
		if isinstance(A,set):return{B.parse_one(A,C)for A in A}
		return A
	def parse_filesystem(C,filesystem_path,workspace_macros):
		E=workspace_macros;G=C._text_encoding_manager.selected_encoding;I=_Path(filesystem_path)
		for(D,J,K)in I.walk(top_down=_B):
			D=_Path(D)
			for L in K:
				A=D/L
				try:H=A.read_text(encoding=G)
				except UnicodeDecodeError:pass
				else:
					F=C.parse_one(H,E)
					if not isinstance(F,str):raise TypeError('parsed file data must be a string')
					if F!=H:A.write_text(F,encoding=G)
				B=C.parse_one(A.name,E)
				if not isinstance(B,str):raise TypeError('parsed file name must be a string')
				if B!=A.name:A=A.rename(A.with_name(B))
			for M in J:
				A=D/M;B=C.parse_one(A.name,E)
				if not isinstance(B,str):raise TypeError('parsed directory name must be a string')
				if B!=A.name:A.rename(A.with_name(B))
		return True