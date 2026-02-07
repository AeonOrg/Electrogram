# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

RecentMeUrls = Union["raw.types.help.RecentMeUrls"]


class RecentMeUrls:  # type: ignore
    """Recent t.me URLs

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.RecentMeUrls

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetRecentMeUrls
    """

    QUALNAME = "pyrogram.raw.base.help.RecentMeUrls"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
