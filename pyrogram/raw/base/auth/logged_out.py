# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

LoggedOut = Union["raw.types.auth.LoggedOut"]


class LoggedOut:  # type: ignore
    """Future auth token » to be used on subsequent authorizations

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            auth.LoggedOut

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.LogOut
    """

    QUALNAME = "pyrogram.raw.base.auth.LoggedOut"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
