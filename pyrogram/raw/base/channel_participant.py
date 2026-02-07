# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChannelParticipant = Union["raw.types.ChannelParticipant", "raw.types.ChannelParticipantAdmin", "raw.types.ChannelParticipantBanned", "raw.types.ChannelParticipantCreator", "raw.types.ChannelParticipantLeft", "raw.types.ChannelParticipantSelf"]


class ChannelParticipant:  # type: ignore
    """Channel participant

    Constructors:
        This base type has 6 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChannelParticipant
            ChannelParticipantAdmin
            ChannelParticipantBanned
            ChannelParticipantCreator
            ChannelParticipantLeft
            ChannelParticipantSelf
    """

    QUALNAME = "pyrogram.raw.base.ChannelParticipant"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
