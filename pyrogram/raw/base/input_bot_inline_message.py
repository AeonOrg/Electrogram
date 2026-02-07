# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputBotInlineMessage = Union["raw.types.InputBotInlineMessageGame", "raw.types.InputBotInlineMessageMediaAuto", "raw.types.InputBotInlineMessageMediaContact", "raw.types.InputBotInlineMessageMediaGeo", "raw.types.InputBotInlineMessageMediaInvoice", "raw.types.InputBotInlineMessageMediaVenue", "raw.types.InputBotInlineMessageMediaWebPage", "raw.types.InputBotInlineMessageText"]


class InputBotInlineMessage:  # type: ignore
    """Represents a sent inline message from the perspective of a bot

    Constructors:
        This base type has 8 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputBotInlineMessageGame
            InputBotInlineMessageMediaAuto
            InputBotInlineMessageMediaContact
            InputBotInlineMessageMediaGeo
            InputBotInlineMessageMediaInvoice
            InputBotInlineMessageMediaVenue
            InputBotInlineMessageMediaWebPage
            InputBotInlineMessageText
    """

    QUALNAME = "pyrogram.raw.base.InputBotInlineMessage"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
