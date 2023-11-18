"""Test cases for the __main__ module."""
import pytest
from click.testing import CliRunner

from flask_moreshell import shell


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(shell)
    assert result.exit_code == 0
