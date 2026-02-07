# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Stickers = Union["raw.types.messages.Stickers", "raw.types.messages.StickersNotModified"]


class Stickers:  # type: ignore
    """Stickers

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.Stickers
            messages.StickersNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetStickers
    """

    QUALNAME = "pyrogram.raw.base.messages.Stickers"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
