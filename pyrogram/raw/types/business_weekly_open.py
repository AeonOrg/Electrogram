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


class BusinessWeeklyOpen(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.BusinessWeeklyOpen`.

    Details:
        - Layer: ``224``
        - ID: ``120B1AB9``

    Parameters:
        start_minute (``int`` ``32-bit``):


        end_minute (``int`` ``32-bit``):


    """

    __slots__: List[str] = ["start_minute", "end_minute"]

    ID = 0x120b1ab9
    QUALNAME = "types.BusinessWeeklyOpen"

    def __init__(self, *, start_minute: int, end_minute: int) -> None:
        self.start_minute = start_minute  # int
        self.end_minute = end_minute  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessWeeklyOpen":
        # No flags

        start_minute = Int.read(b)

        end_minute = Int.read(b)

        return BusinessWeeklyOpen(start_minute=start_minute, end_minute=end_minute)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.start_minute))

        b.write(Int(self.end_minute))

        return b.getvalue()
