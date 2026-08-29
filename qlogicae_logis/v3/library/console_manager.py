from __future__ import annotations
j='selections'
i='setup'
h='-op'
g='View value cache.'
f='View disk cache.'
e='view'
d='value-cache'
c='disk-cache'
P='Show list information.'
O='list'
N='append'
M='key_paths'
L='-kp'
K='--key-path'
J='targets'
I='-t'
H='--target'
G='+'
D=None
C=str
B=''
A=True
from typing import Any
from..library.decorator_manager import DecoratorManager as k
__all__='ConsoleManager'
Q=D
R=D
E=D
S=D
T=D
U=D
V=D
W=D
X=D
Y=D
Z=D
a=D
F=k
def b():global b;global Q;global R;global E;global S;global T;global V;global U;global W;global X;global Y;global Z;global a;import argparse as A;from..library import command_about_manager as B,command_database_manager as C,command_debug_manager as F,command_filesystem_manager as G,command_template_manager as H,command_workflow_manager as I,command_workspace_manager as J,database_manager as K,import_manager as L,task_manager as M,value_cache_database_manager as N;Q=A;R=M.TaskManager;E=L.ImportManager;S=K.DatabaseManager;a=N.ValueCacheDatabaseManager;T=B.CommandAboutManager;V=C.CommandDatabaseManager;U=F.CommandDebugManager;W=I.CommandWorkflowManager;X=H.CommandTemplateManager;Y=J.CommandWorkspaceManager;Z=G.CommandFilesystemManager;b=lambda:D
class l:
	__slots__='_application','_commands','_command_about_manager','_command_database_manager','_command_debug_manager','_command_filesystem_manager','_command_template_manager','_command_workflow_manager','_command_workspace_manager','_task_manager','_import_manager','_database_manager','_value_cache_database_manager'
	def __init__(A):b();A._command_about_manager=E.read_singleton(T);A._command_database_manager=E.read_singleton(V);A._command_debug_manager=E.read_singleton(U);A._command_filesystem_manager=E.read_singleton(Z);A._command_template_manager=E.read_singleton(X);A._command_workflow_manager=E.read_singleton(W);A._command_workspace_manager=E.read_singleton(Y);A._task_manager=E.read_singleton(R);A._import_manager=E.read_singleton(E);A._database_manager=E.read_singleton(S);A._value_cache_database_manager=E.read_singleton(a);A._application=Q.ArgumentParser();A._commands=A._application.add_subparsers(dest='command',metavar=B)
	@F.multi_task_decorator
	def run(self):
		B=self;B.setup()
		try:
			C=B.read_arguments();E=getattr(C,'command_handler',D)
			if E is not D:E(C)
			else:B._application.print_help()
		finally:0
		return A
	@F.multi_task_decorator
	def setup_about_command(self):
		def C(arguments):self._command_about_manager.run_command_about_version();return A
		D=self._commands.add_parser('about',help='Build information.');E=D.add_subparsers(dest='about_command',metavar=B);F=E.add_parser('version',help='Current version on pip.');F.set_defaults(command_handler=C);return A
	@F.multi_task_decorator
	def setup_database_command(self):
		D=self
		def J(arguments):D._command_database_manager.run_command_database_view_disk(key_paths=arguments.key_paths or[]);return A
		def O(arguments):D._command_database_manager.run_command_database_view_value(key_paths=arguments.key_paths or[]);return A
		def P(arguments):D._command_database_manager.run_command_database_clear_disk();return A
		def Q(arguments):D._command_database_manager.run_command_database_clear_value();return A
		R=D._commands.add_parser('database',help='Manage database.');E=R.add_subparsers(dest='database_command',metavar=B);S=E.add_parser(e,help='View database.');F=S.add_subparsers(dest='database_view_command',metavar=B);G=F.add_parser(c,help=f);G.add_argument(K,L,dest=M,action=N,default=[],type=C);G.set_defaults(command_handler=J);H=F.add_parser(d,help=g);H.add_argument(K,L,dest=M,action=N,default=[],type=C);H.set_defaults(command_handler=O);T=E.add_parser('clear',help='Clear database.');I=T.add_subparsers(dest='database_clear_command',metavar=B);U=I.add_parser(c,help='Clear disk cache.');U.set_defaults(command_handler=P);V=I.add_parser(d,help='Clear value cache.');V.set_defaults(command_handler=Q);return A
	@F.multi_task_decorator
	def setup_debug_command(self):
		D=self
		def H(arguments):D._command_debug_manager.run_command_debug_view_value_cache(key_paths=arguments.key_paths or[]);return A
		def I(arguments):D._command_debug_manager.run_command_debug_view_disk_cache(key_paths=arguments.key_paths or[]);return A
		J=D._commands.add_parser('debug',help='Manage debug.');O=J.add_subparsers(dest='debug_command',metavar=B);P=O.add_parser(e,help='View debug.');E=P.add_subparsers(dest='debug_view_command',metavar=B);F=E.add_parser(d,help=g);F.add_argument(K,L,dest=M,action=N,default=[],type=C,help=B);F.set_defaults(command_handler=H);G=E.add_parser(c,help=f);G.add_argument(K,L,dest=M,action=N,default=[],type=C,help=B);G.set_defaults(command_handler=I);return A
	@F.multi_task_decorator
	def setup_filesystem_command(self):
		Z='clean';Y='source_path';X='-sp';W='--source-path';Q='target_paths';K='-tp';F='--target-path';D=self
		def a(arguments):B=arguments;D._command_filesystem_manager.run_command_filesystem_copy(source_path=B.source_path,target_paths=B.target_paths or[]);return A
		def b(arguments):B=arguments;D._command_filesystem_manager.run_command_filesystem_move(source_path=B.source_path,target_path=B.target_path);return A
		def c(arguments):B=arguments;D._command_filesystem_manager.run_command_filesystem_rename(old_path=B.old_path,new_path=B.new_path);return A
		def d(arguments):D._command_filesystem_manager.run_command_filesystem_tree_setup(target_paths=arguments.target_paths or[]);return A
		def e(arguments):D._command_filesystem_manager.run_command_filesystem_clean_path(target_paths=arguments.target_paths or[]);return A
		def f(arguments):D._command_filesystem_manager.run_command_filesystem_clean_selection(targets=arguments.targets or[]);return A
		def g(arguments):D._command_filesystem_manager.run_command_filesystem_clean_list_included();return A
		def j(arguments):D._command_filesystem_manager.run_command_filesystem_clean_list_excluded();return A
		k=D._commands.add_parser('filesystem',help='Filesystem management.');E=k.add_subparsers(dest='filesystem_command',metavar=B);L=E.add_parser('copy',help='Copy filesystem entities.');L.add_argument(W,X,dest=Y,required=A,type=C,help=B);L.add_argument(F,K,dest=Q,required=A,nargs=G,type=C,help=B);L.set_defaults(command_handler=a);M=E.add_parser('move',help='Move filesystem entities.');M.add_argument(W,X,dest=Y,required=A,type=C,help=B);M.add_argument(F,K,dest='target_path',required=A,type=C,help=B);M.set_defaults(command_handler=b);N=E.add_parser('rename',help='Rename filesystem entities.');N.add_argument('--old-path',h,dest='old_path',required=A,type=C,help=B);N.add_argument('--new-path','-np',dest='new_path',required=A,type=C,help=B);N.set_defaults(command_handler=c);l=E.add_parser('tree',help='Filesystem tree management.');m=l.add_subparsers(dest='filesystem_tree_command',metavar=B);R=m.add_parser(i,help='Setup filesystem tree.');R.add_argument(F,K,dest=Q,required=A,nargs=G,type=C,help=B);R.set_defaults(command_handler=d);n=E.add_parser(Z,help='Safe filesystem cleaning.');S=n.add_subparsers(dest='filesystem_clean_command',metavar=B);T=S.add_parser('path',help='Filesystem path cleaning.');T.add_argument(F,K,dest=Q,required=A,nargs=G,type=C,help=B);T.set_defaults(command_handler=e);U=S.add_parser('selection',help='Filesystem paths based on a selection.');U.add_argument(H,I,dest=J,nargs=G,help=B);U.set_defaults(command_handler=f);o=E.add_parser(O,help='Filesystem list management.');p=o.add_subparsers(dest='filesystem_list_command',metavar=B);q=p.add_parser(Z,help=P);V=q.add_subparsers(dest='filesystem_list_clean_command',metavar=B);r=V.add_parser('included',help='Show selections and whitelisted filesystem paths.');r.set_defaults(command_handler=g);s=V.add_parser('excluded',help='Show blacklisted filesystem paths.');s.set_defaults(command_handler=j);return A
	@F.multi_task_decorator
	def setup_workspace_command(self):
		D=self
		def M(arguments):D._command_workspace_manager.run_command_workspace_export(targets=arguments.targets or[]);return A
		def N(arguments):B=arguments;D._command_workspace_manager.run_command_workspace_import(input_path=B.input_path or[],output_path=B.output_path or[]);return A
		def Q(arguments):D._command_workspace_manager.run_command_workspace_replenish();return A
		def R(arguments):D._command_workspace_manager.run_command_workspace_list_exports();return A
		def S(arguments):D._command_workspace_manager.run_command_workspace_setup();return A
		def T(arguments):D._command_workspace_manager.run_command_workspace_install(targets=arguments.targets or[]);return A
		U=D._commands.add_parser('workspace',help='Manage workspaces.');E=U.add_subparsers(dest='workspace_command',metavar=B);K=E.add_parser('export',help='Create workspaces archive file.');K.add_argument(H,I,dest=J,nargs=G,type=C,default=[],help=B);K.set_defaults(command_handler=M);F=E.add_parser('import',help='Extract workspace archive file.');F.add_argument('--input-path','-ip',dest='input_path',default=B,type=C,help=B);F.add_argument('--output-path',h,dest='output_path',default=B,type=C,help=B);F.set_defaults(command_handler=N);V=E.add_parser(i,help='Complete workspace setup.');V.set_defaults(command_handler=S);W=E.add_parser('replenish',help='Filesystem replenishment.');W.set_defaults(command_handler=Q);L=E.add_parser('install',help='Initial or filesystem replenishment.');L.add_argument(H,I,dest=J,nargs='*',type=C,help=B,default=[]);L.set_defaults(command_handler=T);X=E.add_parser(O,help=P);Y=X.add_subparsers(dest='workspace_list_command',metavar=B);Z=Y.add_parser('exports',help='List of exportable workspaces.');Z.set_defaults(command_handler=R);return A
	def setup_template_command(D):
		def K(arguments):D._command_template_manager.run_command_template_apply(targets=arguments.targets or[]);return A
		def L(arguments):D._command_template_manager.run_command_template_list_selections();return A
		M=D._commands.add_parser('template',help='Apply templates.');E=M.add_subparsers(dest='template_command',metavar=B);F=E.add_parser('apply',help='Apply filesystem templates.');F.add_argument(H,I,dest=J,nargs=G,default=[],type=C,help=B);F.set_defaults(command_handler=K);N=E.add_parser(O,help=P);Q=N.add_subparsers(dest='template_list_command',metavar=B);R=Q.add_parser(j,help='Show a list of template selections.');R.set_defaults(command_handler=L);return A
	@F.multi_task_decorator
	def setup_workflow_command(self):
		D=self
		def K(arguments):D._command_workflow_manager.run_command_workflow_run(targets=arguments.targets or[]);return A
		def L(arguments):D._command_workflow_manager.run_command_workflow_list_selections();return A
		M=D._commands.add_parser('workflow',help='Run workflows.');E=M.add_subparsers(dest='workflow_command',metavar=B);F=E.add_parser('run',help='Run workflow selections.');F.add_argument(H,I,dest=J,nargs=G,default=[],type=C,help=B);F.set_defaults(command_handler=K);N=E.add_parser(O,help=P);Q=N.add_subparsers(dest='workflow_list_command',metavar=B);R=Q.add_parser(j,help='Show a list of defined workflows.');R.set_defaults(command_handler=L);return A
	@F.multi_task_decorator
	def read_arguments(self):A=self._application.parse_args();return A
	@F.multi_task_decorator
	def setup(self):B=self;B.setup_about_command();B.setup_workflow_command();B.setup_workspace_command();B.setup_filesystem_command();B.setup_template_command();B.setup_database_command();B.setup_debug_command();return A
	@F.multi_task_decorator
	def shutdown(self):self._task_manager.run_task_full_shutdown();return A