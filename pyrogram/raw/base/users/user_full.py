# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

UserFull = Union["raw.types.users.UserFull"]


class UserFull:  # type: ignore
    """Full user information, with attached context peers for reactions

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            users.UserFull

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            users.GetFullUser
    """

    QUALNAME = "pyrogram.raw.base.users.UserFull"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
