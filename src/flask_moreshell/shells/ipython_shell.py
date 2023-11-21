from typing import Any
from typing import Optional
from typing import Union

from flask.globals import current_app

from flask_moreshell.shells import BaseShell


try:
    import IPython
    from IPython.terminal.ipapp import load_default_config
    from traitlets.config.loader import Config
except ModuleNotFoundError as e:
    raise ModuleNotFoundError("IPython is not installed on your system.") from e


class IpythonShell(BaseShell):
    def get_shell_name(self) -> str:
        return "IPython"

    def get_shell_version(self) -> str:
        return IPython.__version__

    def load(self) -> None:
        config = self._get_config()
        config.TerminalInteractiveShell.banner1 = self.get_banner()  # type: ignore

        IPython.start_ipython(  # type: ignore
            argv=[],
            user_ns=current_app.make_shell_context(),
            config=config,
        )

    @staticmethod
    def _get_config() -> Union[Config, Optional[Any]]:
        if "IPYTHON_CONFIG" in current_app.config:
            return Config(current_app.config["IPYTHON_CONFIG"])
        return load_default_config()  # type: ignore
