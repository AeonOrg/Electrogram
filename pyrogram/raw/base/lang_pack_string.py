# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

LangPackString = Union["raw.types.LangPackString", "raw.types.LangPackStringDeleted", "raw.types.LangPackStringPluralized"]


class LangPackString:  # type: ignore
    """Language pack string

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            LangPackString
            LangPackStringDeleted
            LangPackStringPluralized

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            langpack.GetStrings
    """

    QUALNAME = "pyrogram.raw.base.LangPackString"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
