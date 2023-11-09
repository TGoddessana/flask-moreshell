"""Test cases for the __main__ module."""
import pytest
from click.testing import CliRunner

from flask_moreshell.script import shell


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()
