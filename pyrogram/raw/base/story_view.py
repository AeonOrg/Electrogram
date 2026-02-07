# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StoryView = Union["raw.types.StoryView", "raw.types.StoryViewPublicForward", "raw.types.StoryViewPublicRepost"]


class StoryView:  # type: ignore
    """Story view date and reaction information

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StoryView
            StoryViewPublicForward
            StoryViewPublicRepost
    """

    QUALNAME = "pyrogram.raw.base.StoryView"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
