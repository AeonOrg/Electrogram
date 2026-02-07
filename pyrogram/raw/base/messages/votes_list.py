# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

VotesList = Union["raw.types.messages.VotesList"]


class VotesList:  # type: ignore
    """How users voted in a poll

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.VotesList

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetPollVotes
    """

    QUALNAME = "pyrogram.raw.base.messages.VotesList"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
