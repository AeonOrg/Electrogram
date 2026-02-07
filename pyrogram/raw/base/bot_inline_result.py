# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BotInlineResult = Union["raw.types.BotInlineMediaResult", "raw.types.BotInlineResult"]


class BotInlineResult:  # type: ignore
    """Results of an inline query

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BotInlineMediaResult
            BotInlineResult
    """

    QUALNAME = "pyrogram.raw.base.BotInlineResult"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
