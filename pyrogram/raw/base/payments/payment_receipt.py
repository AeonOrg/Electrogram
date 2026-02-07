# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PaymentReceipt = Union["raw.types.payments.PaymentReceipt", "raw.types.payments.PaymentReceiptStars"]


class PaymentReceipt:  # type: ignore
    """Payment receipt

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            payments.PaymentReceipt
            payments.PaymentReceiptStars

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetPaymentReceipt
    """

    QUALNAME = "pyrogram.raw.base.payments.PaymentReceipt"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
