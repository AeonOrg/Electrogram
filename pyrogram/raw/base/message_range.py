# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MessageRange = Union["raw.types.MessageRange"]


class MessageRange:  # type: ignore
    """Indicates a range of chat messages

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            MessageRange

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSplitRanges
    """

    QUALNAME = "pyrogram.raw.base.MessageRange"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
