import sys
from importlib.metadata import version

from ptpython.repl import embed

from flask_moreshell.shells import BaseShell


class PTPythonShell(BaseShell):
    def get_shell_name(self) -> str:
        return "PTPython"

    def get_shell_version(self) -> str:
        return version("ptpython")

    def load(self) -> None:
        ctx = {}  # type: ignore
        self.load_context(ctx)
        sys.stdout.write(f"{self.get_banner()}\n")
        embed(globals=ctx)
