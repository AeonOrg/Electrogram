# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EmojiKeyword = Union["raw.types.EmojiKeyword", "raw.types.EmojiKeywordDeleted"]


class EmojiKeyword:  # type: ignore
    """Emoji keyword

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            EmojiKeyword
            EmojiKeywordDeleted
    """

    QUALNAME = "pyrogram.raw.base.EmojiKeyword"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
