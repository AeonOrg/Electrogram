# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

User = Union["raw.types.User", "raw.types.UserEmpty"]


class User:  # type: ignore
    """Object defines a user.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            User
            UserEmpty

    Functions:
        This object can be returned by 9 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.UpdateProfile
            account.UpdateUsername
            account.ChangePhone
            users.GetUsers
            contacts.ImportContactToken
            contacts.ImportCard
            channels.GetMessageAuthor
            channels.GetFutureCreatorAfterLeave
            bots.GetAdminedBots
    """

    QUALNAME = "pyrogram.raw.base.User"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
