# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

UrlAuthResult = Union["raw.types.UrlAuthResultAccepted", "raw.types.UrlAuthResultDefault", "raw.types.UrlAuthResultRequest"]


class UrlAuthResult:  # type: ignore
    """URL authorization result

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            UrlAuthResultAccepted
            UrlAuthResultDefault
            UrlAuthResultRequest

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestUrlAuth
            messages.AcceptUrlAuth
    """

    QUALNAME = "pyrogram.raw.base.UrlAuthResult"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
