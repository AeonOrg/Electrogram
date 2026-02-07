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


class MyStickers(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.messages.MyStickers`.

    Details:
        - Layer: ``224``
        - ID: ``FAFF629D``

    Parameters:
        count (``int`` ``32-bit``):


        sets (List of :obj:`StickerSetCovered <pyrogram.raw.base.StickerSetCovered>`):


    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetMyStickers
    """

    __slots__: List[str] = ["count", "sets"]

    ID = 0xfaff629d
    QUALNAME = "types.messages.MyStickers"

    def __init__(self, *, count: int, sets: List["raw.base.StickerSetCovered"]) -> None:
        self.count = count  # int
        self.sets = sets  # Vector<StickerSetCovered>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MyStickers":
        # No flags

        count = Int.read(b)

        sets = TLObject.read(b)

        return MyStickers(count=count, sets=sets)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.count))

        b.write(Vector(self.sets))

        return b.getvalue()
