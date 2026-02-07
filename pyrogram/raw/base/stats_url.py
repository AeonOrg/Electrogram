# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StatsURL = Union["raw.types.StatsURL"]


class StatsURL:  # type: ignore
    """URL with chat statistics

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StatsURL

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetStatsURL
    """

    QUALNAME = "pyrogram.raw.base.StatsURL"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
