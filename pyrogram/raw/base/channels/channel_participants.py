# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChannelParticipants = Union["raw.types.channels.ChannelParticipants", "raw.types.channels.ChannelParticipantsNotModified"]


class ChannelParticipants:  # type: ignore
    """Channel/supergroup participants

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            channels.ChannelParticipants
            channels.ChannelParticipantsNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            channels.GetParticipants
    """

    QUALNAME = "pyrogram.raw.base.channels.ChannelParticipants"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
