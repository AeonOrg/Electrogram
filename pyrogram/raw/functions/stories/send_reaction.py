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


class SendReaction(TLObject):  # type: ignore
    """React to a story.


    Details:
        - Layer: ``224``
        - ID: ``7FD736B2``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The peer that sent the story

        story_id (``int`` ``32-bit``):
            ID of the story to react to

        reaction (:obj:`Reaction <pyrogram.raw.base.Reaction>`):
            Reaction

        add_to_recent (``bool``, *optional*):
            Whether to add this reaction to the recent reactions list ».

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "story_id", "reaction", "add_to_recent"]

    ID = 0x7fd736b2
    QUALNAME = "functions.stories.SendReaction"

    def __init__(self, *, peer: "raw.base.InputPeer", story_id: int, reaction: "raw.base.Reaction", add_to_recent: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.story_id = story_id  # int
        self.reaction = reaction  # Reaction
        self.add_to_recent = add_to_recent  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendReaction":

        flags = Int.read(b)

        add_to_recent = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        story_id = Int.read(b)

        reaction = TLObject.read(b)

        return SendReaction(peer=peer, story_id=story_id, reaction=reaction, add_to_recent=add_to_recent)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.add_to_recent else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.story_id))

        b.write(self.reaction.write())

        return b.getvalue()
