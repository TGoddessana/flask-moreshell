import os
import sys
from abc import ABC
from abc import abstractmethod

from flask.globals import current_app


class BaseShell(ABC):
    """Base class for all shells.

    you can extend this class to implement your own shell.
    """

    def get_banner(self) -> str:
        """
        Return banner text to be displayed when shell starts.

        override this method to customize banner text.
        """
        python_info = f"Python {sys.version} on {sys.platform}"
        shell_info = f"{self.get_shell_name()} {self.get_shell_version()}"
        app_info = (
            f"App: {current_app.import_name} "
            f"[debug: {current_app.debug}, testing: {current_app.testing}]"
        )
        config = f"Config: {current_app.config_class.__name__}"
        return f"{python_info}\n{shell_info}\n{app_info}\n{config}"

    @staticmethod
    def load_context(ctx: dict) -> None:  # type: ignore
        startup = os.environ.get("PYTHONSTARTUP")

        if startup and os.path.isfile(startup):
            with open(startup) as f:
                exec(f.read(), ctx)  # noqa: S102

        ctx.update(current_app.make_shell_context())

    @abstractmethod
    def get_shell_name(self) -> str:
        pass

    @abstractmethod
    def get_shell_version(self) -> str:
        pass

    @abstractmethod
    def load(self) -> None:
        pass
