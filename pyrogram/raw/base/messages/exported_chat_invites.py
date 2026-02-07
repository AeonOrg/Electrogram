# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ExportedChatInvites = Union["raw.types.messages.ExportedChatInvites"]


class ExportedChatInvites:  # type: ignore
    """Info about chat invites exported by a certain admin.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.ExportedChatInvites

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetExportedChatInvites
    """

    QUALNAME = "pyrogram.raw.base.messages.ExportedChatInvites"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
