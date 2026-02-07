# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StickerSet = Union["raw.types.messages.StickerSet", "raw.types.messages.StickerSetNotModified"]


class StickerSet:  # type: ignore
    """Stickerset

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.StickerSet
            messages.StickerSetNotModified

    Functions:
        This object can be returned by 9 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetStickerSet
            stickers.CreateStickerSet
            stickers.RemoveStickerFromSet
            stickers.ChangeStickerPosition
            stickers.AddStickerToSet
            stickers.SetStickerSetThumb
            stickers.ChangeSticker
            stickers.RenameStickerSet
            stickers.ReplaceSticker
    """

    QUALNAME = "pyrogram.raw.base.messages.StickerSet"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
