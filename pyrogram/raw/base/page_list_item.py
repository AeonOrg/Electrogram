# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PageListItem = Union["raw.types.PageListItemBlocks", "raw.types.PageListItemText"]


class PageListItem:  # type: ignore
    """Item in block list

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PageListItemBlocks
            PageListItemText
    """

    QUALNAME = "pyrogram.raw.base.PageListItem"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
