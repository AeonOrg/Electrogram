from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class InputStickerSetShortName(TLObject):  # type: ignore
    """Stickerset by short name, from a stickerset deep link »

    Constructor of :obj:`~pyrogram.raw.base.InputStickerSet`.

    Details:
        - Layer: ``224``
        - ID: ``861CC8A0``

    Parameters:
        short_name (``str``):
            Short name from a stickerset deep link »

    """

    __slots__: List[str] = ["short_name"]

    ID = 0x861cc8a0
    QUALNAME = "types.InputStickerSetShortName"

    def __init__(self, *, short_name: str) -> None:
        self.short_name = short_name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStickerSetShortName":
        # No flags

        short_name = String.read(b)

        return InputStickerSetShortName(short_name=short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.short_name))

        return b.getvalue()
