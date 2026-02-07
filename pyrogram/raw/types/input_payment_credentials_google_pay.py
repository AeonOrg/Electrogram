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


class InputPaymentCredentialsGooglePay(TLObject):  # type: ignore
    """Google Pay payment credentials

    Constructor of :obj:`~pyrogram.raw.base.InputPaymentCredentials`.

    Details:
        - Layer: ``224``
        - ID: ``8AC32801``

    Parameters:
        payment_token (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            Payment token

    """

    __slots__: List[str] = ["payment_token"]

    ID = 0x8ac32801
    QUALNAME = "types.InputPaymentCredentialsGooglePay"

    def __init__(self, *, payment_token: "raw.base.DataJSON") -> None:
        self.payment_token = payment_token  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPaymentCredentialsGooglePay":
        # No flags

        payment_token = TLObject.read(b)

        return InputPaymentCredentialsGooglePay(payment_token=payment_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.payment_token.write())

        return b.getvalue()
