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


class PostInteractionCountersStory(TLObject):  # type: ignore
    """Interaction counters for a story.

    Constructor of :obj:`~pyrogram.raw.base.PostInteractionCounters`.

    Details:
        - Layer: ``224``
        - ID: ``8A480E27``

    Parameters:
        story_id (``int`` ``32-bit``):
            Story ID

        views (``int`` ``32-bit``):
            Number of views

        forwards (``int`` ``32-bit``):
            Number of forwards and reposts to public chats and channels

        reactions (``int`` ``32-bit``):
            Number of reactions

    """

    __slots__: List[str] = ["story_id", "views", "forwards", "reactions"]

    ID = 0x8a480e27
    QUALNAME = "types.PostInteractionCountersStory"

    def __init__(self, *, story_id: int, views: int, forwards: int, reactions: int) -> None:
        self.story_id = story_id  # int
        self.views = views  # int
        self.forwards = forwards  # int
        self.reactions = reactions  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PostInteractionCountersStory":
        # No flags

        story_id = Int.read(b)

        views = Int.read(b)

        forwards = Int.read(b)

        reactions = Int.read(b)

        return PostInteractionCountersStory(story_id=story_id, views=views, forwards=forwards, reactions=reactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.story_id))

        b.write(Int(self.views))

        b.write(Int(self.forwards))

        b.write(Int(self.reactions))

        return b.getvalue()
