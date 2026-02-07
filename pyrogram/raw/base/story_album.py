# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StoryAlbum = Union["raw.types.StoryAlbum"]


class StoryAlbum:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StoryAlbum

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.CreateAlbum
            stories.UpdateAlbum
    """

    QUALNAME = "pyrogram.raw.base.StoryAlbum"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
