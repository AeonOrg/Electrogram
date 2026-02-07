# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BusinessChatLink = Union["raw.types.BusinessChatLink"]


class BusinessChatLink:  # type: ignore
    """

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            BusinessChatLink

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.CreateBusinessChatLink
            account.EditBusinessChatLink
    """

    QUALNAME = "pyrogram.raw.base.BusinessChatLink"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
