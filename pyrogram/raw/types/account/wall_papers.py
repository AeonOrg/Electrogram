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


class WallPapers(TLObject):  # type: ignore
    """Installed wallpapers

    Constructor of :obj:`~pyrogram.raw.base.account.WallPapers`.

    Details:
        - Layer: ``224``
        - ID: ``CDC3858C``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

        wallpapers (List of :obj:`WallPaper <pyrogram.raw.base.WallPaper>`):
            Wallpapers

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetWallPapers
    """

    __slots__: List[str] = ["hash", "wallpapers"]

    ID = 0xcdc3858c
    QUALNAME = "types.account.WallPapers"

    def __init__(self, *, hash: int, wallpapers: List["raw.base.WallPaper"]) -> None:
        self.hash = hash  # long
        self.wallpapers = wallpapers  # Vector<WallPaper>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WallPapers":
        # No flags

        hash = Long.read(b)

        wallpapers = TLObject.read(b)

        return WallPapers(hash=hash, wallpapers=wallpapers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.hash))

        b.write(Vector(self.wallpapers))

        return b.getvalue()
