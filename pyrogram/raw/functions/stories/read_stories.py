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


class ReadStories(TLObject):  # type: ignore
    """Mark all stories up to a certain ID as read, for a given peer; will emit an updateReadStories update to all logged-in sessions.


    Details:
        - Layer: ``224``
        - ID: ``A556DAC8``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The peer whose stories should be marked as read.

        max_id (``int`` ``32-bit``):
            Mark all stories up to and including this ID as read

    Returns:
        List of ``int`` ``32-bit``
    """

    __slots__: List[str] = ["peer", "max_id"]

    ID = 0xa556dac8
    QUALNAME = "functions.stories.ReadStories"

    def __init__(self, *, peer: "raw.base.InputPeer", max_id: int) -> None:
        self.peer = peer  # InputPeer
        self.max_id = max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadStories":
        # No flags

        peer = TLObject.read(b)

        max_id = Int.read(b)

        return ReadStories(peer=peer, max_id=max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.max_id))

        return b.getvalue()
