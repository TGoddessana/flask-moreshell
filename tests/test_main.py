import pytest
from click.testing import CliRunner
from flask import Flask

from flask_moreshell import shell


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    return app


@pytest.fixture
def runner(app):
    return CliRunner()


def test_ipython_shell(runner, app):
    with app.app_context():
        result = runner.invoke(shell, ["--shelltype", "ipython"])
    assert result.exit_code == 0
    assert "IPython" in result.output


# def test_bpython_shell(runner, app):
#     with app.app_context():
#         result = runner.invoke(shell, ["--shelltype", "bpython"])
#         assert result.output == ""
#     assert result.exit_code == 0
#     assert "BPython" in result.output


def test_pypython_shell(runner, app):
    with app.app_context():
        result = runner.invoke(shell, ["--shelltype", "ptpython"])
    assert result.exit_code == 0
    assert "PTPython" in result.output


def test_python_shell(runner, app):
    with app.app_context():
        result = runner.invoke(shell, ["--shelltype", "python"])
    assert result.exit_code == 0
    assert "Python" in result.output
