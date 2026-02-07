# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MessageReplyHeader = Union["raw.types.MessageReplyHeader", "raw.types.MessageReplyStoryHeader"]


class MessageReplyHeader:  # type: ignore
    """Reply information

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            MessageReplyHeader
            MessageReplyStoryHeader
    """

    QUALNAME = "pyrogram.raw.base.MessageReplyHeader"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
