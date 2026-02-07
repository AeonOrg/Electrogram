# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StoryViews = Union["raw.types.stories.StoryViews"]


class StoryViews:  # type: ignore
    """Reaction and view counters for a list of stories

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            stories.StoryViews

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetStoriesViews
    """

    QUALNAME = "pyrogram.raw.base.stories.StoryViews"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
