# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PhoneConnection = Union["raw.types.PhoneConnection", "raw.types.PhoneConnectionWebrtc"]


class PhoneConnection:  # type: ignore
    """Phone call connection

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PhoneConnection
            PhoneConnectionWebrtc
    """

    QUALNAME = "pyrogram.raw.base.PhoneConnection"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
