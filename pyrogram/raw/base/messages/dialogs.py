# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Dialogs = Union["raw.types.messages.Dialogs", "raw.types.messages.DialogsNotModified", "raw.types.messages.DialogsSlice"]


class Dialogs:  # type: ignore
    """Object contains a list of chats with messages and auxiliary data.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.Dialogs
            messages.DialogsNotModified
            messages.DialogsSlice

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDialogs
    """

    QUALNAME = "pyrogram.raw.base.messages.Dialogs"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
