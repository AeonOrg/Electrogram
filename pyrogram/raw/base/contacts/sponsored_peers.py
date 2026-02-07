# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SponsoredPeers = Union["raw.types.contacts.SponsoredPeers", "raw.types.contacts.SponsoredPeersEmpty"]


class SponsoredPeers:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            contacts.SponsoredPeers
            contacts.SponsoredPeersEmpty

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetSponsoredPeers
    """

    QUALNAME = "pyrogram.raw.base.contacts.SponsoredPeers"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
