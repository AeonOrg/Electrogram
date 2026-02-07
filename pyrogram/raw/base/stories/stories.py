# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Stories = Union["raw.types.stories.Stories"]


class Stories:  # type: ignore
    """List of stories

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            stories.Stories

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetPinnedStories
            stories.GetStoriesArchive
            stories.GetStoriesByID
            stories.GetAlbumStories
    """

    QUALNAME = "pyrogram.raw.base.stories.Stories"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
