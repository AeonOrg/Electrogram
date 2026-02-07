# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputBotInlineResult = Union["raw.types.InputBotInlineResult", "raw.types.InputBotInlineResultDocument", "raw.types.InputBotInlineResultGame", "raw.types.InputBotInlineResultPhoto"]


class InputBotInlineResult:  # type: ignore
    """Inline bot result

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputBotInlineResult
            InputBotInlineResultDocument
            InputBotInlineResultGame
            InputBotInlineResultPhoto
    """

    QUALNAME = "pyrogram.raw.base.InputBotInlineResult"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
