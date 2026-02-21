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

    @classmethod
    def read(cls, b: BytesIO, *args: Any) -> Any:  # noqa: ARG004
        valid_since = Int.read(b)
        valid_until = Int.read(b)
        salt = Long.read(b)

        return FutureSalt(valid_since, valid_until, salt)

    def write(self, *args: Any) -> bytes:  # noqa: ARG002
        b = BytesIO()

        b.write(Int(self.valid_since))
        b.write(Int(self.valid_until))
        b.write(Long(self.salt))

        return b.getvalue()
