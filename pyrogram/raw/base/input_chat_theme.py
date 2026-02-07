# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputChatTheme = Union["raw.types.InputChatTheme", "raw.types.InputChatThemeEmpty", "raw.types.InputChatThemeUniqueGift"]


class InputChatTheme:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputChatTheme
            InputChatThemeEmpty
            InputChatThemeUniqueGift
    """

    QUALNAME = "pyrogram.raw.base.InputChatTheme"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
