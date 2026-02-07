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


class StarGiftCollection(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftCollection`.

    Details:
        - Layer: ``224``
        - ID: ``9D6B13B0``

    Parameters:
        collection_id (``int`` ``32-bit``):
            N/A

        title (``str``):
            N/A

        gifts_count (``int`` ``32-bit``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

        icon (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.CreateStarGiftCollection
            payments.UpdateStarGiftCollection
    """

    __slots__: List[str] = ["collection_id", "title", "gifts_count", "hash", "icon"]

    ID = 0x9d6b13b0
    QUALNAME = "types.StarGiftCollection"

    def __init__(self, *, collection_id: int, title: str, gifts_count: int, hash: int, icon: "raw.base.Document" = None) -> None:
        self.collection_id = collection_id  # int
        self.title = title  # string
        self.gifts_count = gifts_count  # int
        self.hash = hash  # long
        self.icon = icon  # flags.0?Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftCollection":

        flags = Int.read(b)

        collection_id = Int.read(b)

        title = String.read(b)

        icon = TLObject.read(b) if flags & (1 << 0) else None

        gifts_count = Int.read(b)

        hash = Long.read(b)

        return StarGiftCollection(collection_id=collection_id, title=title, gifts_count=gifts_count, hash=hash, icon=icon)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.icon is not None else 0
        b.write(Int(flags))

        b.write(Int(self.collection_id))

        b.write(String(self.title))

        if self.icon is not None:
            b.write(self.icon.write())

        b.write(Int(self.gifts_count))

        b.write(Long(self.hash))

        return b.getvalue()
