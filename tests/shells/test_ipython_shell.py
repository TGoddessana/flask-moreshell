import pytest

from flask_moreshell.shells import IpythonShell


@pytest.fixture
def ipython_shell():
    return IpythonShell()


def test_get_shell_name(ipython_shell):
    assert ipython_shell.get_shell_name() == "IPython"


def test_get_shell_version(ipython_shell):
    from IPython import __version__

    assert ipython_shell.get_shell_version() == __version__
