# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StickerSetCovered = Union["raw.types.StickerSetCovered", "raw.types.StickerSetFullCovered", "raw.types.StickerSetMultiCovered", "raw.types.StickerSetNoCovered"]


class StickerSetCovered:  # type: ignore
    """Stickerset preview

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StickerSetCovered
            StickerSetFullCovered
            StickerSetMultiCovered
            StickerSetNoCovered

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAttachedStickers
    """

    QUALNAME = "pyrogram.raw.base.StickerSetCovered"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
