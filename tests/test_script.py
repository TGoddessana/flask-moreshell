"""Test cases for the __main__ module."""
import pytest
from click.testing import CliRunner

from flask_moreshell.script import shell


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_python_shell(runner: CliRunner) -> None:
    """Test the shell command."""
    with open("app.py", "w") as f:
        f.write("from flask import Flask\napp = Flask(__name__)\n")

    result = runner.invoke(shell, ["--shelltype", "python"])
    assert result.exit_code == 0
    assert "Python" in result.output
    assert ">>> " in result.output
