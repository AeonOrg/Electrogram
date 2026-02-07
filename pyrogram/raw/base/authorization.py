# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Authorization = Union["raw.types.Authorization"]


class Authorization:  # type: ignore
    """Represents a logged-in session

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            Authorization

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.AcceptLoginToken
    """

    QUALNAME = "pyrogram.raw.base.Authorization"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
