class ConsoleLogger:

    _LOG_TEMP = "[{prefix}] {message}"

    @staticmethod
    def _log_to_console(message: str) -> None:
        print(message)

    @classmethod
    def log(cls, message: str, *, prefix: str) -> None:
        log_msg = cls._LOG_TEMP.format(prefix=prefix, message=message)
        cls._log_to_console(message=log_msg)

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
