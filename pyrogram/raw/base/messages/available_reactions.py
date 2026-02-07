# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

AvailableReactions = Union["raw.types.messages.AvailableReactions", "raw.types.messages.AvailableReactionsNotModified"]


class AvailableReactions:  # type: ignore
    """Animations and metadata associated with message reactions »

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.AvailableReactions
            messages.AvailableReactionsNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAvailableReactions
    """

    QUALNAME = "pyrogram.raw.base.messages.AvailableReactions"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
