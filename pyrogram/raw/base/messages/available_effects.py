# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

AvailableEffects = Union["raw.types.messages.AvailableEffects", "raw.types.messages.AvailableEffectsNotModified"]


class AvailableEffects:  # type: ignore
    """

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.AvailableEffects
            messages.AvailableEffectsNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAvailableEffects
    """

    QUALNAME = "pyrogram.raw.base.messages.AvailableEffects"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
