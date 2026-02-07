# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MsgDetailedInfo = Union["raw.types.MsgDetailedInfo", "raw.types.MsgNewDetailedInfo"]


class MsgDetailedInfo:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            MsgDetailedInfo
            MsgNewDetailedInfo
    """

    QUALNAME = "pyrogram.raw.base.MsgDetailedInfo"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes")
