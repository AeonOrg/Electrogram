# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BotMenuButton = Union["raw.types.BotMenuButton", "raw.types.BotMenuButtonCommands", "raw.types.BotMenuButtonDefault"]


class BotMenuButton:  # type: ignore
    """Indicates the action to execute when pressing the in-UI menu button for bots

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BotMenuButton
            BotMenuButtonCommands
            BotMenuButtonDefault

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetBotMenuButton
    """

    QUALNAME = "pyrogram.raw.base.BotMenuButton"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
