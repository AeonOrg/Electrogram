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


class AvailableReactions(TLObject):  # type: ignore
    """Animations and metadata associated with message reactions »

    Constructor of :obj:`~pyrogram.raw.base.messages.AvailableReactions`.

    Details:
        - Layer: ``224``
        - ID: ``768E3AAD``

    Parameters:
        hash (``int`` ``32-bit``):
            Hash for pagination, for more info click here

        reactions (List of :obj:`AvailableReaction <pyrogram.raw.base.AvailableReaction>`):
            Animations and metadata associated with message reactions »

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAvailableReactions
    """

    __slots__: List[str] = ["hash", "reactions"]

    ID = 0x768e3aad
    QUALNAME = "types.messages.AvailableReactions"

    def __init__(self, *, hash: int, reactions: List["raw.base.AvailableReaction"]) -> None:
        self.hash = hash  # int
        self.reactions = reactions  # Vector<AvailableReaction>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AvailableReactions":
        # No flags

        hash = Int.read(b)

        reactions = TLObject.read(b)

        return AvailableReactions(hash=hash, reactions=reactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.hash))

        b.write(Vector(self.reactions))

        return b.getvalue()
