# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BoostsStatus = Union["raw.types.premium.BoostsStatus"]


class BoostsStatus:  # type: ignore
    """Contains info about the current boost status of a peer.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            premium.BoostsStatus

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            premium.GetBoostsStatus
    """

    QUALNAME = "pyrogram.raw.base.premium.BoostsStatus"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
