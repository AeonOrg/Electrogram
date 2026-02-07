# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

TopPeers = Union["raw.types.contacts.TopPeers", "raw.types.contacts.TopPeersDisabled", "raw.types.contacts.TopPeersNotModified"]


class TopPeers:  # type: ignore
    """Top peers

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            contacts.TopPeers
            contacts.TopPeersDisabled
            contacts.TopPeersNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetTopPeers
    """

    QUALNAME = "pyrogram.raw.base.contacts.TopPeers"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
