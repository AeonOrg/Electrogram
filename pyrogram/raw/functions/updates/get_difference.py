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


class GetDifference(TLObject):  # type: ignore
    """Get new updates.


    Details:
        - Layer: ``224``
        - ID: ``19C2F763``

    Parameters:
        pts (``int`` ``32-bit``):
            PTS, see updates.

        date (``int`` ``32-bit``):
            date, see updates.

        qts (``int`` ``32-bit``):
            QTS, see updates.

        pts_limit (``int`` ``32-bit``, *optional*):
            PTS limit

        pts_total_limit (``int`` ``32-bit``, *optional*):
            For fast updating: if provided and pts + pts_total_limit < remote pts, updates.differenceTooLong will be returned.Simply tells the server to not return the difference if it is bigger than pts_total_limitIf the remote pts is too big (> ~4000000), this field will default to 1000000

        qts_limit (``int`` ``32-bit``, *optional*):
            QTS limit

    Returns:
        :obj:`updates.Difference <pyrogram.raw.base.updates.Difference>`
    """

    __slots__: List[str] = ["pts", "date", "qts", "pts_limit", "pts_total_limit", "qts_limit"]

    ID = 0x19c2f763
    QUALNAME = "functions.updates.GetDifference"

    def __init__(self, *, pts: int, date: int, qts: int, pts_limit: Optional[int] = None, pts_total_limit: Optional[int] = None, qts_limit: Optional[int] = None) -> None:
        self.pts = pts  # int
        self.date = date  # int
        self.qts = qts  # int
        self.pts_limit = pts_limit  # flags.1?int
        self.pts_total_limit = pts_total_limit  # flags.0?int
        self.qts_limit = qts_limit  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDifference":

        flags = Int.read(b)

        pts = Int.read(b)

        pts_limit = Int.read(b) if flags & (1 << 1) else None
        pts_total_limit = Int.read(b) if flags & (1 << 0) else None
        date = Int.read(b)

        qts = Int.read(b)

        qts_limit = Int.read(b) if flags & (1 << 2) else None
        return GetDifference(pts=pts, date=date, qts=qts, pts_limit=pts_limit, pts_total_limit=pts_total_limit, qts_limit=qts_limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.pts_limit is not None else 0
        flags |= (1 << 0) if self.pts_total_limit is not None else 0
        flags |= (1 << 2) if self.qts_limit is not None else 0
        b.write(Int(flags))

        b.write(Int(self.pts))

        if self.pts_limit is not None:
            b.write(Int(self.pts_limit))

        if self.pts_total_limit is not None:
            b.write(Int(self.pts_total_limit))

        b.write(Int(self.date))

        b.write(Int(self.qts))

        if self.qts_limit is not None:
            b.write(Int(self.qts_limit))

        return b.getvalue()
