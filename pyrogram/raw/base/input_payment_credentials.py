# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputPaymentCredentials = Union["raw.types.InputPaymentCredentials", "raw.types.InputPaymentCredentialsApplePay", "raw.types.InputPaymentCredentialsGooglePay", "raw.types.InputPaymentCredentialsSaved"]


class InputPaymentCredentials:  # type: ignore
    """Payment credentials

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputPaymentCredentials
            InputPaymentCredentialsApplePay
            InputPaymentCredentialsGooglePay
            InputPaymentCredentialsSaved
    """

    QUALNAME = "pyrogram.raw.base.InputPaymentCredentials"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
