# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SecureValue = Union["raw.types.SecureValue"]


class SecureValue:  # type: ignore
    """Secure Telegram Passport value

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            SecureValue

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetAllSecureValues
            account.GetSecureValue
            account.SaveSecureValue
    """

    QUALNAME = "pyrogram.raw.base.SecureValue"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
