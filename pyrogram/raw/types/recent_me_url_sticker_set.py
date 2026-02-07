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


class RecentMeUrlStickerSet(TLObject):  # type: ignore
    """Recent t.me stickerset installation URL

    Constructor of :obj:`~pyrogram.raw.base.RecentMeUrl`.

    Details:
        - Layer: ``224``
        - ID: ``BC0A57DC``

    Parameters:
        url (``str``):
            t.me URL

        set (:obj:`StickerSetCovered <pyrogram.raw.base.StickerSetCovered>`):
            Stickerset

    """

    __slots__: List[str] = ["url", "set"]

    ID = 0xbc0a57dc
    QUALNAME = "types.RecentMeUrlStickerSet"

    def __init__(self, *, url: str, set: "raw.base.StickerSetCovered") -> None:
        self.url = url  # string
        self.set = set  # StickerSetCovered

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RecentMeUrlStickerSet":
        # No flags

        url = String.read(b)

        set = TLObject.read(b)

        return RecentMeUrlStickerSet(url=url, set=set)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.url))

        b.write(self.set.write())

        return b.getvalue()
