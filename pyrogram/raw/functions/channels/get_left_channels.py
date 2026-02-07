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


class GetLeftChannels(TLObject):  # type: ignore
    """Get a list of channels/supergroups we left, requires a takeout session, see here » for more info.


    Details:
        - Layer: ``224``
        - ID: ``8341ECC0``

    Parameters:
        offset (``int`` ``32-bit``):
            Offset for pagination

    Returns:
        :obj:`messages.Chats <pyrogram.raw.base.messages.Chats>`
    """

    __slots__: List[str] = ["offset"]

    ID = 0x8341ecc0
    QUALNAME = "functions.channels.GetLeftChannels"

    def __init__(self, *, offset: int) -> None:
        self.offset = offset  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetLeftChannels":
        # No flags

        offset = Int.read(b)

        return GetLeftChannels(offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.offset))

        return b.getvalue()
