# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

AttachMenuBots = Union["raw.types.AttachMenuBots", "raw.types.AttachMenuBotsNotModified"]


class AttachMenuBots:  # type: ignore
    """Represents a list of bot mini apps that can be launched from the attachment menu »

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            AttachMenuBots
            AttachMenuBotsNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAttachMenuBots
    """

    QUALNAME = "pyrogram.raw.base.AttachMenuBots"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
