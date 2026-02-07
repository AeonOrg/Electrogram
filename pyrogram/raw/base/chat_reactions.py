# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChatReactions = Union["raw.types.ChatReactionsAll", "raw.types.ChatReactionsNone", "raw.types.ChatReactionsSome"]


class ChatReactions:  # type: ignore
    """Available chat reactions

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChatReactionsAll
            ChatReactionsNone
            ChatReactionsSome
    """

    QUALNAME = "pyrogram.raw.base.ChatReactions"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
