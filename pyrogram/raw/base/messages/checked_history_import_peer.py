# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

CheckedHistoryImportPeer = Union["raw.types.messages.CheckedHistoryImportPeer"]


class CheckedHistoryImportPeer:  # type: ignore
    """Contains a confirmation text to be shown to the user, upon importing chat history, click here for more info ».

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.CheckedHistoryImportPeer

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.CheckHistoryImportPeer
    """

    QUALNAME = "pyrogram.raw.base.messages.CheckedHistoryImportPeer"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
