import sys
from importlib import import_module

import click
from flask.cli import with_appcontext

from flask_moreshell.shells.base_shell import BaseShell


def _get_shell_instance(shelltype: str, shell_classes: dict[str, str]) -> BaseShell:
    shell_class_name = shell_classes[shelltype]
    shell_module = import_module(f"flask_moreshell.shells.{shelltype}_shell")
    shell_class: type[BaseShell] = getattr(shell_module, shell_class_name)
    return shell_class()


def _find_available_shell(shell_classes: dict[str, str]) -> BaseShell:
    for shell_class in shell_classes.keys():
        try:
            return _get_shell_instance(shell_class, shell_classes)
        except ModuleNotFoundError:
            continue


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
        _shell = _get_shell_instance(shelltype, shell_classes)
        _shell.load()
        sys.exit(0)
    else:
        _shell = _find_available_shell(shell_classes)
        _shell.load()
        sys.exit(0)
