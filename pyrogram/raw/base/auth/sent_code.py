# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SentCode = Union["raw.types.auth.SentCode", "raw.types.auth.SentCodePaymentRequired", "raw.types.auth.SentCodeSuccess"]


class SentCode:  # type: ignore
    """Contains info on a confirmation code message sent via SMS, phone call or Telegram.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            auth.SentCode
            auth.SentCodePaymentRequired
            auth.SentCodeSuccess

    Functions:
        This object can be returned by 7 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.SendCode
            auth.ResendCode
            auth.ResetLoginEmail
            auth.CheckPaidAuth
            account.SendChangePhoneCode
            account.SendConfirmPhoneCode
            account.SendVerifyPhoneCode
    """

    QUALNAME = "pyrogram.raw.base.auth.SentCode"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
