# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BotCommand = Union["raw.types.BotCommand"]


class BotCommand:  # type: ignore
    """Describes a bot command that can be used in a chat

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BotCommand

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetBotCommands
    """

    QUALNAME = "pyrogram.raw.base.BotCommand"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
