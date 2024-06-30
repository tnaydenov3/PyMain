from solutions.classes.trackable import Trackable
from solutions.file.cls_handler import FileHandler
from solutions.path.path import Path

_DL_ACTION = "Download"


class FileDownloader(FileHandler):

    @classmethod
    def _cl_action(cls) -> str:
        return _DL_ACTION

    __slots__ = ("_target_url",)

    def __init__(self, *, target_url: str, target_path: Path) -> None:
        super().__init__(target_path=target_path)
        self._target_url = target_url
        self._downlaoded_bytes = Trackable(value=0)

    @property
    def target_url(self) -> str:
        return self._target_url
    
    @property
    def downloaded_bytes(self) -> int:
        return self._downlaoded_bytes.value

    def _handle_work(self) -> None:
        pass
