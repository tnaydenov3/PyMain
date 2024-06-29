class Loggable:

    @staticmethod
    def _log_prefix() -> str:
        raise NotImplementedError

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError
