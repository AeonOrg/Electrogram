# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SecureRequiredType = Union["raw.types.SecureRequiredType", "raw.types.SecureRequiredTypeOneOf"]


class SecureRequiredType:  # type: ignore
    """Required secure file type

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            SecureRequiredType
            SecureRequiredTypeOneOf
    """

    QUALNAME = "pyrogram.raw.base.SecureRequiredType"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
