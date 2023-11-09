import os
import sys

import click
from flask.cli import with_appcontext
from flask.globals import current_app


@click.command(context_settings=dict(ignore_unknown_options=True))
@click.option("--shelltype", type=click.STRING, default=None)
@with_appcontext
def shell(shelltype: str):
    """Run `flask shell` command with IPython, BPython, PTPython.

    If you have IPython, PYTPython, or BPython installed, run them with your
    Flask application.
    if none of them are installed, this loads the default python shell.

    you can specify type of shell with --shelltype option.

    :param shelltype: type of shell to use.
    """
    if shelltype:
        try:
            if shelltype == "ipython":
                _load_ipython()
            elif shelltype == "bpython":
                _load_bpython()
            elif shelltype == "ptpython":
                _load_ptpython()
            elif shelltype == "python":
                _load_python()
        except ModuleNotFoundError:
            raise ModuleNotFoundError(f"{shelltype} is not installed on your system.")
    else:
        try:
            _load_ipython()
            sys.exit()
        except ModuleNotFoundError:
            pass
        try:
            _load_bpython()
            sys.exit()
        except ModuleNotFoundError:
            pass
        try:
            _load_ptpython()
            sys.exit()
        except ModuleNotFoundError:
            _load_python()


def _load_ipython():
    """Load ipython shell, with current application."""
    import IPython
    from IPython.terminal.ipapp import load_default_config
    from traitlets.config.loader import Config

    if "IPYTHON_CONFIG" in current_app.config:
        config = Config(current_app.config["IPYTHON_CONFIG"])
    else:
        config = load_default_config()

    config.TerminalInteractiveShell.banner1 = "".join(
        f"Python {sys.version} on {sys.platform}\n"
        f"IPython: {IPython.__version__}\n"
        f"App: {current_app.import_name} [{current_app.debug}]\n"
        f"Instance: {current_app.instance_path}\n"
    )

    IPython.start_ipython(
        argv=[],
        user_ns=current_app.make_shell_context(),
        config=config,
    )


def _load_bpython():
    """Load bpython shell, with current application."""
    import bpython  # type: ignore[import]

    banner = "".join(
        f"Python {sys.version} on {sys.platform}\n"
        f"BPython: {bpython.__version__}\n"
        f"App: {current_app.import_name} [{current_app.debug}]\n"
        f"Instance: {current_app.instance_path}\n"
    )

    ctx = {}
    ctx.update(current_app.make_shell_context())

    bpython.embed(banner=banner, locals_=ctx)


def _load_ptpython():
    from importlib.metadata import version

    from flask.globals import _app_ctx_stack
    from ptpython.repl import embed

    banner = "".join(
        f"Python {sys.version} on {sys.platform}\n"
        f"PTPython: {version('ptpython')}\n"
        f"App: {current_app.import_name} [{current_app.debug}]\n"
        f"Instance: {current_app.instance_path}\n"
    )

    app = _app_ctx_stack.top.app
    ctx = {}

    # Support the regular Python interpreter startup script if someone
    # is using it.
    startup = os.environ.get("PYTHONSTARTUP")
    if startup and os.path.isfile(startup):
        with open(startup) as f:
            eval(compile(f.read(), startup, "exec"), ctx)

    ctx.update(app.make_shell_context())
    print(banner)
    embed(globals=ctx)


def _load_python():
    """Load default python shell."""
    import code

    ctx: dict = {}
    startup = os.environ.get("PYTHONSTARTUP")
    if startup and os.path.isfile(startup):
        with open(startup) as f:
            eval(compile(f.read(), startup, "exec"), ctx)
    ctx.update(current_app.make_shell_context())
    interactive_hook = getattr(sys, "__interactivehook__", None)
    if interactive_hook is not None:
        try:
            import readline
            from rlcompleter import Completer
        except ImportError:
            pass
        else:
            readline.set_completer(Completer(ctx).complete)
        interactive_hook()
    code.interact(local=ctx)
