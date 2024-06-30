from urllib import request
from solutions.classes.trackable_int import TrackableInt
from solutions.path.path import Path

_DEFAULT_DL_CHUNK_SIZE = 1024


class SubDownloader:

    @staticmethod
    def downlaod_url_to_file(
        url: str,
        target_path: Path,
        trackable: TrackableInt,
        chunk_size: int = _DEFAULT_DL_CHUNK_SIZE,
    ) -> None:
        with request.urlopen(url=url) as response:
            with target_path.open("wb") as target_file:
                pass

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
