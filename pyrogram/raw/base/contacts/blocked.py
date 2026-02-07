# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Blocked = Union["raw.types.contacts.Blocked", "raw.types.contacts.BlockedSlice"]


class Blocked:  # type: ignore
    """Info on users from the current user's black list.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            contacts.Blocked
            contacts.BlockedSlice

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetBlocked
    """

    QUALNAME = "pyrogram.raw.base.contacts.Blocked"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
