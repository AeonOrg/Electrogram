# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

TextWithEntities = Union["raw.types.TextWithEntities"]


class TextWithEntities:  # type: ignore
    """Styled text with message entities

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            TextWithEntities

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.SummarizeText
    """

    QUALNAME = "pyrogram.raw.base.TextWithEntities"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
