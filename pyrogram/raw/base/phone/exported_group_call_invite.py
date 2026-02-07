# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ExportedGroupCallInvite = Union["raw.types.phone.ExportedGroupCallInvite"]


class ExportedGroupCallInvite:  # type: ignore
    """An exported group call invitation.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            phone.ExportedGroupCallInvite

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.ExportGroupCallInvite
    """

    QUALNAME = "pyrogram.raw.base.phone.ExportedGroupCallInvite"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
