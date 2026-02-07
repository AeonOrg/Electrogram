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


class GetMessages(TLObject):  # type: ignore
    """Get channel/supergroup messages


    Details:
        - Layer: ``224``
        - ID: ``AD8C9A23``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Channel/supergroup

        id (List of :obj:`InputMessage <pyrogram.raw.base.InputMessage>`):
            IDs of messages to get

    Returns:
        :obj:`messages.Messages <pyrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["channel", "id"]

    ID = 0xad8c9a23
    QUALNAME = "functions.channels.GetMessages"

    def __init__(self, *, channel: "raw.base.InputChannel", id: List["raw.base.InputMessage"]) -> None:
        self.channel = channel  # InputChannel
        self.id = id  # Vector<InputMessage>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessages":
        # No flags

        channel = TLObject.read(b)

        id = TLObject.read(b)

        return GetMessages(channel=channel, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(Vector(self.id))

        return b.getvalue()
