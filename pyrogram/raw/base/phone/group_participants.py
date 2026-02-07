# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

GroupParticipants = Union["raw.types.phone.GroupParticipants"]


class GroupParticipants:  # type: ignore
    """Info about the participants of a group call or livestream

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            phone.GroupParticipants

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.GetGroupParticipants
    """

    QUALNAME = "pyrogram.raw.base.phone.GroupParticipants"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
