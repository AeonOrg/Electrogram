# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

DhConfig = Union["raw.types.messages.DhConfig", "raw.types.messages.DhConfigNotModified"]


class DhConfig:  # type: ignore
    """Contains Diffie-Hellman key generation protocol parameters.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.DhConfig
            messages.DhConfigNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDhConfig
    """

    QUALNAME = "pyrogram.raw.base.messages.DhConfig"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
