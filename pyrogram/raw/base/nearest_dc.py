# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

NearestDc = Union["raw.types.NearestDc"]


class NearestDc:  # type: ignore
    """Object contains info on nearest data center.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            NearestDc

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetNearestDc
    """

    QUALNAME = "pyrogram.raw.base.NearestDc"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
