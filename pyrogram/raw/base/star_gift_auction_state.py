# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StarGiftAuctionState = Union["raw.types.StarGiftAuctionState", "raw.types.StarGiftAuctionStateFinished", "raw.types.StarGiftAuctionStateNotModified"]


class StarGiftAuctionState:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StarGiftAuctionState
            StarGiftAuctionStateFinished
            StarGiftAuctionStateNotModified
    """

    QUALNAME = "pyrogram.raw.base.StarGiftAuctionState"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
