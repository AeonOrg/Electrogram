# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SavedReactionTags = Union["raw.types.messages.SavedReactionTags", "raw.types.messages.SavedReactionTagsNotModified"]


class SavedReactionTags:  # type: ignore
    """

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.SavedReactionTags
            messages.SavedReactionTagsNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSavedReactionTags
    """

    QUALNAME = "pyrogram.raw.base.messages.SavedReactionTags"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
