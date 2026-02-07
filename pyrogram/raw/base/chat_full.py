# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChatFull = Union["raw.types.ChannelFull", "raw.types.ChatFull"]


class ChatFull:  # type: ignore
    """Full info about a channel, supergroup, gigagroup or basic group.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChannelFull
            ChatFull
    """

    QUALNAME = "pyrogram.raw.base.ChatFull"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
