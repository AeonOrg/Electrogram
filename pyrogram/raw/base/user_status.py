# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

UserStatus = Union["raw.types.UserStatusEmpty", "raw.types.UserStatusHidden", "raw.types.UserStatusLastMonth", "raw.types.UserStatusLastWeek", "raw.types.UserStatusOffline", "raw.types.UserStatusOnline", "raw.types.UserStatusRecently"]


class UserStatus:  # type: ignore
    """User online status

    Constructors:
        This base type has 7 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            UserStatusEmpty
            UserStatusHidden
            UserStatusLastMonth
            UserStatusLastWeek
            UserStatusOffline
            UserStatusOnline
            UserStatusRecently
    """

    QUALNAME = "pyrogram.raw.base.UserStatus"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
