# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BotResults = Union["raw.types.messages.BotResults"]


class BotResults:  # type: ignore
    """Result of a query to an inline bot

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.BotResults

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetInlineBotResults
    """

    QUALNAME = "pyrogram.raw.base.messages.BotResults"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
