# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

DraftMessage = Union["raw.types.DraftMessage", "raw.types.DraftMessageEmpty"]


class DraftMessage:  # type: ignore
    """Represents a message draft.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            DraftMessage
            DraftMessageEmpty
    """

    QUALNAME = "pyrogram.raw.base.DraftMessage"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
