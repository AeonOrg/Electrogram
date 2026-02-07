# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputGeoPoint = Union["raw.types.InputGeoPoint", "raw.types.InputGeoPointEmpty"]


class InputGeoPoint:  # type: ignore
    """Defines a GeoPoint.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputGeoPoint
            InputGeoPointEmpty
    """

    QUALNAME = "pyrogram.raw.base.InputGeoPoint"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
