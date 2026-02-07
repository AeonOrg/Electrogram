# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PaymentSavedCredentials = Union["raw.types.PaymentSavedCredentialsCard"]


class PaymentSavedCredentials:  # type: ignore
    """Saved payment credentials

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PaymentSavedCredentialsCard
    """

    QUALNAME = "pyrogram.raw.base.PaymentSavedCredentials"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
