from types import TracebackType


class Tracebacks:

    @staticmethod
    def _get_error_frame(error: Exception) -> TracebackType:
        traceback = error.__traceback__

        while traceback.tb_next:
            traceback = traceback.tb_next

        return traceback

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
