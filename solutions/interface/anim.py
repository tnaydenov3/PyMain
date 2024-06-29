import threading


class Animation(threading.Thread):

    __slots__ = ("_base_msg", "_track_var")

    def __init__(self, *, base_msg: str, track_var: int) -> None:
        self._base_msg = base_msg
        self._track_var = track_var
        super().__init__()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self._base_msg})>"

    @property
    def base_msg(self) -> str:
        return self._base_msg

    @property
    def track_var(self) -> int:
        return self._track_var

    @property
    def msg(self) -> str:
        return self._base_msg.format(self._track_var)

    def run(self) -> None:
        pass

    def stop(self) -> None:
        self.join()
