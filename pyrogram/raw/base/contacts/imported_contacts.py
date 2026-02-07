# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ImportedContacts = Union["raw.types.contacts.ImportedContacts"]


class ImportedContacts:  # type: ignore
    """Object contains info on successfully imported contacts.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            contacts.ImportedContacts

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.ImportContacts
    """

    QUALNAME = "pyrogram.raw.base.contacts.ImportedContacts"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
