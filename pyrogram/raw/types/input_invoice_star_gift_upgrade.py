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


class InputInvoiceStarGiftUpgrade(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``224``
        - ID: ``4D818D5D``

    Parameters:
        stargift (:obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`):
            N/A

        keep_original_details (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["stargift", "keep_original_details"]

    ID = 0x4d818d5d
    QUALNAME = "types.InputInvoiceStarGiftUpgrade"

    def __init__(self, *, stargift: "raw.base.InputSavedStarGift", keep_original_details: Optional[bool] = None) -> None:
        self.stargift = stargift  # InputSavedStarGift
        self.keep_original_details = keep_original_details  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceStarGiftUpgrade":

        flags = Int.read(b)

        keep_original_details = True if flags & (1 << 0) else False
        stargift = TLObject.read(b)

        return InputInvoiceStarGiftUpgrade(stargift=stargift, keep_original_details=keep_original_details)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.keep_original_details else 0
        b.write(Int(flags))

        b.write(self.stargift.write())

        return b.getvalue()
