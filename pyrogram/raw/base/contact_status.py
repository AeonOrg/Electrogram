# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ContactStatus = Union["raw.types.ContactStatus"]


class ContactStatus:  # type: ignore
    """Contact status: online / offline.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ContactStatus

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetStatuses
    """

    QUALNAME = "pyrogram.raw.base.ContactStatus"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
