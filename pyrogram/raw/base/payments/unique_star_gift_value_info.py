# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

UniqueStarGiftValueInfo = Union["raw.types.payments.UniqueStarGiftValueInfo"]


class UniqueStarGiftValueInfo:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            payments.UniqueStarGiftValueInfo

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetUniqueStarGiftValueInfo
    """

    QUALNAME = "pyrogram.raw.base.payments.UniqueStarGiftValueInfo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
