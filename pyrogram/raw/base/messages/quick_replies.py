# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

QuickReplies = Union["raw.types.messages.QuickReplies", "raw.types.messages.QuickRepliesNotModified"]


class QuickReplies:  # type: ignore
    """

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.QuickReplies
            messages.QuickRepliesNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetQuickReplies
    """

    QUALNAME = "pyrogram.raw.base.messages.QuickReplies"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
