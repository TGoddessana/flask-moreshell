from setuptools import setup

setup(
    entry_points={
        "flask.commands": [
            "shell=flask_moreshell:shell",
        ],
    },
)
