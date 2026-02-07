# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

CheckCanSendGiftResult = Union["raw.types.payments.CheckCanSendGiftResultFail", "raw.types.payments.CheckCanSendGiftResultOk"]


class CheckCanSendGiftResult:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            payments.CheckCanSendGiftResultFail
            payments.CheckCanSendGiftResultOk

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.CheckCanSendGift
    """

    QUALNAME = "pyrogram.raw.base.payments.CheckCanSendGiftResult"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
