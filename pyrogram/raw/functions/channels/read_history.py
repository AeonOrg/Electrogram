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


class ReadHistory(TLObject):  # type: ignore
    """Mark channel/supergroup history as read


    Details:
        - Layer: ``224``
        - ID: ``CC104937``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Channel/supergroup

        max_id (``int`` ``32-bit``):
            ID of message up to which messages should be marked as read

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "max_id"]

    ID = 0xcc104937
    QUALNAME = "functions.channels.ReadHistory"

    def __init__(self, *, channel: "raw.base.InputChannel", max_id: int) -> None:
        self.channel = channel  # InputChannel
        self.max_id = max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadHistory":
        # No flags

        channel = TLObject.read(b)

        max_id = Int.read(b)

        return ReadHistory(channel=channel, max_id=max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(Int(self.max_id))

        return b.getvalue()
