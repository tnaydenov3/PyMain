from types import FrameType


class Tracebacks:

    @staticmethod
    def _get_error_frame(*, error: Exception) -> FrameType:
        traceback = error.__traceback__

        while traceback.tb_next:
            traceback = traceback.tb_next

        return traceback.tb_frame

    @classmethod
    def get_error_frame(cls, *, error: Exception) -> FrameType:
        return cls._get_error_frame(error=error)

    @classmethod
    def get_error_funcname(cls, *, error: Exception) -> str:
        return cls._get_error_frame(error=error).f_code.co_name

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
