# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

EmojiGameInfo = Union["raw.types.messages.EmojiGameDiceInfo", "raw.types.messages.EmojiGameUnavailable"]


class EmojiGameInfo:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.EmojiGameDiceInfo
            messages.EmojiGameUnavailable

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetEmojiGameInfo
    """

    QUALNAME = "pyrogram.raw.base.messages.EmojiGameInfo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
