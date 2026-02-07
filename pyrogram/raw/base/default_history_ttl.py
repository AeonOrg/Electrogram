# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

DefaultHistoryTTL = Union["raw.types.DefaultHistoryTTL"]


class DefaultHistoryTTL:  # type: ignore
    """Contains info about the default value of the Time-To-Live setting, applied to all new chats.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            DefaultHistoryTTL

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDefaultHistoryTTL
    """

    QUALNAME = "pyrogram.raw.base.DefaultHistoryTTL"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
