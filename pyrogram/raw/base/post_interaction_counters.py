# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PostInteractionCounters = Union["raw.types.PostInteractionCountersMessage", "raw.types.PostInteractionCountersStory"]


class PostInteractionCounters:  # type: ignore
    """Interaction counters

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PostInteractionCountersMessage
            PostInteractionCountersStory
    """

    QUALNAME = "pyrogram.raw.base.PostInteractionCounters"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
