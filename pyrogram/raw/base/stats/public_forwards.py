# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PublicForwards = Union["raw.types.stats.PublicForwards"]


class PublicForwards:  # type: ignore
    """Contains info about the forwards of a story as a message to public chats and reposts by public channels.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            stats.PublicForwards

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.GetMessagePublicForwards
            stats.GetStoryPublicForwards
    """

    QUALNAME = "pyrogram.raw.base.stats.PublicForwards"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
