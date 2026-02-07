# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ForumTopic = Union["raw.types.ForumTopic", "raw.types.ForumTopicDeleted"]


class ForumTopic:  # type: ignore
    """Contains information about a forum topic

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ForumTopic
            ForumTopicDeleted
    """

    QUALNAME = "pyrogram.raw.base.ForumTopic"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
