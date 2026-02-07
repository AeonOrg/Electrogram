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


class PaymentFormStarGift(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.PaymentForm`.

    Details:
        - Layer: ``224``
        - ID: ``B425CFE1``

    Parameters:
        form_id (``int`` ``64-bit``):
            N/A

        invoice (:obj:`Invoice <pyrogram.raw.base.Invoice>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetPaymentForm
    """

    __slots__: List[str] = ["form_id", "invoice"]

    ID = 0xb425cfe1
    QUALNAME = "types.payments.PaymentFormStarGift"

    def __init__(self, *, form_id: int, invoice: "raw.base.Invoice") -> None:
        self.form_id = form_id  # long
        self.invoice = invoice  # Invoice

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentFormStarGift":
        # No flags

        form_id = Long.read(b)

        invoice = TLObject.read(b)

        return PaymentFormStarGift(form_id=form_id, invoice=invoice)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.form_id))

        b.write(self.invoice.write())

        return b.getvalue()
