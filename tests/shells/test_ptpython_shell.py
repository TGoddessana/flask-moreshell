from importlib.metadata import version

import pytest

from flask_moreshell.shells import PTPythonShell

from .flask_fixture import app


@pytest.fixture
def ptpython_shell():
    return PTPythonShell()


def test_get_shell_name(ptpython_shell):
    assert ptpython_shell.get_shell_name() == "PTPython"


def test_get_shell_version(ptpython_shell):
    assert ptpython_shell.get_shell_version() == version("ptpython")


def test_load(ptpython_shell, monkeypatch, capsys):
    with app.app_context():
        ptpython_shell.load()

    stdout = capsys.readouterr().out

    assert ptpython_shell.get_shell_name() in stdout
    assert ptpython_shell.get_shell_version() in stdout
    assert "PTPython" in stdout
