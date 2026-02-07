# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Photo = Union["raw.types.Photo", "raw.types.PhotoEmpty"]


class Photo:  # type: ignore
    """Object describes a photo.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            Photo
            PhotoEmpty
    """

    QUALNAME = "pyrogram.raw.base.Photo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
