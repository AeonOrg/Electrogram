# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BotCallbackAnswer = Union["raw.types.messages.BotCallbackAnswer"]


class BotCallbackAnswer:  # type: ignore
    """Callback answer of bot

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.BotCallbackAnswer

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetBotCallbackAnswer
    """

    QUALNAME = "pyrogram.raw.base.messages.BotCallbackAnswer"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
