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


class UpdateSentStoryReaction(TLObject):  # type: ignore
    """Indicates we reacted to a story ».

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``7D627683``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The peer that sent the story

        story_id (``int`` ``32-bit``):
            ID of the story we reacted to

        reaction (:obj:`Reaction <pyrogram.raw.base.Reaction>`):
            The reaction that was sent

    """

    __slots__: List[str] = ["peer", "story_id", "reaction"]

    ID = 0x7d627683
    QUALNAME = "types.UpdateSentStoryReaction"

    def __init__(self, *, peer: "raw.base.Peer", story_id: int, reaction: "raw.base.Reaction") -> None:
        self.peer = peer  # Peer
        self.story_id = story_id  # int
        self.reaction = reaction  # Reaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateSentStoryReaction":
        # No flags

        peer = TLObject.read(b)

        story_id = Int.read(b)

        reaction = TLObject.read(b)

        return UpdateSentStoryReaction(peer=peer, story_id=story_id, reaction=reaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.story_id))

        b.write(self.reaction.write())

        return b.getvalue()
