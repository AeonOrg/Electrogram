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


class AvailableEffects(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.messages.AvailableEffects`.

    Details:
        - Layer: ``224``
        - ID: ``BDDB616E``

    Parameters:
        hash (``int`` ``32-bit``):
            Hash for pagination, for more info click here

        effects (List of :obj:`AvailableEffect <pyrogram.raw.base.AvailableEffect>`):


        documents (List of :obj:`Document <pyrogram.raw.base.Document>`):


    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAvailableEffects
    """

    __slots__: List[str] = ["hash", "effects", "documents"]

    ID = 0xbddb616e
    QUALNAME = "types.messages.AvailableEffects"

    def __init__(self, *, hash: int, effects: List["raw.base.AvailableEffect"], documents: List["raw.base.Document"]) -> None:
        self.hash = hash  # int
        self.effects = effects  # Vector<AvailableEffect>
        self.documents = documents  # Vector<Document>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AvailableEffects":
        # No flags

        hash = Int.read(b)

        effects = TLObject.read(b)

        documents = TLObject.read(b)

        return AvailableEffects(hash=hash, effects=effects, documents=documents)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.hash))

        b.write(Vector(self.effects))

        b.write(Vector(self.documents))

        return b.getvalue()
