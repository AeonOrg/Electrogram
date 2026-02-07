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


class UpdateWebPage(TLObject):  # type: ignore
    """An instant view webpage preview was generated

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``7F891213``

    Parameters:
        webpage (:obj:`WebPage <pyrogram.raw.base.WebPage>`):
            Webpage preview

        pts (``int`` ``32-bit``):
            Event count after generation

        pts_count (``int`` ``32-bit``):
            Number of events that were generated

    """

    __slots__: List[str] = ["webpage", "pts", "pts_count"]

    ID = 0x7f891213
    QUALNAME = "types.UpdateWebPage"

    def __init__(self, *, webpage: "raw.base.WebPage", pts: int, pts_count: int) -> None:
        self.webpage = webpage  # WebPage
        self.pts = pts  # int
        self.pts_count = pts_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateWebPage":
        # No flags

        webpage = TLObject.read(b)

        pts = Int.read(b)

        pts_count = Int.read(b)

        return UpdateWebPage(webpage=webpage, pts=pts, pts_count=pts_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.webpage.write())

        b.write(Int(self.pts))

        b.write(Int(self.pts_count))

        return b.getvalue()
