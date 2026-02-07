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


class SaveStarGift(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``2A2A697C``

    Parameters:
        stargift (:obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`):
            N/A

        unsave (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["stargift", "unsave"]

    ID = 0x2a2a697c
    QUALNAME = "functions.payments.SaveStarGift"

    def __init__(self, *, stargift: "raw.base.InputSavedStarGift", unsave: Optional[bool] = None) -> None:
        self.stargift = stargift  # InputSavedStarGift
        self.unsave = unsave  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveStarGift":

        flags = Int.read(b)

        unsave = True if flags & (1 << 0) else False
        stargift = TLObject.read(b)

        return SaveStarGift(stargift=stargift, unsave=unsave)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.unsave else 0
        b.write(Int(flags))

        b.write(self.stargift.write())

        return b.getvalue()
