# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InviteText = Union["raw.types.help.InviteText"]


class InviteText:  # type: ignore
    """Object contains info on the text of a message with an invitation.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.InviteText

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetInviteText
    """

    QUALNAME = "pyrogram.raw.base.help.InviteText"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
