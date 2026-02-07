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


class PageBlockRelatedArticles(TLObject):  # type: ignore
    """Related articles

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``16115A96``

    Parameters:
        title (:obj:`RichText <pyrogram.raw.base.RichText>`):
            Title

        articles (List of :obj:`PageRelatedArticle <pyrogram.raw.base.PageRelatedArticle>`):
            Related articles

    """

    __slots__: List[str] = ["title", "articles"]

    ID = 0x16115a96
    QUALNAME = "types.PageBlockRelatedArticles"

    def __init__(self, *, title: "raw.base.RichText", articles: List["raw.base.PageRelatedArticle"]) -> None:
        self.title = title  # RichText
        self.articles = articles  # Vector<PageRelatedArticle>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockRelatedArticles":
        # No flags

        title = TLObject.read(b)

        articles = TLObject.read(b)

        return PageBlockRelatedArticles(title=title, articles=articles)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.title.write())

        b.write(Vector(self.articles))

        return b.getvalue()
