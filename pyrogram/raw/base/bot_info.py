# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BotInfo = Union["raw.types.BotInfo"]


class BotInfo:  # type: ignore
    """Info about bots (available bot commands, etc)

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BotInfo
    """

    QUALNAME = "pyrogram.raw.base.BotInfo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
