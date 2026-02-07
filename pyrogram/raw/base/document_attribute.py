# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

DocumentAttribute = Union["raw.types.DocumentAttributeAnimated", "raw.types.DocumentAttributeAudio", "raw.types.DocumentAttributeCustomEmoji", "raw.types.DocumentAttributeFilename", "raw.types.DocumentAttributeHasStickers", "raw.types.DocumentAttributeImageSize", "raw.types.DocumentAttributeSticker", "raw.types.DocumentAttributeVideo"]


class DocumentAttribute:  # type: ignore
    """Various possible attributes of a document (used to define if it's a sticker, a GIF, a video, a mask sticker, an image, an audio, and so on)

    Constructors:
        This base type has 8 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            DocumentAttributeAnimated
            DocumentAttributeAudio
            DocumentAttributeCustomEmoji
            DocumentAttributeFilename
            DocumentAttributeHasStickers
            DocumentAttributeImageSize
            DocumentAttributeSticker
            DocumentAttributeVideo
    """

    QUALNAME = "pyrogram.raw.base.DocumentAttribute"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
