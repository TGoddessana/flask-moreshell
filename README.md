# Flask-Moreshell

Flask-Moreshell is a flask extension which supports ipython, bpython, ptpython shells in `flask shell`.  
inspired
by [flask-shell-ipython](https://github.com/ei-grad/flask-shell-ipython), [flask-shell-bpython](https://github.com/jacquerie/flask-shell-bpython), [flask-shell-ptpython](https://github.com/jacquerie/flask-shell-ptpython).

## Installation

you can install `flask-moreshell` via `pip` command.

```bash
pip install flask-moreshell
```

## Usage

you can just use this command:

```shell
flask shell
```

and flask-moreshell tries to find this python REPL alternatives:

1. `ipython`
2. `bpython`
3. `ptpython`

if none of them are installed, just default python shell will be executed.

or you can choose specific shell type, via `--shelltype` option.  
`ipython`, `bpython`, `ptpython` are supported.

ipython usage:

```shell
flask shell --shelltype ipython
```
![ipython-example.png](docs%2Fipython-example.png)

bpython usage:
```shell
flask shell --shelltype bpython
```
![bpython-example.png](docs%2Fbpython-example.png)

ptpython usage:
```shell
flask shell --shelltype ptpython
```
![ptpython-example.png](docs%2Fptpython-example.png)

## License

[MIT](https://choosealicense.com/licenses/mit/)