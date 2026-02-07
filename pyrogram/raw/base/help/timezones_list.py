# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

TimezonesList = Union["raw.types.help.TimezonesList", "raw.types.help.TimezonesListNotModified"]


class TimezonesList:  # type: ignore
    """

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.TimezonesList
            help.TimezonesListNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetTimezonesList
    """

    QUALNAME = "pyrogram.raw.base.help.TimezonesList"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
