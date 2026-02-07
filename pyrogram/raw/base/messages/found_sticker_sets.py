# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

FoundStickerSets = Union["raw.types.messages.FoundStickerSets", "raw.types.messages.FoundStickerSetsNotModified"]


class FoundStickerSets:  # type: ignore
    """Found stickersets

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.FoundStickerSets
            messages.FoundStickerSetsNotModified

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.SearchStickerSets
            messages.SearchEmojiStickerSets
    """

    QUALNAME = "pyrogram.raw.base.messages.FoundStickerSets"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
