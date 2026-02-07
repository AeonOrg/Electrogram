# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Difference = Union["raw.types.updates.Difference", "raw.types.updates.DifferenceEmpty", "raw.types.updates.DifferenceSlice", "raw.types.updates.DifferenceTooLong"]


class Difference:  # type: ignore
    """Occurred changes.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            updates.Difference
            updates.DifferenceEmpty
            updates.DifferenceSlice
            updates.DifferenceTooLong

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            updates.GetDifference
    """

    QUALNAME = "pyrogram.raw.base.updates.Difference"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
