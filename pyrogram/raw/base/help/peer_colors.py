# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PeerColors = Union["raw.types.help.PeerColors", "raw.types.help.PeerColorsNotModified"]


class PeerColors:  # type: ignore
    """Contains info about multiple color palettes ».

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.PeerColors
            help.PeerColorsNotModified

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetPeerColors
            help.GetPeerProfileColors
    """

    QUALNAME = "pyrogram.raw.base.help.PeerColors"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
