# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ReadParticipantDate = Union["raw.types.ReadParticipantDate"]


class ReadParticipantDate:  # type: ignore
    """Contains info about when a certain participant has read a message

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ReadParticipantDate

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetMessageReadParticipants
    """

    QUALNAME = "pyrogram.raw.base.ReadParticipantDate"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
