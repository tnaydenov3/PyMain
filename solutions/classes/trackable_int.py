from solutions.classes.trackable import Trackable


class TrackableInt(Trackable):

    __slots__ = ("_min_value", "_max_value")

    def __init__(
        self,
        *,
        value: int,
        err_value_msg: str,
        min_value: int = None,
        max_value: int = None,
    ) -> None:
        self._min_value = min_value
        self._max_value = max_value

        super().__init__(
            val_type=int,
            value=value,
            err_value_msg=err_value_msg,
        )

    def _check_constraints(self, *, value: int) -> bool:
        if self._min_value is not None and value < self._min_value:
            return False

        if self._max_value is not None and value > self._max_value:
            return False

        return True
