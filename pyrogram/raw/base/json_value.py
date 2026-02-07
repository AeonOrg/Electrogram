# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

JSONValue = Union["raw.types.JsonArray", "raw.types.JsonBool", "raw.types.JsonNull", "raw.types.JsonNumber", "raw.types.JsonObject", "raw.types.JsonString"]


class JSONValue:  # type: ignore
    """JSON value

    Constructors:
        This base type has 6 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            JsonArray
            JsonBool
            JsonNull
            JsonNumber
            JsonObject
            JsonString
    """

    QUALNAME = "pyrogram.raw.base.JSONValue"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
