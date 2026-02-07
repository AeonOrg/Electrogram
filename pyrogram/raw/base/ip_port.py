# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

IpPort = Union["raw.types.IpPort", "raw.types.IpPortSecret"]


class IpPort:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            IpPort
            IpPortSecret
    """

    QUALNAME = "pyrogram.raw.base.IpPort"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
