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


class UpdateChannelMessageForwards(TLObject):  # type: ignore
    """The forward counter of a message in a channel has changed

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``D29A27F4``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Channel ID

        id (``int`` ``32-bit``):
            ID of the message

        forwards (``int`` ``32-bit``):
            New forward counter

    """

    __slots__: List[str] = ["channel_id", "id", "forwards"]

    ID = 0xd29a27f4
    QUALNAME = "types.UpdateChannelMessageForwards"

    def __init__(self, *, channel_id: int, id: int, forwards: int) -> None:
        self.channel_id = channel_id  # long
        self.id = id  # int
        self.forwards = forwards  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelMessageForwards":
        # No flags

        channel_id = Long.read(b)

        id = Int.read(b)

        forwards = Int.read(b)

        return UpdateChannelMessageForwards(channel_id=channel_id, id=id, forwards=forwards)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.channel_id))

        b.write(Int(self.id))

        b.write(Int(self.forwards))

        return b.getvalue()
