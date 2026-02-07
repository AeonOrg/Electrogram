# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

GiveawayInfo = Union["raw.types.payments.GiveawayInfo", "raw.types.payments.GiveawayInfoResults"]


class GiveawayInfo:  # type: ignore
    """Info about a Telegram Premium Giveaway.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            payments.GiveawayInfo
            payments.GiveawayInfoResults

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetGiveawayInfo
    """

    QUALNAME = "pyrogram.raw.base.payments.GiveawayInfo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
