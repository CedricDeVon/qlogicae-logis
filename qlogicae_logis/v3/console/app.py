from __future__ import annotations
def main():from..library import console_manager as B,import_manager as C;A=C.ImportManager.read_singleton(B.ConsoleManager);A.run();A.shutdown()
if __name__=='__main__':main()