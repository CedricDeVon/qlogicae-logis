from __future__ import annotations
_Q='selections'
_P='View value cache.'
_O='View disk cache.'
_N='value-cache'
_M='disk-cache'
_L='Show list information.'
_K='list'
_J='append'
_I='key_paths'
_H='-kp'
_G='--key-path'
_F='targets'
_E='-t'
_D='--target'
_C='+'
_B=None
_A=True
from typing import Any
from..library.decorator_manager import DecoratorManager
__all__='ConsoleManager'
_argparse=_B
_TaskManager=_B
_ImportManager=_B
_DatabaseManager=_B
_CommandAboutManager=_B
_CommandDebugManager=_B
_CommandDatabaseManager=_B
_CommandWorkflowManager=_B
_CommandTemplateManager=_B
_CommandWorkspaceManager=_B
_CommandFilesystemManager=_B
_ValueCacheDatabaseManager=_B
_DecoratorManager=DecoratorManager
def _handle_dynamic_imports():global _handle_dynamic_imports;global _argparse;global _TaskManager;global _ImportManager;global _DatabaseManager;global _CommandAboutManager;global _CommandDatabaseManager;global _CommandDebugManager;global _CommandWorkflowManager;global _CommandTemplateManager;global _CommandWorkspaceManager;global _CommandFilesystemManager;global _ValueCacheDatabaseManager;import argparse as A;from..library import command_about_manager as B,command_database_manager as C,command_debug_manager as D,command_filesystem_manager as E,command_template_manager as F,command_workflow_manager as G,command_workspace_manager as H,database_manager as I,import_manager as J,task_manager as K,value_cache_database_manager as L;_argparse=A;_TaskManager=K.TaskManager;_ImportManager=J.ImportManager;_DatabaseManager=I.DatabaseManager;_ValueCacheDatabaseManager=L.ValueCacheDatabaseManager;_CommandAboutManager=B.CommandAboutManager;_CommandDatabaseManager=C.CommandDatabaseManager;_CommandDebugManager=D.CommandDebugManager;_CommandWorkflowManager=G.CommandWorkflowManager;_CommandTemplateManager=F.CommandTemplateManager;_CommandWorkspaceManager=H.CommandWorkspaceManager;_CommandFilesystemManager=E.CommandFilesystemManager;_handle_dynamic_imports=lambda:_B
class ConsoleManager:
	__slots__='_application','_commands','_command_about_manager','_command_database_manager','_command_debug_manager','_command_filesystem_manager','_command_template_manager','_command_workflow_manager','_command_workspace_manager','_task_manager','_import_manager','_database_manager','_value_cache_database_manager'
	def __init__(A):_handle_dynamic_imports();A._command_about_manager=_ImportManager.read_singleton(_CommandAboutManager);A._command_database_manager=_ImportManager.read_singleton(_CommandDatabaseManager);A._command_debug_manager=_ImportManager.read_singleton(_CommandDebugManager);A._command_filesystem_manager=_ImportManager.read_singleton(_CommandFilesystemManager);A._command_template_manager=_ImportManager.read_singleton(_CommandTemplateManager);A._command_workflow_manager=_ImportManager.read_singleton(_CommandWorkflowManager);A._command_workspace_manager=_ImportManager.read_singleton(_CommandWorkspaceManager);A._task_manager=_ImportManager.read_singleton(_TaskManager);A._import_manager=_ImportManager.read_singleton(_ImportManager);A._database_manager=_ImportManager.read_singleton(_DatabaseManager);A._value_cache_database_manager=_ImportManager.read_singleton(_ValueCacheDatabaseManager);A._application=_argparse.ArgumentParser();A._commands=A._application.add_subparsers(dest='command',metavar='')
	@_DecoratorManager.multi_task_decorator
	def run(self):
		A=self;A.setup()
		try:
			B=A.read_arguments();C=getattr(B,'command_handler',_B)
			if C is not _B:C(B)
			else:A._application.print_help()
		finally:0
		return _A
	@_DecoratorManager.multi_task_decorator
	def setup_about_command(self):
		def A(arguments):self._command_about_manager.run_command_about_version();return _A
		B=self._commands.add_parser('about',help='Build information.');C=B.add_subparsers(dest='about_command',metavar='');D=C.add_parser('version',help='Current version on pip.');D.set_defaults(command_handler=A);return _A
	@_DecoratorManager.multi_task_decorator
	def setup_database_command(self):
		A=self
		def G(arguments):A._command_database_manager.run_command_database_view_disk(key_paths=arguments.key_paths or[]);return _A
		def H(arguments):A._command_database_manager.run_command_database_view_value(key_paths=arguments.key_paths or[]);return _A
		def I(arguments):A._command_database_manager.run_command_database_clear_disk();return _A
		def J(arguments):A._command_database_manager.run_command_database_clear_value();return _A
		K=A._commands.add_parser('database',help='Manage database.');B=K.add_subparsers(dest='database_command',metavar='');L=B.add_parser('view',help='View database.');C=L.add_subparsers(dest='database_view_command',metavar='');D=C.add_parser(_M,help=_O);D.add_argument(_G,_H,dest=_I,action=_J,default=[],type=str);D.set_defaults(command_handler=G);E=C.add_parser(_N,help=_P);E.add_argument(_G,_H,dest=_I,action=_J,default=[],type=str);E.set_defaults(command_handler=H);M=B.add_parser('clear',help='Clear database.');F=M.add_subparsers(dest='database_clear_command',metavar='');N=F.add_parser(_M,help='Clear disk cache.');N.set_defaults(command_handler=I);O=F.add_parser(_N,help='Clear value cache.');O.set_defaults(command_handler=J);return _A
	@_DecoratorManager.multi_task_decorator
	def setup_debug_command(self):
		A=self
		def E(arguments):A._command_debug_manager.run_command_debug_view_value_cache(key_paths=arguments.key_paths or[]);return _A
		def F(arguments):A._command_debug_manager.run_command_debug_view_disk_cache(key_paths=arguments.key_paths or[]);return _A
		G=A._commands.add_parser('debug',help='Manage debug.');H=G.add_subparsers(dest='debug_command',metavar='');I=H.add_parser('view',help='View debug.');B=I.add_subparsers(dest='debug_view_command',metavar='');C=B.add_parser(_N,help=_P);C.add_argument(_G,_H,dest=_I,action=_J,default=[],type=str,help='');C.set_defaults(command_handler=E);D=B.add_parser(_M,help=_O);D.add_argument(_G,_H,dest=_I,action=_J,default=[],type=str,help='');D.set_defaults(command_handler=F);return _A
	@_DecoratorManager.multi_task_decorator
	def setup_filesystem_command(self):
		Q='clean';P='source_path';O='-sp';N='--source-path';H='target_paths';D='-tp';C='--target-path';A=self
		def R(arguments):B=arguments;A._command_filesystem_manager.run_command_filesystem_copy(source_path=B.source_path,target_paths=B.target_paths or[]);return _A
		def S(arguments):B=arguments;A._command_filesystem_manager.run_command_filesystem_move(source_path=B.source_path,target_path=B.target_path);return _A
		def T(arguments):B=arguments;A._command_filesystem_manager.run_command_filesystem_rename(old_path=B.old_path,new_path=B.new_path);return _A
		def U(arguments):A._command_filesystem_manager.run_command_filesystem_tree_setup(target_paths=arguments.target_paths or[]);return _A
		def V(arguments):A._command_filesystem_manager.run_command_filesystem_clean_path(target_paths=arguments.target_paths or[]);return _A
		def W(arguments):A._command_filesystem_manager.run_command_filesystem_clean_selection(targets=arguments.targets or[]);return _A
		def X(arguments):A._command_filesystem_manager.run_command_filesystem_clean_list_included();return _A
		def Y(arguments):A._command_filesystem_manager.run_command_filesystem_clean_list_excluded();return _A
		Z=A._commands.add_parser('filesystem',help='Filesystem management.');B=Z.add_subparsers(dest='filesystem_command',metavar='');E=B.add_parser('copy',help='Copy filesystem entities.');E.add_argument(N,O,dest=P,required=_A,type=str,help='');E.add_argument(C,D,dest=H,required=_A,nargs=_C,type=str,help='');E.set_defaults(command_handler=R);F=B.add_parser('move',help='Move filesystem entities.');F.add_argument(N,O,dest=P,required=_A,type=str,help='');F.add_argument(C,D,dest='target_path',required=_A,type=str,help='');F.set_defaults(command_handler=S);G=B.add_parser('rename',help='Rename filesystem entities.');G.add_argument('--old-path','-op',dest='old_path',required=_A,type=str,help='');G.add_argument('--new-path','-np',dest='new_path',required=_A,type=str,help='');G.set_defaults(command_handler=T);a=B.add_parser('tree',help='Filesystem tree management.');b=a.add_subparsers(dest='filesystem_tree_command',metavar='');I=b.add_parser('setup',help='Setup filesystem tree.');I.add_argument(C,D,dest=H,required=_A,nargs=_C,type=str,help='');I.set_defaults(command_handler=U);c=B.add_parser(Q,help='Safe filesystem cleaning.');J=c.add_subparsers(dest='filesystem_clean_command',metavar='');K=J.add_parser('path',help='Filesystem path cleaning.');K.add_argument(C,D,dest=H,required=_A,nargs=_C,type=str,help='');K.set_defaults(command_handler=V);L=J.add_parser('selection',help='Filesystem paths based on a selection.');L.add_argument(_D,_E,dest=_F,nargs=_C,help='');L.set_defaults(command_handler=W);d=B.add_parser(_K,help='Filesystem list management.');e=d.add_subparsers(dest='filesystem_list_command',metavar='');f=e.add_parser(Q,help=_L);M=f.add_subparsers(dest='filesystem_list_clean_command',metavar='');g=M.add_parser('included',help='Show selections and whitelisted filesystem paths.');g.set_defaults(command_handler=X);h=M.add_parser('excluded',help='Show blacklisted filesystem paths.');h.set_defaults(command_handler=Y);return _A
	@_DecoratorManager.multi_task_decorator
	def setup_workspace_command(self):
		A=self
		def F(arguments):A._command_workspace_manager.run_command_workspace_export(targets=arguments.targets or[]);return _A
		def G(arguments):B=arguments;A._command_workspace_manager.run_command_workspace_import(input_path=B.input_path or[],output_path=B.output_path or[]);return _A
		def H(arguments):A._command_workspace_manager.run_command_workspace_replenish();return _A
		def I(arguments):A._command_workspace_manager.run_command_workspace_list_exports();return _A
		def J(arguments):A._command_workspace_manager.run_command_workspace_setup();return _A
		def K(arguments):A._command_workspace_manager.run_command_workspace_install(targets=arguments.targets or[]);return _A
		L=A._commands.add_parser('workspace',help='Manage workspaces.');B=L.add_subparsers(dest='workspace_command',metavar='');D=B.add_parser('export',help='Create workspaces archive file.');D.add_argument(_D,_E,dest=_F,nargs=_C,type=str,default=[],help='');D.set_defaults(command_handler=F);C=B.add_parser('import',help='Extract workspace archive file.');C.add_argument('--input-path','-ip',dest='input_path',default='',type=str,help='');C.add_argument('--output-path','-op',dest='output_path',default='',type=str,help='');C.set_defaults(command_handler=G);M=B.add_parser('setup',help='Complete workspace setup.');M.set_defaults(command_handler=J);N=B.add_parser('replenish',help='Filesystem replenishment.');N.set_defaults(command_handler=H);E=B.add_parser('install',help='Initial or filesystem replenishment.');E.add_argument(_D,_E,dest=_F,nargs='*',type=str,help='',default=[]);E.set_defaults(command_handler=K);O=B.add_parser(_K,help=_L);P=O.add_subparsers(dest='workspace_list_command',metavar='');Q=P.add_parser('exports',help='List of exportable workspaces.');Q.set_defaults(command_handler=I);return _A
	def setup_template_command(A):
		def D(arguments):A._command_template_manager.run_command_template_apply(targets=arguments.targets or[]);return _A
		def E(arguments):A._command_template_manager.run_command_template_list_selections();return _A
		F=A._commands.add_parser('template',help='Apply templates.');B=F.add_subparsers(dest='template_command',metavar='');C=B.add_parser('apply',help='Apply filesystem templates.');C.add_argument(_D,_E,dest=_F,nargs=_C,default=[],type=str,help='');C.set_defaults(command_handler=D);G=B.add_parser(_K,help=_L);H=G.add_subparsers(dest='template_list_command',metavar='');I=H.add_parser(_Q,help='Show a list of template selections.');I.set_defaults(command_handler=E);return _A
	@_DecoratorManager.multi_task_decorator
	def setup_workflow_command(self):
		A=self
		def D(arguments):A._command_workflow_manager.run_command_workflow_run(targets=arguments.targets or[]);return _A
		def E(arguments):A._command_workflow_manager.run_command_workflow_list_selections();return _A
		F=A._commands.add_parser('workflow',help='Run workflows.');B=F.add_subparsers(dest='workflow_command',metavar='');C=B.add_parser('run',help='Run workflow selections.');C.add_argument(_D,_E,dest=_F,nargs=_C,default=[],type=str,help='');C.set_defaults(command_handler=D);G=B.add_parser(_K,help=_L);H=G.add_subparsers(dest='workflow_list_command',metavar='');I=H.add_parser(_Q,help='Show a list of defined workflows.');I.set_defaults(command_handler=E);return _A
	@_DecoratorManager.multi_task_decorator
	def read_arguments(self):A=self._application.parse_args();return A
	@_DecoratorManager.multi_task_decorator
	def setup(self):A=self;A.setup_about_command();A.setup_workflow_command();A.setup_workspace_command();A.setup_filesystem_command();A.setup_template_command();A.setup_database_command();A.setup_debug_command();return _A
	@_DecoratorManager.multi_task_decorator
	def shutdown(self):self._task_manager.run_task_full_shutdown();return _A