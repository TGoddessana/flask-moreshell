from flask_moreshell.shells.base_shell import BaseShell


try:
    import bpython  # type: ignore
except ModuleNotFoundError as e:
    raise ModuleNotFoundError("BPython is not installed on your system.") from e


class BPythonShell(BaseShell):
    def get_shell_name(self) -> str:
        return "BPython"

    def get_shell_version(self) -> str:
        return str(bpython.__version__)

    def load(self) -> None:
        ctx = {}  # type: ignore
        self.load_context(ctx)
        bpython.embed(banner=self.get_banner(), locals_=ctx)
