import sys

import click
from flask.cli import with_appcontext

from flask_moreshell.shells import BPythonShell
from flask_moreshell.shells import IpythonShell
from flask_moreshell.shells import PTPythonShell
from flask_moreshell.shells import PythonShell


shells = {
    "ipython": IpythonShell,
    "bpython": BPythonShell,
    "ptpython": PTPythonShell,
    "python": PythonShell,
}


@click.command(context_settings=dict(ignore_unknown_options=True))
@click.option(
    "--shelltype",
    type=click.Choice(["ipython", "bpython", "ptpython", "python"]),
    default=None,
)
@with_appcontext
def shell(shelltype: str) -> None:
    """Run `flask shell` command with IPython, BPython, PTPython.

    If you have IPython, PYTPython, or BPython installed, run them with your
    Flask application.
    if none of them are installed, this loads the default python shell.

    you can specify type of shell with --shelltype option.

    :param shelltype: type of shell to use.
    """

    def try_load_shell(_shelltype: str) -> None:
        shell_class = shells.get(_shelltype)
        shell_class().load()

    # If the user specifies a shell type, try to load it
    if shelltype:
        try_load_shell(shelltype)
    else:
        preferred_shells = ["ipython", "bpython", "ptpython", "python"]
        for shelltype in preferred_shells:
            try:
                try_load_shell(shelltype)
                break
            except ModuleNotFoundError:
                continue
    if not shelltype:
        print("No shell type is installed or recognized on your system.")
        sys.exit(1)
