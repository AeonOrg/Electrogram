from __future__ import annotations

from io import BytesIO
from typing import Any

from pyrogram.raw.core.tl_object import TLObject


class Bytes(bytes, TLObject):
    @classmethod
    def read(cls, data: BytesIO, *args: Any) -> bytes:  # noqa: ARG003
        length = int.from_bytes(data.read(1), "little")

        if length <= 253:
            x = data.read(length)
            data.read(-(length + 1) % 4)
        else:
            length = int.from_bytes(data.read(3), "little")
            x = data.read(length)
            data.read(-length % 4)

        return x

    def __new__(cls, value: bytes) -> bytes:  # type: ignore
        b = BytesIO()
        cls.write(value, b)
        return b.getvalue()

    @classmethod
    def write(cls, value: bytes, b: BytesIO):
        length = len(value)

        if length <= 253:
            b.write(bytes([length]))
            b.write(value)
            b.write(bytes(-(length + 1) % 4))
        else:
            b.write(bytes([254]))
            b.write(length.to_bytes(3, "little"))
            b.write(value)
            b.write(bytes(-length % 4))
