# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

CanSendStoryCount = Union["raw.types.stories.CanSendStoryCount"]


class CanSendStoryCount:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            stories.CanSendStoryCount

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.CanSendStory
    """

    QUALNAME = "pyrogram.raw.base.stories.CanSendStoryCount"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
