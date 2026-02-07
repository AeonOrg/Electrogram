# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StarGiftActiveAuctions = Union["raw.types.payments.StarGiftActiveAuctions", "raw.types.payments.StarGiftActiveAuctionsNotModified"]


class StarGiftActiveAuctions:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            payments.StarGiftActiveAuctions
            payments.StarGiftActiveAuctionsNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGiftActiveAuctions
    """

    QUALNAME = "pyrogram.raw.base.payments.StarGiftActiveAuctions"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
