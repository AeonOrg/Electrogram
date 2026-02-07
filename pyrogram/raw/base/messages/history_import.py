# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

HistoryImport = Union["raw.types.messages.HistoryImport"]


class HistoryImport:  # type: ignore
    """Identifier of a history import session, click here for more info ».

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.HistoryImport

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.InitHistoryImport
    """

    QUALNAME = "pyrogram.raw.base.messages.HistoryImport"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
