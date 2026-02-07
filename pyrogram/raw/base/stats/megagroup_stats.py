# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MegagroupStats = Union["raw.types.stats.MegagroupStats"]


class MegagroupStats:  # type: ignore
    """Supergroup statistics

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            stats.MegagroupStats

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.GetMegagroupStats
    """

    QUALNAME = "pyrogram.raw.base.stats.MegagroupStats"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
