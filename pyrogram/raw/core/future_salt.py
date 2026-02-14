from __future__ import annotations

from io import BytesIO
from typing import Any

from .primitives.int import Int, Long
from .tl_object import TLObject


class FutureSalt(TLObject):
    ID = 0x0949D9DC

    __slots__ = ["salt", "valid_since", "valid_until"]

    QUALNAME = "FutureSalt"

    def __init__(self, valid_since: int, valid_until: int, salt: int) -> None:
        self.valid_since = valid_since
        self.valid_until = valid_until
        self.salt = salt

    @staticmethod
    def read(data: BytesIO, *args: Any) -> FutureSalt:  # noqa: ARG004
        valid_since = Int.read(data)
        valid_until = Int.read(data)
        salt = Long.read(data)

        return FutureSalt(valid_since, valid_until, salt)

    def write(self, b: BytesIO | None = None) -> bytes:
        is_top = b is None

        if is_top:
            b = BytesIO()

        Int.write(self.valid_since, b)
        Int.write(self.valid_until, b)
        Long.write(self.salt, b)

        if is_top:
            return b.getvalue()
        return None
