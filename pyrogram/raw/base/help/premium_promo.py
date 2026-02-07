# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PremiumPromo = Union["raw.types.help.PremiumPromo"]


class PremiumPromo:  # type: ignore
    """Telegram Premium promotion information

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            help.PremiumPromo

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetPremiumPromo
    """

    QUALNAME = "pyrogram.raw.base.help.PremiumPromo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
