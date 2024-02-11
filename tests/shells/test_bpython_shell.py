from importlib.metadata import version

import pytest

from flask_moreshell.shells.bpython_shell import BPythonShell


@pytest.fixture
def bpython_shell() -> BPythonShell:
    return BPythonShell()


def test_get_shell_name(bpython_shell: BPythonShell) -> None:
    assert bpython_shell.get_shell_name() == "BPython"


def test_get_shell_version(bpython_shell: BPythonShell) -> None:
    assert bpython_shell.get_shell_version() == version("bpython")
