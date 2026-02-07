# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MessageStats = Union["raw.types.stats.MessageStats"]


class MessageStats:  # type: ignore
    """Message statistics

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            stats.MessageStats

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.GetMessageStats
    """

    QUALNAME = "pyrogram.raw.base.stats.MessageStats"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
