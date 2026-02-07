# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChannelParticipantsFilter = Union["raw.types.ChannelParticipantsAdmins", "raw.types.ChannelParticipantsBanned", "raw.types.ChannelParticipantsBots", "raw.types.ChannelParticipantsContacts", "raw.types.ChannelParticipantsKicked", "raw.types.ChannelParticipantsMentions", "raw.types.ChannelParticipantsRecent", "raw.types.ChannelParticipantsSearch"]


class ChannelParticipantsFilter:  # type: ignore
    """Filter for fetching channel participants

    Constructors:
        This base type has 8 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChannelParticipantsAdmins
            ChannelParticipantsBanned
            ChannelParticipantsBots
            ChannelParticipantsContacts
            ChannelParticipantsKicked
            ChannelParticipantsMentions
            ChannelParticipantsRecent
            ChannelParticipantsSearch
    """

    QUALNAME = "pyrogram.raw.base.ChannelParticipantsFilter"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
