# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SavedDialog = Union["raw.types.MonoForumDialog", "raw.types.SavedDialog"]


class SavedDialog:  # type: ignore
    """Represents a saved message dialog ».

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            MonoForumDialog
            SavedDialog
    """

    QUALNAME = "pyrogram.raw.base.SavedDialog"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
