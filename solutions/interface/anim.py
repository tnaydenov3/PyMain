import threading
import time
from types import FunctionType

from solutions.classes.trackable import Trackable
from solutions.interface.console import ConsoleLogger

_UPDATE_DELAY = 0.1


class Animation(threading.Thread):

    __slots__ = (
        "_base_msg",
        "_prefix",
        "_track_var",
        "_formatting_lambda",
        "_stop_event",
    )

    def __init__(
        self,
        *,
        base_msg: str,
        prefix: str,
        track_var: Trackable,
        formatting_lambda: FunctionType = lambda x: x,
    ) -> None:
        self._base_msg = base_msg
        self._prefix = prefix
        self._track_var = track_var
        self._formatting_lambda = formatting_lambda
        self._stop_event = threading.Event()
        super().__init__()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self._base_msg})>"

    def _anim_message(self) -> str:
        msg_value = self._formatting_lambda(self._track_var.value)
        return self._base_msg.format(msg_value)

    def _log_msg(self) -> None:
        ConsoleLogger.log(message=self._anim_message(), prefix=self._prefix)

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
