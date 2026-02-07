# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EmojiList = Union["raw.types.EmojiList", "raw.types.EmojiListNotModified"]


class EmojiList:  # type: ignore
    """Represents a list of custom emojis.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            EmojiList
            EmojiListNotModified

    Functions:
        This object can be returned by 5 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetDefaultProfilePhotoEmojis
            account.GetDefaultGroupPhotoEmojis
            account.GetDefaultBackgroundEmojis
            account.GetChannelRestrictedStatusEmojis
            messages.SearchCustomEmoji
    """

    QUALNAME = "pyrogram.raw.base.EmojiList"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
