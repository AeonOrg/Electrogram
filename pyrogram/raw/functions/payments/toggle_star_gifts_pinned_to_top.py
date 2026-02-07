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


class ToggleStarGiftsPinnedToTop(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``1513E7B0``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        stargift (List of :obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "stargift"]

    ID = 0x1513e7b0
    QUALNAME = "functions.payments.ToggleStarGiftsPinnedToTop"

    def __init__(self, *, peer: "raw.base.InputPeer", stargift: List["raw.base.InputSavedStarGift"]) -> None:
        self.peer = peer  # InputPeer
        self.stargift = stargift  # Vector<InputSavedStarGift>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleStarGiftsPinnedToTop":
        # No flags

        peer = TLObject.read(b)

        stargift = TLObject.read(b)

        return ToggleStarGiftsPinnedToTop(peer=peer, stargift=stargift)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Vector(self.stargift))

        return b.getvalue()
