# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

AppUpdate = Union["raw.types.help.AppUpdate", "raw.types.help.NoAppUpdate"]


class AppUpdate:  # type: ignore
    """Contains info on app update availability.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.AppUpdate
            help.NoAppUpdate

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetAppUpdate
    """

    QUALNAME = "pyrogram.raw.base.help.AppUpdate"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
