from importlib.metadata import version

import pytest

from flask_moreshell.shells.ptpython_shell import PTPythonShell


@pytest.fixture
def ptpython_shell() -> PTPythonShell:
    return PTPythonShell()


def test_get_shell_name(ptpython_shell: PTPythonShell) -> None:
    assert ptpython_shell.get_shell_name() == "PTPython"


def test_get_shell_version(ptpython_shell: PTPythonShell) -> None:
    assert ptpython_shell.get_shell_version() == version("ptpython")
