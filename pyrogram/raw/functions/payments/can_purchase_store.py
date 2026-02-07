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


class CanPurchaseStore(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``4FDC5EA7``

    Parameters:
        purpose (:obj:`InputStorePaymentPurpose <pyrogram.raw.base.InputStorePaymentPurpose>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["purpose"]

    ID = 0x4fdc5ea7
    QUALNAME = "functions.payments.CanPurchaseStore"

    def __init__(self, *, purpose: "raw.base.InputStorePaymentPurpose") -> None:
        self.purpose = purpose  # InputStorePaymentPurpose

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CanPurchaseStore":
        # No flags

        purpose = TLObject.read(b)

        return CanPurchaseStore(purpose=purpose)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.purpose.write())

        return b.getvalue()
