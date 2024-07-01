from types import FunctionType
from solutions.interface.console import ConsoleLogger


class Loggable:

    @classmethod
    def _log_prefix() -> str:
        raise NotImplementedError

    @classmethod
    def _log_msg(cls, message: str) -> None:
        ConsoleLogger.log(message, prefix=cls._log_prefix())

    @classmethod
    def logfunction(cls, func: FunctionType) -> FunctionType:
        def wrapper(self: "Loggable", *args, **kwargs) -> None:
            message = func(self, *args, **kwargs)
            self._log_msg(message=message)

        return wrapper

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError
