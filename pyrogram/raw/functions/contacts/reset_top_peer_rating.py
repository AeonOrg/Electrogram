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


class ResetTopPeerRating(TLObject):  # type: ignore
    """Reset rating of top peer


    Details:
        - Layer: ``224``
        - ID: ``1AE373AC``

    Parameters:
        category (:obj:`TopPeerCategory <pyrogram.raw.base.TopPeerCategory>`):
            Top peer category

        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peer whose rating should be reset

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["category", "peer"]

    ID = 0x1ae373ac
    QUALNAME = "functions.contacts.ResetTopPeerRating"

    def __init__(self, *, category: "raw.base.TopPeerCategory", peer: "raw.base.InputPeer") -> None:
        self.category = category  # TopPeerCategory
        self.peer = peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetTopPeerRating":
        # No flags

        category = TLObject.read(b)

        peer = TLObject.read(b)

        return ResetTopPeerRating(category=category, peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.category.write())

        b.write(self.peer.write())

        return b.getvalue()
