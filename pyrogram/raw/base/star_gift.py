# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StarGift = Union["raw.types.StarGift", "raw.types.StarGiftUnique"]


class StarGift:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StarGift
            StarGiftUnique
    """

    QUALNAME = "pyrogram.raw.base.StarGift"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
