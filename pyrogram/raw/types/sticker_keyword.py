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


class StickerKeyword(TLObject):  # type: ignore
    """Keywords for a certain sticker

    Constructor of :obj:`~pyrogram.raw.base.StickerKeyword`.

    Details:
        - Layer: ``224``
        - ID: ``FCFEB29C``

    Parameters:
        document_id (``int`` ``64-bit``):
            Sticker ID

        keyword (List of ``str``):
            Keywords

    """

    __slots__: List[str] = ["document_id", "keyword"]

    ID = 0xfcfeb29c
    QUALNAME = "types.StickerKeyword"

    def __init__(self, *, document_id: int, keyword: List[str]) -> None:
        self.document_id = document_id  # long
        self.keyword = keyword  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerKeyword":
        # No flags

        document_id = Long.read(b)

        keyword = TLObject.read(b, String)

        return StickerKeyword(document_id=document_id, keyword=keyword)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.document_id))

        b.write(Vector(self.keyword, String))

        return b.getvalue()
