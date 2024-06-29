class ConsoleLogger:

    @staticmethod
    def _log_to_console(message: str) -> None:
        print(message)

    __slots__ = tuple()

    def __init__(self):
        raise NotImplementedError
