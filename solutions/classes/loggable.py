from solutions.interface.console import ConsoleLogger


class Loggable:

    @staticmethod
    def _log_prefix() -> str:
        raise NotImplementedError

    @classmethod
    def _log_msg(cls, message: str) -> None:
        ConsoleLogger.log(message=message, prefix=cls._log_prefix())

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError
