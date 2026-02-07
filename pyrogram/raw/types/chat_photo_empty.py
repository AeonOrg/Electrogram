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


class ChatPhotoEmpty(TLObject):  # type: ignore
    """Group photo is not set.

    Constructor of :obj:`~pyrogram.raw.base.ChatPhoto`.

    Details:
        - Layer: ``224``
        - ID: ``37C1011C``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x37c1011c
    QUALNAME = "types.ChatPhotoEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatPhotoEmpty":
        # No flags

        return ChatPhotoEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
