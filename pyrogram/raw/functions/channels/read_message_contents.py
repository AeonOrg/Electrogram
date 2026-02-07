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


class ReadMessageContents(TLObject):  # type: ignore
    """Mark channel/supergroup message contents as read


    Details:
        - Layer: ``224``
        - ID: ``EAB5DC38``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Channel/supergroup

        id (List of ``int`` ``32-bit``):
            IDs of messages whose contents should be marked as read

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "id"]

    ID = 0xeab5dc38
    QUALNAME = "functions.channels.ReadMessageContents"

    def __init__(self, *, channel: "raw.base.InputChannel", id: List[int]) -> None:
        self.channel = channel  # InputChannel
        self.id = id  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadMessageContents":
        # No flags

        channel = TLObject.read(b)

        id = TLObject.read(b, Int)

        return ReadMessageContents(channel=channel, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(Vector(self.id, Int))

        return b.getvalue()
