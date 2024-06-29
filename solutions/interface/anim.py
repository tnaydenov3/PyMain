import threading
import time

from solutions.classes.trackable import Trackable
from solutions.interface.console import ConsoleLogger

_UPDATE_DELAY = 0.1


class Animation(threading.Thread):

    __slots__ = ("_base_msg", "_prefix", "_track_var", "_stop_event")

    def __init__(self, *, base_msg: str, prefix: str, track_var: Trackable) -> None:
        self._base_msg = base_msg
        self._prefix = prefix
        self._track_var = track_var
        self._stop_event = threading.Event()
        super().__init__()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self._base_msg})>"

    @property
    def base_msg(self) -> str:
        return self._base_msg

    @property
    def prefix(self) -> str:
        return self._prefix

    @property
    def track_var(self) -> Trackable:
        return self._track_var

    @property
    def msg(self) -> str:
        return self._base_msg.format(self._track_var)

    def _log_msg(self) -> None:
        ConsoleLogger.log(message=self.msg, prefix=self.prefix)

    def _log_update(self) -> None:
        ConsoleLogger.clear_last_line()
        self._log_msg()

    def _update(self) -> None:
        self._log_update()

    def run(self) -> None:
        self._log_msg()
        while not self._stop_event.is_set():
            time.sleep(_UPDATE_DELAY)
            self._update()

    def stop(self) -> None:
        self._stop_event.set()
        self.join()
        self._update()
