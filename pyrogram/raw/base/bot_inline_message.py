# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BotInlineMessage = Union["raw.types.BotInlineMessageMediaAuto", "raw.types.BotInlineMessageMediaContact", "raw.types.BotInlineMessageMediaGeo", "raw.types.BotInlineMessageMediaInvoice", "raw.types.BotInlineMessageMediaVenue", "raw.types.BotInlineMessageMediaWebPage", "raw.types.BotInlineMessageText"]


class BotInlineMessage:  # type: ignore
    """Inline message

    Constructors:
        This base type has 7 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BotInlineMessageMediaAuto
            BotInlineMessageMediaContact
            BotInlineMessageMediaGeo
            BotInlineMessageMediaInvoice
            BotInlineMessageMediaVenue
            BotInlineMessageMediaWebPage
            BotInlineMessageText
    """

    QUALNAME = "pyrogram.raw.base.BotInlineMessage"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
