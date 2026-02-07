# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChatParticipant = Union["raw.types.ChatParticipant", "raw.types.ChatParticipantAdmin", "raw.types.ChatParticipantCreator"]


class ChatParticipant:  # type: ignore
    """Details of a group member.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChatParticipant
            ChatParticipantAdmin
            ChatParticipantCreator
    """

    QUALNAME = "pyrogram.raw.base.ChatParticipant"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
