# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StoryItem = Union["raw.types.StoryItem", "raw.types.StoryItemDeleted", "raw.types.StoryItemSkipped"]


class StoryItem:  # type: ignore
    """Represents a Telegram Story

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StoryItem
            StoryItemDeleted
            StoryItemSkipped
    """

    QUALNAME = "pyrogram.raw.base.StoryItem"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
