# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

FeaturedStickers = Union["raw.types.messages.FeaturedStickers", "raw.types.messages.FeaturedStickersNotModified"]


class FeaturedStickers:  # type: ignore
    """Featured stickers

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.FeaturedStickers
            messages.FeaturedStickersNotModified

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetFeaturedStickers
            messages.GetOldFeaturedStickers
            messages.GetFeaturedEmojiStickers
    """

    QUALNAME = "pyrogram.raw.base.messages.FeaturedStickers"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
