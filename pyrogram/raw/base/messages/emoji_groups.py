# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EmojiGroups = Union["raw.types.messages.EmojiGroups", "raw.types.messages.EmojiGroupsNotModified"]


class EmojiGroups:  # type: ignore
    """Represents a list of emoji categories.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.EmojiGroups
            messages.EmojiGroupsNotModified

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetEmojiGroups
            messages.GetEmojiStatusGroups
            messages.GetEmojiProfilePhotoGroups
            messages.GetEmojiStickerGroups
    """

    QUALNAME = "pyrogram.raw.base.messages.EmojiGroups"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
