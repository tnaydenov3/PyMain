from solutions.classes.trackable_int import TrackableInt
from solutions.file.cls_handler import FileHandler
from solutions.file.sub.f_downloader import SubDownloader
from solutions.interface.anim import Animation
from solutions.interface.util import ConsoleUtil
from solutions.path.path import Path

_MIN_DL_SIZE = 0
_MAX_DL_SIZE = 10 * 1024 * 1024

_DL_CHUNK_SIZE = 1024

_DL_ACTION = "Download"

_ERR_DL_SIZE_EXCEEDED = f"Download size limit of {_MAX_DL_SIZE} bytes exceeded!"

_ANIM_BASE_MESSAGE = 'Downloading "{url}" to file...[{{}}]'


class FileDownloader(FileHandler):

    @classmethod
    def _cl_action(cls) -> str:
        return _DL_ACTION

    __slots__ = ("_source_url", "_downlaoded_bytes")

    def __init__(self, *, source_url: str, target_path: Path) -> None:
        super().__init__(target_path=target_path)
        self._source_url = source_url
        self._downlaoded_bytes = TrackableInt(
            value=0,
            err_value_msg=_ERR_DL_SIZE_EXCEEDED,
            min_value=_MIN_DL_SIZE,
            max_value=_MAX_DL_SIZE,
        )

    def _main_attr(self) -> str:
        return self._source_url

    @property
    def source_url(self) -> str:
        return self._source_url

    @property
    def downloaded_bytes(self) -> int:
        return self._downlaoded_bytes.value

    def download(self, force_dl: bool = False) -> None:
        self._handle(force=force_dl)

    def _download_file(self) -> None:
        SubDownloader.downlaod_url_to_file(
            source_url=self._source_url,
            target_path=self._target_path,
            trackable=self._downlaoded_bytes,
            chunk_size=_DL_CHUNK_SIZE,
        )

    def _handle_work(self) -> None:
        try:
            anim_object = Animation(
                base_msg=self._anim_base_smg(),
                prefix=self._log_prefix(),
                track_var=self._downlaoded_bytes,
                formatting_lambda=ConsoleUtil.size_bytes_to_human_readable,
            )

            anim_object.start()
            self._download_file()

        finally:
            anim_object.stop()

    def _anim_base_smg(self) -> str:
        return _ANIM_BASE_MESSAGE.format(url=self._source_url)
