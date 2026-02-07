# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EmojiKeywordsDifference = Union["raw.types.EmojiKeywordsDifference"]


class EmojiKeywordsDifference:  # type: ignore
    """New emoji keywords

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            EmojiKeywordsDifference

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetEmojiKeywords
            messages.GetEmojiKeywordsDifference
    """

    QUALNAME = "pyrogram.raw.base.EmojiKeywordsDifference"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
