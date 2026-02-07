# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ReplyMarkup = Union["raw.types.ReplyInlineMarkup", "raw.types.ReplyKeyboardForceReply", "raw.types.ReplyKeyboardHide", "raw.types.ReplyKeyboardMarkup"]


class ReplyMarkup:  # type: ignore
    """Reply markup for bot and inline keyboards

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ReplyInlineMarkup
            ReplyKeyboardForceReply
            ReplyKeyboardHide
            ReplyKeyboardMarkup
    """

    QUALNAME = "pyrogram.raw.base.ReplyMarkup"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
