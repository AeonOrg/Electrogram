# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EmojiStatus = Union["raw.types.EmojiStatus", "raw.types.EmojiStatusCollectible", "raw.types.EmojiStatusEmpty", "raw.types.InputEmojiStatusCollectible"]


class EmojiStatus:  # type: ignore
    """Emoji status

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            EmojiStatus
            EmojiStatusCollectible
            EmojiStatusEmpty
            InputEmojiStatusCollectible
    """

    QUALNAME = "pyrogram.raw.base.EmojiStatus"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
