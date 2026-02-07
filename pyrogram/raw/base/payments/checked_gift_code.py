# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

CheckedGiftCode = Union["raw.types.payments.CheckedGiftCode"]


class CheckedGiftCode:  # type: ignore
    """Info about a Telegram Premium Giftcode.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            payments.CheckedGiftCode

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.CheckGiftCode
    """

    QUALNAME = "pyrogram.raw.base.payments.CheckedGiftCode"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
