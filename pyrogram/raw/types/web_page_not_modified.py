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


class WebPageNotModified(TLObject):  # type: ignore
    """The preview of the webpage hasn't changed

    Constructor of :obj:`~pyrogram.raw.base.WebPage`.

    Details:
        - Layer: ``224``
        - ID: ``7311CA11``

    Parameters:
        cached_page_views (``int`` ``32-bit``, *optional*):
            Page view count

    """

    __slots__: List[str] = ["cached_page_views"]

    ID = 0x7311ca11
    QUALNAME = "types.WebPageNotModified"

    def __init__(self, *, cached_page_views: Optional[int] = None) -> None:
        self.cached_page_views = cached_page_views  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageNotModified":

        flags = Int.read(b)

        cached_page_views = Int.read(b) if flags & (1 << 0) else None
        return WebPageNotModified(cached_page_views=cached_page_views)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.cached_page_views is not None else 0
        b.write(Int(flags))

        if self.cached_page_views is not None:
            b.write(Int(self.cached_page_views))

        return b.getvalue()
