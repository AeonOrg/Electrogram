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


class MessageEntityCashtag(TLObject):  # type: ignore
    """Message entity representing a $cashtag.

    Constructor of :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``224``
        - ID: ``4C4E743F``

    Parameters:
        offset (``int`` ``32-bit``):
            Offset of message entity within message (in UTF-16 code units)

        length (``int`` ``32-bit``):
            Length of message entity within message (in UTF-16 code units)

    """

    __slots__: List[str] = ["offset", "length"]

    ID = 0x4c4e743f
    QUALNAME = "types.MessageEntityCashtag"

    def __init__(self, *, offset: int, length: int) -> None:
        self.offset = offset  # int
        self.length = length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityCashtag":
        # No flags

        offset = Int.read(b)

        length = Int.read(b)

        return MessageEntityCashtag(offset=offset, length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.offset))

        b.write(Int(self.length))

        return b.getvalue()
