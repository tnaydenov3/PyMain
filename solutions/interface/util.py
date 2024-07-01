from solutions.interface.util_file import SizeBytesUtil
from solutions.interface.util_time import TimeNanosecondsUtil

_SIZE_UNIT_TEMPL = "{size_num} {unit}"


class ConsoleUtil:

    @staticmethod
    def size_bytes_to_human_readable(size_bytes: int) -> str:
        size_num, unit = SizeBytesUtil.format_bytes(size_bytes=size_bytes)

        return _SIZE_UNIT_TEMPL.format(size_num=size_num, unit=unit)

    @staticmethod
    def time_nanosecs_to_human_readable(time_ns: int) -> str:
        time_num, unit = TimeNanosecondsUtil.format_nanoseconds(time_ns=time_ns)

        return _SIZE_UNIT_TEMPL.format(size_num=time_num, unit=unit)

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
