import sys
import os
import click
from flask.cli import with_appcontext
from flask.globals import current_app


@click.command(context_settings=dict(ignore_unknown_options=True))
@click.option("--shelltype", type=click.STRING, default=None)
@with_appcontext
def shell(shelltype):
    """
    tries to find IPython first, and Bpython.
    if none of them are installed, this loads the default python shell.

    you can specify type of shell with --shelltype option.
    """
    if shelltype:
        if shelltype == "ipython":
            load_ipython()
        elif shelltype == "bpython":
            load_bpython()
        elif shelltype == "python":
            load_python()
    else:
        pass


def load_ipython():
    """load ipython shell, with current application."""
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


def load_bpython():
    """load bpython shell, with current application."""
    import bpython

    banner = "".join(
        f"Python {sys.version} on {sys.platform}\n"
        f"BPython: {bpython.__version__}\n"
        f"App: {current_app.import_name} [{current_app.debug}]\n"
        f"Instance: {current_app.instance_path}\n"
    )

    ctx = {}
    ctx.update(current_app.make_shell_context())

    bpython.embed(banner=banner, locals_=ctx)


def load_python():
    """load default python shell."""
    import code
    banner = (
        f"Python {sys.version} on {sys.platform}\n"
        f"App: {current_app.import_name}\n"
        f"Instance: {current_app.instance_path}"
    )
    ctx: dict = {}
    # Support the regular Python interpreter startup script if someone
    # is using it.
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
    code.interact(banner=banner, local=ctx)
