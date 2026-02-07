# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Found = Union["raw.types.contacts.Found"]


class Found:  # type: ignore
    """Object contains info on users found by name substring and auxiliary data.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            contacts.Found

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.Search
    """

    QUALNAME = "pyrogram.raw.base.contacts.Found"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
