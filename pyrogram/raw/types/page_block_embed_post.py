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


class PageBlockEmbedPost(TLObject):  # type: ignore
    """An embedded post

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``F259A80B``

    Parameters:
        url (``str``):
            Web page URL

        webpage_id (``int`` ``64-bit``):
            ID of generated webpage preview

        author_photo_id (``int`` ``64-bit``):
            ID of the author's photo

        author (``str``):
            Author name

        date (``int`` ``32-bit``):
            Creation date

        blocks (List of :obj:`PageBlock <pyrogram.raw.base.PageBlock>`):
            Post contents

        caption (:obj:`PageCaption <pyrogram.raw.base.PageCaption>`):
            Caption

    """

    __slots__: List[str] = ["url", "webpage_id", "author_photo_id", "author", "date", "blocks", "caption"]

    ID = 0xf259a80b
    QUALNAME = "types.PageBlockEmbedPost"

    def __init__(self, *, url: str, webpage_id: int, author_photo_id: int, author: str, date: int, blocks: List["raw.base.PageBlock"], caption: "raw.base.PageCaption") -> None:
        self.url = url  # string
        self.webpage_id = webpage_id  # long
        self.author_photo_id = author_photo_id  # long
        self.author = author  # string
        self.date = date  # int
        self.blocks = blocks  # Vector<PageBlock>
        self.caption = caption  # PageCaption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockEmbedPost":
        # No flags

        url = String.read(b)

        webpage_id = Long.read(b)

        author_photo_id = Long.read(b)

        author = String.read(b)

        date = Int.read(b)

        blocks = TLObject.read(b)

        caption = TLObject.read(b)

        return PageBlockEmbedPost(url=url, webpage_id=webpage_id, author_photo_id=author_photo_id, author=author, date=date, blocks=blocks, caption=caption)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.url))

        b.write(Long(self.webpage_id))

        b.write(Long(self.author_photo_id))

        b.write(String(self.author))

        b.write(Int(self.date))

        b.write(Vector(self.blocks))

        b.write(self.caption.write())

        return b.getvalue()
