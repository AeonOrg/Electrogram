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


class TogglePinnedToTop(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``B297E9B``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):


        id (List of ``int`` ``32-bit``):


    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "id"]

    ID = 0xb297e9b
    QUALNAME = "functions.stories.TogglePinnedToTop"

    def __init__(self, *, peer: "raw.base.InputPeer", id: List[int]) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TogglePinnedToTop":
        # No flags

        peer = TLObject.read(b)

        id = TLObject.read(b, Int)

        return TogglePinnedToTop(peer=peer, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Vector(self.id, Int))

        return b.getvalue()
