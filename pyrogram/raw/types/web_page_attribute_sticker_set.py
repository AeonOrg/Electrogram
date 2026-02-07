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


class WebPageAttributeStickerSet(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.WebPageAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``50CC03D3``

    Parameters:
        stickers (List of :obj:`Document <pyrogram.raw.base.Document>`):


        emojis (``bool``, *optional*):


        text_color (``bool``, *optional*):


    """

    __slots__: List[str] = ["stickers", "emojis", "text_color"]

    ID = 0x50cc03d3
    QUALNAME = "types.WebPageAttributeStickerSet"

    def __init__(self, *, stickers: List["raw.base.Document"], emojis: Optional[bool] = None, text_color: Optional[bool] = None) -> None:
        self.stickers = stickers  # Vector<Document>
        self.emojis = emojis  # flags.0?true
        self.text_color = text_color  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageAttributeStickerSet":

        flags = Int.read(b)

        emojis = True if flags & (1 << 0) else False
        text_color = True if flags & (1 << 1) else False
        stickers = TLObject.read(b)

        return WebPageAttributeStickerSet(stickers=stickers, emojis=emojis, text_color=text_color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.emojis else 0
        flags |= (1 << 1) if self.text_color else 0
        b.write(Int(flags))

        b.write(Vector(self.stickers))

        return b.getvalue()
