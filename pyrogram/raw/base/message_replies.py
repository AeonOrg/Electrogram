# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MessageReplies = Union["raw.types.MessageReplies"]


class MessageReplies:  # type: ignore
    """Info about post comments (for channels) or message replies (for groups)

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            MessageReplies
    """

    QUALNAME = "pyrogram.raw.base.MessageReplies"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
