# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

DataJSON = Union["raw.types.DataJSON"]


class DataJSON:  # type: ignore
    """Represent a JSON-encoded object

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            DataJSON

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.SendCustomRequest
            bots.InvokeWebViewCustomMethod
            phone.GetCallConfig
    """

    QUALNAME = "pyrogram.raw.base.DataJSON"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
