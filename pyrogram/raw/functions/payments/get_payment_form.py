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


class GetPaymentForm(TLObject):  # type: ignore
    """Get a payment form


    Details:
        - Layer: ``224``
        - ID: ``37148DBB``

    Parameters:
        invoice (:obj:`InputInvoice <pyrogram.raw.base.InputInvoice>`):
            Invoice

        theme_params (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`, *optional*):
            A JSON object with the following keys, containing color theme information (integers, RGB24) to pass to the payment provider, to apply in eventual verification pages: bg_color - Background color text_color - Text color hint_color - Hint text color link_color - Link color button_color - Button color button_text_color - Button text color

    Returns:
        :obj:`payments.PaymentForm <pyrogram.raw.base.payments.PaymentForm>`
    """

    __slots__: List[str] = ["invoice", "theme_params"]

    ID = 0x37148dbb
    QUALNAME = "functions.payments.GetPaymentForm"

    def __init__(self, *, invoice: "raw.base.InputInvoice", theme_params: "raw.base.DataJSON" = None) -> None:
        self.invoice = invoice  # InputInvoice
        self.theme_params = theme_params  # flags.0?DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPaymentForm":

        flags = Int.read(b)

        invoice = TLObject.read(b)

        theme_params = TLObject.read(b) if flags & (1 << 0) else None

        return GetPaymentForm(invoice=invoice, theme_params=theme_params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.theme_params is not None else 0
        b.write(Int(flags))

        b.write(self.invoice.write())

        if self.theme_params is not None:
            b.write(self.theme_params.write())

        return b.getvalue()
