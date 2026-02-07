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


class StoryFwdHeader(TLObject):  # type: ignore
    """Contains info about the original poster of a reposted story.

    Constructor of :obj:`~pyrogram.raw.base.StoryFwdHeader`.

    Details:
        - Layer: ``224``
        - ID: ``B826E150``

    Parameters:
        modified (``bool``, *optional*):
            Whether the story media was modified before reposting it (for example by overlaying a round video with a reaction).

        from_peer (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        from_name (``str``, *optional*):
            Will be set for stories forwarded from a user with forwards privacy enabled, in which case from will also be empty.

        story_id (``int`` ``32-bit``, *optional*):
            , contains the story ID

    """

    __slots__: List[str] = ["modified", "from_peer", "from_name", "story_id"]

    ID = 0xb826e150
    QUALNAME = "types.StoryFwdHeader"

    def __init__(self, *, modified: Optional[bool] = None, from_peer: "raw.base.Peer" = None, from_name: Optional[str] = None, story_id: Optional[int] = None) -> None:
        self.modified = modified  # flags.3?true
        self.from_peer = from_peer  # flags.0?Peer
        self.from_name = from_name  # flags.1?string
        self.story_id = story_id  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryFwdHeader":

        flags = Int.read(b)

        modified = True if flags & (1 << 3) else False
        from_peer = TLObject.read(b) if flags & (1 << 0) else None

        from_name = String.read(b) if flags & (1 << 1) else None
        story_id = Int.read(b) if flags & (1 << 2) else None
        return StoryFwdHeader(modified=modified, from_peer=from_peer, from_name=from_name, story_id=story_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.modified else 0
        flags |= (1 << 0) if self.from_peer is not None else 0
        flags |= (1 << 1) if self.from_name is not None else 0
        flags |= (1 << 2) if self.story_id is not None else 0
        b.write(Int(flags))

        if self.from_peer is not None:
            b.write(self.from_peer.write())

        if self.from_name is not None:
            b.write(String(self.from_name))

        if self.story_id is not None:
            b.write(Int(self.story_id))

        return b.getvalue()
