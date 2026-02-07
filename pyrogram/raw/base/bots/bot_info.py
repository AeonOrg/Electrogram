# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BotInfo = Union["raw.types.bots.BotInfo"]


class BotInfo:  # type: ignore
    """Localized name, about text and description of a bot.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            bots.BotInfo

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetBotInfo
    """

    QUALNAME = "pyrogram.raw.base.bots.BotInfo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
