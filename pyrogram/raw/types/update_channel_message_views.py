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


class UpdateChannelMessageViews(TLObject):  # type: ignore
    """The view counter of a message in a channel has changed

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``F226AC08``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Channel ID

        id (``int`` ``32-bit``):
            ID of the message

        views (``int`` ``32-bit``):
            New view counter

    """

    __slots__: List[str] = ["channel_id", "id", "views"]

    ID = 0xf226ac08
    QUALNAME = "types.UpdateChannelMessageViews"

    def __init__(self, *, channel_id: int, id: int, views: int) -> None:
        self.channel_id = channel_id  # long
        self.id = id  # int
        self.views = views  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelMessageViews":
        # No flags

        channel_id = Long.read(b)

        id = Int.read(b)

        views = Int.read(b)

        return UpdateChannelMessageViews(channel_id=channel_id, id=id, views=views)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.channel_id))

        b.write(Int(self.id))

        b.write(Int(self.views))

        return b.getvalue()
