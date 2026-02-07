# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BoostsList = Union["raw.types.premium.BoostsList"]


class BoostsList:  # type: ignore
    """List of boosts that were applied to a peer by multiple users.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            premium.BoostsList

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            premium.GetBoostsList
            premium.GetUserBoosts
    """

    QUALNAME = "pyrogram.raw.base.premium.BoostsList"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
