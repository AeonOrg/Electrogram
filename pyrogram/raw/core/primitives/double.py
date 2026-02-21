from __future__ import annotations

from struct import pack, unpack
from typing import TYPE_CHECKING, Any, cast

from pyrogram.raw.core.tl_object import TLObject

if TYPE_CHECKING:
    from io import BytesIO


class Double(bytes, TLObject):
    @classmethod
    def read(cls, b: BytesIO, *args: Any) -> Any:  # noqa: ARG003
        return cast("float", unpack("d", b.read(8))[0])

    def __new__(cls, value: float) -> bytes:  # type: ignore
        return pack("d", value)
