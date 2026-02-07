# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChannelDifference = Union["raw.types.updates.ChannelDifference", "raw.types.updates.ChannelDifferenceEmpty", "raw.types.updates.ChannelDifferenceTooLong"]


class ChannelDifference:  # type: ignore
    """Contains the difference (new messages) between our local channel state and the remote state

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            updates.ChannelDifference
            updates.ChannelDifferenceEmpty
            updates.ChannelDifferenceTooLong

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            updates.GetChannelDifference
    """

    QUALNAME = "pyrogram.raw.base.updates.ChannelDifference"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
