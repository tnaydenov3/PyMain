import threading


class Animation(threading.Thread):

    def __init__(self, *, base_msg: str, track_var: int) -> None:
        self._base_msg = base_msg
        self._track_var = track_var
        super().__init__()

    @property
    def base_msg(self) -> str:
        return self._base_msg

    @property
    def track_var(self) -> int:
        return self._track_var
