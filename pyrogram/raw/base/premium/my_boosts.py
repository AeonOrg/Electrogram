# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MyBoosts = Union["raw.types.premium.MyBoosts"]


class MyBoosts:  # type: ignore
    """A list of peers we are currently boosting, and how many boost slots we have left.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            premium.MyBoosts

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            premium.GetMyBoosts
            premium.ApplyBoost
    """

    QUALNAME = "pyrogram.raw.base.premium.MyBoosts"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
