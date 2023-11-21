import importlib
import sys

import click
from flask.cli import with_appcontext


@click.command(context_settings=dict(ignore_unknown_options=True))
@click.option(
    "--shelltype",
    type=click.Choice(["ipython", "bpython", "ptpython", "python"]),
    default=None,
)
@with_appcontext  # type: ignore
def shell(shelltype: str) -> None:
    """Run `flask shell` command with IPython, BPython, PTPython.

    If you have IPython, PYTPython, or BPython installed, run them with your
    Flask application.
    if none of them are installed, this loads the default python shell.

    you can specify type of shell with --shelltype option.

    :param shelltype: type of shell to use.
    """
    shell_classes = {
        "ipython": "IPythonShell",
        "bpython": "BPythonShell",
        "ptpython": "PTPythonShell",
        "python": "PythonShell",
    }

    if shelltype:
        shell_class = shell_classes[shelltype]
        try:
            shell_module = importlib.import_module(
                f"flask_moreshell.shells.{shelltype}_shell"
            )
            shell_class = getattr(shell_module, shell_class)
            shell_class().load()
        except ModuleNotFoundError as e:
            print(e)
    else:
        for shell_class in shell_classes.keys():
            try:
                shell_module = importlib.import_module(
                    f"flask_moreshell.shells.{shell_class}_shell"
                )
                shell_class = getattr(shell_module, shell_classes[shell_class])
                shell_class().load()
                sys.exit(0)
            except ModuleNotFoundError:
                continue
