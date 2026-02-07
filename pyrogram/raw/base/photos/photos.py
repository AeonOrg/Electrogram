# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Photos = Union["raw.types.photos.Photos", "raw.types.photos.PhotosSlice"]


class Photos:  # type: ignore
    """Object contains list of photos with auxiliary data.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            photos.Photos
            photos.PhotosSlice

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            photos.GetUserPhotos
    """

    QUALNAME = "pyrogram.raw.base.photos.Photos"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
