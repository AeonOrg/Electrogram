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


class GetMessageAuthor(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``ECE2A0E6``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`User <pyrogram.raw.base.User>`
    """

    __slots__: List[str] = ["channel", "id"]

    ID = 0xece2a0e6
    QUALNAME = "functions.channels.GetMessageAuthor"

    def __init__(self, *, channel: "raw.base.InputChannel", id: int) -> None:
        self.channel = channel  # InputChannel
        self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessageAuthor":
        # No flags

        channel = TLObject.read(b)

        id = Int.read(b)

        return GetMessageAuthor(channel=channel, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(Int(self.id))

        return b.getvalue()
