# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MaskCoords = Union["raw.types.MaskCoords"]


class MaskCoords:  # type: ignore
    """Mask coordinates (if this is a mask sticker, attached to a photo)

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            MaskCoords
    """

    QUALNAME = "pyrogram.raw.base.MaskCoords"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
