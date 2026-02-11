from __future__ import annotations

from io import BytesIO
from typing import Any, cast

from pyrogram.raw.core.list import List
from pyrogram.raw.core.tl_object import TLObject

from .bool import Bool, BoolFalse, BoolTrue
from .int import Int, Long


class Vector(bytes, TLObject):
    ID = 0x1CB5C415

    @staticmethod
    def read_bare(b: BytesIO, size: int) -> int | Any:
        if size == 4:
            e = int.from_bytes(b.read(4), "little")
            b.seek(-4, 1)

            if e in {BoolFalse.ID, BoolTrue.ID}:
                return Bool.read(b)

            return Int.read(b)

        if size == 8:
            return Long.read(b)

        return TLObject.read(b)

    @classmethod
    def read(cls, data: BytesIO, t: Any = None, *args: Any) -> List:  # noqa: ARG003
        count = Int.read(data)
        left = len(data.read())
        size = (left / count) if count else 0
        data.seek(-left, 1)

        return List(
            t.read(data) if t else Vector.read_bare(data, size) for _ in range(count)
        )

    def __new__(cls, value: list, t: Any = None) -> bytes:  # type: ignore
        b = BytesIO()
        cls.write(value, t, b)
        return b.getvalue()

    @classmethod
    def write(cls, value: list, t: Any = None, b: BytesIO = None) -> bytes | None:
        if b is None:
            return cls(value, t)

        b.write(b"\x15\xc4\xb5\x1c")
        Int.write(len(value), b)

        for i in value:
            if t:
                b.write(t(i))
            else:
                i.write(b)

        return None
