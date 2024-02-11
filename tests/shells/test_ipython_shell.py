import pytest

from flask_moreshell.shells.ipython_shell import IPythonShell


@pytest.fixture
def ipython_shell() -> IPythonShell:
    return IPythonShell()


def test_get_shell_name(ipython_shell: IPythonShell) -> None:
    assert ipython_shell.get_shell_name() == "IPython"


def test_get_shell_version(ipython_shell: IPythonShell) -> None:
    from IPython import __version__

    assert ipython_shell.get_shell_version() == __version__
