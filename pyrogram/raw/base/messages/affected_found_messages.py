# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

AffectedFoundMessages = Union["raw.types.messages.AffectedFoundMessages"]


class AffectedFoundMessages:  # type: ignore
    """Messages found and affected by changes

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.AffectedFoundMessages

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.DeletePhoneCallHistory
    """

    QUALNAME = "pyrogram.raw.base.messages.AffectedFoundMessages"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
