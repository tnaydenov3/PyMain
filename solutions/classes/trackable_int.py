from solutions.classes.trackable import Trackable


class TrackableInt(Trackable):

    __slots__ = ("_max_value", "_min_value")

    def __init__(self, *, value: int, max_value: int, min_value: int = 0) -> None:
        self._max_value = max_value
        self._min_value = min_value

        super().__init__(value=value, val_type=int)
