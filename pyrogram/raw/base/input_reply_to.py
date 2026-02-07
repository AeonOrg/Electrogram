# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputReplyTo = Union["raw.types.InputReplyToMessage", "raw.types.InputReplyToMonoForum", "raw.types.InputReplyToStory"]


class InputReplyTo:  # type: ignore
    """Contains info about a message or story to reply to.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputReplyToMessage
            InputReplyToMonoForum
            InputReplyToStory
    """

    QUALNAME = "pyrogram.raw.base.InputReplyTo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
