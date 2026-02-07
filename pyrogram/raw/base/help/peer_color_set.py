# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PeerColorSet = Union["raw.types.help.PeerColorProfileSet", "raw.types.help.PeerColorSet"]


class PeerColorSet:  # type: ignore
    """Contains info about a color palette ».

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.PeerColorProfileSet
            help.PeerColorSet
    """

    QUALNAME = "pyrogram.raw.base.help.PeerColorSet"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
