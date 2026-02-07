# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChatParticipants = Union["raw.types.ChatParticipants", "raw.types.ChatParticipantsForbidden"]


class ChatParticipants:  # type: ignore
    """Object contains info on group members.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChatParticipants
            ChatParticipantsForbidden
    """

    QUALNAME = "pyrogram.raw.base.ChatParticipants"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
