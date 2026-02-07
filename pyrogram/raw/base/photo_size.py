# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PhotoSize = Union["raw.types.PhotoCachedSize", "raw.types.PhotoPathSize", "raw.types.PhotoSize", "raw.types.PhotoSizeEmpty", "raw.types.PhotoSizeProgressive", "raw.types.PhotoStrippedSize"]


class PhotoSize:  # type: ignore
    """Location of a certain size of a picture

    Constructors:
        This base type has 6 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PhotoCachedSize
            PhotoPathSize
            PhotoSize
            PhotoSizeEmpty
            PhotoSizeProgressive
            PhotoStrippedSize
    """

    QUALNAME = "pyrogram.raw.base.PhotoSize"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
