# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SupportName = Union["raw.types.help.SupportName"]


class SupportName:  # type: ignore
    """Get localized name for support user

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.SupportName

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetSupportName
    """

    QUALNAME = "pyrogram.raw.base.help.SupportName"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
