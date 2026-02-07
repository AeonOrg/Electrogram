# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

GeoPoint = Union["raw.types.GeoPoint", "raw.types.GeoPointEmpty"]


class GeoPoint:  # type: ignore
    """Object defines a GeoPoint.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            GeoPoint
            GeoPointEmpty
    """

    QUALNAME = "pyrogram.raw.base.GeoPoint"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
