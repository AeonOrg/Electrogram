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


class SavedGifs(TLObject):  # type: ignore
    """Saved gifs

    Constructor of :obj:`~pyrogram.raw.base.messages.SavedGifs`.

    Details:
        - Layer: ``224``
        - ID: ``84A02A0D``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

        gifs (List of :obj:`Document <pyrogram.raw.base.Document>`):
            List of saved gifs

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSavedGifs
    """

    __slots__: List[str] = ["hash", "gifs"]

    ID = 0x84a02a0d
    QUALNAME = "types.messages.SavedGifs"

    def __init__(self, *, hash: int, gifs: List["raw.base.Document"]) -> None:
        self.hash = hash  # long
        self.gifs = gifs  # Vector<Document>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedGifs":
        # No flags

        hash = Long.read(b)

        gifs = TLObject.read(b)

        return SavedGifs(hash=hash, gifs=gifs)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.hash))

        b.write(Vector(self.gifs))

        return b.getvalue()
