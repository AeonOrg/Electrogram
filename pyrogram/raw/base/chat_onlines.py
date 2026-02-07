# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChatOnlines = Union["raw.types.ChatOnlines"]


class ChatOnlines:  # type: ignore
    """Number of online users in a chat

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChatOnlines

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetOnlines
    """

    QUALNAME = "pyrogram.raw.base.ChatOnlines"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
