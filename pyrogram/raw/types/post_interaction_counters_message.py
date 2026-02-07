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


class PostInteractionCountersMessage(TLObject):  # type: ignore
    """Interaction counters for a message.

    Constructor of :obj:`~pyrogram.raw.base.PostInteractionCounters`.

    Details:
        - Layer: ``224``
        - ID: ``E7058E7F``

    Parameters:
        msg_id (``int`` ``32-bit``):
            Message ID

        views (``int`` ``32-bit``):
            Number of views

        forwards (``int`` ``32-bit``):
            Number of forwards to public channels

        reactions (``int`` ``32-bit``):
            Number of reactions

    """

    __slots__: List[str] = ["msg_id", "views", "forwards", "reactions"]

    ID = 0xe7058e7f
    QUALNAME = "types.PostInteractionCountersMessage"

    def __init__(self, *, msg_id: int, views: int, forwards: int, reactions: int) -> None:
        self.msg_id = msg_id  # int
        self.views = views  # int
        self.forwards = forwards  # int
        self.reactions = reactions  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PostInteractionCountersMessage":
        # No flags

        msg_id = Int.read(b)

        views = Int.read(b)

        forwards = Int.read(b)

        reactions = Int.read(b)

        return PostInteractionCountersMessage(msg_id=msg_id, views=views, forwards=forwards, reactions=reactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.msg_id))

        b.write(Int(self.views))

        b.write(Int(self.forwards))

        b.write(Int(self.reactions))

        return b.getvalue()
