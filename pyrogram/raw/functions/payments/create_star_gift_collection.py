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


class CreateStarGiftCollection(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``1F4A0E87``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        title (``str``):
            N/A

        stargift (List of :obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`):
            N/A

    Returns:
        :obj:`StarGiftCollection <pyrogram.raw.base.StarGiftCollection>`
    """

    __slots__: List[str] = ["peer", "title", "stargift"]

    ID = 0x1f4a0e87
    QUALNAME = "functions.payments.CreateStarGiftCollection"

    def __init__(self, *, peer: "raw.base.InputPeer", title: str, stargift: List["raw.base.InputSavedStarGift"]) -> None:
        self.peer = peer  # InputPeer
        self.title = title  # string
        self.stargift = stargift  # Vector<InputSavedStarGift>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateStarGiftCollection":
        # No flags

        peer = TLObject.read(b)

        title = String.read(b)

        stargift = TLObject.read(b)

        return CreateStarGiftCollection(peer=peer, title=title, stargift=stargift)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(String(self.title))

        b.write(Vector(self.stargift))

        return b.getvalue()
