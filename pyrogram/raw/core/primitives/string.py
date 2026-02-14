from __future__ import annotations

from io import BytesIO
from typing import cast

from .bytes import Bytes


class String(Bytes):
    @classmethod
    def read(cls, data: BytesIO, *args) -> str:  # noqa: ARG003
        return cast("bytes", super(String, String).read(data)).decode(
            errors="replace",
        )

    def __new__(cls, value: str) -> bytes:
        return super().__new__(cls, value.encode())

    @classmethod
    def write(cls, value: str, b: BytesIO):
        Bytes.write(value.encode(), b)
