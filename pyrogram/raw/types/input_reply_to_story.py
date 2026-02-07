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


class InputReplyToStory(TLObject):  # type: ignore
    """Reply to a story.

    Constructor of :obj:`~pyrogram.raw.base.InputReplyTo`.

    Details:
        - Layer: ``224``
        - ID: ``5881323A``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):


        story_id (``int`` ``32-bit``):
            ID of the story to reply to.

    """

    __slots__: List[str] = ["peer", "story_id"]

    ID = 0x5881323a
    QUALNAME = "types.InputReplyToStory"

    def __init__(self, *, peer: "raw.base.InputPeer", story_id: int) -> None:
        self.peer = peer  # InputPeer
        self.story_id = story_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputReplyToStory":
        # No flags

        peer = TLObject.read(b)

        story_id = Int.read(b)

        return InputReplyToStory(peer=peer, story_id=story_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.story_id))

        return b.getvalue()
