# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

DialogFilter = Union["raw.types.DialogFilter", "raw.types.DialogFilterChatlist", "raw.types.DialogFilterDefault"]


class DialogFilter:  # type: ignore
    """Dialog filter (folder »)

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            DialogFilter
            DialogFilterChatlist
            DialogFilterDefault
    """

    QUALNAME = "pyrogram.raw.base.DialogFilter"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
