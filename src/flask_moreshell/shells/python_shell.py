import code
import sys

from flask_moreshell.shells import BaseShell


class PythonShell(BaseShell):
    def get_shell_name(self) -> str:
        return "Python"

    def get_shell_version(self) -> str:
        return sys.version

    def load(self) -> None:
        ctx = {}  # type: ignore
        self.load_context(ctx)

        interactive_hook = getattr(sys, "__interactivehook__", None)
        if interactive_hook is not None:
            try:
                import readline
                from rlcompleter import Completer
            except ImportError:
                pass
            else:
                readline.set_completer(Completer(ctx).complete)
            interactive_hook()
        code.interact(local=ctx, banner=self.get_banner())
