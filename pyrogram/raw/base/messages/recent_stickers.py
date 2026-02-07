# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

RecentStickers = Union["raw.types.messages.RecentStickers", "raw.types.messages.RecentStickersNotModified"]


class RecentStickers:  # type: ignore
    """Recent stickers

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.RecentStickers
            messages.RecentStickersNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetRecentStickers
    """

    QUALNAME = "pyrogram.raw.base.messages.RecentStickers"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
