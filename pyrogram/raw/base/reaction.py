# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Reaction = Union["raw.types.ReactionCustomEmoji", "raw.types.ReactionEmoji", "raw.types.ReactionEmpty", "raw.types.ReactionPaid"]


class Reaction:  # type: ignore
    """Message reaction

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ReactionCustomEmoji
            ReactionEmoji
            ReactionEmpty
            ReactionPaid
    """

    QUALNAME = "pyrogram.raw.base.Reaction"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
