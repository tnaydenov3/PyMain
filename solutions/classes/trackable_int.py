from solutions.classes.trackable import Trackable


class TrackableInt(Trackable):

    @staticmethod
    def _check_constraints(*, value: int) -> bool:
        return value >= 0

    __slots__ = tuple()

    def __init__(self, *, value: int) -> None:
        super().__init__(value=value, val_type=int)
