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


class StatsPercentValue(TLObject):  # type: ignore
    """Channel statistics percentage.
Compute the percentage simply by doing part * total / 100

    Constructor of :obj:`~pyrogram.raw.base.StatsPercentValue`.

    Details:
        - Layer: ``224``
        - ID: ``CBCE2FE0``

    Parameters:
        part (``float`` ``64-bit``):
            Partial value

        total (``float`` ``64-bit``):
            Total value

    """

    __slots__: List[str] = ["part", "total"]

    ID = 0xcbce2fe0
    QUALNAME = "types.StatsPercentValue"

    def __init__(self, *, part: float, total: float) -> None:
        self.part = part  # double
        self.total = total  # double

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsPercentValue":
        # No flags

        part = Double.read(b)

        total = Double.read(b)

        return StatsPercentValue(part=part, total=total)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Double(self.part))

        b.write(Double(self.total))

        return b.getvalue()
