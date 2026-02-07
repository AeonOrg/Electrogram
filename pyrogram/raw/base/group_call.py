# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

GroupCall = Union["raw.types.GroupCall", "raw.types.GroupCallDiscarded"]


class GroupCall:  # type: ignore
    """A group call

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            GroupCall
            GroupCallDiscarded
    """

    QUALNAME = "pyrogram.raw.base.GroupCall"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
