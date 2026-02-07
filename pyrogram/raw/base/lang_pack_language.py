# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

LangPackLanguage = Union["raw.types.LangPackLanguage"]


class LangPackLanguage:  # type: ignore
    """Language pack language

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            LangPackLanguage

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            langpack.GetLanguages
            langpack.GetLanguage
    """

    QUALNAME = "pyrogram.raw.base.LangPackLanguage"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
