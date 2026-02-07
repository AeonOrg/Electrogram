# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StarGiftCollections = Union["raw.types.payments.StarGiftCollections", "raw.types.payments.StarGiftCollectionsNotModified"]


class StarGiftCollections:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            payments.StarGiftCollections
            payments.StarGiftCollectionsNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGiftCollections
    """

    QUALNAME = "pyrogram.raw.base.payments.StarGiftCollections"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
