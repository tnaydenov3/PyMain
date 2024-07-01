TIME_UNITS_NS = ("ns", "us", "ms", "s")
TIME_MULTIPLE = 1000

_TIME_NUM_ROUNDING_DECIMALS = 3


class TimeNanosecondsUtil:

    @staticmethod
    def format_nanoseconds(*, time_ns: int) -> tuple[float, str]:
        time_num = time_ns

        for unit in TIME_UNITS_NS:
            if time_num < TIME_MULTIPLE:
                break
            time_num /= TIME_MULTIPLE

        time_num = round(number=time_num, ndigits=_TIME_NUM_ROUNDING_DECIMALS)

        return time_num, unit

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
