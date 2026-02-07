# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PageListOrderedItem = Union["raw.types.PageListOrderedItemBlocks", "raw.types.PageListOrderedItemText"]


class PageListOrderedItem:  # type: ignore
    """Represents an instant view ordered list

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PageListOrderedItemBlocks
            PageListOrderedItemText
    """

    QUALNAME = "pyrogram.raw.base.PageListOrderedItem"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
