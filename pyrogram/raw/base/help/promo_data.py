# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PromoData = Union["raw.types.help.PromoData", "raw.types.help.PromoDataEmpty"]


class PromoData:  # type: ignore
    """Info about pinned MTProxy or Public Service Announcement peers.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.PromoData
            help.PromoDataEmpty

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetPromoData
    """

    QUALNAME = "pyrogram.raw.base.help.PromoData"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
