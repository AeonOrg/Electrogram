# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StoryReactionsList = Union["raw.types.stories.StoryReactionsList"]


class StoryReactionsList:  # type: ignore
    """List of peers that reacted to a specific story

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            stories.StoryReactionsList

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetStoryReactionsList
    """

    QUALNAME = "pyrogram.raw.base.stories.StoryReactionsList"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
