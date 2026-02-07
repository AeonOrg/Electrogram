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


class Birthday(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.Birthday`.

    Details:
        - Layer: ``224``
        - ID: ``6C8E1E06``

    Parameters:
        day (``int`` ``32-bit``):


        month (``int`` ``32-bit``):


        year (``int`` ``32-bit``, *optional*):


    """

    __slots__: List[str] = ["day", "month", "year"]

    ID = 0x6c8e1e06
    QUALNAME = "types.Birthday"

    def __init__(self, *, day: int, month: int, year: Optional[int] = None) -> None:
        self.day = day  # int
        self.month = month  # int
        self.year = year  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Birthday":

        flags = Int.read(b)

        day = Int.read(b)

        month = Int.read(b)

        year = Int.read(b) if flags & (1 << 0) else None
        return Birthday(day=day, month=month, year=year)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.year is not None else 0
        b.write(Int(flags))

        b.write(Int(self.day))

        b.write(Int(self.month))

        if self.year is not None:
            b.write(Int(self.year))

        return b.getvalue()
