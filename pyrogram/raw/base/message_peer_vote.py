# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MessagePeerVote = Union["raw.types.MessagePeerVote", "raw.types.MessagePeerVoteInputOption", "raw.types.MessagePeerVoteMultiple"]


class MessagePeerVote:  # type: ignore
    """How a user voted in a poll

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            MessagePeerVote
            MessagePeerVoteInputOption
            MessagePeerVoteMultiple
    """

    QUALNAME = "pyrogram.raw.base.MessagePeerVote"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
