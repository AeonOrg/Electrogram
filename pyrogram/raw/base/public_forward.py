# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PublicForward = Union["raw.types.PublicForwardMessage", "raw.types.PublicForwardStory"]


class PublicForward:  # type: ignore
    """Contains info about the forwards of a story as a message to public chats and reposts by public channels.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PublicForwardMessage
            PublicForwardStory
    """

    QUALNAME = "pyrogram.raw.base.PublicForward"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
