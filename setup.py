from setuptools import setup  # type: ignore[import]

setup(
    entry_points={
        "flask.commands": [
            "shell=flask_moreshell:shell",
        ],
    },
)
