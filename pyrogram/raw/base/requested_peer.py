# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

RequestedPeer = Union["raw.types.RequestedPeerChannel", "raw.types.RequestedPeerChat", "raw.types.RequestedPeerUser"]


class RequestedPeer:  # type: ignore
    """

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            RequestedPeerChannel
            RequestedPeerChat
            RequestedPeerUser
    """

    QUALNAME = "pyrogram.raw.base.RequestedPeer"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
