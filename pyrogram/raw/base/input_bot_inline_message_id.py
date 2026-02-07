# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputBotInlineMessageID = Union["raw.types.InputBotInlineMessageID", "raw.types.InputBotInlineMessageID64"]


class InputBotInlineMessageID:  # type: ignore
    """Represents a sent inline message from the perspective of a bot

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputBotInlineMessageID
            InputBotInlineMessageID64
    """

    QUALNAME = "pyrogram.raw.base.InputBotInlineMessageID"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
