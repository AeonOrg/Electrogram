# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StarGiftAttributeRarity = Union["raw.types.StarGiftAttributeRarity", "raw.types.StarGiftAttributeRarityEpic", "raw.types.StarGiftAttributeRarityLegendary", "raw.types.StarGiftAttributeRarityRare", "raw.types.StarGiftAttributeRarityUncommon"]


class StarGiftAttributeRarity:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StarGiftAttributeRarity
            StarGiftAttributeRarityEpic
            StarGiftAttributeRarityLegendary
            StarGiftAttributeRarityRare
            StarGiftAttributeRarityUncommon
    """

    QUALNAME = "pyrogram.raw.base.StarGiftAttributeRarity"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
