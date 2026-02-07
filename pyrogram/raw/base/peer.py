# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Peer = Union["raw.types.PeerChannel", "raw.types.PeerChat", "raw.types.PeerUser"]


class Peer:  # type: ignore
    """Chat partner or group.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PeerChannel
            PeerChat
            PeerUser

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            chatlists.GetLeaveChatlistSuggestions
    """

    QUALNAME = "pyrogram.raw.base.Peer"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
