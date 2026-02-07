# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StarGiftCollection = Union["raw.types.StarGiftCollection"]


class StarGiftCollection:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StarGiftCollection

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.CreateStarGiftCollection
            payments.UpdateStarGiftCollection
    """

    QUALNAME = "pyrogram.raw.base.StarGiftCollection"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
