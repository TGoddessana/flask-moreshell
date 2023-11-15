"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Flask Moreshell."""


if __name__ == "__main__":
    main(prog_name="flask-moreshell")  # pragma: no cover
