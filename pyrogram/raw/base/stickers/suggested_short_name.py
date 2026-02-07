# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SuggestedShortName = Union["raw.types.stickers.SuggestedShortName"]


class SuggestedShortName:  # type: ignore
    """A suggested short name for the specified stickerpack

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            stickers.SuggestedShortName

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stickers.SuggestShortName
    """

    QUALNAME = "pyrogram.raw.base.stickers.SuggestedShortName"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
