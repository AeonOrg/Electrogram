# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StarGiftAttribute = Union["raw.types.StarGiftAttributeBackdrop", "raw.types.StarGiftAttributeModel", "raw.types.StarGiftAttributeOriginalDetails", "raw.types.StarGiftAttributePattern"]


class StarGiftAttribute:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StarGiftAttributeBackdrop
            StarGiftAttributeModel
            StarGiftAttributeOriginalDetails
            StarGiftAttributePattern
    """

    QUALNAME = "pyrogram.raw.base.StarGiftAttribute"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
