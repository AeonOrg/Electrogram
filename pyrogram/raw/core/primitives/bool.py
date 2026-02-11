from __future__ import annotations

from io import BytesIO
from typing import Any

from pyrogram.raw.core.tl_object import TLObject


class BoolFalse(bytes, TLObject):
    ID = 0xBC799737
    value = False

    @classmethod
    def read(cls, *args: Any) -> bool:  # noqa: ARG003
        return cls.value

    def __new__(cls) -> bytes:  # type: ignore
        return b"\x37\x97\x79\xbc"


class BoolTrue(BoolFalse):
    ID = 0x997275B5
    value = True

    def __new__(cls) -> bytes:  # type: ignore
        return b"\xb5\x75\x72\x99"


class Bool(bytes, TLObject):
    @classmethod
    def read(cls, data: BytesIO, *args: Any) -> bool:  # noqa: ARG003
        return int.from_bytes(data.read(4), "little") == BoolTrue.ID

    def __new__(cls, value: bool) -> bytes:  # type: ignore
        return BoolTrue() if value else BoolFalse()

    @classmethod
    def write(cls, value: bool, b: BytesIO):
        b.write(BoolTrue() if value else BoolFalse())
