# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StoryReaction = Union["raw.types.StoryReaction", "raw.types.StoryReactionPublicForward", "raw.types.StoryReactionPublicRepost"]


class StoryReaction:  # type: ignore
    """How a certain peer reacted to or interacted with a story

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StoryReaction
            StoryReactionPublicForward
            StoryReactionPublicRepost
    """

    QUALNAME = "pyrogram.raw.base.StoryReaction"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
