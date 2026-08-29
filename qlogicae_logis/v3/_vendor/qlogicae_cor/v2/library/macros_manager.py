from __future__ import annotations
T="'values' must be a mapping"
M=tuple
S=KeyError
R=reversed
K=property
P=False
O=set
D=None
F=ValueError
E=TypeError
C=str
A=isinstance
__all__='MacrosManager',
from typing import Any
B=D
G=D
L=D
H=D
I=D
def J():global J;global B;global G;global L;global H;global I;import re;from collections.abc import Mapping as A;from pathlib import Path;from.singleton_manager import SingletonManager as C;from.text_encoding_manager import TextEncodingManager as E;B=re;G=Path;L=A;H=C;I=E;J=lambda:D
class N:
	__slots__='_selected_identifier_pattern','_selected_macros_pattern','_text_encoding_manager'
	def __init__(A):J();A._text_encoding_manager=H.get_singleton(I);A._selected_identifier_pattern=B.compile('^[A-Za-z0-9._-]+$');A._selected_macros_pattern=B.compile('\\$\\{\\{\\s*([A-Za-z0-9._-]+)\\s*\\}\\}')
	@K
	def selected_identifier_pattern(self):return self._selected_identifier_pattern
	@selected_identifier_pattern.setter
	def selected_identifier_pattern(self,value):self._selected_identifier_pattern=B.compile(value)
	@K
	def selected_macros_pattern(self):return self._selected_macros_pattern
	@selected_macros_pattern.setter
	def selected_macros_pattern(self,value):self._selected_macros_pattern=B.compile(value)
	def _resolve_value(B,value):
		A=value
		if callable(A):return A()
		return A
	def resolve_many(K,values):
		H=values
		if not A(H,L):raise E(T)
		for B in H:
			if not A(B,C):raise E('macro names must be strings')
			if not K._selected_identifier_pattern.fullmatch(B):raise F(f"invalid macro name: '{B}'")
		D={}
		for P in H:
			if P in D:continue
			I=[P];J=O()
			while I:
				B=I[-1]
				if B in D:I.pop();J.discard(B);continue
				if B not in H:raise F(f"key path '{B}' is an unknown macro")
				M=H[B]
				if not A(M,C):D[B]=K._resolve_value(M);I.pop();J.discard(B);continue
				J.add(B);N=[]
				for Q in K._selected_macros_pattern.finditer(M):
					G=Q.group(1)
					if G in D:continue
					if G not in H:raise F(f"key path '{B}' references unknown macro '{G}'")
					if G in J:raise F(f"circular macro reference: '{B}' -> '{G}'")
					if G not in N:N.append(G)
				if N:I.extend(R(N));continue
				def S(match):A=match.group(1);return C(D[A])
				D[B]=K._selected_macros_pattern.sub(S,M);I.pop();J.remove(B)
		return D
	def resolve_one(M,key,values,cache,stack):
		K=stack;J=values;G=key;D=cache
		if not A(G,C):raise E("'key' must be a string")
		if not A(J,L):raise E(T)
		if not A(D,dict):raise E("'cache' must be a dictionary")
		if not A(K,O):raise E("'stack' must be a set")
		if G not in J:raise S(f"unknown macro '{G}'")
		if G in D:return D[G]
		N=[(G,P)]
		while N:
			B,U=N.pop()
			if B in D:continue
			if not U:
				if B in K:raise F(f"key path '{B}' is a circular reference")
				if B not in J:raise F(f"key path '{B}' is an unknown macro")
				H=J[B]
				if not A(H,C):D[B]=M._resolve_value(H);continue
				K.add(B);N.append((B,True));Q=[]
				for V in M._selected_macros_pattern.finditer(H):
					I=V.group(1)
					if I not in J:raise S(f"macro '{B}' references unknown macro '{I}'")
					if I in K:raise F(f"circular macro reference: '{B}' -> '{I}'")
					if I not in D:
						if I not in Q:Q.append(I)
				N.extend((A,P)for A in R(Q))
			else:
				H=J[B]
				if not A(H,C):D[B]=M._resolve_value(H)
				else:D[B]=M._selected_macros_pattern.sub(lambda match:C(D[match.group(1)]),H)
				K.remove(B)
		return D[G]
	def parse_many(A,values,resolved):return A.parse_one(values,resolved)
	def parse_one(D,value,resolved):
		E=resolved;B=value
		if A(B,C):
			def F(match):
				A=match;B=A.group(1)
				if B not in E:return C(A.group(0))
				return C(D._resolve_value(E[B]))
			return D._selected_macros_pattern.sub(F,B)
		if A(B,dict):return{A:D.parse_one(B,E)for(A,B)in B.items()}
		if A(B,list):return[D.parse_one(A,E)for A in B]
		if A(B,M):return M(D.parse_one(A,E)for A in B)
		if A(B,O):return{D.parse_one(A,E)for A in B}
		return B
	def parse_filesystem(F,filesystem_path,workspace_macros):
		I=workspace_macros;K=F._text_encoding_manager.selected_encoding;M=G(filesystem_path)
		for(H,N,O)in M.walk(top_down=P):
			H=G(H)
			for Q in O:
				B=H/Q
				try:L=B.read_text(encoding=K)
				except UnicodeDecodeError:pass
				else:
					J=F.parse_one(L,I)
					if not A(J,C):raise E('parsed file data must be a string')
					if J!=L:B.write_text(J,encoding=K)
				D=F.parse_one(B.name,I)
				if not A(D,C):raise E('parsed file name must be a string')
				if D!=B.name:B=B.rename(B.with_name(D))
			for R in N:
				B=H/R;D=F.parse_one(B.name,I)
				if not A(D,C):raise E('parsed directory name must be a string')
				if D!=B.name:B.rename(B.with_name(D))
		return True