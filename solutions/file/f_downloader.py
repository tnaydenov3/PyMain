from solutions.classes.trackable_int import TrackableInt
from solutions.file.cls_handler import FileHandler
from solutions.interface.anim import Animation
from solutions.interface.util import ConsoleUtil
from solutions.path.path import Path

_MIN_DL_SIZE = 0
_MAX_DL_SIZE = 10 * 1024 * 1024

_DL_ACTION = "Download"

_ERR_DL_SIZE_EXCEEDED = f"Download size limit of {_MAX_DL_SIZE} bytes exceeded!"

_ANIM_BASE_MESSAGE = 'Downloading "{url}" to file...[{dl_size}]'


class FileDownloader(FileHandler):

    @classmethod
    def _cl_action(cls) -> str:
        return _DL_ACTION

    __slots__ = ("_target_url",)

    def __init__(self, *, target_url: str, target_path: Path) -> None:
        super().__init__(target_path=target_path)
        self._target_url = target_url
        self._downlaoded_bytes = TrackableInt(
            value=0,
            err_value_msg=_ERR_DL_SIZE_EXCEEDED,
            min_value=_MIN_DL_SIZE,
            max_value=_MAX_DL_SIZE,
        )

    @property
    def target_url(self) -> str:
        return self._target_url

    @property
    def downloaded_bytes(self) -> int:
        return self._downlaoded_bytes.value

    def _download_file(self) -> None:
        pass

    def _handle_work(self) -> None:
        try:
            anim_object = Animation(
                base_msg=_ANIM_BASE_MESSAGE,
                prefix=self._log_prefix(),
                track_var=self._downlaoded_bytes,
                formatting_lambda=ConsoleUtil.size_bytes_to_human_readable,
            )

        finally:
            anim_object.stop()
