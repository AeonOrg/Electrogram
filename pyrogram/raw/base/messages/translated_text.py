# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

TranslatedText = Union["raw.types.messages.TranslateResult"]


class TranslatedText:  # type: ignore
    """Translated text with entities.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.TranslateResult

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.TranslateText
    """

    QUALNAME = "pyrogram.raw.base.messages.TranslatedText"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
