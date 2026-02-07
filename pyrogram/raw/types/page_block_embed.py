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


class PageBlockEmbed(TLObject):  # type: ignore
    """An embedded webpage

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``A8718DC5``

    Parameters:
        caption (:obj:`PageCaption <pyrogram.raw.base.PageCaption>`):
            Caption

        full_width (``bool``, *optional*):
            Whether the block should be full width

        allow_scrolling (``bool``, *optional*):
            Whether scrolling should be allowed

        url (``str``, *optional*):
            Web page URL, if available

        html (``str``, *optional*):
            HTML-markup of the embedded page

        poster_photo_id (``int`` ``64-bit``, *optional*):
            Poster photo, if available

        w (``int`` ``32-bit``, *optional*):
            Block width, if known

        h (``int`` ``32-bit``, *optional*):
            Block height, if known

    """

    __slots__: List[str] = ["caption", "full_width", "allow_scrolling", "url", "html", "poster_photo_id", "w", "h"]

    ID = 0xa8718dc5
    QUALNAME = "types.PageBlockEmbed"

    def __init__(self, *, caption: "raw.base.PageCaption", full_width: Optional[bool] = None, allow_scrolling: Optional[bool] = None, url: Optional[str] = None, html: Optional[str] = None, poster_photo_id: Optional[int] = None, w: Optional[int] = None, h: Optional[int] = None) -> None:
        self.caption = caption  # PageCaption
        self.full_width = full_width  # flags.0?true
        self.allow_scrolling = allow_scrolling  # flags.3?true
        self.url = url  # flags.1?string
        self.html = html  # flags.2?string
        self.poster_photo_id = poster_photo_id  # flags.4?long
        self.w = w  # flags.5?int
        self.h = h  # flags.5?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockEmbed":

        flags = Int.read(b)

        full_width = True if flags & (1 << 0) else False
        allow_scrolling = True if flags & (1 << 3) else False
        url = String.read(b) if flags & (1 << 1) else None
        html = String.read(b) if flags & (1 << 2) else None
        poster_photo_id = Long.read(b) if flags & (1 << 4) else None
        w = Int.read(b) if flags & (1 << 5) else None
        h = Int.read(b) if flags & (1 << 5) else None
        caption = TLObject.read(b)

        return PageBlockEmbed(caption=caption, full_width=full_width, allow_scrolling=allow_scrolling, url=url, html=html, poster_photo_id=poster_photo_id, w=w, h=h)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.full_width else 0
        flags |= (1 << 3) if self.allow_scrolling else 0
        flags |= (1 << 1) if self.url is not None else 0
        flags |= (1 << 2) if self.html is not None else 0
        flags |= (1 << 4) if self.poster_photo_id is not None else 0
        flags |= (1 << 5) if self.w is not None else 0
        flags |= (1 << 5) if self.h is not None else 0
        b.write(Int(flags))

        if self.url is not None:
            b.write(String(self.url))

        if self.html is not None:
            b.write(String(self.html))

        if self.poster_photo_id is not None:
            b.write(Long(self.poster_photo_id))

        if self.w is not None:
            b.write(Int(self.w))

        if self.h is not None:
            b.write(Int(self.h))

        b.write(self.caption.write())

        return b.getvalue()
