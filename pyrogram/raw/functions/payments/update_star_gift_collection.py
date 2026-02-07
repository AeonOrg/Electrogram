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


class UpdateStarGiftCollection(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``4FDDBEE7``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        collection_id (``int`` ``32-bit``):
            N/A

        title (``str``, *optional*):
            N/A

        delete_stargift (List of :obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`, *optional*):
            N/A

        add_stargift (List of :obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`, *optional*):
            N/A

        order (List of :obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`, *optional*):
            N/A

    Returns:
        :obj:`StarGiftCollection <pyrogram.raw.base.StarGiftCollection>`
    """

    __slots__: List[str] = ["peer", "collection_id", "title", "delete_stargift", "add_stargift", "order"]

    ID = 0x4fddbee7
    QUALNAME = "functions.payments.UpdateStarGiftCollection"

    def __init__(self, *, peer: "raw.base.InputPeer", collection_id: int, title: Optional[str] = None, delete_stargift: Optional[List["raw.base.InputSavedStarGift"]] = None, add_stargift: Optional[List["raw.base.InputSavedStarGift"]] = None, order: Optional[List["raw.base.InputSavedStarGift"]] = None) -> None:
        self.peer = peer  # InputPeer
        self.collection_id = collection_id  # int
        self.title = title  # flags.0?string
        self.delete_stargift = delete_stargift  # flags.1?Vector<InputSavedStarGift>
        self.add_stargift = add_stargift  # flags.2?Vector<InputSavedStarGift>
        self.order = order  # flags.3?Vector<InputSavedStarGift>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStarGiftCollection":

        flags = Int.read(b)

        peer = TLObject.read(b)

        collection_id = Int.read(b)

        title = String.read(b) if flags & (1 << 0) else None
        delete_stargift = TLObject.read(b) if flags & (1 << 1) else []

        add_stargift = TLObject.read(b) if flags & (1 << 2) else []

        order = TLObject.read(b) if flags & (1 << 3) else []

        return UpdateStarGiftCollection(peer=peer, collection_id=collection_id, title=title, delete_stargift=delete_stargift, add_stargift=add_stargift, order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.delete_stargift else 0
        flags |= (1 << 2) if self.add_stargift else 0
        flags |= (1 << 3) if self.order else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.collection_id))

        if self.title is not None:
            b.write(String(self.title))

        if self.delete_stargift is not None:
            b.write(Vector(self.delete_stargift))

        if self.add_stargift is not None:
            b.write(Vector(self.add_stargift))

        if self.order is not None:
            b.write(Vector(self.order))

        return b.getvalue()
