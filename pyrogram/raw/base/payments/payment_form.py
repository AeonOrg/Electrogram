# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PaymentForm = Union["raw.types.payments.PaymentForm", "raw.types.payments.PaymentFormStarGift", "raw.types.payments.PaymentFormStars"]


class PaymentForm:  # type: ignore
    """Payment form

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            payments.PaymentForm
            payments.PaymentFormStarGift
            payments.PaymentFormStars

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetPaymentForm
    """

    QUALNAME = "pyrogram.raw.base.payments.PaymentForm"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
