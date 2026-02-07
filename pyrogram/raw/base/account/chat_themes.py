# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChatThemes = Union["raw.types.account.ChatThemes", "raw.types.account.ChatThemesNotModified"]


class ChatThemes:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.ChatThemes
            account.ChatThemesNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetUniqueGiftChatThemes
    """

    QUALNAME = "pyrogram.raw.base.account.ChatThemes"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
