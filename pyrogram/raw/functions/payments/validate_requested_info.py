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


class ValidateRequestedInfo(TLObject):  # type: ignore
    """Submit requested order information for validation


    Details:
        - Layer: ``224``
        - ID: ``B6C8F12B``

    Parameters:
        invoice (:obj:`InputInvoice <pyrogram.raw.base.InputInvoice>`):
            Invoice

        info (:obj:`PaymentRequestedInfo <pyrogram.raw.base.PaymentRequestedInfo>`):
            Requested order information

        save (``bool``, *optional*):
            Save order information to re-use it for future orders

    Returns:
        :obj:`payments.ValidatedRequestedInfo <pyrogram.raw.base.payments.ValidatedRequestedInfo>`
    """

    __slots__: List[str] = ["invoice", "info", "save"]

    ID = 0xb6c8f12b
    QUALNAME = "functions.payments.ValidateRequestedInfo"

    def __init__(self, *, invoice: "raw.base.InputInvoice", info: "raw.base.PaymentRequestedInfo", save: Optional[bool] = None) -> None:
        self.invoice = invoice  # InputInvoice
        self.info = info  # PaymentRequestedInfo
        self.save = save  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ValidateRequestedInfo":

        flags = Int.read(b)

        save = True if flags & (1 << 0) else False
        invoice = TLObject.read(b)

        info = TLObject.read(b)

        return ValidateRequestedInfo(invoice=invoice, info=info, save=save)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.save else 0
        b.write(Int(flags))

        b.write(self.invoice.write())

        b.write(self.info.write())

        return b.getvalue()
