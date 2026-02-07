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


class StoryViewPublicRepost(TLObject):  # type: ignore
    """A certain peer has reposted the story.

    Constructor of :obj:`~pyrogram.raw.base.StoryView`.

    Details:
        - Layer: ``224``
        - ID: ``BD74CF49``

    Parameters:
        peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The peer that reposted the story.

        story (:obj:`StoryItem <pyrogram.raw.base.StoryItem>`):
            The reposted story.

        blocked (``bool``, *optional*):
            Whether we have completely blocked this user, including from viewing more of our stories.

        blocked_my_stories_from (``bool``, *optional*):
            Whether we have blocked this user from viewing more of our stories.

    """

    __slots__: List[str] = ["peer_id", "story", "blocked", "blocked_my_stories_from"]

    ID = 0xbd74cf49
    QUALNAME = "types.StoryViewPublicRepost"

    def __init__(self, *, peer_id: "raw.base.Peer", story: "raw.base.StoryItem", blocked: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None) -> None:
        self.peer_id = peer_id  # Peer
        self.story = story  # StoryItem
        self.blocked = blocked  # flags.0?true
        self.blocked_my_stories_from = blocked_my_stories_from  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryViewPublicRepost":

        flags = Int.read(b)

        blocked = True if flags & (1 << 0) else False
        blocked_my_stories_from = True if flags & (1 << 1) else False
        peer_id = TLObject.read(b)

        story = TLObject.read(b)

        return StoryViewPublicRepost(peer_id=peer_id, story=story, blocked=blocked, blocked_my_stories_from=blocked_my_stories_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.blocked else 0
        flags |= (1 << 1) if self.blocked_my_stories_from else 0
        b.write(Int(flags))

        b.write(self.peer_id.write())

        b.write(self.story.write())

        return b.getvalue()
