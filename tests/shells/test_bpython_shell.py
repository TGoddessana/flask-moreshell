from importlib.metadata import version

import pytest

from flask_moreshell.shells import BPythonShell


@pytest.fixture
def bpython_shell():
    return BPythonShell()


def test_get_shell_name(bpython_shell):
    assert bpython_shell.get_shell_name() == "BPython"


def test_get_shell_version(bpython_shell):
    assert bpython_shell.get_shell_version() == version("bpython")
