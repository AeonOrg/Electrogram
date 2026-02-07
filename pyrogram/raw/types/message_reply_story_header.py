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


class MessageReplyStoryHeader(TLObject):  # type: ignore
    """Represents a reply to a story

    Constructor of :obj:`~pyrogram.raw.base.MessageReplyHeader`.

    Details:
        - Layer: ``224``
        - ID: ``E5AF939``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):


        story_id (``int`` ``32-bit``):
            Story ID

    """

    __slots__: List[str] = ["peer", "story_id"]

    ID = 0xe5af939
    QUALNAME = "types.MessageReplyStoryHeader"

    def __init__(self, *, peer: "raw.base.Peer", story_id: int) -> None:
        self.peer = peer  # Peer
        self.story_id = story_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageReplyStoryHeader":
        # No flags

        peer = TLObject.read(b)

        story_id = Int.read(b)

        return MessageReplyStoryHeader(peer=peer, story_id=story_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.story_id))

        return b.getvalue()
