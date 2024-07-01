from typing import Any

from solutions.interface.console import ConsoleLogger

_DEBUG_PREF = "DEBUG"


class Debug:

    @staticmethod
    def _log_debug_val(*, debug_val: Any) -> None:
        ConsoleLogger.log(message=debug_val, prefix=_DEBUG_PREF)

    @classmethod
    def log(cls, debug_val: Any, /) -> None:
        cls._log_debug_val(debug_val=debug_val)

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
