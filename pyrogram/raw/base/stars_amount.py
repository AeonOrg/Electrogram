# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StarsAmount = Union["raw.types.StarsAmount", "raw.types.StarsTonAmount"]


class StarsAmount:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StarsAmount
            StarsTonAmount
    """

    QUALNAME = "pyrogram.raw.base.StarsAmount"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
