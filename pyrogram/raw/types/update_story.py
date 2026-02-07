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


class UpdateStory(TLObject):  # type: ignore
    """A new story was posted.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``75B3B798``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            ID of the poster.

        story (:obj:`StoryItem <pyrogram.raw.base.StoryItem>`):
            The story that was posted.

    """

    __slots__: List[str] = ["peer", "story"]

    ID = 0x75b3b798
    QUALNAME = "types.UpdateStory"

    def __init__(self, *, peer: "raw.base.Peer", story: "raw.base.StoryItem") -> None:
        self.peer = peer  # Peer
        self.story = story  # StoryItem

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStory":
        # No flags

        peer = TLObject.read(b)

        story = TLObject.read(b)

        return UpdateStory(peer=peer, story=story)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.story.write())

        return b.getvalue()
