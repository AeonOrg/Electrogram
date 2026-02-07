# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SavedContact = Union["raw.types.SavedPhoneContact"]


class SavedContact:  # type: ignore
    """Saved contact

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            SavedPhoneContact

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetSaved
    """

    QUALNAME = "pyrogram.raw.base.SavedContact"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
