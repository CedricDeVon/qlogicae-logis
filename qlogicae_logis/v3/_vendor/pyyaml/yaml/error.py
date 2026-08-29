B=None
__all__=['Mark','YAMLError','MarkedYAMLError']
class Mark:
	def __init__(A,name,index,line,column,buffer,pointer):A.name=name;A.index=index;A.line=line;A.column=column;A.buffer=buffer;A.pointer=pointer
	def get_snippet(A,indent=4,max_length=75):
		J=' ... ';I='\x00\r\n\x85\u2028\u2029';G=max_length;F=indent
		if A.buffer is B:return
		E='';C=A.pointer
		while C>0 and A.buffer[C-1]not in I:
			C-=1
			if A.pointer-C>G/2-1:E=J;C+=5;break
		H='';D=A.pointer
		while D<len(A.buffer)and A.buffer[D]not in I:
			D+=1
			if D-A.pointer>G/2-1:H=J;D-=5;break
		K=A.buffer[C:D];return' '*F+E+K+H+'\n'+' '*(F+A.pointer-C+len(E))+'^'
	def __str__(A):
		C=A.get_snippet();D='  in "%s", line %d, column %d'%(A.name,A.line+1,A.column+1)
		if C is not B:D+=':\n'+C
		return D
class YAMLError(Exception):0
class MarkedYAMLError(YAMLError):
	def __init__(A,context=B,context_mark=B,problem=B,problem_mark=B,note=B):A.context=context;A.context_mark=context_mark;A.problem=problem;A.problem_mark=problem_mark;A.note=note
	def __str__(A):
		C=[]
		if A.context is not B:C.append(A.context)
		if A.context_mark is not B and(A.problem is B or A.problem_mark is B or A.context_mark.name!=A.problem_mark.name or A.context_mark.line!=A.problem_mark.line or A.context_mark.column!=A.problem_mark.column):C.append(str(A.context_mark))
		if A.problem is not B:C.append(A.problem)
		if A.problem_mark is not B:C.append(str(A.problem_mark))
		if A.note is not B:C.append(A.note)
		return'\n'.join(C)