# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MessageViews = Union["raw.types.messages.MessageViews"]


class MessageViews:  # type: ignore
    """View, forward counter + info about replies

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.MessageViews

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetMessagesViews
    """

    QUALNAME = "pyrogram.raw.base.messages.MessageViews"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
