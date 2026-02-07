# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChatFull = Union["raw.types.messages.ChatFull"]


class ChatFull:  # type: ignore
    """Full info about a channel, supergroup, gigagroup or basic group.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.ChatFull

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetFullChat
            channels.GetFullChannel
    """

    QUALNAME = "pyrogram.raw.base.messages.ChatFull"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
