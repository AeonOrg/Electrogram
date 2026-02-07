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


class AssignPlayMarketTransaction(TLObject):  # type: ignore
    """Informs server about a purchase made through the Play Store: for official applications only.


    Details:
        - Layer: ``224``
        - ID: ``DFFD50D3``

    Parameters:
        receipt (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            Receipt

        purpose (:obj:`InputStorePaymentPurpose <pyrogram.raw.base.InputStorePaymentPurpose>`):
            Payment purpose

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["receipt", "purpose"]

    ID = 0xdffd50d3
    QUALNAME = "functions.payments.AssignPlayMarketTransaction"

    def __init__(self, *, receipt: "raw.base.DataJSON", purpose: "raw.base.InputStorePaymentPurpose") -> None:
        self.receipt = receipt  # DataJSON
        self.purpose = purpose  # InputStorePaymentPurpose

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AssignPlayMarketTransaction":
        # No flags

        receipt = TLObject.read(b)

        purpose = TLObject.read(b)

        return AssignPlayMarketTransaction(receipt=receipt, purpose=purpose)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.receipt.write())

        b.write(self.purpose.write())

        return b.getvalue()
