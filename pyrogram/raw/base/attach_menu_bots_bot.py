# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

AttachMenuBotsBot = Union["raw.types.AttachMenuBotsBot"]


class AttachMenuBotsBot:  # type: ignore
    """Represents a bot mini app that can be launched from the attachment menu »

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            AttachMenuBotsBot

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAttachMenuBot
    """

    QUALNAME = "pyrogram.raw.base.AttachMenuBotsBot"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
