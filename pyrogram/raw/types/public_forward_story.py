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


class PublicForwardStory(TLObject):  # type: ignore
    """Contains info about a forward of a story as a repost by a public channel.

    Constructor of :obj:`~pyrogram.raw.base.PublicForward`.

    Details:
        - Layer: ``224``
        - ID: ``EDF3ADD0``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The channel that reposted the story.

        story (:obj:`StoryItem <pyrogram.raw.base.StoryItem>`):
            The reposted story (may be different from the original story).

    """

    __slots__: List[str] = ["peer", "story"]

    ID = 0xedf3add0
    QUALNAME = "types.PublicForwardStory"

    def __init__(self, *, peer: "raw.base.Peer", story: "raw.base.StoryItem") -> None:
        self.peer = peer  # Peer
        self.story = story  # StoryItem

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PublicForwardStory":
        # No flags

        peer = TLObject.read(b)

        story = TLObject.read(b)

        return PublicForwardStory(peer=peer, story=story)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.story.write())

        return b.getvalue()
