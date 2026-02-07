# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PeerLocated = Union["raw.types.PeerLocated", "raw.types.PeerSelfLocated"]


class PeerLocated:  # type: ignore
    """Geolocated peer

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PeerLocated
            PeerSelfLocated
    """

    QUALNAME = "pyrogram.raw.base.PeerLocated"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
