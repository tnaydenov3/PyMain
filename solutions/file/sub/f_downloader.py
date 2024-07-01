from http.client import HTTPResponse
from urllib import request
from solutions.classes.trackable_int import TrackableInt
from solutions.path.path import Path


class SubDownloader:

    @staticmethod
    def downlaod_url_to_file(
        *,
        source_url: str,
        target_path: Path,
        trackable: TrackableInt,
        chunk_size: int,
    ) -> None:
        with request.urlopen(url=source_url) as response:
            assert isinstance(response, HTTPResponse)

            with target_path.open(mode="wb") as target_file:
                while True:

                    chunk = response.read(amt=chunk_size)
                    if not chunk:
                        break
                    target_file.write(chunk)
                    trackable.value += len(chunk)

    __slots__ = tuple()

    def __init__(self) -> None:
        raise NotImplementedError
