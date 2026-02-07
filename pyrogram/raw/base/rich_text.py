# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

RichText = Union["raw.types.TextAnchor", "raw.types.TextBold", "raw.types.TextConcat", "raw.types.TextEmail", "raw.types.TextEmpty", "raw.types.TextFixed", "raw.types.TextImage", "raw.types.TextItalic", "raw.types.TextMarked", "raw.types.TextPhone", "raw.types.TextPlain", "raw.types.TextStrike", "raw.types.TextSubscript", "raw.types.TextSuperscript", "raw.types.TextUnderline", "raw.types.TextUrl"]


class RichText:  # type: ignore
    """Rich text

    Constructors:
        This base type has 16 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            TextAnchor
            TextBold
            TextConcat
            TextEmail
            TextEmpty
            TextFixed
            TextImage
            TextItalic
            TextMarked
            TextPhone
            TextPlain
            TextStrike
            TextSubscript
            TextSuperscript
            TextUnderline
            TextUrl
    """

    QUALNAME = "pyrogram.raw.base.RichText"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
