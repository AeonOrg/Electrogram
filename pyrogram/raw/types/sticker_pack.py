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


class StickerPack(TLObject):  # type: ignore
    """A stickerpack is a group of stickers associated to the same emoji.
It is not a sticker pack the way it is usually intended, you may be looking for a StickerSet.

    Constructor of :obj:`~pyrogram.raw.base.StickerPack`.

    Details:
        - Layer: ``224``
        - ID: ``12B299D4``

    Parameters:
        emoticon (``str``):
            Emoji

        documents (List of ``int`` ``64-bit``):
            Stickers

    """

    __slots__: List[str] = ["emoticon", "documents"]

    ID = 0x12b299d4
    QUALNAME = "types.StickerPack"

    def __init__(self, *, emoticon: str, documents: List[int]) -> None:
        self.emoticon = emoticon  # string
        self.documents = documents  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerPack":
        # No flags

        emoticon = String.read(b)

        documents = TLObject.read(b, Long)

        return StickerPack(emoticon=emoticon, documents=documents)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.emoticon))

        b.write(Vector(self.documents, Long))

        return b.getvalue()
