# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PaymentResult = Union["raw.types.payments.PaymentResult", "raw.types.payments.PaymentVerificationNeeded"]


class PaymentResult:  # type: ignore
    """Payment result

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            payments.PaymentResult
            payments.PaymentVerificationNeeded

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.SendPaymentForm
            payments.SendStarsForm
    """

    QUALNAME = "pyrogram.raw.base.payments.PaymentResult"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
