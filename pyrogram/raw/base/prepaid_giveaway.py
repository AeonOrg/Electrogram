# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PrepaidGiveaway = Union["raw.types.PrepaidGiveaway", "raw.types.PrepaidStarsGiveaway"]


class PrepaidGiveaway:  # type: ignore
    """Contains info about a prepaid giveaway ».

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PrepaidGiveaway
            PrepaidStarsGiveaway
    """

    QUALNAME = "pyrogram.raw.base.PrepaidGiveaway"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
