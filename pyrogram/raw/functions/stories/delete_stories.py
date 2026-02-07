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


class DeleteStories(TLObject):  # type: ignore
    """Deletes some posted stories.


    Details:
        - Layer: ``224``
        - ID: ``AE59DB5F``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Channel/user from where to delete stories.

        id (List of ``int`` ``32-bit``):
            IDs of stories to delete.

    Returns:
        List of ``int`` ``32-bit``
    """

    __slots__: List[str] = ["peer", "id"]

    ID = 0xae59db5f
    QUALNAME = "functions.stories.DeleteStories"

    def __init__(self, *, peer: "raw.base.InputPeer", id: List[int]) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteStories":
        # No flags

        peer = TLObject.read(b)

        id = TLObject.read(b, Int)

        return DeleteStories(peer=peer, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Vector(self.id, Int))

        return b.getvalue()
