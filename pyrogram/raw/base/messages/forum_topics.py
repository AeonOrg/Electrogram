# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ForumTopics = Union["raw.types.messages.ForumTopics"]


class ForumTopics:  # type: ignore
    """Contains information about multiple forum topics

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.ForumTopics

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetForumTopics
            messages.GetForumTopicsByID
    """

    QUALNAME = "pyrogram.raw.base.messages.ForumTopics"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
