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


class DifferenceEmpty(TLObject):  # type: ignore
    """No events.

    Constructor of :obj:`~pyrogram.raw.base.updates.Difference`.

    Details:
        - Layer: ``224``
        - ID: ``5D75A138``

    Parameters:
        date (``int`` ``32-bit``):
            Current date

        seq (``int`` ``32-bit``):
            Number of sent updates

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            updates.GetDifference
    """

    __slots__: List[str] = ["date", "seq"]

    ID = 0x5d75a138
    QUALNAME = "types.updates.DifferenceEmpty"

    def __init__(self, *, date: int, seq: int) -> None:
        self.date = date  # int
        self.seq = seq  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DifferenceEmpty":
        # No flags

        date = Int.read(b)

        seq = Int.read(b)

        return DifferenceEmpty(date=date, seq=seq)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.date))

        b.write(Int(self.seq))

        return b.getvalue()
