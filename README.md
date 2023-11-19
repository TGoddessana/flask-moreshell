<img src="https://github.com/TGoddessana/flask-moreshell/assets/88619089/804d2934-be56-4ea7-8ad8-9c787d5b2dd2" style="width: 40%">

# Flask Moreshell

flask shell with IPython, BPython, PTPython!

[![PyPI](https://img.shields.io/pypi/v/flask-moreshell.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/flask-moreshell.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/flask-moreshell)][python version]
[![License](https://img.shields.io/badge/license-MIT-blue)][license]

[![Read the documentation at https://flask-moreshell.readthedocs.io/](https://img.shields.io/readthedocs/flask-moreshell/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/tgoddessana/flask-moreshell/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/tgoddessana/flask-moreshell/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/flask-moreshell/
[status]: https://pypi.org/project/flask-moreshell/
[python version]: https://pypi.org/project/flask-moreshell
[read the docs]: https://flask-moreshell.readthedocs.io/
[tests]: https://github.com/tgoddessana/flask-moreshell/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/tgoddessana/flask-moreshell
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Features

This package provides functionality to allow flask shell commands to be used with the ipython, bpython, and ptpython
shells.

## Requirements

- Python 3.9+
- Flask 2.3+

## Installation

You can install _Flask Moreshell_ via [pip] from [PyPI]:

```console
$ pip install flask-moreshell
```

or anything else that can install packages from PyPI. for example, [poetry](https://python-poetry.org/)
or [pipenv](https://pipenv.pypa.io/en/latest/).

## Usage

after the package is installed, you can use the `flask shell` command as usual.

```shell
$ flask shell
```

and you can see python REPLs like this, with flask app loaded.

![shell_usage](https://github.com/TGoddessana/flask-moreshell/assets/88619089/fdbdb4de-1f18-48fd-84da-d7dae2eb88ad)

By default, make sure that `ipython`, `bpython`, and `ptpython` are installed in your current virtual environment. When
you
use the `flask shell` command, the package will look for and load the Python REPLs in that order.

if you want to use a specific shell, you can use the `--shelltype` option.

see [Usage] for more information.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Flask Moreshell_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

[pypi]: https://pypi.org/
[file an issue]: https://github.com/tgoddessana/flask-moreshell/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/tgoddessana/flask-moreshell/blob/main/LICENSE
[contributor guide]: https://github.com/tgoddessana/flask-moreshell/blob/main/CONTRIBUTING.md
[usage]: https://flask-moreshell.readthedocs.io/en/latest/usage.html
