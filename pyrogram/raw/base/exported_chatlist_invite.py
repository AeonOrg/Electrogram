# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ExportedChatlistInvite = Union["raw.types.ExportedChatlistInvite"]


class ExportedChatlistInvite:  # type: ignore
    """An exported chat folder deep link ».

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ExportedChatlistInvite

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            chatlists.EditExportedInvite
    """

    QUALNAME = "pyrogram.raw.base.ExportedChatlistInvite"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
