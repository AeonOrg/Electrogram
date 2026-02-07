# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

VideoSize = Union["raw.types.VideoSize", "raw.types.VideoSizeEmojiMarkup", "raw.types.VideoSizeStickerMarkup"]


class VideoSize:  # type: ignore
    """Represents an animated video thumbnail

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            VideoSize
            VideoSizeEmojiMarkup
            VideoSizeStickerMarkup
    """

    QUALNAME = "pyrogram.raw.base.VideoSize"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
