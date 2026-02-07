# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ExportedChatInvite = Union["raw.types.messages.ExportedChatInvite", "raw.types.messages.ExportedChatInviteReplaced"]


class ExportedChatInvite:  # type: ignore
    """Contains info about a chat invite, and eventually a pointer to the newest chat invite.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.ExportedChatInvite
            messages.ExportedChatInviteReplaced

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetExportedChatInvite
            messages.EditExportedChatInvite
    """

    QUALNAME = "pyrogram.raw.base.messages.ExportedChatInvite"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
