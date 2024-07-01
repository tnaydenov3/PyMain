from typing import Any

from solutions.interface.colors import TextColors
from solutions.interface.console import ConsoleLogger

_MSG_DEBUG_PREF = "DEBUG"
_DEBUG_PREF = TextColors.yellow(_MSG_DEBUG_PREF)


class Debug:

    @staticmethod
    def _log_debug_val(*, debug_val: Any) -> None:
        ConsoleLogger.log(debug_val, prefix=_DEBUG_PREF)

    @classmethod
    def log(cls, debug_val: Any, /) -> None:
        cls._log_debug_val(debug_val=debug_val)

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
