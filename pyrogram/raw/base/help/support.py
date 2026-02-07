# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Support = Union["raw.types.help.Support"]


class Support:  # type: ignore
    """Info about the support user, relevant to the current user.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.Support

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetSupport
    """

    QUALNAME = "pyrogram.raw.base.help.Support"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
