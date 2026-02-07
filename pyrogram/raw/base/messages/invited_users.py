# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InvitedUsers = Union["raw.types.messages.InvitedUsers"]


class InvitedUsers:  # type: ignore
    """

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.InvitedUsers

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.AddChatUser
            messages.CreateChat
            channels.InviteToChannel
    """

    QUALNAME = "pyrogram.raw.base.messages.InvitedUsers"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
