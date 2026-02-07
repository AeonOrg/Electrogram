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


class PageBlockMap(TLObject):  # type: ignore
    """A map

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``A44F3EF6``

    Parameters:
        geo (:obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`):
            Location of the map center

        zoom (``int`` ``32-bit``):
            Map zoom level; 13-20

        w (``int`` ``32-bit``):
            Map width in pixels before applying scale; 16-102

        h (``int`` ``32-bit``):
            Map height in pixels before applying scale; 16-1024

        caption (:obj:`PageCaption <pyrogram.raw.base.PageCaption>`):
            Caption

    """

    __slots__: List[str] = ["geo", "zoom", "w", "h", "caption"]

    ID = 0xa44f3ef6
    QUALNAME = "types.PageBlockMap"

    def __init__(self, *, geo: "raw.base.GeoPoint", zoom: int, w: int, h: int, caption: "raw.base.PageCaption") -> None:
        self.geo = geo  # GeoPoint
        self.zoom = zoom  # int
        self.w = w  # int
        self.h = h  # int
        self.caption = caption  # PageCaption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockMap":
        # No flags

        geo = TLObject.read(b)

        zoom = Int.read(b)

        w = Int.read(b)

        h = Int.read(b)

        caption = TLObject.read(b)

        return PageBlockMap(geo=geo, zoom=zoom, w=w, h=h, caption=caption)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.geo.write())

        b.write(Int(self.zoom))

        b.write(Int(self.w))

        b.write(Int(self.h))

        b.write(self.caption.write())

        return b.getvalue()
