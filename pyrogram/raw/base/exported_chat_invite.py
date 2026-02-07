# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ExportedChatInvite = Union["raw.types.ChatInviteExported", "raw.types.ChatInvitePublicJoinRequests"]


class ExportedChatInvite:  # type: ignore
    """Exported chat invite

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChatInviteExported
            ChatInvitePublicJoinRequests

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ExportChatInvite
    """

    QUALNAME = "pyrogram.raw.base.ExportedChatInvite"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
