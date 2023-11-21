import sys
from importlib.metadata import version


try:
    from ptpython.repl import embed
except ModuleNotFoundError as e:
    raise ModuleNotFoundError("PTPython is not installed on your system.") from e

from flask_moreshell.shells.base_shell import BaseShell


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
