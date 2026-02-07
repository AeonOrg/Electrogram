# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

AffectedHistory = Union["raw.types.messages.AffectedHistory"]


class AffectedHistory:  # type: ignore
    """Object contains info on affected part of communication history with the user or in a chat.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.AffectedHistory

    Functions:
        This object can be returned by 7 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.DeleteHistory
            messages.ReadMentions
            messages.UnpinAllMessages
            messages.ReadReactions
            messages.DeleteSavedHistory
            messages.DeleteTopicHistory
            channels.DeleteParticipantHistory
    """

    QUALNAME = "pyrogram.raw.base.messages.AffectedHistory"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
