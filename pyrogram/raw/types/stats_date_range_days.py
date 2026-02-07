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


class StatsDateRangeDays(TLObject):  # type: ignore
    """Channel statistics date range

    Constructor of :obj:`~pyrogram.raw.base.StatsDateRangeDays`.

    Details:
        - Layer: ``224``
        - ID: ``B637EDAF``

    Parameters:
        min_date (``int`` ``32-bit``):
            Initial date

        max_date (``int`` ``32-bit``):
            Final date

    """

    __slots__: List[str] = ["min_date", "max_date"]

    ID = 0xb637edaf
    QUALNAME = "types.StatsDateRangeDays"

    def __init__(self, *, min_date: int, max_date: int) -> None:
        self.min_date = min_date  # int
        self.max_date = max_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsDateRangeDays":
        # No flags

        min_date = Int.read(b)

        max_date = Int.read(b)

        return StatsDateRangeDays(min_date=min_date, max_date=max_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.min_date))

        b.write(Int(self.max_date))

        return b.getvalue()
