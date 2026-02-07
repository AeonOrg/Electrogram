# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PeerColor = Union["raw.types.InputPeerColorCollectible", "raw.types.PeerColor", "raw.types.PeerColorCollectible"]


class PeerColor:  # type: ignore
    """Represents a color palette ».

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputPeerColorCollectible
            PeerColor
            PeerColorCollectible
    """

    QUALNAME = "pyrogram.raw.base.PeerColor"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
