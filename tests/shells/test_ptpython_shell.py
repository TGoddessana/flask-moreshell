from importlib.metadata import version

import pytest
from flask import Flask

from flask_moreshell.shells.ptpython_shell import PTPythonShell


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    return app


@pytest.fixture
def ptpython_shell():
    return PTPythonShell()


def test_get_shell_name(ptpython_shell):
    assert ptpython_shell.get_shell_name() == "PTPython"


def test_get_shell_version(ptpython_shell):
    assert ptpython_shell.get_shell_version() == version("ptpython")


def test_load(ptpython_shell, monkeypatch, capsys, app):
    with app.app_context():
        ptpython_shell.load()

    stdout = capsys.readouterr().out

    assert ptpython_shell.get_shell_name() in stdout
    assert ptpython_shell.get_shell_version() in stdout
    assert "PTPython" in stdout
