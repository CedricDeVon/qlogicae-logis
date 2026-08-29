_A=None
__all__=['Mark','YAMLError','MarkedYAMLError']
class Mark:
	def __init__(A,name,index,line,column,buffer,pointer):A.name=name;A.index=index;A.line=line;A.column=column;A.buffer=buffer;A.pointer=pointer
	def get_snippet(A,indent=4,max_length=75):
		I=' ... ';H='\x00\r\n\x85\u2028\u2029';F=max_length;E=indent
		if A.buffer is _A:return
		D='';B=A.pointer
		while B>0 and A.buffer[B-1]not in H:
			B-=1
			if A.pointer-B>F/2-1:D=I;B+=5;break
		G='';C=A.pointer
		while C<len(A.buffer)and A.buffer[C]not in H:
			C+=1
			if C-A.pointer>F/2-1:G=I;C-=5;break
		J=A.buffer[B:C];return' '*E+D+J+G+'\n'+' '*(E+A.pointer-B+len(D))+'^'
	def __str__(A):
		B=A.get_snippet();C='  in "%s", line %d, column %d'%(A.name,A.line+1,A.column+1)
		if B is not _A:C+=':\n'+B
		return C
class YAMLError(Exception):0
class MarkedYAMLError(YAMLError):
	def __init__(A,context=_A,context_mark=_A,problem=_A,problem_mark=_A,note=_A):A.context=context;A.context_mark=context_mark;A.problem=problem;A.problem_mark=problem_mark;A.note=note
	def __str__(A):
		B=[]
		if A.context is not _A:B.append(A.context)
		if A.context_mark is not _A and(A.problem is _A or A.problem_mark is _A or A.context_mark.name!=A.problem_mark.name or A.context_mark.line!=A.problem_mark.line or A.context_mark.column!=A.problem_mark.column):B.append(str(A.context_mark))
		if A.problem is not _A:B.append(A.problem)
		if A.problem_mark is not _A:B.append(str(A.problem_mark))
		if A.note is not _A:B.append(A.note)
		return'\n'.join(B)